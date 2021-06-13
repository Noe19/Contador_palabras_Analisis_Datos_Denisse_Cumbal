
palabras ={}
def iniciarContador():
  archivo= open('Contar.txt','r')
  linea = archivo.readline()
  lineas = linea.split()
  while linea!="":
     for palabra1 in lineas:
      if palabra1 in palabras:

        x=int(palabras[palabra1])
        palabras[palabra1]=x+1
      else:
        palabras[palabra1]=1
     linea = archivo.readline()
     lineas = linea.split()
  archivo.close()

def imprimir():
  for a in palabras:
    num = str(palabras[a])
    print(a+"= "+num)

iniciarContador()
print(" El numero de repeticion de las palabras es: ")
imprimir()