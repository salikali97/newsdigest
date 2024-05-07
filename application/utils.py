
import json


def dict_to_string(articles):
    # langchain_data = ""
    user_response = ""
    # Iterate over the list of dictionaries
    for idx, data_dict in enumerate(articles):
        # Append the data from each dictionary to the string
        user_response += f"Title: {data_dict['title']}, "
        user_response += f"Description: {data_dict['description']}, "
        user_response += f"Content: {data_dict['content']}, "
        user_response += f"URL: {data_dict['url']} "

    return user_response



def convert_to_dict(response_str):
    # Split the response string into individual entries
    response_str = bytes(response_str, "utf-8").decode("unicode_escape")
    entries = response_str.split("\n\n")

    # Initialize an empty dictionary to store title, content, and URL
    data_dict = {'data':[]}
    
    # Iterate over each entry and extract title, content, and URL
    for entry in entries:
        # Split the entry into title, content, and URL
        parts = entry.split("\n")
        title = parts[0].split(": ")[1]
        content = parts[2].split(": ")[1]
        url = parts[1].split(": ")[1]
        # Store the title, content, and URL in the dictionary
        data_dict['data'].append({"title":title,"content": content, "url": url})

    # Convert the dictionary to JSON format
    json_data = json.dumps(data_dict, indent=4)

    # Print the JSON data
    print(json_data)
    return json_data