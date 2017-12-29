from tkinter import *
import xlrd
import pandas as pd
import tkinter.filedialog
import tkinter.messagebox

class Model:
    # The function load csv file
    def load_csv(self, filePath):
        try:
            df = pd.read_csv(filePath)
            return df
        except:
            tkinter.messageBox.showerror("project", "the path " + filePath + " is not exist")

    def devide(self,df):
        userIndex = 2
        iterateIndex = 1
        list = []
        for index, row in df.iterrows():
            partofrow = '#' + str(userIndex) + '.' + str(iterateIndex)
            if partofrow in row['TIME']:
                iterateIndex = iterateIndex+1
                print(row)
            # else: list.append(row)


        # for r in df.set_index('TIME'):
        #     if r.filter(like='#', axis=0):
        #         print("bllala")
        # group = df.set_index('TIME').filter(like='#', axis=0)
        # print(group)

    def build(self,filePath):
        df = self.load_csv(filePath)
        self.devide(df)

class project:
    model = Model()

    # The function give the user the search for the path
    def browse(self):
        file = tkinter.filedialog.askopenfilename()
        self.var.set(file)

    def build(self):
        filePath = self.var.get()
        self.model.build(filePath)

    # The function init the gui
    def __init__(self, master):
        self.master = master
        self.master.title("out project")
        self.labelDir = Label(master, text="file Path")
        self.var = StringVar()
        dirname = Entry(master, textvariable=self.var)
        self.browse_button = Button(master, text="Browse", command=lambda: self.browse())  # button browse
        self.build_button = Button(master, text="Build", command=lambda: self.build())  # button build
        # self.classify_button = Button(master, text="Classify", command=lambda: self.classify())
        self.labelDir.grid(row=0, column=0, sticky=W)
        dirname.grid(row=0, column=1, columnspan=2, sticky=W + E)
        self.browse_button.grid(row=0, column=3)
        self.build_button.grid(row=2, column=1)
        # self.classify_button.grid(row=3, column=1)


root = Tk()
my_gui = project(root)
root.mainloop()