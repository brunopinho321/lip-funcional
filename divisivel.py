
#criar lista de numeros ate o numero que quer verificar
def listaNum(numero):
	return range(1,numero+1)

#retorna os numeros da lista que divide o numero que quer verificar
def divisivel(numero):
	f = lambda x, y = numero: y%x==0
	return filter(f, listaNum(numero))

#retorna se tem algo na lista e se o tamanho dela e maior que 2
def tamanho(lista):
	if not lista:
		return
	elif len(lista) == 2:
		return bool(1)
	else:
		return bool(0)

def primo(numero):
	return tamanho(divisivel(numero))

def listaPrimos(lista):
	return filter(primo,lista)

def entrada():
	return map(int, raw_input().split())	

def imprimir(lista):
	if len(lista) == 0:
		print ' '
	elif len(lista) == 1:
		print lista[0]
	else: 
		print lista[0],
		imprimir(lista[1:])

imprimir(listaPrimos(entrada()))
