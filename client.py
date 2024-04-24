import rpyc
import sys
import time

def gera_vetor(n):
    vetor = []
    for i in range(n):
        vetor.append(i)
    return vetor

def testa_vetor(conn, tamanho):
    print(f"Testando soma de vetor de tamanho {tamanho}")
    start = time.time()
    vetor = gera_vetor(tamanho)
    print(f" Soma obtida: {conn.soma_vetor(vetor)}")
    end = time.time()
    print(f" Tempo de execução no cliente: {end-start} segundos")

def questao_1(conn):
    print(conn)
    print(conn.get_answer())
    print(conn.the_real_answer_though)

def questao_2(conn):
    questao_1(conn)

def questao_3(conn):
    print(conn.get_question())

def questao_4(conn):
    tamanho_vetor= 10000
    v = gera_vetor(tamanho_vetor)
    soma = conn.soma_vetor(v)
    print(f"Resultado da soma do vetor de tamanho {tamanho_vetor}: {soma}")

def questao_5(conn):
    tamanho_vetor = 10000
    testa_vetor(conn, tamanho_vetor)

def questao_8(conn):
    tamanho = 100
    testa_vetor(conn, tamanho)   
    tamanho = 1000
    testa_vetor(conn, tamanho)
    tamanho = 10000
    testa_vetor(conn, tamanho)

def questao_9(conn):
    questao_8(conn)

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
if __name__ == "__main__":
    server = sys.argv[1]
    conn = rpyc.connect(server,18861).root


    print(f"Conexão estabelecida? - {conn.is_connected()}")
    print(f"IP do servidor: {conn.get_server_ip()}")
    q = input("Digite o número da questão que deseja executar: ")
    eval(f"questao_{q}")(conn)
