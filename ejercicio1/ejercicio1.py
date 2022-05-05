""""taller-ejercicio1:
averiguar en que cuadrante esta el eje X y y"""

print("----------------------------------------")
print("---------- cordenada X y Y -------------")
print("----------------------------------------")

# input
X=int(input("digite la cordenada X: "))
Y=int(input("digite la cordenada Y: "))

# processing
if X>0 and Y>0:
    print("el punto esta en primer cuadrante")
else:
    if  X<0 and Y>0:
        print("el punto esta en el segundo cuadrante")
if  X<0 and Y<0:
    print("el punto esta en el tercer cuadrante")
else:
    if  X>0 and Y<0:
        print("el punto esta en el cuarto cuadrante")
if X==0 and Y==0:
    print("el punto esta en el punto de origen")