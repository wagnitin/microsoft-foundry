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

# Make a request using the client for language detection
text_spanish = "¡Hola! Me llamo Josefina y vivo en Madrid, España."
result_spanish = client.detect_language([text_spanish])[0]

# Print the results
print(f"Detected language: {result_spanish.primary_language.name} (ISO 639-1 code: {result_spanish.primary_language.iso6391_name}) with confidence score: {result_spanish.primary_language.confidence_score}")

text_hindi = "नमस्ते! मेरा नाम जोसेफिना है और मैं दिल्ली, भारत में रहती हूँ।"
result_hindi = client.detect_language([text_hindi])[0]  

# Print the results for Hindi text
print(f"Detected language: {result_hindi.primary_language.name} (ISO 639-1 code: {result_hindi.primary_language.iso6391_name}) with confidence score: {result_hindi.primary_language.confidence_score}")

text_french = "Bonjour! Je m'appelle Josefina et je vis à Paris, France."
result_french = client.detect_language([text_french])[0]
# Print the results for French text
print(f"Detected language: {result_french.primary_language.name} (ISO 639-1 code: {result_french.primary_language.iso6391_name}) with confidence score: {result_french.primary_language.confidence_score}")

text_german = "Hallo! Ich heiße Josefina und ich lebe in Berlin, Deutschland."
result_german = client.detect_language([text_german])[0]    
# Print the results for German text
print(f"Detected language: {result_german.primary_language.name} (ISO 639-1 code: {result_german.primary_language.iso6391_name}) with confidence score: {result_german.primary_language.confidence_score}")

text_japanese = "こんにちは！私の名前はジョセフィーナで、東京、日本に住んでいます。"
result_japanese = client.detect_language([text_japanese])[0]
# Print the results for Japanese text
print(f"Detected language: {result_japanese.primary_language.name} (ISO 639-1 code: {result_japanese.primary_language.iso6391_name}) with confidence score: {result_japanese.primary_language.confidence_score}")   

text_korean = "안녕하세요! 제 이름은 조세피나이고, 서울, 대한민국에 살고 있습니다."
result_korean = client.detect_language([text_korean])[0]
# Print the results for Korean text
print(f"Detected language: {result_korean.primary_language.name} (ISO 639-1 code: {result_korean.primary_language.iso6391_name}) with confidence score: {result_korean.primary_language.confidence_score}")

text_russian = "Привет! Меня зовут Жозефина, и я живу в Москве, Россия."
result_russian = client.detect_language([text_russian])[0]
# Print the results for Russian text
print(f"Detected language: {result_russian.primary_language.name} (ISO 639-1 code: {result_russian.primary_language.iso6391_name}) with confidence score: {result_russian.primary_language.confidence_score}")

text_marathi = "नमस्कार! माझं नाव जोसेफिना आहे आणि मी मुंबई, भारतात राहते."
result_marathi = client.detect_language([text_marathi])[0]
# Print the results for Marathi text


print(f"Detected language: {result_marathi.primary_language.name} (ISO 639-1 code: {result_marathi.primary_language.iso6391_name}) with confidence score: {result_marathi.primary_language.confidence_score}")
