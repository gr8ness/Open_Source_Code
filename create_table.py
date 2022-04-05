import boto3

#creates table with partition and sort key, attributes and provision throughput
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='MyMovies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
            },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
            'AttributeName': 'year',
            'AttributeType': 'N'
            },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    
print("Table status:", table.table_status)