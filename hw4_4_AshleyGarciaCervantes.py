##################################################################
# File: hw4_3_AshleyGarciaCervantes.py
# Purpose: Practice for loops, dictionaries, and random. 
# Ashley Garcia  10/20/21
##################################################################
def main():
    import random
    #initialize variables
    num_rolls = 0
    total = 0
    faces = []
    face = 1
    curr_face = random.randint(1, 6)
    
    #process
    while curr_face >= face:
        faces.append(curr_face)
        num_rolls += 1
        total += curr_face
        face = curr_face
        curr_face = random.randint(1,6)
        
    #output
    print('All rolled faces:',faces)
    print('Total number of successful rolls:', total)
    print('Number successful rolls:', num_rolls)
main()
    
    
    
