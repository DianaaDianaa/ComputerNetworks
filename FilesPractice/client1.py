import socket
import struct


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 1234))

file_path = input("File path: ")
file_name = input("File name: ")
clientSocket.send(file_path.encode())

file_content = clientSocket.recv(1024)
file_length = clientSocket.recv(4)
file_length = struct.unpack('!i', file_length)[0]

print(f"Received the content from the server: {file_content.decode()}\n Received the file length from the server: {file_length}")

new_file_name = f"{file_name}-copy"
f = open(new_file_name, 'w')
f.write(file_content.decode())
f.close()

clientSocket.close()
