#!/usr/bin/env python3
import ftplib

# Definir las credenciales y la dirección del servidor FTP
ftp_host = 'descargas.igarle.es'
ftp_username = 'qlik_datajuice'
ftp_password = 'D@taJu1c3'

# Intentar conectarse al servidor FTP
try:
    ftp = ftplib.FTP(ftp_host)
    ftp.login(ftp_username, ftp_password)
    print("Conexión al servidor FTP establecida correctamente.")
except ftplib.all_errors as e:
    print("Error al conectarse al servidor FTP:", e)
    exit(1)

# Manejar errores durante la transferencia de archivos
try:
    # Realizar acciones de transferencia de archivos aquí
    # Por ejemplo, subir o descargar archivos
    with open("/home/jsegarra/ftp/test1.txt", 'rb') as file:
        ftp.storbinary('STOR test1.txt', file)
    print("Archivo transferido exitosamente.")
except ftplib.all_errors as e:
    print("Error durante la transferencia de archivos:", e)

# Cerrar la conexión FTP
ftp.quit()
