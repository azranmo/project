import xlrd
import pandas as pd



class Model:

    def readFromCSV(self):
        # Assign spreadsheet filename to file
        file = 'C:\esti.csv'
        df = pd.read_csv(file)
        return df

    def devide(self,df):
        for index, row in df.iterrows():
            if '#' in row['TIME']:
                print(row)
        # for r in df.set_index('TIME'):
        #     if r.filter(like='#', axis=0):
        #         print("bllala")
        # group = df.set_index('TIME').filter(like='#', axis=0)
        # print(group)












    def build(self):
        df = self.readFromCSV()
        self.devide(df)







def main():
    print("gg")
    print("fff")
    model = Model()
    model.build()


if __name__ == "__main__":
    main()