a=int(input("Enter number a"))
b=int(input("Enter number b"))

print("Enter you choice\n 1.Add\n 2.Sub\n 3.Div\n 4.Multiply")
ch=int(input("Enter Choice"))

match ch:
    case 1:
        def add(a,b):
            return(a+b)
        print(add(a,b))

    case 2:
        def sub(a,b):
            return(a-b)
        print(sub(a,b))

    case 3:
        def div(a,b):
            return(a/b)
        print(div(a,b))

    case 4:
        def mul(a,b):
            return(a*b)
        print(mul(a,b))    

    case _:
        print("INvalid")