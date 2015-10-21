

# A game about you Name # Using Sting & List
##########################################################
#string

giveName = str(input('Give Me your Name:'))         # Ask User Name
nameLength = len(giveName)                          # getting Name length
nameChar = str(giveName[0])                         # changing 1st character
nameChange = giveName.replace(nameChar, 'Z')        # changing the name 1st Char
nameChangeUpper = nameChange.upper()                # Change the Name to Uppercase
###############################################################
# list

nameList = list(giveName)               # changing name to list
nameReverse = nameList.reverse()        # reverse name (list)
###############################################################

print('your Name is:', giveName)
print('your Name Start with Letter: ', nameChar)
print('Your Name Length is: ', len(giveName))
print('it would be cool if your name started with \"Z\":', nameChangeUpper)
print('it would be cool if we write your name in reverse:', nameList)

####################################################################
#tuple
nametuple =tuple(giveName )
print(nametuple)

#######################################3333
# Dictionaries

dicName = {}
dicName['name'] = giveName

print(dicName)
