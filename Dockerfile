FROM python:3.8-slim-buster

RUN apt-get update

# Install dependencies

RUN pip install boto3, openpyxl, python-dotenv, minio

# Copy local code to the container image.

COPY . .

COPY ./run.py .

CMD [ "python", "upload_files.py" ]