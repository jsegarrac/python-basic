'''Exercise 
Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they 
update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members 
and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by 
reading/writing whole lines and ensuring the header remains )
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the 
cleanFiles function.'''

'''
El club de fans de los Raptors de tu universidad local mantiene un registro de sus miembros activos en un documento .txt. 
Todos los meses actualizan el archivo eliminando a los miembros que no están activos. Te han encomendado la tarea de automatizar 
esto con tus habilidades en Python.
Dado el archivo currentMem, elimina cada miembro con un 'no' en su columna Active. Lleva un registro de cada uno de los miembros 
eliminados y añádelos al archivo exMem. Asegúrate de que se conserve el formato de los archivos originales. (Sugerencia: haz esto leyendo/escribiendo líneas completas y asegurándote de que el encabezado permanezca)
Ejecuta el bloque de código a continuación antes de comenzar el ejercicio. Se te ha proporcionado el código de esqueleto. Edita solo la función cleanFiles.
'''

#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)