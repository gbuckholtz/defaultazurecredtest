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
    key_vault_url = "https://it-dplatf-dev-kv.vault.azure.net/"
    client = SecretClient(vault_url=key_vault_url, credential=credential)
    print("Authentication successful!")
    
    # Get the specific secret
    secret_name = "dplatf-003-factory-source-cs-ora"
    print(f"Retrieving secret: {secret_name}")
    
    secret = client.get_secret(secret_name)
    print(f"Secret retrieved successfully!")
    print(f"Secret name: {secret.name}")
    print(f"Secret value: {secret.value[:5]}... (truncated for security)")
    print(f"Secret properties: {secret.properties.tags}")
    
except Exception as e:
    print(f"Authentication failed: {str(e)}")
