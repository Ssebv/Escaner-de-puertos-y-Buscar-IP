import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de tu pc es: {}".format(hostname))

print("Tu direccon IP es: {}".format(ip))