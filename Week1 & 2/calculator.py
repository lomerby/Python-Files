
while True:
    try:
        num1 = int(input("input 1st  number \n:"))
    except ValueError:
        print("invalid input")
        op =  input("inpur operator\n :")
    try:
        num2 = int(input("input 2nd number \n:"))
    except ValueError:
        print("invalid input")
        match op :
            case "+":
                print(num1, "+",num2, "=",num1+num2)
            case "-":
                print (num1, "-",num2, "=",num1-num2)    
            case "/":
                print (num1, "/",num2, "=",num1/num2)   
            case "*":
                print (num1, "*",num2, "=",num1*num2) 
            case default:
                print("input proper operator")
                
