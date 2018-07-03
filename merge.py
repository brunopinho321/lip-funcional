def me(l1,l2):
	if not l1:
		return l2
	if not l2:
		return l1
	if l1[0] > l2[0]:
		return [l2[0]]+me(l1,l2[1:])
	if l1[0] < l2[0]:
		return [l1[0]]+me(l1[1:],l2)
	if l1[0] == l2[0]:
		return [l2[0]]+[l1[0]]+me(l1[1:],l2[1:])

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


imprimir(me(entrada(),entrada()))
