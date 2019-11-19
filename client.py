import socket
import sys

while True:


    #chooses some product.
    product = input("Gucci bag, 3000 euro\n"
                    "iPhone 11, 1000 euro\n"
                    "idk what to put, 2000 euro\n"
                    "(Please copy and paste the whole line as it is."
                    "No further function for this.)")

    price = product.split(", ")[1].split(" ")[0]
    product = product.split(", ")[0]

    #connects with the server.
    sock_for_N1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_for_N1.connect((sys.argv[1], 8001))

    sock_for_N1.send(price.encode())

    #writes the payment information of the customer.
    name = input("Name : ")
    bank_account = input("Bank account : ")

    #ends the information to the server.
    info_customer = name + ", " + bank_account
    sock_for_N1.send(info_customer.encode())



    #waits the result from the server about whether it is possible to pay.
    data = sock_for_N1.recv(1024)

    #closes the socket.
    sock_for_N1.close()

    #prints the result.
    if data.decode() == "OK":
        print("Payment succeeded.")
        print("You boguht " + product + "\n The price is " + price)
        break

    else:
        print("Payment failed.\n")
        print("The reason is : ")
        print(data.decode()+"\n")
        print("Do you want to try again?\n")
        user_input = input("If yes : Y\n")
        if user_input == "Y":
            print("\n\n\n")
        else:
            break

