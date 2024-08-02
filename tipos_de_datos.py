import numpy as np 

arr = np.array([1,2,3,4], dtype="float64")#Definiendo un array con una lista
print(arr)
arr.dtype #imprimir el tipo de dato
print(arr.dtype)

#otra forma
arr = np.array([1,2,3,4])#Definiendo un array con una lista
print(arr)
arr = arr.astype(np.float64) #imprimir el tipo de dato
print(arr.dtype)

#Forma Boliana
arr = np.array([0,1,2,3,4])#Definiendo un array con una lista
arr = arr.astype(np.bool_)
print(arr)

#estrick_str
arr = np.array([0,1,2,3,4])#Definiendo un array con una lista
arr = arr.astype(np.str_)
print(arr)

#entero
arr = np.array(["0","1","2","3","4"])#Definiendo un array con una lista
arr = arr.astype(np.int8)
print(arr)

