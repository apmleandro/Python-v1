# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' This is a code to remove a duplicate from a lista'''

#1 CREATE LIST
#2 CONVERT LIST TO A DICTIONARY
#resoaning: by creating a dictionary of a list I will exclude repetition because
#we can't have duplicated in a dictionary
#3 CONVERT THE DICTIONARY TO LIST AGAIN
#Now it doesn't have a duplicate anymore
#PRINT RESULT

lista= [2,2,3,5,5,6,7,8,9]

remove_dup=dict.fromkeys(lista)
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
newlist=list(remove_dup)
print(newlist)

