na=input("enter employee name:")
sal=int(input("enter salary:"))
print("1) manger")
print("2) analysit")
print("3) clerk")
option=int(input("enter your option"))

if option > 4:
    print("u enter option is invalid")
else:
    if option==1:
        totalsal=sal*0.2
        print("bonus sal=", totalsal)
        print("totalsalary=", totalsal+sal)
    else:
        if option == 2:
            totalsal=sal*0.1
            print("bonus sal=",totalsal)
            print("totalsalary=",totalsal+sal)
        else:
            totalsal=sal*0.5
            print("bonous sal=",totalsal)
            print("totalsalary=",totalsal+sal)
            



