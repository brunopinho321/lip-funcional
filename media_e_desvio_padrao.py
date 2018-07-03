def soma(lista):
	if not lista:
		return 0
	else:
		return lista[0] + soma(lista[1:])
	
def media(lista):
	return soma(lista)/float(len(lista))
		
def menosMedia(lista):
	menos = lambda num: num - media(lista)
	return map(menos,lista)	

potencia = lambda num: num**2

def varianca(lista):
	quadrado = lambda lista: map(potencia,lista)
	return media(quadrado(menosMedia(lista)))

def desviopadrao(lista):
	return (varianca(lista)**(0.5))

def mediaEdesvio(lista):
	return [media(lista),desviopadrao(lista)]	

def imprimir(lista):
	if len(lista) == 1:
		print lista[0]
	else: 
		print lista[0],
		imprimir(lista[1:])

def entrada():
	return map(float, raw_input().split())		

imprimir(mediaEdesvio(entrada()))
