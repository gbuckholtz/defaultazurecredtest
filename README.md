# Azure DefaultAzureCredential Test

This project tests the Azure DefaultAzureCredential authentication flow with detailed logging enabled.

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
   pip install azure-identity azure-keyvault-secrets
   ```

## Running the Test

To run the test script:

```bash
python azure_credential_test.py
```

You can also use the VS Code task "Run Azure Credential Test" which will activate the virtual environment and run the script.

## What This Script Does

The script:
1. Enables DEBUG level logging to see detailed authentication attempts
2. Creates a DefaultAzureCredential instance with logging enabled
3. Attempts to access an Azure Key Vault 
4. Reports success or failure

## Troubleshooting

If authentication fails:
- Check your Azure CLI login status with `az account show`
- Check environment variables for service principal credentials
- Verify managed identity availability if running in Azure
- Check Visual Studio Code Azure sign-in status

## DefaultAzureCredential Flow

DefaultAzureCredential tries these authentication methods in order:
1. Environment variables (service principal)
2. Managed Identity 
3. Azure CLI credentials
4. Azure PowerShell credentials
5. Visual Studio Code credentials
6. Azure Developer CLI credentials
7. Interactive browser authentication (when specified)
