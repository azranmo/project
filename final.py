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
        listColorGame = []
        listBricksGame = []
        listSearchFacebook = []
        listMail = []
        users = {}
        firstIter = True
        for row in df.itertuples():
            indexRow = row[0]
            timeRow = row[1]
            if '#' + str(userIndex) in timeRow: #new user
                if firstIter==False:
                    dictOperations = {}
                    dictOperations['listColorGame'] = listColorGame
                    dictOperations['listBricksGame'] = listBricksGame
                    dictOperations['listSearchFacebook'] = listSearchFacebook
                    dictOperations['listMail'] = listMail
                    userID = userIndex - 1
                    users[str(userID)] = dictOperations
                userIndex = userIndex + 1
                iterateIndex = 1
                listColorGame = []
                listBricksGame = []
                listSearchFacebook = []
                listMail = []
                firstIter = False
            elif '#' + str(userIndex-1) + '.' + str(iterateIndex+1) in timeRow:
                iterateIndex = iterateIndex + 1
            else:
                if iterateIndex==1:
                    listColorGame.append(row)
                elif iterateIndex==2:
                    listBricksGame.append(row)
                elif iterateIndex==3:
                    listSearchFacebook.append(row)
                else:
                    listMail.append(row)

        print(listColorGame)
        print(listBricksGame)
        print(listSearchFacebook)
        print(listMail)
        print("****************")
        print(users)


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