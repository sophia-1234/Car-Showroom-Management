#welcome page
import os
import pickle
os.system('cls' if os.name == 'nt' else 'clear')
print".............."                                                                     
s={}
for i in range(15):
   print 
print"                                                            WELCOME TO HYUNDAI SHOWROOM"
print"                                                                YOUR DREAM,WE DELIVER"
for i in range(5):
   print
print"                                      Over 100 branches all over the world and 50 years of experience"
for i in range(5):
   print
print"Email:hyundai2016@gmail.com"
print"contact:09324566455"






#customer is given an option to quite or continue
num=input("Press 0 to exit or another key to proceed:")
if num==0:
  exit()
else:
  #customer details are taken in a new page and these details are stored in a file names f
  os.system('cls' if os.name == 'nt' else 'clear')
  print"----------------------------"
  print"ENTER THE FOLLOWING DETAILS"
  print"----------------------------"
  print 
  name=raw_input("NAME:")
  add=raw_input("ADDRESS:")
  tel=raw_input("TELEPHONE NUMBER:")
  f=open("customerdetail.txt","a")
  f.write(name)
  f.write(add)
  f.write(tel)
  f.close()
  str=raw_input("please enter ***** to go to the next page........")
  if str!="*****":
    exit()
  else:
   #the available cars are displayed to the user in a table format
   os.system('cls' if os.name == 'nt' else 'clear')
   f1=open("carinfo.txt","r")
   n=1
   s= pickle.load(f1)
   print"..................................."
   print"CARS AVAILABLE IN THE SHOWROOM ARE"
   print"..................................."
   for i in range(3):
    print 
   d=s.keys()
   print"%5s"%"s.no","%10s"%"CODE","%10s"%"NAME","%10s"%"COLOUR","%10s"%"MILEAGE","%15s"%"TYPE","%10s"%"COST","%20s"%"NUMBBER OF CARS"
   for i in d:
    print"%5s"%n,"%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%15s"%s[i][3],"%10s"%s[i][4],"%20s"%s[i][5]
    n=n+1
   for i in range(3):
    print
   print"Dear customers,\n PLEASE NOTE THE CODE NUMBER OF THE CAR YOU ARE INTERESTED IN"
   c=raw_input("Enter $$$^^^$$$ to continue")
   if c!="$$$^^^$$$":
      exit()
   else:

    #search the car based on the users choose
    os.system('cls' if os.name == 'nt' else 'clear')
    print"SEARCH ENGINE "
    print"**************"
    for i in range(3):
     print 
    print "1. SORTING BASED ON Model number "
    print "2. Model,Milage,cost"
    print "3. Milage,Cost"
    print "4. Cost"
    print "5. Milage"
    print "OTHERWISE PRESS 0 TO PROCEED TO BUYING"
    n=input("enter a number based on your selection")
    if n==0:
     pass
    elif n==1:
     #SORT THE MODEL CODE AND DISPLAY THE TABLE
     d.sort()
     for i in d:
      print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%20s"%s[i][5]
      pass
    elif n==2:
     os.system('cls' if os.name == 'nt' else 'clear')
     #SEARCH THE AVAILABLITY OF THE CAR WHEN THE USER ENTERS HIS DESIRED QUALITIES....ie model name,mileage,cost
     searchname=raw_input("NAME:")
     searchmil1=raw_input(" MINIMUM MILEAGE:")
     searchmil2=raw_input(" MAXIMUM MILEAGE:")
     searchcost1=input("MINIMUM COST:")
     searchcost2=input("MAXIMUM COST:")
     flag=0
     for i in d:
      if(searchname==s[i][0]):
       if(searchmil1<=s[i][2]<=searchmil2):
         if(searchcost1<=s[i][4]<=searchcost2):
          flag=1
          print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%10s"%s[i][5]

     if flag==1:
      print "Search result: postive"
   
     else:
      print "Search result: negative"

    elif n==3:
     os.system('cls' if os.name == 'nt' else 'clear')
     #SEARCH THE AVAILABLITY OF THE CAR WHEN THE USER ENTERS HIS DESIRED QUALITIES....ie mileage,cost
     searchmil1=raw_input(" MINIMUM MILEAGE: ")
     searchmil2=raw_input(" MAXIMUM MILEAGE: ")
     searchcost1=input("MINIMUM COST:")
     searchcost2=input("MAXIMUM COST:")
     flag=0
     for i in d:
      if(searchmil1<=s[i][2]<=searchmil2 and searchcost1<=s[i][4]<=searchcost2 ):
      
         flag=1
         print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%10s"%s[i][5]

     if flag==1:
       print "Search result: postive"
   
     else:
       print "Search result: negative"

   
    elif n==4:
     #SEARCH THE AVAILABLITY OF THE CAR WHEN THE USER ENTERS HIS DESIRED QUALITIES....ie cost
     os.system('cls' if os.name == 'nt' else 'clear')
     searchcost1=input("MINIMUM COST:")
     searchcost2=input("MAXIMUM COST:")
     flag=0
     for i in d:
       if(searchcost1<=s[i][4]<=searchcost2 ):
      
          flag=1
          print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%10s"%s[i][5]
       else:
          pass
     if flag==1:
        print "Search result: postive"
     else:
        print "Search result: negative"
    elif n==5:
     os.system('cls' if os.name == 'nt' else 'clear')
     #SEARCH THE AVAILABLITY OF THE CAR WHEN THE USER ENTERS HIS DESIRED QUALITIES....ie mileage
     searchmil1=raw_input("MINIMUM MILEAGE: ")
     searchmil2=raw_input("MAXIMUM MILEAGE:")
     flag=0
     for i in d:
       if(searchmil1<=s[i][2]<=searchmil2 ):
      
          flag=1
          print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%10s"%s[i][5]
       else:
          pass
     if flag==1:
        print "Search result: postive"
   
     else:
        print "Search result: negative"
    else:
      print"sorry the option you entered is not available"

   p=raw_input("enter %%%%% to continue")
   if p!="%%%%%":
    exit()
   else:
    #now the buying procedure begins"
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Proceded to buying the car"
    for i in range(3):
       print 
    series=input("Enter the series number of the car you want to buy")
    os.system('cls' if os.name == 'nt' else 'clear')
    d=s.keys()
   
    for i in d:
     if series==i:
      #ASKING THE USER TO CONFIRM THE CAR THAT HE HAS SELECTED
      print "The car you want to buy is......"
      print
      print
      print "%10s"%i,"%10s"%s[i][0],"%10s"%s[i][1],"%10s"%s[i][2],"%10s"%s[i][3],"%10s"%s[i][4],"%10s"%s[i][5]
      print
      print
      print "press 1 for confirming or any other key to exit"
      numm=input()
      if numm!=1:
        exit()
      else:
       #THE BILL IS DISPLAYED
       os.system('cls' if os.name == 'nt' else 'clear')
       import datetime
       dt=datetime.datetime.now()
      
       import time
       t="LOADING..."
       
       for u in t:
         print u 
         time.sleep(4)


       
       print "                                              BILL     "
       print "                                            --------   "
       print
       import datetime
       dt=datetime.datetime.now()
       print  dt.day,"-",dt.month,"-",dt.year
       print dt.hour,":", dt.minute,":", dt.second
       
       for i in range(3):
        print 

       print"NAME:","%-10s"% name 
       print"ADDRESS:","%-10s"% add
       print"TELEPHONE:","%-10s"% tel
       for i in range(3):
        print 
       
       for i in d:
        if series==i:
         print "CAR SERIES NUMBER:","%20s"%i,"\t","NAME:   ","%20s"%s[i][0]
         print "COLOUR:           ","%20s"%s[i][1],"\t","MILEAGE:","%20s"%s[i][2]
         print "ENGINE:","%10s"%s[i][3]
         for j in range(3):
          print 
         print"COST                                                  :","%25d"%s[i][4]
         print"TAX                                                   :","%25d"%1500
         print"TOTAL                                                 :","%25d"%(s[i][4]+1500)
         for j in range(3):
           print
         print "thank you "
         print "PLEASE collect you car in 15 days time,bill must be submitted during the Transaction"
         f4=open("deliver.txt","a+")
         pickle.dump(series,f4)
         f4.close()
         s[i][5]=s[i][5]-1
         if s[i][5]==0:
           del s[i]
   f1.close()
   
  f1=open("carinfo.txt","w")
  cust={}
  pickle.dump(s,f1)
  f1.close()
  h =raw_input("enter !!!!! if you have any feed backs or anyother key to exit()")
  if h!="!!!!!":
     exit()
  else:
   f4=open("comment.txt","r")
   cust=pickle.load(f4)
   print cust
   f4.close()
   os.system('cls' if os.name == 'nt' else 'clear')
   
   f4=open ("comment.txt","w")
   comment=raw_input("Enter your valuable feedbacks")
   y=s.keys()
   for i in y:
    x=(name,comment)
    cust[series]=x
   pickle.dump(cust,f4)
   print cust
   f4.close()

   '''f5=open("deliver.txt","r")
   trans=pickle.load(f4)
   print trans
   f5.close()'''
   
   f5=open ("deliver.txt","w")
   comment=raw_input("Enter your valuable feedbacks")
   y=s.keys()
   for i in y:
    x=(name,add,tel,i,s[i][0],s[i][1],s[i][2],s[i][3],s[i][4])
    trans[series]=x
   pickle.dump(trans,f5)
   print trans
   f5.close()

