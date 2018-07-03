def f1(lista,p,q):
	troca = lambda num: num if num != p else p+q
	return map(troca,lista)
	
	
def imprimir(lista):
	if len(lista) == 1:
		print lista[0]
	else: 
		print lista[0],
		imprimir(lista[1:])
		
def entrada():
	return map(int, raw_input().split())	
		
imprimir(f1(entrada(),int(input()),int(input())))
