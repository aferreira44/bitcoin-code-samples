#!/bin/bash

# This script generates a new address and private key

# Genera a random wallet name
SEED=$(bx seed)

# Create a new private key
PRIV_KEY=$(bx ec-new $SEED)

# TODO: need to build bx with ICU support to use bx ec-to-ek
# PRIV_KEY_HASHED=$(bx ec-to-ek "passphrase" $PRIV_KEY)

# Get the WIF format of the private key
WIF=$(bx ec-to-wif $PRIV_KEY)

# Get the public key
PUB_KEY=$(bx ec-to-public $PRIV_KEY)

# Get the address
ADDRESS=$(bx ec-to-address $PUB_KEY)

echo "Seed: $SEED"
echo "Private Key: $PRIV_KEY"
# echo "Private Key Hashed: $PRIV_KEY_HASHED"
echo "WIF: $WIF"
echo "Public Key: $PUB_KEY"
echo "New Address: $ADDRESS"