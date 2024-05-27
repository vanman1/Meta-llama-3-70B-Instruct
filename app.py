import requests

# Define the API endpoint
API_URL = "http://api.example.com/v1/chat/completions"  # Replace with the actual URL you get from the leases tab


# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Write your prompt
prompt = "Hey, what are the cycles of the moon" # Insert any prompt you like here

# Define the chat messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt},
]

# Define the payload with the model name and messages
payload = {
    "model": "meta-llama/Meta-Llama-3-70B-Instruct",
    "messages": messages
}

# Make the POST request to the API
response = requests.post(API_URL, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    reply = response_data["choices"][0]["message"]["content"]
    
    print("Your message:", prompt)
    print()
    print("Chatbot reply:", reply)
else:
    # Print an error message if the request failed
    print(f"Request failed with status code {response.status_code}")
    print("Response:", response.text)
