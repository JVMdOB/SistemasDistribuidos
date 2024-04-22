import rpyc
import sys
import time

def gera_vetor(n):
    vetor = []
    for i in range(n):
        vetor.append(i)
    return vetor

def testa_vetor(vetor, conn, tamanho):
    print(f"Testando vetor de tamanho {tamanho}")
    start = time.time()
    print(f" Soma obtida: {conn.array_sum(vetor)}")
    end = time.time()
    print(f" Tempo de execução: {end-start} segundos")

def questao_8(conn):
    tamanho = 100
    vetor = gera_vetor(tamanho)
    testa_vetor(vetor, conn, tamanho)   
    tamanho = 1000
    vetor = gera_vetor(tamanho)
    testa_vetor(vetor, conn, tamanho)
    tamanho = 10000
    vetor = gera_vetor(tamanho)
    testa_vetor(vetor, conn, tamanho)

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
    
server = sys.argv[1]
tamanho_vetor = int(sys.argv[2])
conn = rpyc.connect(server,18861).root


print(f"Conexão estabelecida? - {conn.is_connected()}")
print(f"IP do servidor: {conn.get_server_ip()}")
questao_8(conn)