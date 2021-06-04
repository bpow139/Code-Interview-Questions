'''
This script was a problem from Reddit. Take an array such as 
['Jack 3', 'King 4', 'Queen 2']
Be able to seperate the words from the numbers. For example I just want Jack, King and Queen.
Or just want 3,4, and 2
'''

array = ['Jack 3', 'King 4', 'Queen 2']

# This for loop will print out only the number portion of the array.
for i in range(len(array)):
	space = array[i].find(' ')
	print(array[i][space + 1])
	
