from tkinter import *
import pymysql
from ExecuteSQLScript import *
from tkinter import messagebox

class Lms(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1366x768+0+0")
        self.title("Library Management System")
        container=Frame(self,bg='blue')
        container.pack()

        self.frames = {}
        for F in (Home, IssueBook, EnterBook, ShowBook, ReturnBook):
            new_frame_name=F.__name__
            frame=F(parent=container,controller=self)
            frame.grid(row=0,column=0,sticky="nsew")
            self.frames[new_frame_name]=frame
            self.show_frame("Home")

        self.db = pymysql.connect(user='root', password='', host='localhost')

        c = self.db.cursor()
        ExecuteSQLScript().execute('sql_script.sql',c)
        self.db.commit()
        self.db.close()

    def show_frame(self,new_frame_name):
        frame = self.frames[new_frame_name]
        frame.tkraise()

    def qExit(self):
        qExit = messagebox.askyesno('Quit library','Do you want to quit library management system?')
        if qExit > 0:
            self.destroy()
            return


class Home(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent,bg='yellow')

        button1= Button(self,text="Show the list\n of available books.",width=15,height=10,command=lambda : controller.show_frame("ShowBook"))

        button2= Button(self,text="Issue a book.",width=15,height=10,command=lambda :controller.show_frame("IssueBook"))

        button3= Button(self,text="Return a book.",width=15,height=10,command=lambda :controller.show_frame("ReturnBook"))

        button4= Button(self,text="Enter a book.",width=15,height=10,command=lambda :controller.show_frame("EnterBook"))

        exit_button=Button(self,text="Exit",width=10,height=5,command=lambda: controller.qExit())


        button1.grid(row=0,column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=1, column=0)
        button4.grid(row=1, column=1)
        exit_button.grid(row=2,columnspan=2,sticky="nsew")


class IssueBook(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Issue book")
        label.grid(row=0,columnspan=2)
        button1= Button(self,text="Home",width=15,height=10,command=lambda : controller.show_frame("Home"))

        button2= Button(self,text="Submit",width=15,height=10,command=lambda: self.issue_book())

        label1 = Label(self,text="Member Id",width=15,height=5,justify=LEFT)
        label2 = Label(self, text="Issue NO.", width=15, height=5,justify=LEFT)
        label3 = Label(self, text="Book name", width=15, height=5,justify=LEFT)
        label4 = Label(self, text="Book code", width=15, height=5,justify=LEFT)
        label5 = Label(self, text="Issuing date", width=15, height=5,justify=LEFT)
        label6 = Label(self, text="Returning date", width=15, height=5,font=('freeboofer',10,'bold'),justify=LEFT)
        self.e1_text= IntVar()
        self.e2_text = StringVar()
        self.e3_text = StringVar()
        self.e4_text = IntVar()
        self.e5_text = StringVar()
        self.e6_text = StringVar()

        self.entry1 = Entry(self,width=15,bg='medium turquoise',cursor='dot',fg='red',highlightcolor='blue',relief='flat'\
                            ,selectforeground='yellow',\
                            selectbackground='black',textvariable=self.e1_text,justify=LEFT)
        self.entry2 = Entry(self, width=15,bg='medium turquoise',textvariable=self.e2_text,justify=LEFT,relief='flat')
        self.entry3 = Entry(self, width=15,bg='medium turquoise',textvariable=self.e3_text,justify=LEFT,relief='flat')
        self.entry4 = Entry(self,width=15,font='freeboofer',bg='medium turquoise',textvariable=self.e4_text,justify=LEFT,relief='flat')
        self.entry5 = Entry(self, width=15,bg='medium turquoise',textvariable=self.e5_text,justify=LEFT,relief='flat')
        self.entry6 = Entry(self, width=15,bg='medium turquoise',textvariable=self.e6_text,justify=LEFT,relief='flat')

        label1.grid(row=1, column=0)
        label2.grid(row=2, column=0)
        label3.grid(row=3, column=0)
        label4.grid(row=4, column=0)
        label5.grid(row=5, column=0)
        label6.grid(row=6, column=0)

        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        self.entry3.grid(row=3, column=1)
        self.entry4.grid(row=4, column=1)
        self.entry5.grid(row=5, column=1)
        self.entry6.grid(row=6, column=1)

        button1.grid(row=7,column=0)
        button2.grid(row=7, column=1)

    def issue_book(self):
        import datetime
        import pytz
        db = pymysql.connect(user='root', password='', host='localhost', db='lms')

        c = db.cursor()
        self.issue_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
        self.return_date = self.issue_date + datetime.timedelta(days=15,hours=23-self.issue_date.hour,minutes=59-self\
                                                                .issue_date.minute,seconds=59-self.issue_date.second)
        print("current date=",self.issue_date)
        print("return date=",self.return_date)

        c.execute("INSERT INTO issued_books (book_id,reader_id,issue_date,return_date) VALUES ('%d','%d','%s','%s')" \
                  % (self.e4_text.get(), self.e1_text.get(),self.issue_date,self.return_date))

        c.execute("select date(issue_date) from issued_books where book_id='%d'\
         and reader_id='%d'"%(self.e4_text.get(), self.e1_text.get()))
        data= c.fetchone()

        for row in data: self.e5_text.set(row)
        c.execute("select date(return_date) from issued_books where book_id='%d'\
                 and reader_id='%d'" % (self.e4_text.get(), self.e1_text.get()))
        data = c.fetchone()

        for row in data: self.e6_text.set(row)

        c.execute("select book_name from available_books where book_id='%d'" % (self.e4_text.get()))
        data = c.fetchone()
        for row in data: self.e3_text.set(row)

        c.execute("select issue_id from issued_books where book_id='%d'\
                 and reader_id='%d'" % (self.e4_text.get(), self.e1_text.get()))
        data = c.fetchone()
        for row in data: self.e2_text.set(row)
        db.commit()
        db.close()


class EnterBook(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Enter book")
        label.grid(row=0,columnspan=2)
        button1= Button(self,text="Home",width=15,height=10,command=lambda : controller.show_frame("Home"))

        button2= Button(self,text="Submit",width=15,height=10,command=lambda: self.enter_book())

        label1 = Label(self,text="Book code",width=15,height=5,justify=LEFT)
        label2 = Label(self, text="Book name", width=15, height=5,justify=LEFT)
        label3 = Label(self, text="Author name", width=15, height=5,justify=LEFT)
        label4 = Label(self, text="Acronym", width=15, height=5,justify=LEFT)
        label5 = Label(self, text="Rack no.", width=15, height=5,justify=LEFT)
        label6 = Label(self, text="Total copies", width=15, height=5,justify=LEFT)
        self.e1_text=IntVar()

        self.e2_text=StringVar()
        self.e3_text = StringVar()

        self.entry1 = Entry(self,width=15,textvariable=self.e1_text,bg='medium turquoise',justify=LEFT)
        self.entry2 = Entry(self, width=15,textvariable=self.e2_text,bg='medium turquoise',justify=LEFT)
        self.entry3 = Entry(self, width=15,textvariable=self.e3_text,bg='medium turquoise',justify=LEFT)
        self.entry4 = Entry(self, width=15,bg='medium turquoise',justify=LEFT)
        entry5 = Entry(self, width=15,bg='medium turquoise',justify=LEFT)
        entry6 = Entry(self, width=15,bg='medium turquoise',justify=LEFT)

        label1.grid(row=1,column=0)
        label2.grid(row=2, column=0)
        label3.grid(row=3, column=0)
        #label4.grid(row=4, column=0)
        label5.grid(row=5, column=0)
        label6.grid(row=6, column=0)

        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        self.entry3.grid(row=3, column=1)
        #self.entry4.grid(row=4, column=1)
        entry5.grid(row=5, column=1)
        entry6.grid(row=6, column=1)


        button1.grid(row=7,column=0)
        button2.grid(row=7, column=1)

    def enter_book(self):

        db = pymysql.connect(user='root', password='', host='localhost',db='lms')

        c = db.cursor()
        c.execute("INSERT INTO available_books (book_name,Author) VALUES ('%s','%s')"%(self.e2_text.get(),self.e3_text.get()))
        c.execute("select book_id from available_books where book_name='%s' and Author='%s'"%(self.e2_text.get(),self.e3_text.get()))
        data= c.fetchone()
        for row in data: self.e1_text.set(row)
        db.commit()

        db.close()


class ShowBook(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        frame_top1=Frame(self,width=1366,height=50,bg='black')
        self.frame_top2=Frame(self,width=1366,height=768-300,bg='green')
        frame_top3=Frame(self,width=1366,height=150,bg='blue')
        frame_top4=Frame(self,width=1366,height=100,bg='yellow')
        frame_top1.grid(row=0, column=0,sticky='nsew')
        self.frame_top2.grid(row=1, column=0,sticky='nsew')
        frame_top3.grid(row=2, column=0,sticky='nsew')
        frame_top4.grid(row=3, column=0,sticky='nsew')
        frame_top1.pack_propagate(0)
        self.frame_top2.grid_propagate(0)
        frame_top3.grid_propagate(0)
        frame_top4.pack_propagate(0)
        self.canvas=Canvas(self.frame_top2)
        self.frame=Frame(self.canvas)
        myscrollbar = Scrollbar(self.frame_top2, orient="vertical", command=self.canvas.yview,width=25)
        self.canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>",self.myfunction)


        label = Label(frame_top1, text="List of total available books")
        label.pack(side=TOP,anchor='center')
        frame_temp=Frame(frame_top4,width=500,height=100,bg='yellow')
        frame_temp.pack(side=LEFT)
        frame_tem2=Frame(frame_top3,height=150,width=500,bg='blue')
        frame_tem2.grid(row=0,column=0,columnspan=3,rowspan=3)

        button1 = Button(frame_top4, text="Home", width=15, height=2, command=lambda: controller.show_frame("Home"))

        button2 = Button(frame_top4, text="Refresh", width=15, height=2,command=lambda : self.show_books())
        button1.pack(side=LEFT,anchor='n')
        button2.pack(side=LEFT,anchor='n')

        self.total_books=IntVar()
        self.available_books=IntVar()
        self.issued_books=IntVar()
        #
        label1 = Label(frame_top3, text="Total no. of books")#, width=15, height=2)
        label2 = Label(frame_top3, text="Available books")#, width=15, height=2)
        label3 = Label(frame_top3, text="Issued books")#, width=15, height=2)
        label4 = Label(frame_top3,textvariable=self.total_books)#, width=15, height=2,
        label5 = Label(frame_top3,textvariable=self.available_books)#, width=15, height=2,
        label6 = Label(frame_top3,textvariable=self.issued_books)#, width=15, height=2,



        #
        label1.grid(row=0,column=3)
        label2.grid(row=1,column=3)
        label3.grid(row=2,column=3)
        Label(frame_top3,width=1,height=1,bg='blue').grid(row=0,column=4,columnspan=2)
        label4.grid(row=0,column=6)
        label5.grid(row=1,column=6)
        label6.grid(row=2,column=6)
        #

        #
        label21 = Label(self.frame, text="Serial Num",width=11)
        label21.grid(row=0,column=0)#(row=0, column=0)
        label22=Label(self.frame, text="Book ID",width=7)
        label22.grid(row=0, column=1)
        label23=Label(self.frame, text="Book Name",width=20,anchor='w')
        label23.grid(row=0, column=2)
        label24=Label(self.frame, text="Author",width=15,anchor='w')
        label24.grid(row=0, column=3)
        label25=Label(self.frame, text="Rack Num",width=8)
        label25.grid(row=0, column=4)
        label26=Label(self.frame, text="Total Copies",width=12)
        label26.grid(row=0, column=5)

    def show_books(self):
        db = pymysql.connect(user='root', password='', host='localhost', db='lms')

        c = db.cursor()
        c.execute("select sum(Total_copies) from available_books")
        data = c.fetchone()
        for row in data: self.total_books.set(row)

        c.execute("select count(issue_id) from issued_books")
        data = c.fetchone()
        for row in data: self.issued_books.set(row)

        self.available_books.set(str(int(self.total_books.get()) - int(self.issued_books.get())))


        c.execute("select * from available_books")
        data = c.fetchall()
        rows = 0
        columns = 0
        num = 0
        for row in data:
            rows += 1
            num += 1
            Label(self.frame, text=num,width=11,justify=LEFT).grid(row=rows, column=columns)

            Label(self.frame, text=row[0],width=7,justify=LEFT).grid(row=rows, column=columns + 1)
            Label(self.frame, text=row[1],width=20,justify=LEFT,anchor='w').grid(row=rows, column=columns + 2)
            Label(self.frame, text=row[2],width=15,justify=LEFT,anchor='w').grid(row=rows, column=columns + 3)
            Label(self.frame, text=row[3],width=8,justify=LEFT).grid(row=rows, column=columns + 4)
            Label(self.frame, text=row[4],width=12,justify=LEFT).grid(row=rows, column=columns + 5)


        db.commit()

        db.close()

    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=1341, height=768-300)


class ReturnBook(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Enter Book id and Reader id")
        label.grid(row=0, columnspan=2)

        button1 = Button(self, text="Home", width=15, height=5, command=lambda: controller.show_frame("Home"))

        button2 = Button(self, text="Submit", width=15, height=5,command=lambda: self.return_book())

        label1 = Label(self, text="Book id", width=15, height=5)
        label2 = Label(self, text="Reader id", width=15, height=5)
        self.e1_text=IntVar()
        self.e2_text=IntVar()

        entry1=Entry(self,width=15,textvariable=self.e1_text,bg='medium turquoise')
        entry2=Entry(self,width=15,textvariable=self.e2_text,bg='medium turquoise')

        label1.grid(row=1, column=0)
        entry1.grid(row=1,column=1)
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
        button1.grid(row=3, column=0)
        button2.grid(row=3, column=1)

    def return_book(self):
        db = pymysql.connect(user='root', password='', host='localhost', db='lms')

        c = db.cursor()
        c.execute("delete from issued_books where book_id='%d' and reader_id='%d'" % (
                   self.e1_text.get(), self.e2_text.get()))
        db.commit()

        db.close()


if __name__ == '__main__':
    app = Lms()

    app.mainloop()