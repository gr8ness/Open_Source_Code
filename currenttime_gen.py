#import json
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
    
    
print(time_date)