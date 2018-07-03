def tamanho(lista):
	if not lista:
		return 0
	else: 
		return 1+tamanho(lista[1:])

def imprimir(lista):
	if tamanho(lista) == 1:
		print lista[0]
	else: 
		print lista[0],
		imprimir(lista[1:])
	
def imprimir2(num):
	imprimir(map(f,range(1,num+1)))

def f(num):
	if num <= 1:
		return num
	else:
		return f(num-1) + f(num-2)


imprimir2(int(input()))
