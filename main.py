from input import pide_valor, representar
from calculos import aproximacion_serie, error

def main():
    x = pide_valor("Introduce el valor de x (-1 < x < 1): ")
    N = int(pide_valor("Introduce el valor de N (1 <= N < 50): ", tipo=int, inf=1, sup=50))

    errores = []
    for i in range(1, N+1):
        errores.append(error(x, i))
    representar(list(range(1, N+1)), errores, title=f"Errores de aproximación para x={x}", xlabel="Número de términos (N)", ylabel="Error")

    print("Último error (N={}): {}".format(N, errores[-1]))
main()