 import boto3
    #the name of your resource in your region
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
   
    #search for the table name
    table = dynamodb.Table('MyMovies')
    
    #puts an item in the dynamoDB table
    response = table.put_item(Item={
    'year': 2008,
    'title': "Iron Man",
    })
