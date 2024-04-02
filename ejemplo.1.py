
import os

#clasificacion de estudiantes de acuerdo a puntaja 

ls_categoria1 = [] # puntaje entre 30-50, edad  entre 15-20 años 
ls_categoria2 =[] # puntaj entre 51-80, edad entre 21-30 años 
ls_categoria3 = []# puntaje entre 81-100, edad entre 31-50 años 
sw = True

def fnt_limpiar ():
    os.system ('cls')
    print('bienvenido al sistema clasificacion de estudiantes')
    print('AUTOR juan jose hernandez ')
    print(' UNIVERSIDAD CATOLICA LUIS AMIGO')
    print( 'categoria 1 ', ls_categoria1 )
    print('categoria 2 ', ls_categoria2 )
    print('categoria 3 ', ls_categoria3)
def fnt_registrar (id,nombre,puntaje,edad):
    if id == ' ' or puntaje ==' ' or nombre == '' or edad == ' ':
        enter = input('\nDebe ingresar todos los datos <ENTER>')
    else: 
        if id in ls_categoria1:#  or ls_categoria2 or ls_categoria3: # si id ya se encentra registrado 
                enter = input('\nEsta persona ya se encuentra registrada <ENTER>')
        else:
            Auxp = int(puntaje)
            Auxe = int(edad)
            
            if( Auxp >= 30 and Auxp  <= 50) and(Auxe>= 15 and Auxe <= 20):
                    ls_categoria1.append([id,nombre,edad,puntaje])
                    
            elif ( Auxp>= 51 and Auxp <= 80) and (Auxe >= 21 and Auxe <= 30):
                    ls_categoria2.append([id,nombre,edad,puntaje])
            elif (Auxp >= 81 and Auxp <= 100) and (Auxe >= 31 and Auxe <=50):
                    ls_categoria3.append([id,nombre,edad,puntaje])
            enter = input(f'\n estudiante {nombre} registrado con exito <ENTER>')
def fnt_selector (op):
    fnt_limpiar()
    if op == '1':
        id = input('id: ')
        puntaje =   input('puntaje: ')
        nombre = input('nombre: ')
        edad = input('Edad: ')
        fnt_registrar(id,nombre,puntaje,edad)
  
        
                           
        
    
while sw == True:
    fnt_limpiar()
    opciones = input('\n\n <<<<<<<< MENU PRINCIPAL>>>>>>>>>\n\n1.registrar\n\n2.consultar\n -> ')
    fnt_selector(opciones)
    
   
    
    