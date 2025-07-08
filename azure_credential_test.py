from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# For debugging, enable logging
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    # This will show which credential is being tried
    credential = DefaultAzureCredential(logging_enable=True)
    
    # Add debugging info about the credential
    print(f"Credential object created: {credential}")
    print(f"Credential type: {type(credential)}")
    
    # Check if a token can be obtained (this validates the credential)
    token = credential.get_token("https://management.azure.com/.default")
    print(f"Token obtained successfully: {token.token[:10]}... (truncated)")
    print(f"Token expires on: {token.expires_on}")
    
    # Try to access a resource
    client = SecretClient(vault_url="https://your-keyvault.vault.azure.net/", credential=credential)
    print("Authentication successful!")
    
except Exception as e:
    print(f"Authentication failed: {str(e)}")
