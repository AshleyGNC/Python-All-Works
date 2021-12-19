##################################################################
# File: hw7_AshleyGarciaCervantes.py
# Purpose: Practice string, lists, dictionaries.
# Ashley Garcia 12/1/21
##################################################################
#============= Function Definiton ==================
#Function: inputs a phrase and gets the acronym
#Parameter: None
#Return: a string with the acronym of the phrase given
def acronym():
    text = input('Enter phrase: ')
    list_text = text.strip().split()
    new_text = []

    for i in list_text:
        if i[0] < 'a':
            new_text.append(i[0])

    acronym = ''.join(str(e) for e in new_text)

    return acronym


#Function: gives the positive numbers of a list in ascending order, without repetitions.
#Parameter: list of numbers. (lst)
#Return: a string with the positive numbers in ascending order. (new_lst)
def processList(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if int(i) >= 0:
            new_lst.append(i)

    #remove repeats    
    for num in new_lst:
        if new_lst.count(num) > 1:
            new_lst.remove(num)
            
    new_lst = ' '.join(str(e) for e in new_lst)
    
    return new_lst


#Function: takes the words in a given sentence(str) and counts the number of times that word appears in the sentence.
#Parameter: list of words from the sentence inputed. (tokens)
#Return: dictionary that has as key the words on the list and as value the amount of times the words appear in the list. (dic)
def wordCount(tokens):
    dic = {}
    for token in tokens:
        dic[token] = tokens.count(token)
    return dic
    
   

#================================ MAIN =====================================
def main():
#-------------- Testing acronym()-----------------
    print(acronym())

#-------------- Testing processList()-------------   
    lst_strg = input('Enter a set of numbers separated by space: ')
    lst = lst_strg.strip().split()
    print(processList(lst))
    
#-------------- Testing wordCount()---------------
    strg = input('Enter text: ')
    lst = strg.strip().split()
    
    #making a list without special characters
    newlst = []
    for word in lst:
        newlst.append(''.join(letter for letter in word if letter.isalnum()))

    maindict = wordCount(newlst)
    token_lst = list(maindict.items())
    
    print(token_lst)
    

main()
