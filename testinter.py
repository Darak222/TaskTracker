import customtkinter
import tkinter as tk
from test import classDict
import sqlite3 as sl

connect = sl.connect('testbase.db')

app = customtkinter.CTk()
app.geometry("800x800")



def class_dropdown_callback(choice):
    subclassDropdown.configure(values = classDict[choice])
    subclassDropdown.set("Select subclass")

def submit_character():
    characterName = getCharactername.get("0.0", "end")
    characterName = characterName.strip()

    with connect:
        databaseCharacters = connect.execute("SELECT Character from CHARACTERS")
        for databaseCharacter in databaseCharacters:
            if characterName in databaseCharacter:
                errorTextbox.configure(state = "normal")
                errorTextbox.delete("0.0", "end")
                errorTextbox.insert("0.0", "Character with selected name already exists")
                errorTextbox.configure(state = "disabled")
                return 0

    if len(characterName) <= 2:
        errorTextbox.configure(state = "normal")
        errorTextbox.delete("0.0", "end")
        errorTextbox.insert("0.0", "Character name length must be greater than 2")
        errorTextbox.configure(state = "disabled")
        return 0
    
    if subclassChosen.get() == "Select subclass":
        errorTextbox.configure(state = "normal")
        errorTextbox.delete("0.0", "end")
        errorTextbox.insert("0.0", "Please select your subclass!")
        errorTextbox.configure(state = "disabled")
        return 0
    
    characterItemLevel = getItemlevel.get("0.0", "end")
    try:
        characterItemLevel = int(characterItemLevel)
    except ValueError:
        errorTextbox.configure(state = "normal")
        errorTextbox.delete("0.0", "end")
        errorTextbox.insert("0.0", "Item level must be a number!")
        errorTextbox.configure(state = "disabled")
        return 0
    if characterItemLevel < 0 or characterItemLevel > 9999:
        errorTextbox.configure(state = "normal")
        errorTextbox.delete("0.0", "end")
        errorTextbox.insert("0.0", "Item level must be between 0 and 9999")
        errorTextbox.configure(state = "disabled")
        return 0
    
    errorTextbox.configure(state = "normal")
    errorTextbox.delete("0.0", "end")
    errorTextbox.insert("0.0", "Character succesfuly created!")
    errorTextbox.configure(state = "disabled")

    sql = 'INSERT INTO CHARACTERS (Character, Class, ItemLevel) values(?, ?, ?)'
    data = [(characterName, subclassChosen.get(), characterItemLevel)]
    with connect:
        connect.executemany(sql, data)
        
    resetInputs()
    #print("Character created!\nCharacter name: " + characterName + "\nCharacter main class: " + classChosen.get() + "\nCharacter subclass: " + subclassChosen.get() + "\nCharacters item level: " + str(characterItemLevel))

def resetInputs():
    getCharactername.delete("0.0", "end")
    getCharactername.insert("0.0", "Character name")
    classDropdown.set(keys[0])
    subclassDropdown.set("Select subclass")
    getItemlevel.delete("0.0", "end")
    getItemlevel.insert("0.0", "Insert item level")

keys = list(classDict.keys())

classChosen = customtkinter.StringVar(value = keys[0])
subclassChosen = customtkinter.StringVar(value = classDict[keys[0]][0])

errorTextbox = customtkinter.CTkTextbox(app, height = 1, width = 400, fg_color = "transparent", border_spacing = 1)
errorTextbox.insert("0.0", "")
errorTextbox.configure(state = "disabled")
errorTextbox.pack(padx = 20, pady = 2)

characternameTextbox = customtkinter.CTkTextbox(app, height = 1, width = 200, fg_color = "transparent", border_spacing = 1)
characternameTextbox.insert("0.0", "Insert character name")
characternameTextbox.configure(state = "disabled")
characternameTextbox.pack(padx = 20, pady = 2)

getCharactername = customtkinter.CTkTextbox(app, height=1, width = 150, border_spacing = 1)
getCharactername.insert("0.0", "Character name")
#characterName = getCharactername.get("0.0", "end")
getCharactername.pack(padx = 20, pady = 2)

classTextbox = customtkinter.CTkTextbox(app, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
classTextbox.insert("0.0", "Select main class")
classTextbox.configure(state = "disabled")
classTextbox.pack(padx = 20, pady = 2)

classDropdown = customtkinter.CTkComboBox(master = app, values = keys, command = class_dropdown_callback, variable = classChosen)
classDropdown.pack(padx = 20, pady = 20)
classDropdown.set(keys[0])

subclassTextbox = customtkinter.CTkTextbox(app, height=1, width = 200, fg_color = "transparent")
subclassTextbox.insert("0.0", "Select your subclass")
subclassTextbox.configure(state = "disabled")
subclassTextbox.pack(padx = 20, pady = 2)

subclassDropdown = customtkinter.CTkComboBox(master = app, values = classDict[classChosen.get()], variable = subclassChosen)
subclassDropdown.pack(padx = 20, pady = 20)
subclassDropdown.set("Select subclass")

#itemlevelButton = customtkinter.CTkButton(app, text = "Insert Item Level", command = input_itemlevel)
#itemlevelButton.pack(padx = 20, pady = 20)

itemlevelTextbox = customtkinter.CTkTextbox(app, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
itemlevelTextbox.insert("0.0", "Insert character item level")
itemlevelTextbox.configure(state = "disabled")
itemlevelTextbox.pack(padx = 20, pady = 2)

getItemlevel = customtkinter.CTkTextbox(app, height=1, width = 150, border_spacing = 1)
getItemlevel.insert("0.0", "Insert item level")
#characterItemlevel = getItemlevel.get("0.0", "end")
getItemlevel.pack(padx = 20, pady = 2)

submitButton = customtkinter.CTkButton(master = app, text = "Submit Character", command = submit_character)
submitButton.pack(padx = 20, pady = 20)

app.mainloop()