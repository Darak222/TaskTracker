import customtkinter
import tkinter as tk
from test import classDict
import sqlite3 as sl



class CreateCharacterFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Create Character", **kwargs):
        super().__init__(*args, **kwargs)
        from test import classDict

        self.connect = sl.connect('testbase.db')

        self.keys = list(classDict.keys())

        self.classChosen = customtkinter.StringVar(value = self.keys[0])
        self.subclassChosen = customtkinter.StringVar(value = classDict[self.keys[0]][0])

        self.errorTextbox = customtkinter.CTkTextbox(self, height = 1, width = 400, fg_color = "transparent", border_spacing = 1)
        self.errorTextbox.insert("0.0", "")
        self.errorTextbox.configure(state = "disabled")
        self.errorTextbox.pack(padx = 20, pady = 2)

        self.characternameTextbox = customtkinter.CTkTextbox(self, height = 1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.characternameTextbox.insert("0.0", "Insert character name")
        self.characternameTextbox.configure(state = "disabled")
        self.characternameTextbox.pack(padx = 20, pady = 2)

        self.getCharactername = customtkinter.CTkTextbox(self, height=1, width = 150, border_spacing = 1)
        self.getCharactername.insert("0.0", "Character name")
        #characterName = getCharactername.get("0.0", "end")
        self.getCharactername.pack(padx = 20, pady = 2)

        self.classTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.classTextbox.insert("0.0", "Select main class")
        self.classTextbox.configure(state = "disabled")
        self.classTextbox.pack(padx = 20, pady = 2)

        self.classDropdown = customtkinter.CTkComboBox(master = self, values = self.keys, command = self.class_dropdown_callback, variable = self.classChosen)
        self.classDropdown.pack(padx = 20, pady = 20)
        self.classDropdown.set(self.keys[0])

        self.subclassTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent")
        self.subclassTextbox.insert("0.0", "Select your subclass")
        self.subclassTextbox.configure(state = "disabled")
        self.subclassTextbox.pack(padx = 20, pady = 2)

        self.subclassDropdown = customtkinter.CTkComboBox(master = self, values = classDict[self.classChosen.get()], variable = self.subclassChosen)
        self.subclassDropdown.pack(padx = 20, pady = 20)
        self.subclassDropdown.set("Select subclass")

        #itemlevelButton = customtkinter.CTkButton(self, text = "Insert Item Level", command = input_itemlevel)
        #itemlevelButton.pack(padx = 20, pady = 20)

        self.itemlevelTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.itemlevelTextbox.insert("0.0", "Insert character item level")
        self.itemlevelTextbox.configure(state = "disabled")
        self.itemlevelTextbox.pack(padx = 20, pady = 2)

        self.getItemlevel = customtkinter.CTkTextbox(self, height=1, width = 150, border_spacing = 1)
        self.getItemlevel.insert("0.0", "Insert item level")
        #characterItemlevel = getItemlevel.get("0.0", "end")
        self.getItemlevel.pack(padx = 20, pady = 2)

        self.submitButton = customtkinter.CTkButton(master = self, text = "Submit Character", command = self.submit_character)
        self.submitButton.pack(padx = 20, pady = 20)

    def class_dropdown_callback(self, choice):
        self.subclassDropdown.configure(values = classDict[choice])
        self.subclassDropdown.set("Select subclass")

    def submit_character(self):
        characterName = self.getCharactername.get("0.0", "end")
        characterName = characterName.strip()

        with self.connect:
            databaseCharacters = self.connect.execute("SELECT Character from CHARACTERS")
            for databaseCharacter in databaseCharacters:
                if characterName in databaseCharacter:
                    self.errorTextbox.configure(state = "normal")
                    self.errorTextbox.delete("0.0", "end")
                    self.errorTextbox.insert("0.0", "Character with selected name already exists")
                    self.errorTextbox.configure(state = "disabled")
                    return 0

        if len(characterName) <= 2:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Character name length must be greater than 2")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        if self.subclassChosen.get() == "Select subclass":
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Please select your subclass!")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        characterItemLevel = self.getItemlevel.get("0.0", "end")
        try:
            characterItemLevel = int(characterItemLevel)
        except ValueError:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Item level must be a number!")
            self.errorTextbox.configure(state = "disabled")
            return 0
        if characterItemLevel < 0 or characterItemLevel > 9999:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Item level must be between 0 and 9999")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        self.errorTextbox.configure(state = "normal")
        self.errorTextbox.delete("0.0", "end")
        self.errorTextbox.insert("0.0", "Character succesfuly created!")
        self.errorTextbox.configure(state = "disabled")

        sql = 'INSERT INTO CHARACTERS (Character, Class, ItemLevel) values(?, ?, ?)'
        data = [(characterName, self.subclassChosen.get(), characterItemLevel)]
        with self.connect:
            self.connect.executemany(sql, data)
            
        self.resetInputs()
        #print("Character created!\nCharacter name: " + characterName + "\nCharacter main class: " + classChosen.get() + "\nCharacter subclass: " + subclassChosen.get() + "\nCharacters item level: " + str(characterItemLevel))

    def resetInputs(self):
        self.getCharactername.delete("0.0", "end")
        self.getCharactername.insert("0.0", "Character name")
        self.classDropdown.set(self.keys[0])
        self.subclassDropdown.set("Select subclass")
        self.getItemlevel.delete("0.0", "end")
        self.getItemlevel.insert("0.0", "Insert item level")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x800")
        self.title("Test")

        self.create_character_frame = CreateCharacterFrame(self, header_name = "Create Character 1")
        self.create_character_frame.grid(row = 1, column = 0, padx = 20, pady = 20)

app = App()
app.mainloop()

