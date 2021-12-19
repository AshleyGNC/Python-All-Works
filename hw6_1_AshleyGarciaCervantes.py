#File: hw6_1_AshleyGarciaCervantes.py
#Purpose: The program provides information and processes the golden ratio constant by computing the formula.
#Name: Ashley Garcia Cervantes
#Date: 11/3/21
#==============================================================================

#=============================== Function Definition ==========================
#Funtion: Prints information about the golden ratio constant
#Parameter: None
#Return: None
def goldenRatioInfo():
    print('The golden ratio appears in some patterns in nature, including the spiral arrangement of leaves and other plant parts.', end='')
    print('When used in a design, it fosters organic and natural-looking compositions that are aesthetically pleasing to the eye.', end='')
    print('In photography, the Golden Ratio can help create a composition that will draw the eyes to the important elements of the photo.', end='')
    print('Whether it\'s to convey important information or to create an aesthetically pleasing photograph', end='')
    print('The Golden Ratio Constant has also been used to analyze the proportions of man-made systems such as financial markets.')


#-------------------------------------------------------------------------------
#Function: Prints the formula that defines how the constant is computed
#Parameter: None
#Return: None
def goldenRatioFormula():
    print('\nFormula: ')
    print('Golden Ratio Constant = (1 + math.sqrt(5)) / 2\n')


#-------------------------------------------------------------------------------
#Function: Computes the value of the golden ratio constant
#Parameter: None
#Return: the value of the golden ratio constant
#Use: value = goldenRation()
def goldenRatio():
    value = (1  + math.sqrt(5)) / 2
    return value


#===================================== MAIN ===================================   
import math

def main():
    goldenRatioInfo()
    goldenRatioFormula()
    print('Golden Ratio Constant =', goldenRatio())
    

main()
    
