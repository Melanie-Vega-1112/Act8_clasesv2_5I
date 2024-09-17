class Informacion:
    def mi_lista(self):
        lista_nomperros=["boby", "Dollar","fany"]
        for x in lista_nomperros:
            print(x)
            
# Creando el objeto
datos=Informacion()
print("listado de nombres de perros")
datos.mi_lista()

# Tuplas
print("---Tuplas---")
print("Razas de perros:")
razaperros=("pitbull", "chihuas", "doberman", "shitzu")
print(razaperros)

# Conjuntos
print("---conjuntos---")
print("Accesorios para mascotas")
accesorios=("correa", "moños", "shampoo")
print(accesorios)
for x in accesorios:
    print (x)
    
# Diccionario
print("---Diccionario---")
print("edades de perros")
dicc = {
    "pitbull": 3,
    "chihuahua": 5,
    "doberman": 2,
    "shitzu":1
    }
print(dicc)