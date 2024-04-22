import rpyc
import socket

class MyService(rpyc.Service):

    def exposed_get_server_ip(self):
        return socket.gethostbyname(socket.gethostname())

    def __init__(self):
        self.connected = False

    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        self.connected = True
        print(f"Conexão iniciada com cliente localizado em IP: {conn._channel.stream.sock.getpeername()[0]} e Porta: {conn._channel.stream.sock.getpeername()[1]}")

    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        self.connected = False
        print(f"Conexão encerrada com cliente localizado em {conn._channel.stream.sock.getpeername()}")

    def exposed_array_sum(self, array):
        if self.connected:
            return sum(array)
        else:
            print("Conexão não estabelecida")

    def exposed_get_answer(self): 
        # este é um método exposto
        return 42

    exposed_the_real_answer_though = 43     # este é um atributo exposto

    def exposed_get_question(self):  
        # este método não é exposto
        return "Qual é  a cor do cavalo branco de Napoleão?"

    def exposed_connect(self):
        # este é um método exposto para conectar
        self.connected = True

    def exposed_disconnect(self):
        # este é um método exposto para desconectar
        self.connected = False
        

    def exposed_is_connected(self):
        # este é um método exposto para verificar se está conectado
        return self.connected

#Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()