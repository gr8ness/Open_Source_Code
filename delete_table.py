import boto3

#deletes dynamoDB table
client = boto3.client('dynamodb')

try:
    resp = client.delete_table(
        TableName="MyMovies123",
    )
    print("Table deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)
