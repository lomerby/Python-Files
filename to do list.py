lis = {}
sn = 0


while True:
    x = input ("1)view to do list\n2)Add to list \n3)Edit list\n4)Quit\n:")
    if x == "1":
        if not lis:
            print ("To do list is empty\n:")
        else:
            print(lis)
            print ("TO DO LIST :")
            for i in lis:
                  
                print (i,lis[i],"\n")


    elif x == "2":
        task= input("Add a task to do list\n:")
        sn = sn + 1
        lis[sn] = task

    elif x == "4":
        break

    elif x == "3" :
        if not lis:
            print ("To do list is empty\n:")
        else:
            print ("TO DO LIST :")
            for i in lis:
                print (i,lis[i],"\n")
                
            popp= int(input("input a number to q    be deleted"))
            if popp in lis:
                lis.pop(popp)

       