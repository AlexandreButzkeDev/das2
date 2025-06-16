import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_s3_bucket(bucket_name, region=None):
    try:
        # Create S3 client
        s3_client = boto3.client('s3', region_name=region)

        # Create the bucket
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    bucket_name = "rafael19032004"
    region = "sa-east-1"  # Altere para a região desejada
    create_s3_bucket(bucket_name, region)