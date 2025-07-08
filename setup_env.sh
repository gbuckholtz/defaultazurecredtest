#!/bin/bash
# Script to help set up Azure credentials environment variables
# This is a helper script for testing different credential types

# Service Principal Credentials (uncomment and fill values to test)
# export AZURE_TENANT_ID="your-tenant-id"
# export AZURE_CLIENT_ID="your-client-id"
# export AZURE_CLIENT_SECRET="your-client-secret"

# Or use Azure CLI (ensure you're logged in)
 az login

# Set your Key Vault URL (uncomment and update)
# export AZURE_KEY_VAULT_URL="https://your-keyvault.vault.azure.net/"

echo "Environment variables set up for testing Azure credentials"
echo "Run 'source setup_env.sh' to apply these variables to your shell session"
