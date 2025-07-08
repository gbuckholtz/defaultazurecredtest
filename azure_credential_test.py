from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
import os

# For debugging, enable logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Storage account settings - adjust these as needed
storage_account_name = "itdplatflakehousedevdls"
container_name = "landing"
blob_name = "pscs-landing/ps_person.parquet"

try:
    # This will show which credential is being tried
    credential = DefaultAzureCredential(logging_enable=True)
    
    # Add debugging info about the credential
    print(f"Credential object created: {credential}")
    print(f"Credential type: {type(credential)}")
    
    # Check if a token can be obtained (this validates the credential)
    token = credential.get_token("https://storage.azure.com/.default")
    print(f"Token obtained successfully: {token.token[:10]}... (truncated)")
    print(f"Token expires on: {token.expires_on}")
    
    # Create the BlobServiceClient
    account_url = f"https://{storage_account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
    
    # Get account information to test connection
    account_info = blob_service_client.get_account_information()
    print(f"Connected to storage account: {storage_account_name}")
    print(f"Account kind: {account_info['sku_name']}")
    print(f"Account tier: {account_info.get('account_kind', 'Unknown')}")
    
    # List containers to check permissions
    print("\nListing available containers:")
    containers = list(blob_service_client.list_containers())
    container_list = [container.name for container in containers]
    for i, container in enumerate(container_list, 1):
        print(f"  {i}. {container}")
    
    # Continue with the original container and blob if it exists
    print(f"\nAttempting to access container: {container_name}")
    if container_name in container_list:
        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)
        print(f"Connected to container: {container_name}")
        
        # List blobs in the container (first 5)
        print("\nListing blobs in this container (first 5):")
        blobs = list(container_client.list_blobs(name_starts_with='pscs-landing/'))[:5]
        for i, blob in enumerate(blobs, 1):
            print(f"  {i}. {blob.name}")
        
        # Try to access the specific blob
        print(f"\nAttempting to access blob: {blob_name}")
        try:
            # Get the blob client
            blob_client = container_client.get_blob_client(blob_name)
            
            # Get blob properties first to check if it exists
            properties = blob_client.get_blob_properties()
            print(f"Found blob: {blob_name}")
            print(f"Blob size: {properties.size} bytes")
            print(f"Content type: {properties.content_settings.content_type}")
            
            # Download the blob
            print(f"Downloading blob...")
            blob_data = blob_client.download_blob()
            content = blob_data.readall()
            
            # Print information about the downloaded blob
            print(f"Blob downloaded successfully!")
            print(f"Blob size: {len(content)} bytes")
            print(f"First 100 bytes (hex): {content[:100].hex()}")
            
        except ResourceNotFoundError:
            print(f"Error: Blob '{blob_name}' not found in container '{container_name}'")
        except HttpResponseError as e:
            print(f"Error accessing blob: {e.message}")
            print(f"Error code: {e.error_code if hasattr(e, 'error_code') else 'Unknown'}")
            print(f"Request ID: {e.response.request.headers.get('x-ms-client-request-id') if hasattr(e, 'response') else 'Unknown'}")
    else:
        print(f"Error: Container '{container_name}' not found in account '{storage_account_name}'")
    
except Exception as e:
    print(f"Operation failed: {str(e)}")
