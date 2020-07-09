from concurrent import futures
import grpc
import sendsave_pb2
import sendsave_pb2_grpc
import time 
import threading
import json 

class listener(sendsave_pb2_grpc.SendSaveServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()
    
    def Send(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):

        file1= open("1.json","r", encoding="utf8")
        data1=json.load(file1)

        file2= open("2.json","r", encoding="utf8")
        data2=json.load(file2)

        file3= open("3.json","r", encoding="utf8")
        data3=json.load(file3)

        file4= open("4.json","r", encoding="utf8")
        data4=json.load(file4)

        file5= open("5.json","r", encoding="utf8")
        data5=json.load(file5)

        file6= open("6.json","r", encoding="utf8")
        data6=json.load(file6)

        file7= open("7.json","r", encoding="utf8")
        data7=json.load(file7)

        file8= open("8.json","r", encoding="utf8")
        data8=json.load(file8)

        file9= open("9.json","r", encoding="utf8")
        data9=json.load(file9)

        file10= open("10.json","r", encoding="utf8")
        data10=json.load(file10)

    def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        sends ave_pb2_grpc.add_SendSaveServiceServicer_to_server(Listener(), server)
        server.add_insecure_port("[::]:9999")
        server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)



if __name__ == "__main__":
    serve()        

