import os
from google.cloud import pubsub_v1
import base64

# Import service account credentials key and set environment
pub_sub_credentials = "de-projects-pub-sub_credentials_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = pub_sub_credentials

# Create Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = "projects/de-projects-359322/topics/pubsubtobigquery"

# Open image and convert base64 format
with open("golden_dog.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

# Publish base64(binary) format data to Pub/Sub topic
publisher.publish(topic_path, data=encoded_image)

