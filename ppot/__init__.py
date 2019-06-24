import socket
import threading
class HoneyPot(object):
    def __init__(self,port_list,bindip,log):
        super(HoneyPot, self).__init__()
        self.port_list=port_list
        self.logger=log
        self.bindip=bindip
        self.listeners={}
        self.server=socket.socket()

        self.logger.debug('Initializing PPOT')

    def start_listening(self):
        for port in self.port_list:
            self.logger.info("Listening on {0}".format(port))
            self.listeners[port]=threading.Thread(target=self.start_new_listener_on_port,args=(port,))
            self.listeners[port].start()
    def start_new_listener_on_port(self,port):
        listener=socket.socket()
        listener.bind((self.bindip,int(port)))
        listener.listen(5)
        while True:
            client, add = listener.accept()
            client_handler=threading.Thread(target=self.handle_connection,args=(client,add[0],add[1]))
            client_handler.start()

    def handle_connection(self,client_socket,ip,port):
        self.logger.info("Connection  from {0} on port {1}".format(ip,port))
        client_socket.close()

    def run(self):
        self.start_listening()