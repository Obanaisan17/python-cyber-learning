import threading
import logging
import time

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

def threadFunction(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(5)
    logging.info(f"Thread {name}: finishing")

logging.info("-----Creating-------")
t = threading.Thread(target=threadFunction, args=(1,))

logging.info("-----Start-------")
t.start()

logging.info("----waiting------")
t.join()
print("something")
