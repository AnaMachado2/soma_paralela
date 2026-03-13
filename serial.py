import time

def soma_serial(arquivo):
    soma = 0

    with open(arquivo, "r") as f:
        for linha in f:
            soma += int(linha.strip())

    return soma


if __name__ == "__main__":

    arquivo = "numero1.txt"

    inicio = time.time()

    resultado = soma_serial(arquivo)

    fim = time.time()

    tempo = fim - inicio

    print("Soma:", resultado)
    print("Tempo de execução:", tempo, "segundos")
