import sys
import socket

objetivo = socket.gethostbyname(input("Ingrese la direccion IP: "))

print("Escaneando objetivo: {}".format(objetivo))

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print(" Puerto {}:  Abierto".format(port))
        s.close()
except:
    print("\nSaliendo del programa...")
    sys.exit()
    