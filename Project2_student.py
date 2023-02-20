
print("...............Welcome to SUBATASH software.............")
print("\n\n")
print("...............Who are you?...................")
print("\n") 
flagresult=0
flagaddstudent=0
while 1:
 print("Enter 1: For AUTHORITY ")
 print("Enter 2: For STUDENT ")
 print("Enter 3: For TEACHER    ")
 print("Enter 4: For Exit this")
 x=int(input())
 if x==1:#vaiable for menubar
  while 1:
    print("Enter 1 : For ADD student")
    print("Enter 2 : For SEARCHING  ")
    print("Enter 3 : See All student's Details")
    print("Enter 4 : ADD Student's Tution Fee")
    print("Enter 5 : outstanding balance For All students")
    print("Enter 6 : How meny students are eligible For class")
    print("Enter 7 : Result's Input")
    print("Enter 8 : For Back ")
    aut=int(input())
    if aut==1: 
        flagaddstudent=1
        print("How meny student you want to add :",end=" ")
        addstudent=int(input())
        #substu=addstudent-1 # For while loop because of mine
        addtution=[0]*addstudent
        outstanding=[-2000]*addstudent
        stuname=[]
        stuid=[]
        studate=[]
        stuclass=[]
        stugpa=[]
        stumobile=[]
        stugardmobile=[]
        #while addstudent>=0:
        for i in range(0,addstudent): #add student information 
          
            #def menustudent():
            print("studnet number ",i+1)
            print("Name             :",end=" ")
            stuname1=str(input())
            stuname.append(stuname1)
            print("ID               :",end=" ")
            stuid1=str(input())
            stuid.append(stuid1)
            print("Date of birth    :",end=" ")
            studate1=str(input())
            studate.append(studate1)
            print("Student class    :",end=" ")
            stuclass1=str(input())
            stuclass.append(stuclass1)
            print("SSC GPA          :",end=" ")
            stugpa1=str(input())
            stugpa.append(stugpa1)
            print("Student's MObile :",end=" ")
            stumobile1=str(input())
            stumobile.append(stumobile1)
            print("Guardian MObile  :",end=" ")
            stugard1=str(input())
            stugardmobile.append(stugard1)
            print("Successfully Registration student number",i+1)
    if aut==2 and flagaddstudent==1:
           print("Enter the  serial number  :",end=" ")
           qsearch=int(input())
           print("...............")
           print("student :",qsearch)
           print("Name                  :",end=" ")
           print(stuname[qsearch-1])
           print("ID                    :",end=" ")
           print(stuid[qsearch-1])
           print("Student class         :",end=" ")
           print(stuclass[qsearch-1])
           print("SSC GPA          :",end=" ")
           print(stugpa[qsearch-1])
           print("Student's MObile      :",end=" ")
           print(stumobile[qsearch-1])
           print("Date of birth         :",end=" ")
           print(studate[qsearch-1])
           print("Guardian MObile       :",end=" ")
           print(stugardmobile[qsearch-1]) 
           print("Student's Balance     :",end=" ")
           print(addtution[qsearch-1]) 
           print("Outstanding balance   :",end=" ")
           print(-2000+addtution[qsearch-1])
           print(".......................")     
   
    if aut==3 and flagaddstudent==1:
        for i in range(0,addstudent): #see student information
           print("student             :",i+1)
           print("Name                :",end=" ")
           print(stuname[i])
           print("ID                  :",end=" ")
           print(stuid[i])
           print("Student class       :",end=" ")
           print(stuclass[i])
           print("SSC GPA             :",end=" ")
           print(stugpa[i])
           print("Student's MObile    :",end=" ")
           print(stumobile[i]) 
           print("Date of birth       :",end=" ")
           print(studate[i])
           print("Guardian MObile     :",end=" ")
           print(stugardmobile[i]) 
           print("Student's Balance   :",end=" ")
           print(addtution[i]) 
           print("Outstanding balance   :",end=" ")
           print(-2000+addtution[i])
           print(".......................")     
    if aut==4 and flagaddstudent==1:
            print("SEARCH ID For add tution fee student's :",end=" ")
            searchid5=int(input())
        #for i in range(0,addstudent):
          #searchid5-1==
            print("How balance you want to add out of 2000:",end=" ")

            addtution1=int(input()) 
            temp=addtution1
            addtution1=addtution[searchid5-1]
            addtution[searchid5-1]=temp 
            print("..........Successfully submitted tution fee......")
             
    if aut==5 and flagaddstudent==1:
      for i in range(0,addstudent):
        print(stuname[i],stuid[i],-2000+addtution[i])
    if aut==6 and flagaddstudent==1:
      for i in range(0,addstudent):
         if -2000+addtution[i]>=-1000:
           print(stuid[i],stuname[i],":     eligible")      
         else:
           print(stuname[i],"           :     Not Eligible")     
    if aut==7 and flagaddstudent==1:
      sturesult=[]
      
      for i in range(0,addstudent):
       flagresult=1
       print(stuid[i],stuname[i],end="  :  ")
       sturesult1=int(input())
       sturesult.append(sturesult1)
       print("\n")
       print("Successfully added result.......")
       print("\n")
      maxresult= max(sturesult)
        

    if aut==8:

      print("\n Shifted previous page \n")
      break
    if flagaddstudent==0:
      print("\n.....Please firsly add student....\n")
 if x==2:
   if flagresult==0 and flagaddstudent==0:
    print("\n\n") 
    print(".....Upcoming this freature.....")
    print("\n\n")
   elif flagresult==1 and flagaddstudent==1:
      print(".........................")
      print("The Highest result is :",maxresult)
      print(".....................")
      for i in range(0,addstudent):
         print(stuid[i],stuname[i],(":       "),sturesult[i])
 if x==3:
    print("\n\n")
    print(".....Upcoming this freature.....")
    print("\n\n")
 if x==4:
    print("Ok bye")
    print("\n\n")
    break        
