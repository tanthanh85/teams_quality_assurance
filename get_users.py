import msal
import requests
import urllib3
from dotenv import load_dotenv
import os

load_dotenv()

urllib3.disable_warnings()



# Define your Azure app credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')


#d0c4d46d-f018-4226-b406-c491f350251a

# The authority URL for Microsoft identity platform
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Define the Graph API endpoint and scope
SCOPE = ["https://graph.microsoft.com/.default"]
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0/users"

# Function to get the access token
def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    
    result = app.acquire_token_for_client(scopes=SCOPE)
    
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Unable to obtain access token. Check your credentials.")

# Function to retrieve users
def get_users():
    token = get_access_token()
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(GRAPH_API_ENDPOINT, headers=headers,verify=False)
    
    if response.status_code == 200:
        users = response.json()
        #print(users)
        return users['value']
    else:
        raise Exception(f"Error fetching users: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:
        users = get_users()
        for user in users:
            print(f"User: {user['displayName']}, Email: {user['mail']}")
    except Exception as e:
        print(e)
