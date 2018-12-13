cus_name=input("enter customer name ")
units=int(input("enter units as consumed"))
print("1)industry slab")
print("2) commercial ")
print("3) residencial")

option = int(input("enter your option:"))

if option == 4:
    print("invalid")

else:
    if option == 1:
        totalbill=units*5.25
        print(totalbill)
    else:
        if option==2:
            totalbill=units*4.00
            print(totalbill)
        else:
            totalbill=units*3.08
            print(totalbill)