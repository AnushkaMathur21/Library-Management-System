import tkinter
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
from chart import Generate_Report

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #VARIABLES
        self.member_var=StringVar()
        self.rollno_var=StringVar()
        self.admno_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.course_var=StringVar()
        self.branch_var=StringVar()
        self.section_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.author_var=StringVar()
        self.dateofborrow_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.subject_var=StringVar()

        lbl_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        #MAIN FRAME
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=125,width=1530,height=405)

        #LEFT DATA FRAME
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",18,"bold"))
        DataFrameLeft.place(x=0,y=0,width=900,height=380)

        lbl_membertype=Label(DataFrameLeft,bg="powder blue",text="  Member Type-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_membertype.grid(row=0,column=0,sticky=W)
        com_membertype=ttk.Combobox(DataFrameLeft,font=("times new roman",14),width=27,textvariable=self.member_var,state="readonly")
        com_membertype["value"]=("Admin Staff","Student","Professor")
        com_membertype.grid(row=0,column=1)

        roll_number=Label(DataFrameLeft,bg="powder blue",text="  Roll No.-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        roll_number.grid(row=1,column=0,sticky=W)
        txt_roll=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.rollno_var,width=29)
        txt_roll.grid(row=1,column=1)

        adm_number=Label(DataFrameLeft,bg="powder blue",text="  Admission No.-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        adm_number.grid(row=2,column=0,sticky=W)
        txt_adm=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.admno_var,width=29)
        txt_adm.grid(row=2,column=1)

        lbl_firstname=Label(DataFrameLeft,bg="powder blue",text="  First Name-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_firstname.grid(row=3,column=0,sticky=W)
        txt_firstname=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.firstname_var,width=29)
        txt_firstname.grid(row=3,column=1)

        lbl_lastname=Label(DataFrameLeft,bg="powder blue",text="  Last Name-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_lastname.grid(row=4,column=0,sticky=W)
        txt_lastname=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.lastname_var,width=29)
        txt_lastname.grid(row=4,column=1)

        lbl_course=Label(DataFrameLeft,bg="powder blue",text="  Course-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_course.grid(row=5,column=0,sticky=W)
        com_course=ttk.Combobox(DataFrameLeft,font=("times new roman",14),textvariable=self.course_var,width=27,state="readonly")
        com_course["value"]=("B.TECH","MCA","B.PHARMA")
        com_course.grid(row=5,column=1)

        lbl_branch=Label(DataFrameLeft,bg="powder blue",text="  Branch-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_branch.grid(row=6,column=0,sticky=W)
        com_branch=ttk.Combobox(DataFrameLeft,font=("times new roman",14),textvariable=self.branch_var,width=27,state="readonly")
        com_branch["value"]=("CSE","ECE","IT","EEE","ME","CE")
        com_branch.grid(row=6,column=1)

        lbl_section=Label(DataFrameLeft,bg="powder blue",text="  Section-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_section.grid(row=7,column=0,sticky=W)
        com_section=ttk.Combobox(DataFrameLeft,font=("times new roman",14),textvariable=self.section_var,width=27,state="readonly")
        com_section["value"]=("A","B","C")
        com_section.grid(row=7,column=1)

        lbl_mobile=Label(DataFrameLeft,bg="powder blue",text="  Mobile No.-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=8,column=0,sticky=W)
        txt_mobile=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.mobile_var,width=29)
        txt_mobile.grid(row=8,column=1)

        lbl_bookid=Label(DataFrameLeft,bg="powder blue",text="  Book ID-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_bookid.grid(row=0,column=2,sticky=W)
        txt_bookid=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.bookid_var,width=29)
        txt_bookid.grid(row=0,column=3)

        lbl_bookname=Label(DataFrameLeft,bg="powder blue",text="  Book Name-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_bookname.grid(row=1,column=2,sticky=W)
        txt_bookname=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.bookname_var,width=29)
        txt_bookname.grid(row=1,column=3)

        lbl_author=Label(DataFrameLeft,bg="powder blue",text="  Author-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_author.grid(row=2,column=2,sticky=W)
        txt_author=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.author_var,width=29)
        txt_author.grid(row=2,column=3)

        lbl_dateofborrow=Label(DataFrameLeft,bg="powder blue",text="  Date of Borrow-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_dateofborrow.grid(row=3,column=2,sticky=W)
        txt_dateofborrow=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.dateofborrow_var,width=29)
        txt_dateofborrow.grid(row=3,column=3)

        lbl_duedate=Label(DataFrameLeft,bg="powder blue",text="  Due date-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_duedate.grid(row=4,column=2,sticky=W)
        txt_duedate=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.duedate_var,width=29)
        txt_duedate.grid(row=4,column=3)

        lbl_days=Label(DataFrameLeft,bg="powder blue",text="  Number of days-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_days.grid(row=5,column=2,sticky=W)
        txt_days=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.daysonbook_var,width=29)
        txt_days.grid(row=5,column=3)

        lbl_latereturnfee=Label(DataFrameLeft,bg="powder blue",text="  Late Return Fee-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_latereturnfee.grid(row=6,column=2,sticky=W)
        txt_latereturnfee=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.latereturnfine_var,width=29)
        txt_latereturnfee.grid(row=6,column=3)

        lbl_dateoverdue=Label(DataFrameLeft,bg="powder blue",text="  Date over due-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_dateoverdue.grid(row=7,column=2,sticky=W)
        txt_dateoverdue=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.dateoverdue_var,width=29)
        txt_dateoverdue.grid(row=7,column=3)

        lbl_subject=Label(DataFrameLeft,bg="powder blue",text="  Subject-  ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_subject.grid(row=8,column=2,sticky=W)
        txt_subject=Entry(DataFrameLeft,font=("times new roman",14),textvariable=self.subject_var,width=29)
        txt_subject.grid(row=8,column=3)

        #RIGHT DATA FRAME
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",18,"bold"))
        DataFrameRight.place(x=910,y=0,width=560,height=380)

        bookslist=['1. Core Python Applications Programming','2. Fundamentals of Python: First Programs with MindTap','3. Introduction to Computer Science using Python','4. Introduction to Computing and Problem Solving with Python','5. How to think like a Computer Scientist: Learning with Python','6. Learning Python','7. Python Programming: An introduction to Computer Science','8. Python Programming for Absolute Beginners','9. Python Cookbook','10. Higher Engineering Mathematics','11. Advance Engineering Mathematics','12. Introductory methods of Numerical solutions','13. Numerical Methods','14. An introduction to Numerical Methods and Analysis','15. Data Structures using C and C++','16. Data Structures: A Pseudocode approach with C','17. Fundamentals of Data Structures','18. Data Structures and Algorithms in C++','19. Data Structures and Program Design in C','20. Computer System Architecture','21. Computer Architecture and Organization','22. Computer Architecture','23. Computer Organization','24. Discrete Structures','25. Mathematics: A Discrete Introduction','26. Discrete and Combinational Mathematics','27. Technical Communication- Principles and Practices','28. Personality Development and Soft Skills','29. Soft Skills & Employbility','30. Technical Communication']

        def select_book(event=""):
            x=str(listbox.get(listbox.curselection()))
            if(x=="1. Core Python Applications Programming"):
                self.bookid_var.set("BKID5001")
                self.bookname_var.set("Core Python Applications Programming")
                self.author_var.set("Wesley J. Chun")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="2. Fundamentals of Python: First Programs with MindTap"):
                self.bookid_var.set("BKID5002")
                self.bookname_var.set("Fundamentals of Python: First Programs with MindTap")
                self.author_var.set("Kenneth A. Lambert")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="3. Introduction to Computer Science using Python"):
                self.bookid_var.set("BKID5003")
                self.bookname_var.set("Introduction to Computer Science using Python")
                self.author_var.set("Charles Dierbach")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="4. Introduction to Computing and Problem Solving with Python"):
                self.bookid_var.set("BKID5004")
                self.bookname_var.set("Introduction to Computing and Problem Solving with Python")
                self.author_var.set("Jeeva Jose, P. Sojan Lal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="5. How to think like a Computer Scientist: Learning with Python"):
                self.bookid_var.set("BKID5005")
                self.bookname_var.set("How to think like a Computer Scientist: Learning with Python")
                self.author_var.set("Allen B. Downey, Jeffrey Elkner, Chris Meyers")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="6. Learning Python"):
                self.bookid_var.set("BKID5006")
                self.bookname_var.set("Learning Python")
                self.author_var.set("Mark Lutz")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")
            
            if(x=="7. Python Programming: An introduction to Computer Science"):
                self.bookid_var.set("BKID5007")
                self.bookname_var.set("Python Programming: An introduction to Computer Science")
                self.author_var.set("John Zelle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="8. Python Programming for Absolute Beginners"):
                self.bookid_var.set("BKID5008")
                self.bookname_var.set("Python Programming for Absolute Beginners")
                self.author_var.set("Michel Dawson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")

            if(x=="9. Python Cookbook"):
                self.bookid_var.set("BKID5009")
                self.bookname_var.set("Python Cookbook")
                self.author_var.set("David Beazley, Brian Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Python")
            
            if(x=="10. Higher Engineering Mathematics"):
                self.bookid_var.set("BKID5010")
                self.bookname_var.set("Higher Engineering Mathematics")
                self.author_var.set("Dr. B.S. Grewal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Mathematics")

            if(x=="11. Advance Engineering Mathematics"):
                self.bookid_var.set("BKID5011")
                self.bookname_var.set("Advance Engineering Mathematics")
                self.author_var.set("Peter V. O'Neil")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Mathematics")
            
            if(x=="12. Introductory methods of Numerical solutions"):
                self.bookid_var.set("BKID5012")
                self.bookname_var.set("Introductory methods of Numerical solutions")
                self.author_var.set("S.S. Sastry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Mathematics")

            if(x=="13. Numerical Methods"):
                self.bookid_var.set("BKID5013")
                self.bookname_var.set("Numerical Methods")
                self.author_var.set("R.K. Jain, S.R.K. Iyengar")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Mathematics")

            if(x=="14. An introduction to Numerical Methods and Analysis"):
                self.bookid_var.set("BKID5014")
                self.bookname_var.set("An introduction to Numerical Methods and Analysis")
                self.author_var.set("James F. Epperson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Mathematics")

            if(x=="15. Data Structures using C and C++"):
                self.bookid_var.set("BKID5015")
                self.bookname_var.set("Data Structures using C and C++")
                self.author_var.set("Aaron M. Tenenbaum, Yedidyah Langsam, Moshe J. Augenstein")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Data Structure")

            if(x=="16. Data Structures: A Pseudocode approach with C"):
                self.bookid_var.set("BKID5016")
                self.bookname_var.set("Data Structures: A Pseudocode approach with C")
                self.author_var.set("Gilberg, Forouzan")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Data Structure")

            if(x=="17. Fundamentals of Data Structures"):
                self.bookid_var.set("BKID5017")
                self.bookname_var.set("Fundamentals of Data Structures")
                self.author_var.set("Horowitz, Sahani")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Data Structure")
            
            if(x=="18. Data Structures and Algorithms in C++"):
                self.bookid_var.set("BKID5018")
                self.bookname_var.set("Data Structures and Algorithms in C++")
                self.author_var.set("Michael T. Goodrich, Roberto Tamamssia, David M. MOunt")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Data Structure")

            if(x=="19. Data Structures and Program Design in C"):
                self.bookid_var.set("BKID5019")
                self.bookname_var.set("Data Structures and Program Design in C")
                self.author_var.set("R. Kruse Etal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Data Structure")

            if(x=="20. Computer System Architecture"):
                self.bookid_var.set("BKID5020")
                self.bookname_var.set("Computer System Architecture")
                self.author_var.set("M. Mano")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Computer Organization and Architecture")

            if(x=="21. Computer Architecture and Organization"):
                self.bookid_var.set("BKID5021")
                self.bookname_var.set("Computer Architecture and Organization")
                self.author_var.set("John P. Hayes")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Computer Organization and Architecture")

            if(x=="22. Computer Architecture"):
                self.bookid_var.set("BKID5022")
                self.bookname_var.set("Computer Architecture")
                self.author_var.set("Behrooz Parahami")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Computer Organization and Architecture")
            
            if(x=="23. Computer Organization"):
                self.bookid_var.set("BKID5023")
                self.bookname_var.set("Computer Organization")
                self.author_var.set("Carl Hamacher, Zvonko Vranesic, Safwat Zaky")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Computer Organization and Architecture")

            if(x=="24. Discrete Structures"):
                self.bookid_var.set("BKID5024")
                self.bookname_var.set("Discrete Structures")
                self.author_var.set("Koshy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Discrete Structures and Theory of Logic")

            if(x=="25. Mathematics: A Discrete Introduction"):
                self.bookid_var.set("BKID5025")
                self.bookname_var.set("Mathematics: A Discrete Introduction")
                self.author_var.set("E.R. Scheinerman")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Discrete Structures and Theory of Logic")
            
            if(x=="26. Discrete and Combinational Mathematics"):
                self.bookid_var.set("BKID5026")
                self.bookname_var.set("Discrete and Combinational Mathematics")
                self.author_var.set("R.P. Grimaldi")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Discrete Structures and Theory of Logic")

            if(x=="27. Technical Communication- Principles and Practices"):
                self.bookid_var.set("BKID5027")
                self.bookname_var.set("Technical Communication- Principles and Practices")
                self.author_var.set("Meenakshi Raman, Sangeeta Sharma")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Technical Communication")

            if(x=="28. Personality Development and Soft Skills"):
                self.bookid_var.set("BKID5028")
                self.bookname_var.set("Personality Development and Soft Skills")
                self.author_var.set("Barun K. Mitra")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Technical Communication")

            if(x=="29. Soft Skills & Employbility"):
                self.bookid_var.set("BKID5029")
                self.bookname_var.set("Soft Skills & Employbility")
                self.author_var.set("Sabina Pillai, Agna Fernandez")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Technical Communication")

            if(x=="30. Technical Communication"):
                self.bookid_var.set("BKID5030")
                self.bookname_var.set("Technical Communication")
                self.author_var.set("Pfeiffer")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofborrow_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.subject_var.set("Technical Communication")

        list_scrollbar=Scrollbar(DataFrameRight)
        list_scrollbar.grid(row=0,column=1,sticky="ns")

        listbox=Listbox(DataFrameRight,font=("times new roman",14,"bold"),width=50,height=14)
        listbox.bind("<<ListboxSelect>>",select_book)
        listbox.grid(row=0,column=0,padx=4)
        list_scrollbar.config(command=listbox.yview)

        for item in bookslist:
            listbox.insert(END,item)

        #BUTTON FRAME
        FrameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=65)

        add_btn=Button(FrameButton,text="Add Data",command=self.add_data,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        add_btn.grid(row=0,column=0)

        update_btn=Button(FrameButton,text="Update Data",command=self.update_data,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5)

        delete_btn=Button(FrameButton,text="Delete Data",command=self.delete_data,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(FrameButton,text="Reset Data",command=self.reset_data,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5)

        generate_btn=Button(FrameButton,text="Generate Report",command=self.generate,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        generate_btn.grid(row=0,column=4)

        logout_btn=Button(FrameButton,text="Log Out",command=self.exit,font=("times new roman",14,"bold"),width=21,bg="blue",fg="white")
        logout_btn.grid(row=0,column=5,padx=5)

        #INFORMATION FRAME
        FrameInformation=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameInformation.place(x=0,y=595,width=1530,height=195)

        table_frame=Frame(FrameInformation,bd=6,relief=RIDGE,bg="powder blue")
        table_frame.place(x=0,y=2,width=1465,height=170)

        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,column=("membertype","rollno","admno","firstname","lastname","course","branch","section","mobile","bookid","bookname","author","dateofborrow","duedate","days","latereturnfine","dateoverdue","subject"))

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("rollno",text="Roll No.")
        self.library_table.heading("admno",text="Admission No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("course",text="Course")
        self.library_table.heading("branch",text="Branch")
        self.library_table.heading("section",text="Section")
        self.library_table.heading("mobile",text="Mobile No.")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("bookname",text="Book Name")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateofborrow",text="Date of Borrow")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("days",text="Number of days")
        self.library_table.heading("latereturnfine",text="Late Return Fee")
        self.library_table.heading("dateoverdue",text="Date over due")
        self.library_table.heading("subject",text="Subject")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("rollno",width=100)
        self.library_table.column("admno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("course",width=100)
        self.library_table.column("branch",width=100)
        self.library_table.column("section",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("bookname",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateofborrow",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("subject",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    #BUTTON FUNCTIONS
    
    #ADD DATA
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into books values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.rollno_var.get(),
                                                                                                            self.admno_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.course_var.get(),
                                                                                                            self.branch_var.get(),
                                                                                                            self.section_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.bookname_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateofborrow_var.get(),
                                                                                                            self.duedate_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.subject_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member has been inserted successfully!",parent=self.root)

    #UPDATE DATA
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("update books set membertype=%s,rollno=%s,firstname=%s,lastname=%s,course=%s,branch=%s,section=%s,mobile=%s,bookid=%s,bookname=%s,author=%s,dateofborrow=%s,duedate=%s,days=%s,latereturnfine=%s,dateoverdue=%s,subject=%s where admno=%s",(
                                                                                                                                                                                                                                                                            self.member_var.get(),
                                                                                                                                                                                                                                                                            self.rollno_var.get(),
                                                                                                                                                                                                                                                                            self.firstname_var.get(),
                                                                                                                                                                                                                                                                            self.lastname_var.get(),
                                                                                                                                                                                                                                                                            self.course_var.get(),
                                                                                                                                                                                                                                                                            self.branch_var.get(),
                                                                                                                                                                                                                                                                            self.section_var.get(),
                                                                                                                                                                                                                                                                            self.mobile_var.get(),
                                                                                                                                                                                                                                                                            self.bookid_var.get(),
                                                                                                                                                                                                                                                                            self.bookname_var.get(),
                                                                                                                                                                                                                                                                            self.author_var.get(),
                                                                                                                                                                                                                                                                            self.dateofborrow_var.get(),
                                                                                                                                                                                                                                                                            self.duedate_var.get(),
                                                                                                                                                                                                                                                                            self.daysonbook_var.get(),
                                                                                                                                                                                                                                                                            self.latereturnfine_var.get(),
                                                                                                                                                                                                                                                                            self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                                            self.subject_var.get(),
                                                                                                                                                                                                                                                                            self.admno_var.get(),
                                                                                                                                                                                                                                                                        ))
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()

        messagebox.showinfo("Success","Member has been updated successfully!",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from books")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.rollno_var.set(row[1]),
        self.admno_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.course_var.set(row[5]),
        self.branch_var.set(row[6]),
        self.section_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.bookname_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateofborrow_var.set(row[12]),
        self.duedate_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.subject_var.set(row[17])

    #RESET DATA
    def reset_data(self):
        self.member_var.set(""),
        self.rollno_var.set(""),
        self.admno_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.course_var.set(""),
        self.branch_var.set(""),
        self.section_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.bookname_var.set(""),
        self.author_var.set(""),
        self.dateofborrow_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.subject_var.set(""),
    
    #GENERATE REPORT
    def generate(self):
        self.new_window=Toplevel(self.root)  
        self.app=Generate_Report(self.new_window)

    #LOG OUT
    def exit(self):
        iexit=tkinter.messagebox.askyesno("Library Management System","Do you want to log-out?",parent=self.root)
        if iexit>0:
            self.root.destroy()
            return
        
    #DELETE DATA
    def delete_data(self):
        if self.admno_var.get()=="" or self.rollno_var.get()=="":
            messagebox.showerror("Error","First select the member!",parent=self.root)
        else:
            delete=messagebox.askyesno("Delete","Do you want to delete this member's  details?",parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
                my_cursor=conn.cursor()
                query="delete from books where admno=%s"
                value=(self.admno_var.get(),)
                my_cursor.execute(query,value)
            else:
                if not delete:
                    return

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted successfully!",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()