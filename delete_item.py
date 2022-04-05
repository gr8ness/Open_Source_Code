import boto3

#deletes item from dynamoDB table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('MyMovies')

response = table.delete_item(Key={
    'year': 2008,
    'title': "Iron Man",
})

print(response)
