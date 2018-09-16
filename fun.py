# function
# ----------------
# it is  colletion of task with some imput and some expted outputs


# Types ---
# ==========

# 1. Inbuit functions
# ----------------------

	# alredy  dedinded by the python devopers

		# example
		# --------------
			# print(),len(),id(),ord(),min(),max(),sum(),set(),list()
			# tuple(),dict(),int(),float(),str()



# Built-in Functions
  # 69 in python 3.x
# --------------------------------------------------------		
# abs()	delattr()	hash()	memoryview()	set()
# all()	dict()	help()	min()	setattr()
# any()	dir()	hex()	next()	slice()
# ascii()	divmod()	id()	object()	sorted()
# bin()	enumerate()	input()	oct()	staticmethod()
# bool()	eval()	int()	open()	str()
# breakpoint()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()






# User Defined Functions
# ----------------------------

# user is going to define the function with task and the 
# number of inputs and outputs should be by the user 



# how do define ?
# ----------------

# syntax

# def funcname(argumets):
# 	body of the function


# def  ----------- > it is key word for deinf a function
# funcname ---------> any function name


# Function call

# funcname(paramerts)  # if function have any argumts then pass the paremets

# example -----1
# ---------------------

# a = 1
# b = 2
# def add(): # functiono deination
# 	print(a+b)  #task of the function
# 	return 'kuchbhi'
# # add() #function call
# # print(add)
# print(add())




# Argumets
# --------------------

# argumts are of 4 Types

	# 1.Postiona Argumets
	# 2.default Argumets
	# 3. keyword Argumets
	# 4. Arbitary or varble length argumts


# 1.Postional Argumets
# ------------------------_

# pass by value



# def add(a,b):
# 	print(a+b)
# 	return 'Finished adding'
# add(4,5)


# default Argumets
# ----------------------

# def add(a = 1,b =2):
# 	print(a+b)
# 	return 'Finished adding'
# print(add(4,5))

# keyword argumts
# -------------------------
# pass by reference workings

# def add(a,b):
# 	print(a+b)
# 	return 'Finished adding'
# add(a = 45,b = 3)



# Arbitary or varble length Argumets
# ---------------------------------------

# a = 1,2,3,4


# a  =1
# print(type(a))

# def greeting(*name):
# 	print(name)
# 	# print(a)
# greeting('Batman','superman','Ironman','Hulck')


# *args ----------- > It by convention

# def greeting(*args):
# 	print(args)
# 	# print(len(name))
# 	for a in range(0,len(args)):
# 		# print(a)
# 		print('welcome',args[a])	
# 	# print('welcome',name[1])


# greeting('Batman','superman','Ironman','Hulck')


# kwargs------------> convention way of writing

# def greeting(**kwargs):
# 	# print(kwargs)
# 	for a,b in kwargs.items():
# 		print(a)
# 		print(b)
# 		print('This is ',a,'from',b)

# greeting(superman = "usa",Batman = 'Poland',Ironman = 'India')

# ==================================
# lambda Functions
# ====================================

# anonymys funtion or lambda function

# lambda  -------- > keyword inpython


 # it is a single line function


# syntax 
# ------------

# function defination
# ------------------------
# lambda arg:expression

# function call
# ================

# var = lambda arg:expression

# var() ----------> function call



# example -----1 
# ----------------

# suq = lambda a: a**2
# # print(suq(5))

# print(suq(5))




# map() -------------> map to the vale in the colletion seq and gves o/p True or Flase  accoding to the expression
# filter() ----------> filter the values in the colltion or seq and gies o/p as the reaming elemts accoding to the expression
# reduce() --------> used to compute the value in the seq 


# map(function,sequence)
# filter(function,sequence)
# reduce(function,sequence)


# l = [a for a in range(0,11)]
# print(l)


# even = list(map(lambda a : a%2 == 0,l))
# print(even)

# odd = list(filter(lambda a: a%2 != 0,l))
# print(odd)


python code to demonstrate working of reduce() 
  
# importing functools for reduce() 
import functools 
  
# initializing list 
  
l = [a for a in range(0,11)]
print(l)
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,l)) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,l)) 











