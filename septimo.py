n=int(input("Introduce numero:"))

resto=n%2
if resto==0:
	print n,"Es par"
else:
	print n,"Es impar"

resto=n%3
if resto==0:
	print n,"Es multiplo de 3"

resto=n%5
if resto==0:
	print n,"Es multiplo de 5"

resto=n%7
if resto==0:
	print n,"Es multiplo de 7"
