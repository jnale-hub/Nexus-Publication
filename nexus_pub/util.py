import os
import json

ARTICLE_DATA_DIR = "articles"
DEFAULT_IMAGE = ""

def list_articles():
    """
    Returns a list of dictionaries containing article information.
    """
    articles = []
    
    for filename in os.listdir(ARTICLE_DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(ARTICLE_DATA_DIR, filename), "r") as file:
                article_data = json.load(file)
                articles.append(article_data)
    
    return articles
