import math

def distancia_euclidiana(x_1, y_1, x_2, y_2)->float:
    x = x_2 - x_1
    y = y_2 - y_1

    return (math.sqrt((x*x)-(y*y)))


    