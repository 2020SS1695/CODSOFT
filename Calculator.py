
print('SIMPLE CALCULATOR : \n   ON OFF  ^   % \n   7   8   9   / \n   4   5   6   * \n   1   2   3   - \n   0   .   =   +')
input('PLEASE CLICK ON "ENTER" BUTTON TO SWITH ON THE CALCULATOR\n')
while(1) :
    m=float(input('ENTER THE FIRST NUMBER\n'))
    n=float(input('ENTER THE SECOND NUMBER\n'))
    op=input('ENTER THE OPERATION YOU WANT TO PERFOM (+, -, *, /, %, ^ )\n')
    match op:
        case "+":
            print(m, "+", n , "=", m+n) 
            print('\n')
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case "-":
            print(m, "-", n , "=", m-n)
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case "*":
            print(m, "*", n , "=", m*n)
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case "/":
            print(m, "/", n , "=", m/n)
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case "%":
            print(m, "%", n , "=", m%n)
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case "^":
            print(m, "^", n , "=", m**n)
            p=input('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION\n')
            match p:
                case "0":
                    exit(0)
                case "1":
                    print('\n') 
                case _:
                    print('CLICK ON "0" TO SWITCH OFF THE CALCULATOR \t CLICK ON "1" TO CONTINUE THE CALCULATION')
        case _:
            print('INVALID INPUT, PLEASE TRY AGAIN..')
        
        

