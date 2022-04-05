import boto3
import json

#imports items from json file and populates dynamodb table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#name of the table database
table = dynamodb.Table('MyMovies')
#open table to put items
with open("movie_list.json") as json_file:
    movie_list = json.load(json_file)
    for movies in movie_list:
        year = movies['year']
        title = movies['title']

        print("Adding movies:", year, title)
        
        #putting the attributes in the table
        table.put_item(
           Item={
               'year': year,
               'title': title,
            }
        )
