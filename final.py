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

        dictOperations = {}
        dictOperations['listColorGame'] = listColorGame
        dictOperations['listBricksGame'] = listBricksGame
        dictOperations['listSearchFacebook'] = listSearchFacebook
        dictOperations['listMail'] = listMail
        userID = userIndex - 1
        users[str(userID)] = dictOperations
        return users


    def build(self,filePath):
        dfTouches = self.load_csv(filePath)
        users = self.devide(dfTouches)

class project:
    model = Model()

    # The function give the user the search for the path
    def browse(self):
        file = tkinter.filedialog.askopenfilename()
        self.var.set(file)

    def build(self):
        touchesPath = self.var.get()
        questPath = self.var2.get()
        self.model.build(touchesPath,questPath)

    # The function init the gui
    def __init__(self, master):
        self.master = master
        self.master.title("out project")
        self.labelDir = Label(master, text="touches Path")
        self.var = StringVar()
        dirname = Entry(master, textvariable=self.var)
        self.labelDir2 = Label(master, text="quest Path")
        self.var2 = StringVar()
        dirname2 = Entry(master, textvariable=self.var2)
        self.browse_button = Button(master, text="Browse", command=lambda: self.browse())  # button browse
        self.build_button = Button(master, text="Build", command=lambda: self.build())  # button build
        # self.classify_button = Button(master, text="Classify", command=lambda: self.classify())
        self.labelDir.grid(row=0, column=0, sticky=W)
        self.labelDir.grid(row=1, column=0, sticky=W)
        dirname.grid(row=0, column=1, columnspan=2, sticky=W + E)
        dirname2.grid(row=1, column=1, columnspan=2, sticky=W + E)
        self.browse_button.grid(row=0, column=3)
        self.build_button.grid(row=2, column=1)
        # self.classify_button.grid(row=3, column=1)


root = Tk()
my_gui = project(root)
root.mainloop()