import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel

class CustomerSupportQuery(BaseModel):
    product_name: str
    issue_description: str
    customer_address: str
    customer_email: str
    customer_contact_number: str

schema=CustomerSupportQuery.model_json_schema()

response_format={
    "type": "json_object",
}

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model= "openai/gpt-oss-120b"
role="user"
system_prompt="You are a helpful assistant that extracts information from customer support queries and returns it strictly based on this schema {schema} and in the following format {response_format}. If any of the information is missing, please return an empty string for that key. Give it in a Json format only and do not add any extra text or explanation."
text="Hello i am a customer who just purchased an Iphone 18 Pro Max and i am having a issue with its speakers. My address is Mumbai, My email is abc@gmail.com, and my contact number is 9876543210. I would like to know how to get it fixed. Please help me with the process."
prompt=f""" this is a customer support query. Please extract the following information from this {text} and return it in a JSON format with the following keys: "product_name", "issue_description", "customer_address", "customer_email", "customer_contact_number". If any of the information is missing, please return an empty string for that key. """
message_system={
    "role":"system",
    "content":system_prompt
    }
message={
    "role":role, 
    "content":prompt
    }
messsages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messsages,response_format=response_format)
#print(response.choices[0].message.content)

## Printing the json output
import json
raw_json=response.choices[0].message.content
data_file=json.loads(raw_json)
ticket=CustomerSupportQuery(**data_file)

print(ticket.product_name)
print(ticket.issue_description)
print(ticket.customer_address)
print(ticket.customer_email)
print(ticket.customer_contact_number)