import random
task = {1: "A", 2: "C", 3: "C", 4: "D", 5: "C"}
b = 0
x = [1, 2, 3, 4, 5]
counter = 0
random.shuffle(x)

while b < 5:
    for i in x:
        b = b + 1
        if i == 1:
            while True:
                qst1 = input("whats the larget planet in out solar system :\n A)jupiter\nB)Mars\nC)Earth\nD)Pluto").lower().strip()
                if qst1 in ['a', 'jupiter']:
                    print("correct")
                    counter = counter + 1
                    break
                elif qst1 in ['b', 'c', 'd']:
                    print("wrong")
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D")

        if i == 2:
            while True:
                qst2 = input("whats the larget number :\n A)201\nB)40\nC)50000\nD)30").lower().strip()
                if qst2 in ['a', 'b', 'c', 'd']:
                    if qst2 == 'c':
                        print("correct")
                        counter = counter + 1
                    else:
                        print("wrong")
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D")

        if i == 3:
            while True:
                qst3 = input("whats the smallest number :\n A)100\nB)40\nC)5\nD)30").lower().strip()
                if qst3 in ['a', 'b', 'c', 'd']:
                    if qst3 == 'c':
                        print("correct")
                        counter = counter + 1
                    else:
                        print("wrong")
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D")

        if i == 4:
            while True:
                qst4 = input("whats the even number :\n A)201\nB)403\nC)500001\nD)30").lower().strip()
                if qst4 in ['a', 'b', 'c', 'd']:
                    if qst4 == 'd':
                        print("correct")
                        counter = counter + 1
                    else:
                        print("wrong")
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D")

        if i == 5:
            while True:
                qst5 = input("whats the odd number :\n A)20\nB)40\nC)500001\nD)30").lower().strip()
                if qst5 in ['a', 'b', 'c', 'd']:
                    if qst5 == 'c':
                        print("correct")
                        counter = counter + 1
                    else:
                        print("wrong")
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D")

print("your score is :", counter)

# Refactor quiz input handling for improved validation and readability