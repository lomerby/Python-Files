import random
task = {1: "A" , 2: "C",3: "C",4:"D", 5:"C"}
b = (0)
x = [1, 2, 3, 4, 5]
counter =(0)
random.shuffle(x)
while b < 5:
    for i in x :
        b = b + 1
        if i == 1:
            qst1=input("whats the larget planet in out solar system :\n A)jupiter\nB)Mars\nC)Earth\nD)Pluto")
            if qst1 == "a":
                print ("correct")
                counter = counter + 1
            else :
                print ("wrong")    

        
        if i == 2:
            b = b + 1
            qst2=input("whats the larget number :\n A)201\nB)40\nC)50000\nD)30")
            if qst2 == "c":
                print ("correct")
                counter = counter + 1
            else :
                print ("wrong")         

    
    
        if i == 3:
            b = b + 1
            qst3=input("whats the smallest number :\n A)100\nB)40\nC)5\nD)30")
            if qst3 == "c":
                print ("correct")
                counter = counter + 1
            else :
                print ("wrong")          
            
        if i == 4:
            b = b + 1
            qst4=input("whats the even number :\n A)201\nB)403\nC)500001\nD)30")
            if qst4 == "d":
                print ("correct")
                counter = counter + 1
            else :
                print ("wrong")  

        if i == 5:
            b = b + 1
            qst5=input("whats the odd number :\n A)20\nB)40\nC)500001\nD)30")
            if qst5 == "c":
                print ("correct")
                counter = counter + 1
            else :
                print ("wrong")              
print ("your score is :",counter)