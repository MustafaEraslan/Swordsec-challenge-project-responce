from multiprocessing import Process
import client

if __name__ == "__main__":
    COUNT = 10
    PROCESSES = {}
    for x in range(COUNT):
        PROCESSES[x] = Process(target=client.run)

    for x in range(COUNT):
        PROCESSES[x].start()