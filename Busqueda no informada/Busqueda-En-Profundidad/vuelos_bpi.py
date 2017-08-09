# Vuelos con busqueda en profundidad iterativa
from arbol import Nodo

def DFS_prof_iter(nodo, solucion):
	for limite in range(0,100):
		visitados=[]
		sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
		if sol != None:
			return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
	if limite > 0:
		visitados.append(nodo)
		if nodo.get_datos == solucion:
			return nodo
		else: