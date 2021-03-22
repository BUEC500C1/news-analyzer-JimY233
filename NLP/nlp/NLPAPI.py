import os
os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key/google_nlp_key.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


import os
from google.oauth2 import service_account
import json

#Use github secret passed as environment var
service_account_info = json.loads(os.environ['GOOGLE_SECRET'])
credentials = service_account.Credentials.from_service_account_info(service_account_info)                                
client = language.LanguageServiceClient(credentials=credentials)


def NLP_analyze(text):
    
    # Instantiates a client
    #client = language.LanguageServiceClient()

    # The text to analyze
    #with open('Tweets.txt', 'r') as review_file:
    #    text = review_file.read()

    #text = u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    #print('Text: {}'.format(text))
    #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    return sentiment
