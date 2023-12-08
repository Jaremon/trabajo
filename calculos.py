def aproximacion_serie(x, N):
    resultado = 0
    for i in range(1, N+1):
        resultado += (x**i)/i
    return resultado

def error(x, N):
    convergencia = 1/(1 - x)
    aproximacion = aproximacion_serie(x, N)
    error = abs(convergencia - aproximacion)
    return error