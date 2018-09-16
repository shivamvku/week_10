# dictonary
# -------------------

# it is colletionof key value paied element unstructed



# 	a = {} ---------> empty dictonary

# 	a = {key:value}

			# key data types
			# -----------------
				# int
				# float
				# str
				# bool
				# complex
				# tuple

			# value data types
			# -----------------
				# int
				# float
				# str
				# bool
				# complex
				# tuple
				# list
				# set
				# dict

# example -1
# -----------------
a ={1:'hello','hi':56.78,4+7j:56,(4,3,5,6):78.34,1:'somthing'}

# print(a)
# print(type(a))

# Acess the value in dic
# _____________________

# is done by keys


# print(a[1])
# print(a['hi'])
# print(a[4+7j])
# print(a[(4,3,5,6)])




# print(a)
# del a[1] 
# a[key] = value
# a['key'] = 'value'
# a[1] = 57646

# inbuilt methods
# ----------------------
# a.pop(1)
# a.popitem()
# a.clear()
# print(a.keys())
# print(a.values())
# print(a.items())

# Dict compershension
# -------------------------
# .formkeys(keys,seq)

# keys = {1,2,3,4}
# valeu = 'somthing'
# d = dict.fromkeys(keys,valeu)
# print(d)


# d = {2:4,3:9}
# d = {a:a**2 for a in range(0,11)}
# print(d)

# inbuilt fucntion

# print(len(d))
# print(sum(d))
# print(min(d))
# print(max(d))
# print(all(d))
# print(any(d))