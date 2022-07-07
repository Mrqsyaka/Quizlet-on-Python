import pandas as pd
import tkinter.filedialog as tkFileDialog
import tkinter
"""creation of list from excel column"""
file_loc = tkFileDialog.askopenfilename(initialdir = "E:\Deutsch\worter")
export = pd.read_excel(file_loc, header=None)
Deutsch = export.values.T[0].tolist()
English = export.values.T[1].tolist()
"""learn mode"""

"""mistakes list"""
Mistakes_List_English = []
Mistakes_List_Deutsch = []

"""practising"""
for i in range (0,len(English)):
    inputt = input(f"{English[i]} >>> ")
    while Deutsch[i] != inputt:
        """you must enter a reversed word in German"""
        if inputt == "r":
            b = list(Deutsch[i])
            c = str(b.reverse())
            inputtt=input(f"reversed {English[i]} ({Deutsch[i]})>>> ")
            while inputtt != ("".join(b)):
                print(("".join(b)))
                inputtt =input(f"reversed {English[i]} ({Deutsch[i]})>>> ")
        if inputt == "go to":
            for i in range (len(English)): print(f"{i} --- {English[i]}")
            i = int(input("enter number of a word >>> "))
            """to get first part of a word write "part" """
        if inputt == "part":
            index = int(int(len(Deutsch[i]))/2)
            print(Deutsch[i][0:index])
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
            """to get the whole word write "show" """
        if inputt == "show":
            index = int(int(len(Deutsch[i])))
            print(Deutsch[i][0:index])
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
            """to skip a word write "skip" """
        if inputt == "skip":
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
            i = i+1
        if inputt == "help":
            print('to skip a word write "skip"\nto get the whole word write "show"\nto get first part of a word write "part"\nyou must enter a reversed word in German "r"')
        inputt = input(f"{English[i]} >>> ")
    
"""fixing mistakes"""
for i in range (0,len(Mistakes_List_English)):
    inputt = input(f"{Mistakes_List_English[i]} >>> ")
    while Mistakes_List_Deutsch[i] != inputt:
        if inputt == "go to":
            ...
            """to get first part of a word write "part" """
        if inputt == "part":
            index = int(int(len(Mistakes_List_Deutsch[i]))/2)
            print(Mistakes_List_Deutsch[i][0:index])
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
            """to get the whole word write "show" """
        if inputt == "show":
            index = int(int(len(Mistakes_List_Deutsch[i])))
            print(Mistakes_List_Deutsch[i][0:index])
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
            """to skip a word write "skip" """
        if inputt == "skip":
            i = i+1
            Mistakes_List_English.append(English[i])
            Mistakes_List_Deutsch.append(Deutsch[i])
        if inputt == "help":
            print('to skip a word write "skip"\nto get the whole word write "show"\nto get first part of a word write "part"')
        inputt = input(f"{Mistakes_List_English[i]} >>> ")