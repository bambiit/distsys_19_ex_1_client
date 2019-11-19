import socket
from random import randrange
from multiprocessing import Pool
from contextlib import closing
import string
import random
import datetime

HOST = ""
PORT = 8001


def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(50))


def connect_to_server(call_no):
   try:
       print("Connect to Server ", call_no)
       sock_for_N1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock_for_N1.connect((HOST, PORT))

       bank_account = random.randint(0, 999999999999999999)
       amount = randrange(12000)
       name = random_string()

       sock_for_N1.sendall(str.encode("\n".join([str(bank_account), str(amount), name])))

       ##wait the result from the server about whether it is possible to pay.
       data = sock_for_N1.recv(1024)

       sock_for_N1.close()

       if data.decode() == "OK":
           print("Payment succeeded.")

       else:
           print("Payment failed.\n")
           print("The reason is : ")
           print(data.decode() + "\n")
   except Exception as err:
        print("There is an error ", err.message)


def main():
    loop = 50
    call_no_array = []
    for x in range(0, loop):
        call_no_array.append(x)

    start_time = datetime.datetime.now()

    with closing(Pool(processes=50)) as pool :
        pool.map(connect_to_server, call_no_array)
        pool.terminate()

    end_time = datetime.datetime.now()

    duration = end_time - start_time
    print duration


if __name__ == '__main__':
    main()
