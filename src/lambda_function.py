import os
from pathlib import Path
import tweepy
import csv
import numpy as np
import pandas as pd
import io

def lambda_handler(event, context):
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
    df = pd.read_csv(url, usecols=['total_vaccinations', 'total_vaccinations_per_hundred'])
    output = df.tail(1)
    total_vaxx = output.iat[0,0].astype(int).astype(str)
    total_perc=output.iat[0,1].astype(str)
    tweet = "✅"+ total_vaxx +" vaccinations have been issued, " +total_perc +"% of the planet's population! ✅"

    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Post tweet:"+ tweet)
    api.update_status(tweet)

    return {"statusCode": 200, "tweet": tweet}
