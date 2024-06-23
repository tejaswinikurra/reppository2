
expression = input().split(" ")
stack = []
operators = ["+", "-", "*", "/"]
for i in expression:
    if i not in operators:
        #print(i)
        stack.append(i)
        print(stack)
    if i in operators:
        print(i)
        n = int(stack.pop(0))
        n1 = int(stack.pop(0))
        print("n, n1:", n, n1)
        if i == "+":
            c = n+n1
            stack.append(c)
            #print(stack)
        elif i == "-":
            c = n-n1
            stack.append(c)
            #print(stack)
        elif i == "*":
            c = n*n1
            stack.append(c)
            #print(stack)
        elif i == "/":
            c = n/n1
            stack.append(c)
            #print(stack)
for k in stack:
    print(k)