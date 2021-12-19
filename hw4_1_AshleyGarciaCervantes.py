##################################################################
# File: hw4_1_AshleyGarciaCervantes.py
# Purpose: Practice for loops and random. 
# Ashley Garcia  10/20/21
##################################################################
def main():
    import random
    #input
    n = int(input('Enter number of rolls: '))
    counts = [0, 0]
    #process
    for i in range(n):
        face = random.randint(1, 6)
        print(face)
        if face % 2 != 0:
            counts[0] += 1
        else:
            counts[1] += 1
    #output
    print('Number of times Odd Numbers ocurred:', counts[0])
    print('Number of times Even Numbers ocurred:', counts[1])
    
main()
    
