from minio import Minio
import os
import openpyxl
from dotenv.main import load_dotenv
import boto3


# Create a client with the MinIO server playground, its access key

load_dotenv()

client = Minio(
    os.environ['URL_MINIO'],
    access_key=os.environ['ACCESS_KEY_MINIO'],
    secret_key=os.environ['SECRET_KEY_MINIO'],
    secure=False  # Set to False if using an insecure connection (not recommended for production)
)

s3_client = boto3.client(
    's3',
    endpoint_url=os.environ['URL_S3'],
    aws_access_key_id=os.environ['S3_ACCESS_KEY'],
    aws_secret_access_key=os.environ['S3_SECRET_KEY'],
    region_name=os.environ['S3_REGION']
)

def download_file(bucket_name, object_name, local_directory):
    try:
        # Check if the bucket exists
        if client.bucket_exists(bucket_name):
            # Ensure the local_directory exists, create if it doesn't
            os.makedirs(local_directory, exist_ok=True)

            # Generate the file path for the downloaded file
            filename = object_name.split("/")[-1]
            local_file_path = os.path.join(local_directory, filename)

            # Download the file from MinIO
            client.fget_object(bucket_name, object_name, local_file_path)

            print(f"File downloaded successfully: {local_file_path}")
        else:
            print(f"Bucket '{bucket_name}' does not exist.")
    except Exception as e:
        print(f"Error downloading file: {str(e)}")


def upload_file_to_s3(bucket_name, file_path, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File uploaded successfully to {bucket_name}: {object_name}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")


path = os.environ['PATH_FOLDER_EXCEL']
wb_obj = openpyxl.load_workbook(path) 
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row 
m_column = sheet_obj.max_column

for i in range(1, m_row + 1):
    path_url = sheet_obj.cell(row = i, column = 1).value
    try:
        bucket_name_minio = os.environ['BUCKET_NAME_MINIO']
        object_name_minio = path_url
        local_file_path = "/opt/sampoerna-minio/static"
        download_file(bucket_name_minio, object_name_minio, local_file_path)
        print("Download file from Minio success", path_url)
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
    
    try:
        bucket_name_s3 = os.environ['S3_BUCKET']
        object_name_s3 = path_url
        file_path = "/opt/sampoerna-minio/static/{}".format(path_url.split("/")[-1])
        upload_file_to_s3(bucket_name_s3, file_path, object_name_s3)
        print("Upload file to S3 success", path_url)
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
    
    try:
        os.remove(file_path)
        print("Delete file success", path_url)
    except Exception as e:
        print(f"Error deleting file: {str(e)}")

print("Done")