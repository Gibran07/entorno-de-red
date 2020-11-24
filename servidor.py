import socket
import re

#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(20) #Máximo de conexiones

vocales = r"[aeiouAEIOU]"
palabra = r"[a-zA-Z]{1,}\b"
numeros = r"[0-9]"
palabrasMay = r"[A-Z]\w+"
palabrasfv= r"[a-zA-Záéíóú]{1,}[^aeiouAEIOUáéíóú\s\W]\b"

print(f"\n\nServidor en espera direccion {ip}:{port}")

while True:
    conexion, address = socket_server.accept()
    print ("La conexión  ha sido establecida")
    
    while True:
        
        message = conexion.recv(1024)
        message = message.decode()
        print(message)
        
#___________________________________________________________________________
   
        coincidencias = re.findall(vocales, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        mensaje = f"Se encontraron {suma} vocales en el servidor"
        conexion.send(mensaje.encode('utf-8'))  
#_________________________________________________________________________
        
      

        coincidencias = re.findall(palabra, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        mensaje = f"Se encontraron {suma} palabras en el servidor"
        conexion.send(mensaje.encode('utf-8'))

#__________________________________________________________________________       
        
        

        coincidencias = re.findall(numeros, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        mensaje = f"Se encontraron {suma} numeros en el servidor"
#___________________________________________________________________________
        
        conexion.send(mensaje.encode('utf-8'))
        
        coincidencias = re.findall(palabrasMay, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        mensaje = f"Se encontraron {suma} palabras que inician con mayuscula en el servidor"
       
#___________________________________________________________________________
        
        conexion.send(mensaje.encode('utf-8'))
        
        coincidencias = re.findall(palabrasfv, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        mensaje = f"Se encontraron {suma} palabras que no finalizan con una vocal en el servidor"   

#___________________________________________________________________________
        mensaje = f"Se encontraron {suma} palabras que no finalizan con una vocal"
        conexion.send(mensaje.encode('utf-8'))

        mensaje = "."
        conexion.send(mensaje.encode('utf-8'))

print("Servidor Finalizado")