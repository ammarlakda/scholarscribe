import requests, json
from dotenv import dotenv_values

config = dotenv_values(".env")

headers = {
    "Authorization": "Bearer " + config["NOTION_KEY"],
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def createPage(title: str, notes: str):
    """
        Takes titles and notes and add them to the notion database
        Parameters: 
            should be self-explanatory
        Output:
            the notion api response
    """
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": config["DB_ID"] },
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Notes": {
                "rich_text": [
                    {
                        "text": {
                            "content": notes
                        }
                    }
                ]
            }
        }
    }
    
    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)

    return res

if __name__ == "__main__":
    createPage("Lecture 2", "•hello hello hello")