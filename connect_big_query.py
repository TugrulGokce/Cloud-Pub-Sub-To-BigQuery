from google.cloud import bigquery
import os
import base64
from PIL import Image
from io import BytesIO

# Import service account credentials key and set environment
big_query_credentials = 'de-projects-big-query-credentials-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = big_query_credentials

# Create BigQuery publisher client
client = bigquery.Client()

# Query to table
query_for_base64 = "SELECT data FROM `<project-id>.<dataset-name>.<table-name>`;"
query = client.query(query_for_base64)

# Convert format QueryJob to byte
query_result = list(query)
convert_query_to_byte = query_result[0][0].encode()

# Decode image and show
decoded_image = Image.open(BytesIO(base64.b64decode(convert_query_to_byte)))
decoded_image.show()
