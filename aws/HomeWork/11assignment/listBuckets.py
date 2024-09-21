import boto3

def listBuckets():
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        print("List of S3 Buckets:")
        for bucket in response['Buckets']:
            print(bucket['Name'])
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    listBuckets()
