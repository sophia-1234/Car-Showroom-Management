d={2388:["xcent","black","14km/l","diesel engine",350000,3],
3410:["verna","white","15km/l","petrol engine",430000,5],
2399:["getz","blue","19km/l","diesel engine",567000,1],
8888:["i20","blue","16km/l","petrol engine",568000,10]}

#display the cars available in the showroom
print" THE Cars available in the showroom are"
print"........................................"
for i in range(3):
    print 

import os
import pickle 
os.system('cls' if os.name == 'nt' else 'clear')
f1=open("carinfo.txt","w")
pickle.dump(d,f1)
f1.close()
f1=open("carinfo.txt","r")
x=pickle.load(f1)
print"the cars available in the showroom is"
sum=0
for i in x :
 print "%10s"%i,"%10s"%d[i][0],"%10s"%d[i][1],"%10s"%d[i][2],"%10s"%d[i][3],"%10s"%d[i][4],"%10s"%d[i][5]
 sum=sum+d[i][5]

#displays the total number of cars in the showroom
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print
print "the total number of cars available in the show room is", sum
print
print"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

f1.close()
p=input("enter 1 to go to the next page")
#Allows the staff to choose desired operations
if p==1:

 os.system('cls' if os.name == 'nt' else 'clear')
 print"<<<<<<<<<<<       CHOOSE THE operation      >>>>>>>>>>>>"
 print
 print "1.enter a new car:"
 print 
 print "2.read the feed back form the customer:"
 
 num=input()
 if num==1:
  #ALLOW THE STAFF TO ENTER THE DETAILS OF THE NEW CAR
  os.system('cls' if os.name == 'nt' else 'clear') 
  n=input("ENTER THE NUMBER OF NEW CAR THT HAV COME:")

  for i in range(n):
 
   l=[]
   f1=open("carinfo.txt","w")
   series=input("enter the series number the car:")
   name=raw_input("enter the name of the car:")
   col=raw_input("enter the col of the car:")
   mile=raw_input("enter the milage of the car:")
   e=raw_input("enter the engine of the car:")
   cost=input("enter the cost of the car:")
   n=input("enter the number of the car:")
   t=[name,col,mile,e,cost,n]
   d[series]=t
  
   pickle.dump(d,f1)

     
 elif num==2:
    #PRINTS THE FEEDBACK GIVEN BY THE USER
    os.system('cls' if os.name == 'nt' else 'clear')
    f4=open("comment.txt","r")
    w= pickle.load(f4)
    print w
    for i in w:
     print i,"%10s"%w[i][0],"%20s"%w[i][1]
    f4.close()
 else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print"sorry the option is not available"

