import boto3
from boto3.dynamodb.conditions import Key

#queries items from dynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyMovies')

response = table.query(KeyConditionExpression=Key('year').eq(2019))

print("The query returned the following items:")
for item in response['Items']:
    
    print(item)
