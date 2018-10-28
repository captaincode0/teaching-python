a = int(input("Introduce el número 1: "))
b = int(input("Introduce el número 2: "))
c = int(input("Introduce el número 3: "))

mayor = a

if a>b and a>c:
	mayor = a
elif b>a and b>c:
	mayor = b
else:
	mayor = c

print("El mayor es {0}".format(mayor))