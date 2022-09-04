from rpc_client import rpc

# Retrieving a block and adding all the transaction outputs values

# Get the block height that will be used to calculate the sum of the block value.
blockheight = int(input("Enter block height: "))

# Get the blockhash of the block height
blockchash = rpc.getblockhash(blockheight)

# Retrieve the block data by its hash
block = rpc.getblock(blockchash)

# Get all the transactions in the block
transactions = block["tx"]

block_value = 0

# Iterate through the transactions in the block and add the value of each transaction to the block value.
for txid in transactions:
    tx_value = 0
    # Retrieve the raw transaction by ID
    raw_tx = rpc.getrawtransaction(txid)

    # Decode the transaction
    decoded_tx = rpc.decoderawtransaction(raw_tx)

    # Iterate through each output in the transaction
    for output in decoded_tx["vout"]:
        # Add up the value of each output
        tx_value += output["value"]

    # Add value of this transaction to the total
    block_value += tx_value

print(f"Total value in block: {block_value}")
