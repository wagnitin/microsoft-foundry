# Import packages
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Load environment variables from .env file
load_dotenv()
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("API_KEY")

# Create the client
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

text = "Maria Garcia called from 020 7946 0958 and asked to send documents to 42 Market Road, London, UK, SW1A 1AA."

result = client.recognize_pii_entities([text])[0]

# Print the results
print("Redacted text:", result.redacted_text)
print("\nEntities found:")
for entity in result.entities:
    print(f"  {entity.text} | category={entity.category} | confidence={entity.confidence_score}")