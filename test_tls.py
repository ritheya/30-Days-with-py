import socket
import ssl

host = "ac-dbzbhro-shard-00-00.fpjuapg.mongodb.net"

context = ssl.create_default_context()

try:
    with socket.create_connection((host, 27017), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=host) as secure:
            print("TLS connected!")
            print(secure.version())

except Exception as e:
    print(type(e).__name__, e)