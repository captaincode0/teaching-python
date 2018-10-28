# Data types
'''
	Simples
		Números
			Reales
			Complejos
			Enteros
				Representación
					Binaria
					Octal
					Decimal
					Hexadecimal
		Boleaanos
			True, False
		Cadena (String)
			"hello world"
'''


'''
	Operadores numéricos
		>: mayor que
		<: menor que
		<=: menor o igual que
		>=: mayor o igual que
'''

x = 97
print(x)
x = b'01100001'
print(x)
x = 0x61
print(x)

y = 0.123711391
print(y)

string = "Moy"
print(string)

'''
	Operaciones lógicas
		-And (and, &&)
		-Or (or, ||)
		-Xor (xor, ~) 
		-Not (not, !)

	Operadores
		= : igual a
		!= : diferente de
'''

is_son_of_my_grandmother = True
is_brother_of_my_mother = False

print("Is my uncle? {0}".format(is_son_of_my_grandmother and is_brother_of_my_mother))

a = 5
b = 2

print(a>5)
print(a>b)
print(b>a)
print(a<=b)
print(b<=a)