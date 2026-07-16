from openai import OpenAI

endpoint = "<your-endpoint>"
deployment_name = "gpt-5-mini"
api_key =  "<your-api-key>"  # Replace with your actual API key

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    # input="What is the capital of France?",
    instructions="""
             You are a helpful AI assistant who supports employees with expense claims.
             Provide concise, accurate information only on topics related to expenses.
             Do not provide any information about topics that are not directly related to expenses.
         """,
         input="What kinds of business expense are typically reimbursed by employers?",
)

print(f"answer: {response.output[1]}")