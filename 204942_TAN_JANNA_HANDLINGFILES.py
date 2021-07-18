#product dictionary
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

#problem 1
def get_product(code):
    return products[code]


#problem 2
def get_property(code,property):
    return products[code][property]


#problem 3
def main():
    i=0
    raw_orders = []
    while True:
        clerk = input("Input customer's orders: ")
        if clerk =="/":
            break
        else:
            order_list = clerk.split(",")
            raw_orders += [order_list]
            i+=1
    a_qty=0
    b_qty=0
    c_qty=0
    d_qty=0
    e_qty=0
    f_qty=0
    total =0
    for j in raw_orders:
        order_code = j[0]
        order_qty = j[1]
        details = get_product(order_code)
        price = get_property(order_code,"price")
        name = details["name"]
        if name == "Americano":
            a_qty += int(order_qty)
            a_subtotal = str(price * a_qty)
        elif name == "Brewed Coffee":
            b_qty += int(order_qty)
            b_subtotal = str(price * b_qty)
        elif name == "Cappuccino":
            c_qty += int(order_qty)
            c_subtotal = str(price * c_qty)
        elif name == "Dalgona":
            d_qty += int(order_qty)
            d_subtotal = str(price * d_qty)
        elif name == "Espresso":
            e_qty += int(order_qty)
            e_subtotal = str(price * e_qty)
        elif name == "Frappuccino":
            f_qty += int(order_qty)
            f_subtotal = str(price * f_qty)

    with open("receipt.txt","w") as f:
        f.write("CODE\t\t\t\t\t\t\tNAME\t\t\t\t\t\tQUANTITY\t\t\t\t\tSUBTOTAL")
    with open("receipt.txt","a+") as f:
        if a_qty>0:
            f.write("\namericano\t\t\t\t\tAmericano\t\t\t\t"+str(a_qty)+"\t\t\t\t\t\t\t\t\t"+a_subtotal)
            total+=float(a_subtotal)
        if b_qty>0:
            f.write("\nbrewedcoffee\t\t\tBrewed Coffee\t\t"+str(b_qty)+"\t\t\t\t\t\t\t\t\t"+b_subtotal)
            total+=float(b_subtotal)
        if c_qty>0:
            f.write("\ncappuccino\t\t\t\tCappuccino\t\t\t"+str(c_qty)+"\t\t\t\t\t\t\t\t\t"+c_subtotal)
            total+=float(c_subtotal)
        if d_qty>0:
            f.write("\ndalgona\t\t\t\t\t\tDalgona\t\t\t\t\t"+str(d_qty)+"\t\t\t\t\t\t\t\t\t"+d_subtotal)
            total+=float(d_subtotal)
        if e_qty>0:
            f.write("\nespresso\t\t\t\t\tEspresso\t\t\t\t"+str(e_qty)+"\t\t\t\t\t\t\t\t\t"+e_subtotal)
            total+=float(e_subtotal)
        if f_qty>0:
            f.write("\nfrappuccino\t\t\t\tFrappuccino\t\t\t"+str(f_qty)+"\t\t\t\t\t\t\t\t\t"+f_subtotal)
            total+=float(f_subtotal)
        f.write("\n")
        f.write("\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(total))


main()
