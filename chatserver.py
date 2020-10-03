 import socket
import threading

class Server:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections=[]
    host=""
    port=8888
    def __init__(self):
        self.sock.bind((self.host,self.port))
        self.sock.listen(2)

    def handler(self,c,a):
        while True:
            try:
                data=c.recv(1024)
                for connection in self.connections:
                    if connection != c:
                        connection.send(data)
                if not data:
                    print(str(a[0])+" : "+str(a[1])," disconnected")
                    self.connections.remove(c)
                    c.close()
                    break
            except:
                print(str(a[0])+" : "+str(a[1])," disconnected")
                self.connections.remove(c)
                c.close()
                break

                

    def run(self):
        while True:
            try:
                c,a=self.sock.accept()
                cthread=threading.Thread(target=self.handler,args=(c,a))
                cthread.daemon=True
                cthread.start()
                self.connections.append(c)
                print(str(a[0])+" : "+str(a[1]),"Connected")
            except:
                print(str(a[0])+" : "+str(a[1])," disconnected")
                self.connections.remove(c)
                c.close()
                continue
                

server=Server()
server.run()
