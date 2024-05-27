# Meta-llama 70B-Instruct
- This repo will guide you through the process of running Meta-llama 3 70B on Akash Network.
- Need Access to the meta llama models on your huggingface account.
- Apply for Access permission from the authors

# Guide on how to deploy llama to Akask network
- Follow the below step by step process or check this [youtube](https://youtu.be/MjKLa3hYznA) tutorial
#
- Create an acces key to access the models
- First Create a Keplr wallet account
- Fund the wallet with AKT tokens
- Minimum of 0.5 AKT is required for deployments
- Go to [Akash console](https://console.akash.network/).
- Login with keplr wallet
- Approve the sign in transaction
- Go to Deployments
- Click `Build Your Template`
- Name your deployment(Optional)
- Go to yaml editor
- Paste the SDL From [SDL](https://github.com/vanman1/Meta-llama-3-70B-Instruct/blob/main/deploy.yaml)
- Replace the `Hf_token` with your hf token [link](https://huggingface.co/settings/tokens)
- Click Deploy
- Accept the transaction
- Accept the bids from the provider you like
- Wait for a while for the models to be downloaded
- After the model is downloaded you can now access your Llama 3 70B endpoint  by clicking on "Forwarded Port" on the "Leases" tab.
- Use that ENDPOINT in your API Code to interact with the model

# Testing The Model Deployment

- First, ensure you have the requests library installed. If you don't have it installed yet, you can install it via pip
- ```
  pip install requests
  ```
- Now use the api request from [app.py](https://github.com/vanman1/Meta-llama-3-70B-Instruct/blob/main/app.py)
- Replace `api.example.com` with the url you get in leases tab
- Run it in your terminal to see the response
- Change the user message to chat with the llama model running on akash.
