#SUBPROGRAMA
import math
def processa_distancia_p(* points: int) -> float: 
    dist = 0
    i = j = 0
    P1 = 0
    while i < 2 and j < 2:
        P1 += (points[i] ** 2) + (points[i] ** 2)
        i += 1
        j += 1
    dist = math.sqrt(P1)
    return dist


def dobra_valores(* numbers):
    Lista = tuple(map(*2, numbers))
    return Lista


#PROGRAMA PRINCIPAL
distancia = processa_distancia_p(56, 34, 24, 90)
print(f' A DISTAMCIA É: {distancia}')
