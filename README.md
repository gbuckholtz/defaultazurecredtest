# Azure DefaultAzureCredential Test

This project tests the Azure DefaultAzureCredential authentication flow with detailed logging enabled, connecting to Azure Blob Storage.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install azure-identity azure-storage-blob
   ```

## Authentication Options

This project demonstrates how to use DefaultAzureCredential to authenticate to Azure services. DefaultAzureCredential tries these authentication methods in order:

1. Environment variables (service principal)
2. Managed Identity 
3. Azure CLI credentials
4. Azure PowerShell credentials
5. Visual Studio Code credentials
6. Azure Developer CLI credentials
7. Interactive browser authentication (when specified)

## Running the Test

1. Make sure you are logged in with Azure CLI:
   ```bash
   az login --scope https://storage.azure.com/.default
   ```

2. Run the test script:
   ```bash
   python azure_credential_test.py
   ```

## Troubleshooting

If authentication fails:
- Check your Azure CLI login status with `az account show`
- Check environment variables for service principal credentials
- Verify managed identity availability if running in Azure
- Check that your account has proper permissions on the storage account

### Common Error Messages

- **AuthorizationPermissionMismatch**: Your account doesn't have permission to access the specified resource
- **ResourceNotFound**: The specified blob or container doesn't exist
- **CredentialUnavailableError**: None of the credential types in DefaultAzureCredential could authenticate

## Customizing the Script

You can modify the following variables in the script to test different storage accounts:

```python
# Storage account settings - adjust these as needed
storage_account_name = "your-storage-account"
container_name = "your-container"
blob_name = "your-blob-path"
```
