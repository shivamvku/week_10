# # if contion:

# # print(type(a),type(b))

# # print(a+b)
# a = int(input('Enter a number\n'))
# b = int(input('Enter a number\n'))
# if a>b:
# 	print(a,'is greater')
# else:
# 	print(b,'is greater')

# print('this is out of the stamts')



# nested if else

 
# syntax
# --------------

# if contion:
# 	body of iif

# 	if contion:
# 		body of iff

# 		if contion:
# 			body of iff

# 		else:
# 			body of else
# 	else:
# 		body of else

# else:
# 	body of else



# a = int(input('Enter a number\n'))

# if a>=0:
# 	if a>0:
# 		print('Postive number')
# 	else:
# 		print('Nutral')
# else:
# 	print('Negative number')




# if(a>0):
# 	print('Postive number')
# elif(a<0):
# 	print('Negative number')
# else:
# 	print('Nutral number')






# Control flows
# -----------------------

# loops
# -------------

# for loop
# while loop


# for a in range(3,21,4):
# 	print(a)


# for a in "DigtalLync":
# 	print(a)


# while loop
# ====================


# while codtion:
# 	body of while loop

# a =1
# while a <= 10:
# 	print(a)
# 	a+=1
	


# Flow Control
# 0---------------0

# break ----- > keyword for breaking a loop
# continue ----> keyword for continueing the loop
# pass ---------> keyword for an empty body


# a = 'DigtalLync'

# for val in a:
# 	if val == 'L':
# 		break
# 	print(val)


# for val in a:
# 	if val == 'L':
# 		continue
# 	print(val)

# for x in range(1,10):
# 	pass



# Input and Output and Facier formating stylr


# a = input('Enter a value\n')

# b = input('Enter aother value\n')

# print(a+b)



# formating style
# --------------------

# type formater

# %s -------- > for strings
# %d ---------> for intergers
# %f ---------- > for float vales



# old formating style
# -----------------------
# a = input('Enter a value\n')
# b = input('Enter another value\n')

# print('%s and %s are the avngers'%(a,b))

# print('%s and %s are the avngers'%('Hulck','Superman'))

# print('%s and %s are the avngers and %f and %f are there respectve marks in examination'%('Hulck','Superman',99.34564355,95.23434324))





# new formating style or fancier formating style
# --------------------------------------



# print('{1} and {0} are the avngers'.format('Hulck','Superman'))


# print('{:.3s} and {:.3s} are the avngers and {:.2f} and {:.2f} are there respectve marks in examination'.format('Hulck','Superman',99.34564355,95.23434324))



# a = input('Enter a value\n')
# b = input('Enter another value\n')

# print('The company name is ',a,b)
# print('The company name is ',a+b)


# inbuilt methods and fuction for strings

# a = input('Enter a value\n')
# inbult methods
# -------------------
# .upper()
# .lower()
# .title()
# .lstrip()
# .rstrip()
# .strip()


# print(a.upper())
# print(a.lower())
# print(a.title())

# a = 20*'-'+'Hello'+20*'*'
# print(a)
# print(a.lstrip('-'))
# print(a.rstrip('*'))
# print(a.strip('*'))

# s1 = a.lstrip('-')
# print(s1)
# print(s1.rstrip('*'))
