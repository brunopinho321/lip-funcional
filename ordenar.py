def ordenar(lista):
		if len(lista) <= 1:
			return lista 
		else:
				menor = lambda i, j = lista[0]: i<j 
				igual = lambda i, j = lista[0]: i==j
				maior = lambda i, j = lista[0]: i>j
				return ordenar(filter(menor,lista)) + filter(igual,lista) +ordenar( filter(maior,lista))

def entrada():
	return map(int, raw_input().split())	

def imprimir(lista):
	if len(lista) == 0:
		print ''
	elif len(lista) == 1:
		print lista[0]
	else: 
		print lista[0],
		imprimir(lista[1:])


imprimir(ordenar(entrada()))
