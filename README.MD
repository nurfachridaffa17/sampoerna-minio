## INTRODUCTION

This is the simple script pyhon to get object data from minio storage. after that, it will be saved to the local storage. And then, it will be uploaded to the s3 storage.

## INSTALLATION & USAGE

1. Install python3
2. Install pip
3. Install boto3
4. Install minio

## CONFIGURATION

1. Create file .env
2. Add the following configuration to the .env file

```
# Minio
URL_MINIO={MINIO URL}
ACCESS_KEY_MINIO={ACCESS KEY MINIO}
SECRET_KEY_MINIO={SECRET KEY MINIO}
BUCKET_NAME_MINIO={BUCKET NAME MINIO}

# S3 Bucket production and development
URL_S3={S3 URL}
S3_ACCESS_KEY={S3 ACCESS KEY}
S3_SECRET_KEY={S3 SECRET KEY}
S3_BUCKET={S3 BUCKET NAME}
S3_REGION={S3 REGION}

# Path folder
PATH_FOLDER_EXCEL={PATH FOLDER EXCEL}
```
