"""
Instalar la biblioteca de Python `twisted` 
y crear un servidor de chat que permita 
a los usuarios enviar mensajes a todos 
los demás usuarios conectados.
"""
from twisted.internet import protocol, reactor


class ChatServer(protocol.Protocol):
    """
    Servidor de chat que permite a los usuarios
    """
    connections = []

    def connectionMade(self):
        """
        Se llama cuando un cliente se conecta al servidor.
        """

        print("Cliente conectado:", self.transport.getPeer())
        self.connections.append(self)

    def connectionLost(self, reason):
        """
        Se llama cuando un cliente se desconecta del servidor.
        """

        print("Cliente desconectado:", self.transport.getPeer())
        self.connections.remove(self)

    def dataReceived(self, data):
        """
        Se llama cuando un cliente envía un mensaje al servidor.
        """

        message = data.decode()
        print("Mensaje recibido:", message)

        # Enviar el mensaje a todos los clientes conectados
        for client in self.connections:
            client.transport.write(data)


class ChatServerFactory(protocol.Factory):
    """
    Fábrica de servidores de chat.
    """

    def buildProtocol(self, addr):
        """
        Construir un servidor de chat.
        """

        return ChatServer()


# Iniciar el servidor de chat
if __name__ == '__main__':

    reactor.listenTCP(8000, ChatServerFactory())

    print("Servidor de chat iniciado en el puerto 8000...")

    reactor.run()
