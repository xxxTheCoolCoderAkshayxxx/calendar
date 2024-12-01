import tkinter
import calendar
class calenderApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Akshay's calender")
        self.root.geometry("300x300")
        self.root.config(background="light grey")
        self.createwidgets()
    def createwidgets(self):
        titleLabel=tkinter.Label(self.root,text="calender",bg="Red",font=("Arial",24))
        titleLabel.grid(row=0,column=0,columnspan=2,pady=10)
        yearLabel=tkinter.Label(self.root,text="year: ",bg="Red",font=("Arial",12))
        yearLabel.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
        
        self.yearEntry=tkinter.Entry(self.root,bg="light grey")
        self.yearEntry.grid(row=1,column=2)
        showBtn=tkinter.Button(text="Show calender",command=self.showcalender)
        showBtn.grid(row=2,column=0,columnspan=2)
        exitBtn=tkinter.Button(text="Exit",bg="light grey",command=self.root.quit)
        exitBtn.grid(row=3,column=0,columnspan=2,pady=10)
    def showcalender(self):
        calendarWindow=tkinter.Toplevel(self.root)
        calendarWindow.title("yearly Calendar")
        calendarWindow.geometry("600x400")
        year=int(self.yearEntry.get())
        calendarContent=calendar.calendar(year)
        calendarText=tkinter.Text(calendarWindow,font=("Arial",12),wrap="none")
        calendarText.insert(tkinter.END,calendarContent)
        calendarText.pack(expand=True,fill="both")
        scrollBar=tkinter.Scrollbar(calendarWindow,command=calendarText.yview)
        scrollBar.pack(side="right",fill="y")
        calendarText.config(yscrollcommand=scrollBar.set)
if __name__ == "__main__":
    root=tkinter.Tk()
    app=calenderApp(root)
    root.mainloop()
    



