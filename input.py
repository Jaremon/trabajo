def pide_valor(mensaje, tipo=float, inf=-1, sup=1):
    while True:
        try:
            valor = tipo(input(mensaje))
            if inf < valor < sup:
                return valor
            else:
                print("Error: El valor debe estar en el intervalo ({}, {}).".format(inf, sup))
        except ValueError:
            print("Error: Introduce un valor numérico válido.")

def representar(xv, yv, title="Título", xlabel="Etiqueta eje X", ylabel="Etiqueta eje Y"):
    import matplotlib.pyplot as plt
    plt.plot(xv, yv, 'o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()