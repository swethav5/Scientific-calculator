from tkinter import *
import math
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=90, height=5,background="white", foreground="black")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        #self.configure(background="light green") 
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B",None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('1/x')
        b16 = self.createButton('-')
        b17 = self.createButton('x^2')
        b18 = self.createButton('x^3')
        b19 = self.createButton('10^x')
        b20 = self.createButton('+')
        b21 = self.createButton('sin')
        b22 = self.createButton('cos')
        b23 = self.createButton('tan')
        b24 = self.createButton('log')
        b25 = self.createButton('=',None,50)

        # buttons stored in list
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1,7):
            for column in range(4):
                buttons[count].grid(row=row,column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[24].grid(row=7,column=0,columnspan=40)

    def createButton(self,val,write=True,width=20,height=2,fg='blue',bg='white'):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val,command = lambda: self.click(val,write), width=width,height=height,fg=fg,bg=bg)

    def click(self,text,write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
        if write == None:

            #only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                # replace the unicode value of division ./.with python division symbol / using regex
                self.equation= re.sub(u"\u00F7", '/', self.equation)
               # print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == u"\u232B":
                self.clear_screen()
           
        elif text == 'sin':
            answer = math.sin(math.radians(float(self.equation)))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
           
        elif text == 'cos':
            answer = math.cos(math.radians(float(self.equation)))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
           
        elif text == 'tan':
             answer = math.tan(math.radians(float(self.equation)))
             self.clear_screen()
             self.insert_screen(answer,newline=True)
             
        elif text == 'log':
            answer=math.log(float(self.equation))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
           
        elif text == 'x^3':
            answer=pow(int(self.equation),3)
            self.clear_screen()
            self.insert_screen(answer,newline=True)
           
        elif text == 'x^2':
            answer=pow(int(self.equation),2)
            self.clear_screen()
            self.insert_screen(answer,newline=True)
           
        elif text == '10^x':
            answer=pow(10,int(self.equation))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
        elif text == '1/x':
            answer=float(1/(int(self.equation)))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
        else:
            # add text to screen
            self.insert_screen(text)
       

    def clear_screen(self):
        #to clear screen
        #set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state ='disabled')

root = Tk()
my_gui = Calculator(root)
root.mainloop()


