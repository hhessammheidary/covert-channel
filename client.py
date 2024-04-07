import socket




if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6633
    address = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        command = "ls -l"
        client.sendto(command.encode(), address)

