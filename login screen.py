from tkinter import*

def signup():
    screen1=Toplevel()
    screen1.title("Sign Up")
    screen1.geometry("300x300")
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Please enter your details down below : ").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username").pack()
    Entry(screen1,textvariable=username).pack()
    


def login():
    print("Dimulai")
    
    

    
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x300")
    screen.title("test")
    Label(text="Test1.0",bg="red",width="300",font=("Times New Roman",12)).pack()
    Button(text="Login",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Sign Up",width="30",command=signup).pack()
    screen.mainloop

main_screen()
                
