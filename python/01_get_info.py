import pprint
from rpc_client import rpc

# Running RPC methods via Bitcoin Core's JSON-RPC API using python-bitcoinlib
# to get information about the node, the blockchain and the network.

# Run the rpc commands, store the resulting data in variables
blockchain_info = rpc.getblockchaininfo()
mempool_info = rpc.getmempoolinfo()
network_info = rpc.getnetworkinfo()
wallet_info = rpc.getwalletinfo()
peer_info = rpc.getpeerinfo()
mining_info = rpc.getmininginfo()
rpc_info = rpc.getrpcinfo()
utxoset_info = rpc.gettxoutsetinfo()

# Construct PrettyPrinter object to print the data
pp = pprint.PrettyPrinter(width=30, compact=True, sort_dicts=False)

# Print the data
print("\n\n### Blockchain Info ###\n\n")
pp.pprint(blockchain_info)

print("\n\n### Mempool Info ###\n\n")
pp.pprint(mempool_info)

print("\n\n### Network Info ###\n\n")
pp.pprint(network_info)

print("\n\n### Wallet Info ###\n\n")
pp.pprint(wallet_info)

print("\n\n### Peer Info ###\n\n")
pp.pprint(peer_info)

print("\n\n### Mining Info ###\n\n")
pp.pprint(mining_info)

print("\n\n### RPC Info ###\n\n")
pp.pprint(rpc_info)

print("\n\n### UTXOSet Info ###\n\n")
pp.pprint(utxoset_info)
