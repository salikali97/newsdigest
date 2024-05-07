
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
import ast
import json
from datetime import datetime,timedelta
from application.constants import newsurl, langchainurl
from application.config import apikey
from application.utils import dict_to_string,convert_to_dict

router = APIRouter(prefix='/api/v1')


@router.get('/news')
async def baseroute(keyword:str):
    """
    Get the input topics for news recommendation 

    Args:
        text (str): The news on these topics to be summarized. 
            Example: ['sports','technology']

    Returns:
        dict:
            title: The title of the news
            content: The description of the news
            url: The related url of the news
    """
    try:
        
        keywords = ast.literal_eval(keyword)

        if keywords==[''] or len([kw.strip() for kw in keywords if kw.strip()])<len(keywords):
            return JSONResponse(content={'message':'Keyword cannot be empty'},status_code=400)
        
        elif len(keywords)>5:
            return JSONResponse(content={'message':'Keyword limit exceeded, please enter less than 6 keywords'},status_code=400)
        
        # Check for special characters in each keyword
        invalid_keywords = [kw for kw in keywords if any(char in '!@#$%^&*()_+=[{}]:;"\'\\|,.<>?/' for char in kw)]
        if invalid_keywords:
            return JSONResponse(content={"Invalid keywords: " + ', '.join(invalid_keywords)},status_code=400)
        langchain_data = ""
        delta_utc_date = (datetime.utcnow().date()-timedelta(days=3)).strftime('%Y-%m-%d')
        
        # get news for each topic
        for key in keywords:
            url = f'{newsurl}?q={key}&from={delta_utc_date}&sortBy=publishedAt+AND+relevancy&pageSize=4&language=en&apiKey={apikey}'
            news_response=requests.get(url)
            news_dict = json.loads(news_response.content.decode('utf-8'))
            if len(news_dict['articles'])==0:
                return JSONResponse(content={'message':'No related news articles found for this keyword'},status_code=400)
            
           
            langchain_data += dict_to_string(news_dict['articles'])

            print(langchain_data)
            
        # call api for langchain
        url = f'{langchainurl}'
        user_response=requests.post(url, json={'news': langchain_data})

        if user_response.status_code!=200 or (user_response.content.decode('utf-8').split('\n')[0])=='[]':
            return JSONResponse(content={'message':'No response recieved from summarizer'},status_code=400)
        response = user_response.content

        message = convert_to_dict(response.decode('utf-8'))

        
        return JSONResponse(content={"message": json.loads(message)},status_code=200)

    except Exception as e:
        print(e)
        return JSONResponse(content={'message':'something went wrong, please reload'},status_code=400)
        