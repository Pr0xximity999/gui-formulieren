from logging import exception
from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.resizable(0,0)
window.geometry('450x400')
window.title('Registration window')

#showinfo('Welcome', 'Welcome to this registration for the annual gamer convention')
#showinfo('Welcome', 'You will need to awnser a few questions before your registration will be accepted')

def tick(arg1='', arg2='', arg3=''):
    print(arg1)

widgets = {}
#places a widget on the grid with the correct question and options
def gridAlign(frame:Frame, widget, questionName:str, question:str, options:list=[], afterText:str=''):
    global widgets
    #Defines the current row
    currentRow = frameWidgetCount[frame]
    frameWidgetCount[frame] = frameWidgetCount[frame] + 1

    #Defines the stringvar and question label
    stringV = StringVar(name=questionName)
    stringV.trace('w', tick)

    #A label just for the spacing
    spaceLbl = Label(frame, width=5)
    spaceLbl.grid(column=1, row=currentRow)

    #The label for the question text
    questionLbl = Label(frame, text=question)
    questionLbl.grid(column=0, row=currentRow, sticky=W, pady=5)

    #The label for the optional text behind the widget
    afterlbl = Label(frame, text=afterText)
    afterlbl.grid(column=3, row=currentRow, sticky=E)

    #Makes the correct widget and places them on the grid
    if widget == Entry:
        widget = Entry(frame, textvariable=stringV)     

    elif widget == Spinbox:
        widget = Spinbox(frame, from_=options[0], to=options[-1], textvariable=stringV)

    elif widget == Radiobutton:
        for i in range(len(options)):
            widget = Radiobutton(frame, text=options[i], value=options[i][0], variable=stringV, tristatevalue='x')
            widget.deselect()
            widget.grid(row=currentRow, column=i + 2, sticky=W)
        widgets.update({questionName: stringV})
        return
    
    else:
        raise exception('Choose a valid widget')
            
    #And lastly, adds them to a dictionairy
    widget.grid(column=2, row=currentRow, columnspan=2, sticky=W)
    widgets.update({questionName: stringV})
    
    
#The frames for the window
frame1 = Frame(window) 
frame2 = Frame(window)

frameList = [frame1, frame2]

frameWidgetCount = {
    frame1  :   0,
    frame2  :   0
}
frameNum = -1
def nextFrame():#Switches aroundthe frames
    global frameNum
    currentframe = frameList[frameNum]
    currentframe.place(relx=1.1, rely=1.1)
    frameNum += 1
    currentframe = frameList[frameNum]
    currentframe.place(relheight=1, relwidth=1, relx=0, rely=0)

def finish():#When the user is finished
    showwarning('sus', 'YO MAMA DO BE SUS THO')
    exit()

#Frame 1 stuff
gridAlign(frame1, Entry, 'name', 'What is your name')   #The name question

gridAlign(frame1, Spinbox, 'age', 'How old are you', [0, str('inf')], 'years')   #The age question

gridAlign(frame1, Entry, 'country', 'Where do you live(Country)')   #The country question

gridAlign(frame1, Radiobutton, 'isGamer', 'Are you a gamer', ['yes', 'no'])  #The gamer question

gridAlign(frame1, Radiobutton, 'playsFortnite', 'Do you play fortnite', ['yes', 'no'])  #The most important question question

gridAlign(frame1, Radiobutton, 'keyboardType', 'What kind of keyboard do you have', ['mechanical', 'membrame']) #The keyboard question


#Frame 2 stuff
gridAlign(frame2, Radiobutton, 'watchesAnime', 'Do you watch anime', ['yes', 'no', 'I rather not say'])

#The buttons for going to the next frame or finishing the questioning
for i in frameList:
    btn = Button(i)
    btn.configure(text='Next page', command=nextFrame) if i != frameList[-1] else btn.configure(text='Finish', command=finish)
    btn.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

nextFrame()
window.mainloop()