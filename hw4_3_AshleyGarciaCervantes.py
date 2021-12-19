##################################################################
# File: hw4_3_AshleyGarciaCervantes.py
# Purpose: Practice for loops, dictionaries, and random. 
# Ashley Garcia  10/20/21
##################################################################
def main():
    import random
    hist = {
        2:'',
        3:'',
        4:'',
        5:'',
        6:'',
        7:'',
        8:'',
        9:'',
        10:'',
        11:'',
        12:'',
        }
  #input
    n = int(input('Enter number of rolls: '))
  #process
    for i in range(n):
        face1 = random.randint(1, 6)
        face2 = random.randint(1, 6)
        face_sum = (face1 + face2)
        hist[face_sum] += '*'
  #output
    for i in range(2, 13):
        print(f'{i}{hist[i]}')
                
    
main()
