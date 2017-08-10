# Viaje por carretera con busqueda de coste uniforme
from arbol import Nodo

def compara(x, y):
	return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
	solucionado = False
	nodos_visitados = []
	nodos_frontera = []
	