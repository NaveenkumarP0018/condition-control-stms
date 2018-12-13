cus_name=input("enter customer name ")
units=int(input("enter units as consumed"))
print("1)industry slab")
print("2) commercial ")
print("3) residencial")

option = int(input("enter your option:"))

if option > 4:
    print("invalid")
else:
    if option==1:
        if units>100:
            totalbill=units*4.25
            print(totalbill)
        else:
            totalbill=units*3.55
            print(totalbill)
    else:
        if option == 2:
            if units>150:
                totalbill=units*5.55
                print(totalbill)
            else:
                totalbill=units*4.25
                print(totalbill)


        else:
            if option==3:
                if units>50:
                    totalbill=units*2.25
                    print(totalbill)
                else:
                    totalbill=units*1.25
                    print(totalbill)

print("good bye")

