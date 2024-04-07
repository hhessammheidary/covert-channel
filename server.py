import socket
import subprocess

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()



if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6633

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ip, port))
    print("server is up")
    while True:    
        data, addr = server.recvfrom(1024)
        command = data.decode()
        print(f"Received command '{command}' from {addr[0]}:{addr[1]}")
        execute_command(command)
        server.close()