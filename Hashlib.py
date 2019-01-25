#import hash library
import hashlib

#import os 
import os

#import csv file
import csv




#file address
os.chdir("C:\\Python27\\vishal.singh")


#open csv file
with open('zoo.csv') as filezoo:

#read csv file
    csvread=csv.reader(filezoo,delimiter=',')
    for i in csvread:
        text = hashlib.sha1(i[2])

#print
        print text
