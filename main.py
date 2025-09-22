from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from library import LibraryManagementSystem
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Library Management System")

        #VARIABLES
        self.var_username=StringVar()
        self.var_password=StringVar()

        #bg image
        img4=Image.open(r"Images\bgimg.jpg")
        img4=img4.resize((1538,665),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=128,width=1538,height=665)

        lbl_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=620,y=260,width=300,height=370)

        get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"))
        get_str.place(x=20,y=20)

        username=Label(frame,text="Username-",font=("times new roman",14,"bold"),bg="powderblue")
        username.place(x=70,y=80)
        self.text_user=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",14,"bold"))
        self.text_user.place(x=20,y=120)

        password=Label(frame,text="Password-",font=("times new roman",14,"bold"),bg="powderblue")
        password.place(x=70,y=160)
        self.text_pass=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",14,"bold"),show='*')
        self.text_pass.place(x=20,y=200)

        def show_password():
            if self.text_pass.cget('show')=='*':
                self.text_pass.config(show='')
            else:
                self.text_pass.config(show='*')

        check=Checkbutton(frame,text="Show Password",command=show_password,font=("times new roman",14,"bold"),bg="powderblue")
        check.place(x=45,y=230)

        login_btn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="black",fg="white",activebackground="white",activeforeground="black")
        login_btn.place(x=60,y=280,width=120,height=40)
    
    def login(self):
        if self.text_user.get()=="" or self.text_pass.get()=="":
            messagebox.showerror("Error","All fields are required !",parent=self.root)
        elif self.text_user.get()=="Anushka" and self.text_pass.get()=="2107":
            self.enter()
            self.reset()
        else:
            messagebox.showerror("Invalid","Invalid Username or Password !",parent=self.root)

    def enter(self):
        self.new_window=Toplevel(self.root)  
        self.app=LibraryManagementSystem(self.new_window)

    def reset(self):
        self.var_username.set(""),
        self.var_password.set(""),

if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()