from tkinter import *

window=Tk()
window.geometry("400x400")

def Close():
        exit()

def main():
        Merk=StringVar()
        NoPol=StringVar()
        Warna=StringVar()
        Kondisi=StringVar()
        
        L1=Label(text="Merk")
        L1.grid(row=0,column=0)
        E1=Entry(window,textvariable=Merk)
        E1.grid(row=0,column=1)

        L1=Label(text="NoPol")
        L1.grid(row=0,column=2)
        E2=Entry(window,textvariable=NoPol)
        E2.grid(row=0,column=3)

        L1=Label(text="Warna")
        L1.grid(row=1,column=0)
        E3=Entry(window,textvariable=Warna)
        E3.grid(row=1,column=1)

        L1=Label(text="Kondisi")
        L1.grid(row=1,column=2)
        E4=Entry(window,textvariable=Kondisi)
        E4.grid(row=1,column=3)

        L1=Label(text="")
        L1.grid(row=2,column=0)

        list1=Listbox(window,height=6,width=25)
        list1.grid(row=3,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        b1=Button(window,text="View All",width=15)
        b1.grid(row=2,column=3)

        b1=Button(window,text="Search Entry",width=15)
        b1.grid(row=3,column=3)

        b1=Button(window,text="Add Entry",width=15)
        b1.grid(row=4,column=3)

        b1=Button(window,text="Update Selected",width=15)
        b1.grid(row=5,column=3)

        b1=Button(window,text="Delete Selected",width=15)
        b1.grid(row=6,column=3)

        b1=Button(window,text="Close",width=15,command=Close)
        b1.grid(row=7,column=3)
        window.mainloop()





        




        
main()

