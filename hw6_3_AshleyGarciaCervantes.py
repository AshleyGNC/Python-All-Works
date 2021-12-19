#File: hw6_3_AshleyGarciaCervantes.py
#Purpose: The program reads a grade scale and student IDs and test scores for each student,
#         assigns grades to each student and print the average test score,
#         the grade scale and corresponding grade, then a table of student IDs and assigned grades.
#Name: Ashley Garcia Cervantes
#Date: 11/3/21
#===================================================================================

#========================== Function Definitions ===================================
#Function: inputs grades and appends to list
#Parameter: None
#Return: a list with the grades inputed by user
#Use: scale = getScale()
def getScale():
    n = 0
    number = 0
    scale = []
    while n < 4:
        grade = int(input('Enter integer values between 0 - 100, increasing: '))
        
        #Validate the input. Value entry is between 0 and 100 and is greater than previous.
        if grade > 0 and grade < 100:
            if number < grade:
                scale.append(grade)
                number = grade
                n += 1
            
    return scale

#------------------------------------------------------------------------------------
#Function: inputs ID and Test Scores, adds such values to a dictionary
#Parameter: None
#Return: a dictionary where the key is ID numbers and the value associated is the score
#Use: scores = getData()
def getData():
    dataStr = input('Enter ID and Test Score, press enter to stop: ')
    scores = {}
    while dataStr != '':
        dataStr = dataStr.split( )
        data = [int(x) for x in dataStr]

        # Validate the input. Repeat prompt till valid value is entered.
        if data[0] >= 100 and data[0] <= 999:
            if data[1] >= 0  and data[1] <= 100:
                scores[data[0]] = data[1]
                dataStr = input('Enter ID and Test Score, press enter to stop: ')
            else:
                dataStr = input('Invalid- Enter ID and Test Score, press enter to stop: ')
        else:
            dataStr = input('Invalid- Enter ID and Test Score, press enter to stop: ')
     
    return scores


#--------------------------------------------------------------------------------------
#Function: Assigns a letter grade to each score based on the scale
#Parameter: list of numbers scale, student score for one student
#Return: a grade letter per student's score
#Use: grade = setGrade(scale, a_score)
def setGrade(scale, a_score):
    if a_score < scale[0]:
        grade = 'F'

    elif a_score < scale[1] and a_score >= scale[0]:
        grade = 'D'

    elif a_score < scale[2] and a_score >= scale[1]:
        grade = 'C'
        
    elif a_score < scale[3] and a_score >= scale[2]:
        grade = 'B'
        
    elif a_score >= scale[3]:
        grade = 'A'

    return grade


#----------------------------------------------------------------------------------------
#Function: Calculates the average test score
#Parameter: dictionary of students' scores
#Return: the average test score
#Use: average = average(scores)
def average(scores):
    sumScores = 0
    for i in scores:
        sumScores += int(scores[i])
    average = sumScores / len(scores)
    return average


#-----------------------------------------------------------------------------------------
#Function: Prints the grade letter based on the scale
#Parameter: list scale[]
#Return: None
def printScale(scale):
    letters = ['A', 'B', 'C', 'D', 'F']
    for i in range(len(letters)):
        if i == 0:
            print(f'{letters[i]}       score >= {scale[-1 -i]}')
        elif i == 4:
            print(f'{letters[i]} {scale[-i]-1} >= score')
        else:
            print(f'{letters[i]} {scale[-i]-1} >= score >= {scale[-1 -i]}')


#-----------------------------------------------------------------------------------------
#Funtion: Prints a table with student IDs and Grades
#Parameter: dictionary grades{}
#Return: None
def printGrades(grades):
    print ("{:<10} {:<10}".format('ID', 'GRADE'))
    for key, value in grades.items():
        print ("{:<10} {:<10} ".format(key, value))
        

            
#===================================== MAIN ==============================================
def main():
    scale = getScale()
    scores = getData() 
    grades = {} #stores Student IDs with respective grade letter.
    for i in scores:
        grades[i] = setGrade(scale, scores[i])
    print(f'\nThe average score is: {average(scores):.0f}\n')
    printScale(scale)
    print()
    printGrades(grades)
    
main()
