from bitcoin.rpc import RawProxy
from dotenv import dotenv_values

config = dotenv_values()

# Create a connection to local Bitcoin Core node
try:
    rpc = RawProxy(
        service_url=f"http://{config.get('RPC_USER')}:{config.get('RPC_PASS')}@{config.get('RPC_HOST')}:{config.get('RPC_PORT')}"
    )
except:
    rpc = RawProxy()