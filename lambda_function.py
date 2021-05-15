import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    Booknames=[]

    url =  'https://bookmeter.com/users/' + event['id'] + '/summary'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    Thumbnails = soup.select(".book-list--grid .book__thumbnail img")
    for Thumbnail in Thumbnails:
        Booknames.append(Thumbnail.get('alt'))
    Authors = [n.get_text() for n in soup.select(".book-list--grid .detail__authors")]

    booklist = {key: val for key, val in zip(Booknames, Authors)}
    print(booklist)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Hello",
        "isBase64Encoded": False
    }