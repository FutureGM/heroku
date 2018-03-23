# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

# Twitter API Keys
consumer_key = "vbtDKBb6MLz1UDuXqjulinZWP"
consumer_secret = "porfKt9UTtSp2XRYfqT7W5CaLAsgTFgXAgsjFYaAyxc42asmnw"
access_token = "2503131714-U09cIrTKKguHgX4tLYxSIWFKqkpM3FCpko8huUm"
access_token_secret = "QT9zEyQXvVzObM46BrIsx9kgqnwmZmhUjtNhafPU3iGcB"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Weather API
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"

city_list = ["Jakarta", "Detroit", "Austin", "Tokyo", "Beijing"]


# Create a function that gets the weather in London and Tweets it
def WeatherTweet(city):
    """Get Weather in London and Tweet it out."""
    # @TODO: Construct a Query URL for the OpenWeatherMap
    units = "imperial"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    query_url = f"{url}appid={api_key}&q={city}&units={units}"
    print(query_url)

    # @TODO: Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)
    api.update_status("%s Weather as of %s: %s F" %
                      (city, datetime.datetime.now().strftime("%I:%M %p"), weather_json["main"]["temp"]))

    # Add counter for unique tweets


while True:
    city_list = ["Jakarta", "Detroit", "Austin", "Tokyo", "Beijing"]
    for city in city_list:
        WeatherTweet(city)
    time.sleep(3600)
