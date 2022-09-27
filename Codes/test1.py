print("Welcome to the Shopping Cart Program!")
cart = []
prices = []
total = []
total_price = []
while True:
    print()
    print ("Please type in one of these")
    print ("1. Add item ")
    print ("2. View cart ")
    print ("3. Remove Item ")
    print ("4 compute total")
 
    select = int(input(" Type in a number to go on "))
    item = ""
    if select == 1:
        while item != "ok":
            item = input(" What would you like to add?  ")
            price = float(input(" type in the price "))
            prices.append(price)
             
            ok = input ("type in ok when you're done.")
            if item != "ok":
                cart.append(item)
                print(f"'{item}' has been added to your cart.")
                print(f" The price is ${price}")
                break
    if select == 2:
        print("This is what is in your shopping cart")
        for item in cart:
            print(item,price)
            ok = input ("press ok when you're done")
            if item != "ok":
                break
             
     
                     
    if select == 3:
        takeout = input(" Type in what you would like to remove?  ")
        cart.remove(takeout)
        continue
         
     
    if select == 4:
        for price in total_price:
            sum+= price
            print(sum(total_price))
            input ("type in ok when you're done")
            if item != "ok":
                break
             
             
         
    if select == 5:
        print ("comeback soon.")
        break