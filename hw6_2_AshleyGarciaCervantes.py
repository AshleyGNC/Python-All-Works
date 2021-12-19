#File: hw6_2_AshleyGarciaCervantes.py
#Purpose: The program computes a real number to the power of an integer value (x^k) by using a function with 2 parameters.
#Name: Ashley Garcia Cervantes
#Date: 11/3/21

#====================== Funtion Definitions ====================
#Function: Computes the value of a real number to the power of another number
#Parameter: a real number(x), an integer value(k)
#Returns: the value of x^k
#Use: result = intpower(x,k)
def intpower(x,k):
    result = 1
    
    if k > 0:
        for power in range(k):
            result *= x
    
    elif k < 0:
        for power in range(-k):
            result *= x

        result = 1 / result
        
    return result


#============================= MAIN =============================
def main():
    print(" {:<10}{:<10}".format('K', '10^K'))
    print(f'------  ----------')
    # testing integer powers of 10
    for i in range(-5, 6):
          print(" {:<10}{:<10}".format(i, intpower(10, i)))
    
main()

