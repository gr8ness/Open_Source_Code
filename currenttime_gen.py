"""#import json
#import boto3
import datetime
import dateutil.tz

 # using now() to get current time 
current_time = datetime.datetime.now() 
    
    # Using of now() to get current time
current_time = datetime.datetime.now(dateutil.tz.gettz('US/Eastern'))
    
    #location variable
location = "The current time in New York,NY is :"
    
    #location and current time varaiable
time_date = location + current_time
    
    
print(time_date)"""


import json
import boto3
import datetime
import dateutil.tz

def lambda_handler(event, context):
    # calling boto3 to SQS with response variable
    client = boto3.client("sqs")
    response = client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/611031238384/MySQS_lambda",
        MessageBody=json.dumps(event['body'])
    )
    
    # using now() to get current time 
    current_time = datetime.datetime.now() 
    
    # Using of now() to get current time
    current_time = datetime.datetime.now(dateutil.tz.gettz('US/Eastern'))
    
    #location variable
    location = "The current time in New York,NY is :"
    
    #location and current time varaiable
    todaytime = {'location', 'current_time'}
    
  
    print(location)
    print(current_time)
    
    
    return {
        'statusCode':200,
        'body': json.dumps(str(todaytime))
        
            }
