from tkinter import*
import customtkinter as ctk
from PIL import Image,ImageTk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Generate_Report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Library Management System")

        #bg image
        img4=Image.open(r"Images\bgimg2.jpg")
        img4=img4.resize((1538,665),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=128,width=1538,height=665)

        lbl_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        generate_btn=Button(self.root,text="Generate Report",command=self.generate,font=("times new roman",20,"bold"),width=21,height=2,bd=5,bg="black",fg="white")
        generate_btn.place(x=600,y=400)

    #GENERATE REPORT
    def count(self,subjects):
        py=math=ds=coa=dstl=tc=0
        for s in subjects:
            if s=='Python':
                py+=1
            elif s=='Mathematics':
                math+=1
            elif s=='Data Structure':
                ds+=1
            elif s=='Computer Organization and Architecture':
                coa+=1
            elif s=='Discrete Structures and Theory of Logic':
                dstl+=1
            elif s=='Technical Communication':
                tc+=1
        subject_count=[py,math,ds,coa,dstl,tc]
        return(subject_count)
    
    def count_member(self,members):
        ads=std=prf=0
        for m in members:
            if m=='Admin Staff':
                ads+=1
            elif m=='Student':
                std+=1
            elif m=='Professor':
                prf+=1
        member_count=[ads,std,prf]
        return(member_count)
    
    def count_course(self,course):
        btech=mca=bpharma=0
        for c in course:
            if c=='B.TECH':
                btech+=1
            elif c=='MCA':
                mca+=1
            elif c=='B.PHARMA':
                bpharma+=1
        course_count=[btech,mca,bpharma]
        return(course_count)
    
    def count_branch(self,branch):
        cse=ece=it=eee=me=ce=0
        for b in branch:
            if b=='CSE':
                cse+=1
            elif b=='ECE':
                ece+=1
            elif b=='IT':
                it+=1
            elif b=='EEE':
                eee+=1
            elif b=='ME':
                me+=1
            elif b=='CE':
                ce+=1
        branch_count=[cse,ece,it,eee,me,ce]
        return(branch_count)
        
    def generate(self):
        stats_frame = ctk.CTkScrollableFrame(master=self.root)
        stats_frame.pack(expand=True, fill="both")
        stats_frame.columnconfigure((0,1), weight=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select subject from books")
        rows=my_cursor.fetchall()
        subject_label=[x[0] for x in rows]
        conn.commit()
        conn.close()
        subject_count=self.count(subject_label)        

        fig1,ax1=plt.subplots()
        subject=['Python','Mathematics','Data Structure','Computer Organization and Architecture','Discrete Structures and Theory of Logic','Technical Communication']
        color1=['skyblue','lightpink','yellow','red','lightgreen','brown']
        ax1.pie(subject_count,labels=subject,colors=color1,autopct='%1.1f%%')
        ax1.set_title("Subject Wise")
        
        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select membertype from books")
        rows=my_cursor.fetchall()
        member_label=[x[0] for x in rows]
        conn.commit()
        conn.close()
        member_count=self.count_member(member_label)

        fig2,ax2=plt.subplots()
        member=['Admin Staff','Student','Professor']
        color2=['skyblue','lightpink','yellow']
        ax2.pie(member_count,labels=member,colors=color2,autopct='%1.1f%%')
        ax2.set_title("Member Type Wise")

        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select course from books")
        rows=my_cursor.fetchall()
        course_label=[x[0] for x in rows]
        conn.commit()
        conn.close()
        course_count=self.count_course(course_label)

        fig3,ax3=plt.subplots()
        course=['B.TECH','MCA','B.PHARMA']
        color3=['lightgreen','lightpink','yellow']
        ax3.pie(course_count,labels=course,colors=color3,autopct='%1.1f%%')
        ax3.set_title("Course Wise")

        conn=mysql.connector.connect(host="localhost",username="root",password="2107",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select branch from books")
        rows=my_cursor.fetchall()
        branch_label=[x[0] for x in rows]
        conn.commit()
        conn.close()
        branch_count=self.count_branch(branch_label)

        fig4,ax4=plt.subplots()
        branch=['CSE','ECE','IT','EEE','ME','CE']
        color4=['lightgreen','skyblue','yellow']
        ax4.pie(branch_count,labels=branch,colors=color4,autopct='%1.1f%%')
        ax4.set_title("B.Tech Branch Wise")

        graph_frame=Frame(stats_frame)
        graph_frame.pack(fill="both")

        upper_frame=Frame(graph_frame)
        upper_frame.pack(fill="both",expand=True)

        canvas1=FigureCanvasTkAgg(fig1,upper_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left",fill="both",expand=True)

        canvas2=FigureCanvasTkAgg(fig2,upper_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left",fill="both",expand=True)

        lower_frame=Frame(graph_frame)
        lower_frame.pack(fill="both",expand=True)

        canvas3=FigureCanvasTkAgg(fig3,lower_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left",fill="both",expand=True)

        canvas4=FigureCanvasTkAgg(fig4,lower_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side="left",fill="both",expand=True)

if __name__=="__main__":
    root=Tk()
    obj=Generate_Report(root)
    root.mainloop()