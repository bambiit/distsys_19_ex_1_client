import socket


while True:


    sock_for_N1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_for_N1.connect(("localhost", 8001))

    print("Something")

    ## choose some product
    product = input("Gucci bag, 3000 euro\n"
                    "iPhone 11, 1000 euro\n"
                    "idk what to put, 2000 euro\n"
                    "(Please copy and paste as it is. No further function for this.)")
    price = product.split(", ")[1].split(" ")[0]
    product = product.split(", ")[0]


    sock_for_N1.send(price.encode())

    ## write the payment information of the customer
    name = input("Name : ")
    bank_account = input("Bank account : ")

    info_customer = name + ", " + bank_account
    sock_for_N1.send(info_customer.encode())


    ##wait the result from the server about whether it is possible to pay.
    data = sock_for_N1.recv(1024)


    sock_for_N1.close()

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

