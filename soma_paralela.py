import time
import threading

def soma_parcial(linhas, resultados, indice):
    soma = 0
    for linha in linhas:
        soma += int(linha.strip())
    resultados[indice] = soma


def soma_paralela(arquivo, n_threads):

    with open(arquivo, "r") as f:
        linhas = f.readlines()

    tamanho = len(linhas)
    bloco = tamanho // n_threads

    threads = []
    resultados = [0] * n_threads

    for i in range(n_threads):

        inicio = i * bloco
        fim = (i + 1) * bloco if i != n_threads - 1 else tamanho

        parte = linhas[inicio:fim]

        t = threading.Thread(
            target=soma_parcial,
            args=(parte, resultados, i)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sum(resultados)


if __name__ == "__main__":

    arquivo = "numero1.txt"

    for n in [2,4,8,12]:

        inicio = time.time()

        resultado = soma_paralela(arquivo, n)

        fim = time.time()

        tempo = fim - inicio

        print("Threads:", n)
        print("Soma:", resultado)
        print("Tempo:", tempo, "segundos")
        print("----------------------")
