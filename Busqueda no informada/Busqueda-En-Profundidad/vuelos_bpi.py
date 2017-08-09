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
			# expandir nodos hijo (ciudades con conexiones)
			dato_nodo = nodo.get_datos()
			lista_hijos = []
			for un_hijo in conexiones[dato_nodo]:
				hijo = Nodo(un_hijo)
				if not hijo.en_lista(visitados):
					lista_hijos.append(hijo)

			nodo.set_hijos(lista_hijos)

			for nodo_hijo in nodo.get_hijos():
				if not nodo_hijo.get_datos() in visitados:
					# llamada recursiva
					sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1)
					if sol != None:
						return sol

		return None
