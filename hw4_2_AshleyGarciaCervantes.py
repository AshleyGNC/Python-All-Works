##################################################################
# File: hw4_2_AshleyGarciaCervantes.py
# Purpose: Practice for loops and random. 
# Ashley Garcia  10/20/21
##################################################################
def main():
    import random
    the_sum = 0
    #input
    n = int(input('Enter number of rolls: '))
    #process
    for i in range(n):
        face1 = random.randint(1, 6)
        face2 = random.randint(1, 6)
        print(face1, face2)
        if (face1 + face2) == 6 or (face1 + face2) == 7:
            the_sum += 1 
        
    #output        
    print('Number of successes (sum is in [6, 7]) is', the_sum)
    
main()
    
