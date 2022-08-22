import pprint
from rpc_client import rpc

# Running RPC methods via Bitcoin Core's JSON-RPC API using python-bitcoinlib to retrieve a transaction data.

# Alice's transaction ID
txid = "1deaf3be12ee78f3e0146a0594cd74266238974946ed44f9afd7bae14046edd7"

# First, retrieve the raw transaction in hex
raw_tx = rpc.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = rpc.decoderawtransaction(raw_tx)

# Construct PrettyPrinter object to print the data
pp = pprint.PrettyPrinter(width=30, compact=True, sort_dicts=False)

# Print the data
print("\n\n### Raw Transaction ###\n\n")
pp.pprint(raw_tx)

print("\n\n### Decoded Transaction ###\n\n")
pp.pprint(decoded_tx)
