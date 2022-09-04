#!/bin/bash

# This script is used to dump the private key of a given address

# Generate a random wallet name
WALLET_NAME=$(openssl rand -base64 6)

# Create a new wallet
nigiri rpc -named createwallet wallet_name=$WALLET_NAME descriptors=false >> /dev/null

# Get the a new address
NEW_ADDRESS=$(nigiri rpc -rpcwallet=$WALLET_NAME getnewaddress)

# Get the private key
PRIV_KEY=$(nigiri rpc -rpcwallet=$WALLET_NAME dumpprivkey $NEW_ADDRESS)

echo "New Address: $NEW_ADDRESS"
echo "Private Key: $PRIV_KEY"