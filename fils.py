# # file ??
# # ==================

# # it is a colletion some information
	
# # Type of files 
# # =================
# 	# text file
# 	# image file
# 	# csv file
# 	# execle file
# 	# word file
# 	# doc file
# 	# audio file
# 	# video file
# 	# .
# 	# .
# 	# .
# 	# .
# 	# .
# # Repsersston of file with there e xetion
	
# 	# text file ---------- .txt
# 	# docmunt file ------- .doc
# 	# csv file ----------- .csv
# 	# html file --------- .html
# 	# ......................

# 	# .............
# 	# .................
# # Properties of file
# # =======================

# # name
# # extesion
# # size
# # location
# # Type
# # data and time of cration of file
# # permission
# # 	read 
# # 	write
# # encoding 
# # 	utf - 8
# # 	utf -16

# # Steps to create a file in python
# # ====================================

# # opertions on files
# # --------------------------
# # 1. open the file
# # 2. mode

# # 	write -------- 'w'
# # 	read ---------- 'r'
# # 	append -----  'a'
# # 	readbinary ------ 'rb'
# # 	writebinary ------- 'wb'
# # 	write advance ------- 'w+'
# # 	read advance  ---------- 'r+'
# # 3. close the file


# # Example ---------1
# # =========================+
# # inbu function

# # 	open('name of the file','mode of the file',encoding)


# # file = open('sample.txt','w')
# # file.write('This is a first line in the file\n')
# # file.write('This is the 2nd line')

# # file.close()



# # file = open('sample.txt','r')
# # # data = file.read(3)
# # data1 = file.readline()
# # data2 = file.readline()
# # print(data1)
# # print(data2)
# # file.close()





# # file = open('sample.txt','a')

# # file.write('this is a new data\n')
# # file.write('The new is is this')
# # file.close()



# # file objet posiitions

# # seek(pos,offest) ------ it take file object to a desied postions
# # tell(pos,offset) ------- it gives you the current postions of file object



# # file = open('sample.txt','r')

# # print(file.tell())

# # file.seek(0,0)

# # print(file.tell())

# # # print(file.read())

# # file.seek(45)
# # print(file.read())

# # file.close()







# # csv ------- comma seperated vallue

#  # reader(...)
#  #        csv_reader = reader(iterable [, dialect='excel']
#  #                                [optional keyword args])
#  #            for row in csv_reader:
#  #                process(row)
#  # writer(...)
#  #        csv_writer = csv.writer(fileobj [, dialect='excel']
#  #                                    [optional keyword args])
#  #            for row in sequence:
#  #                csv_writer.writerow(row)


# import csv
# from csv import *


# file = open('info.csv','r')

# data = ['name,age,addess'.split(','),
# 		'batman,40,usa'.split(','),
# 		'superman,40,usa'.split(','),
# 		'ironman,40,usa'.split(','),
# 		'wonderwomen,40,usa'.split(','),
# 		'himna,40,usa'.split(',')]
# # print(data)
# print(type(data))


# def likhna(file,data):
# 	var = writer(file,delimiter = ',')
# 	for line in data:
# 		var.writerow(line)

# likhna(file,data)

# # def readcsv(file):
# # 	var = reader(file,delimiter=',')
# # 	for row in var:
# # 		print(row)


# # readcsv(file)
# file.close()



# Python direcort
# =========================


# folder and file manger is is done by opperating system

# import os

# # os.mkdir('dummyfolder')
# # print(os.getcwd())
# # os.chdir('/home/vineet/Documents/vineet/python/week_10/dummyfolder')
# # print(os.getcwd())

# # os.rename('dummyfolder','goodfolder')
# # os.remove('sample.txt')
# os.rmdir('goodfolder')




