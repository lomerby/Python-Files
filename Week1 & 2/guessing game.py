import random
a= random.randint(0,100)
trial = 0
while True :
    trials = trial + 1
    print (trials)
    b = int(input ("input a random number \n :"))
    if b < a :
        print("too small")
    elif b == a :
        print ("correct")
        break
    else : print ("too large")