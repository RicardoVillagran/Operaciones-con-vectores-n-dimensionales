# -*- coding: utf-8 -*-
"""
Desarrollar un prgorama que 
realice operaciones con vectores 
n-dimensionales
SUMA
Resta
Producto por un escalar
Norma
Angulo entre 2 vectores

Ricardo Villagran Herrera
"""
import numpy as np
"""
np_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]).reshape(2,3,3) 
print(np_array)
"""

def dimensionesdelvector():
  
    dimension= int(input('Introduce las Dimensiones que Tendra tu Arreglo\n'))
    b=1

    l=[]
    while b<=dimension:
        tamaniodedimension=int(input(f'Ingrese el tamanio de la dimension {b}\n'))
        l.append(tamaniodedimension)
        b+=1
       
        if b==dimension+1:
            print(f"\nEl tamanio de las dimensiones de tu arreglo seran {l}")
            break
    listadimensionesdelvector=l
   
    
    producto=1
    for l in l:
        producto*=l
    print(f"\nTu arreglo tendra {producto} elementos")
    listadevectoresbuenos=[]
    
    x=int(input(f"Ingrese los {producto} que componen a tu vector de acuerdo al tamanio de las dimensiones asignadas\n"))
    listadevectoresbuenos.append(x)
    while len(listadevectoresbuenos)!=producto:
        
        x=int(input("Ingresa el siguiente elemento\n"))
        listadevectoresbuenos.append(x)
    print(listadevectoresbuenos)    
    
    
    np_array = np.array(listadevectoresbuenos).reshape(tuple(listadimensionesdelvector)) 
    return np_array,producto,listadimensionesdelvector
   
def segundovector(tamanio,listadedimensionesdelvector):
    listaDeElementosdelSegundoVector=[]
    
    x=int(input(f"Ingrese los {tamanio} que componen al segundo vector\n"))
    listaDeElementosdelSegundoVector.append(x)
    while len(listaDeElementosdelSegundoVector)!=tamanio:
        
        x=int(input("Ingresa el siguiente elemento\n"))
        listaDeElementosdelSegundoVector.append(x)
    print(listaDeElementosdelSegundoVector)    
   
    
    segundovectormatriz = np.array(listaDeElementosdelSegundoVector).reshape(tuple(listadedimensionesdelvector)) 
    return  segundovectormatriz
  
def suma(vector1,vector2,listadedimensionesdelvector):
    vector1.flatten()
    vector2.flatten()
    VectorSuma=[]
    for i in range(len(vector1)):
        VectorSuma.append(vector1[i]+vector2[i])
    
    VectorSuma=np.array(VectorSuma)
    VectorSuma=VectorSuma.reshape(tuple(listadedimensionesdelvector))
    
    return VectorSuma

def resta(vector1,vector2,listadedimensionesdelvector):
    vector1.flatten()
    vector2.flatten()
    VectorResta=[]
    for i in range(len(vector1)):
        VectorResta.append(vector1[i]-vector2[i])
    
    VectorResta=np.array(VectorResta)
    VectorResta=VectorResta.reshape(tuple(listadedimensionesdelvector))
    
    return VectorResta

def multiescalar(vector1,vector2,listadedimensionesdelvector):
    escalar=int(input("Ingrese el escalar por el cual quiere multiplicar"))
    vector1.flatten()
    vector2.flatten()
    productoescalar=[]
    for i in range(len(vector1)):
        productoescalar.append(vector1[i]*escalar)
    
    productoescalar=np.array(productoescalar)
    productoescalar=productoescalar.reshape(tuple(listadedimensionesdelvector))
    
    escalar2=[]
    for i in range(len(vector2)):
        escalar2.append(vector2[i]*escalar)
    
    escalar2=np.array(escalar2)
    escalar2=escalar2.reshape(tuple(listadedimensionesdelvector))
    
    return productoescalar, escalar2

def norma(a,b):
    #vecotr de una sola dimension
    return a+b

def angulo(a,b):
    return a+b

    
    
def menu(vector1,vector2,listadedimensionesdelvector):
    while True:
        print(f"\nQue tipo de operacion deseas realizar con \n{vector1} \ny \n{vector2}\n\
              s para SUMAR\n\
              r para restar\n\
              p para producto por un escalar\n\
              n para encontrar la NORMA\n\
              a para encontrar el angulo\n\
              x para salir:")
        opcion=input()
        if opcion=='s':
            
            print(f"El Resultado de la Suma de \n{vector1} \ny \n{vector2} \nes: \n{suma(vector1,vector2,listadedimensionesdelvector)}")
        if opcion=='r':
            print(f"El Resultado de la Resta de \n{vector1} \ny \n{vector1} \nes: \n{resta(vector1,vector2,listadedimensionesdelvector)}")
        if opcion=='p':
            print(f"El Resultado del Producto Escalar de \n{vector1} \ny \n{vector1} \nes: \n{multiescalar(vector1,vector2,listadedimensionesdelvector)}")
      #  if opcion=='n':
          #  print(f"El Resultado de la Norma de {a} y {b} es: {suma(a,b)}")
    #    if opcion=='a':
     #       print(f"El Resultado del Angulo entre {a} y {b} es: {suma(a,b)}")
        if opcion =='x':
            break
        input("Presione cualquier tecla para volver a mostrar el menu  ")
       
vector1,tamanio,listadedimensionesdelvector=dimensionesdelvector()
vector2=segundovector(tamanio, listadedimensionesdelvector)
print(listadedimensionesdelvector)
menu(vector1, vector2,listadedimensionesdelvector)




            
                  
                                 