#News Summarization Microservices
This project comprises two microservices: one built with FastAPI for interacting with the News API and calling the Langchain API to summarize news articles, and the other built with Flask to process news articles using the Langchain model and return the summarized results.

#Setup Instructions
FastAPI Service
Clone the Repository:
bash
Copy code
git clone <repository-url>
cd fastapi-service
Create a Virtual Environment:
bash
Copy code
python -m venv venv
source venv/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Set Environment Variables:
Create a .env file in the fastapi-service directory and add the following variables:

makefile
Copy code
API_KEY=<your-news-api-key>
Run the FastAPI Service:
bash
Copy code
uvicorn main:app --reload
Langchain Service
Navigate to the Langchain Service Directory:
bash
Copy code
cd ../langchain-service
Create a Virtual Environment:
bash
Copy code
python -m venv venv
source venv/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Set Environment Variables:
Create a .env file in the langchain-service directory and add the following variable:

makefile
Copy code
OPENAI_API_KEY=<your-langchain-api-key>
Run the Flask Service:
bash
Copy code
flask run
Usage
Once both services are running, you can access the FastAPI service at http://localhost:8000 and the Langchain service at http://localhost:5000. Refer to the API documentation provided by FastAPI for available endpoints and parameters.


#News Aggregator API Documentation
This API provides endpoints to interact with the News Aggregator service. Below are the available endpoints:

Base URL
GET: http://localhost/api/v1/
Endpoints
1. Get News Articles
Method: GET
URL: http://localhost:8000/api/v1/news?keyword=["football","elections","technology","cricket","AI","entertainment","India"]
Description: Fetches news articles based on specified keywords.
Parameters:
keyword (list): List of keywords to search for in news articles.
Response:
Status Code: 200 OK
Body: List of news articles matching the provided keywords.
Error Response:
Status Code: 400 Bad Request
Body: Error message indicating the issue with the request.
2. Summarize News Articles
Method: POST
URL: http://localhost:5000/api/v1/newslang
Description: Summarizes news articles using the Langchain API.
Request Body:
Concatenated articles returned from the News Aggregator API.
Response:
Summarized news articles.
Error Response:
Error message indicating the issue with the request.
Usage
To use these endpoints, send HTTP requests to the specified URLs with the appropriate parameters and request body. Ensure to handle both successful responses and error responses as described above.



