from twython import Twython
import random
import os

app_key = "wdJgxDzEv8QcuQV6jMf65eZX6"
app_secret = "1dvPRcEpGZQeS3kDs5juUylRNWVymeFQmipB7hQPBAeRULduaU"
oauth_token ="1074749175458353153-0Z0zhsQhtZohYHNTMQih0ZOmdHRqBg"
oauth_token_secret = "gMb5IckMoHF0noo6EUuNyakeI5JuzZW1UfgjDaPdsBkRW"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

folder1 = "C:\\Users\\HP\\Desktop\\Slike"

def RandomImageTwitt(folder):
    # Takes the folder where your images are as the input
    images = os.listdir(folder)


    photo = open(folder + "\\" + (images[random.randint(0, len(images)) - 1]), 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(media_ids=[response['media_id']])


try:
    RandomImageTwitt(folder1)
except:
    "doslo je do greske"

