import customtkinter
import tkinter as tk
import sqlite3 as sl
from ClassList import classDict



class CreateCharacterFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Create Character", **kwargs):
        super().__init__(*args, **kwargs)

        self.connect = sl.connect('testbase.db')

        self.keys = list(classDict.keys())

        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure(0, weight = 1)

        self.grid_rowconfigure(1, weight = 0)

        self.classChosen = customtkinter.StringVar(value = self.keys[0])
        self.subclassChosen = customtkinter.StringVar(value = classDict[self.keys[0]][0])

        self.errorTextbox = customtkinter.CTkTextbox(self, height = 1, width = 400, fg_color = "transparent", border_spacing = 1)
        self.errorTextbox.insert("0.0", "")
        self.errorTextbox.configure(state = "disabled")
        self.errorTextbox.grid(row = 0, column = 0, padx = 20, pady = 1)

        self.characternameTextbox = customtkinter.CTkTextbox(self, height = 1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.characternameTextbox.insert("0.0", "Insert character name")
        self.characternameTextbox.tag_config("center", justify='center')
        self.characternameTextbox.insert(1.0, " ")
        self.characternameTextbox.tag_add("center", "1.0", "end")
        self.characternameTextbox.configure(state = "disabled")
        self.characternameTextbox.grid(row = 1, column = 0, padx = 20, pady = 2)

        self.getCharactername = customtkinter.CTkTextbox(self, height=1, width = 150, border_spacing = 1)
        self.getCharactername.insert("0.0", "Character name")
        self.getCharactername.grid(row = 2, column = 0, padx = 20, pady = 5)

        self.classTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.classTextbox.insert("0.0", "Select main class")
        self.classTextbox.tag_config("center", justify='center')
        self.classTextbox.insert(1.0, " ")
        self.classTextbox.tag_add("center", "1.0", "end")
        self.classTextbox.configure(state = "disabled")
        self.classTextbox.grid(row = 3, column = 0, padx = 20, pady = 5)

        self.classDropdown = customtkinter.CTkComboBox(master = self, values = self.keys, command = self.class_dropdown_callback, variable = self.classChosen)
        self.classDropdown.grid(row = 4, column = 0, padx = 20, pady = 5)
        self.classDropdown.set(self.keys[0])

        self.subclassTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent")
        self.subclassTextbox.insert("0.0", "Select your subclass")
        self.subclassTextbox.tag_config("center", justify='center')
        self.subclassTextbox.insert(1.0, " ")
        self.subclassTextbox.tag_add("center", "1.0", "end")       
        self.subclassTextbox.configure(state = "disabled")
        self.subclassTextbox.grid(row = 5, column = 0, padx = 20, pady = 5)

        self.subclassDropdown = customtkinter.CTkComboBox(master = self, values = classDict[self.classChosen.get()], variable = self.subclassChosen)
        self.subclassDropdown.grid(row = 6, column = 0, padx = 20, pady = 5)
        self.subclassDropdown.set("Select subclass")

        self.itemlevelTextbox = customtkinter.CTkTextbox(self, height=1, width = 200, fg_color = "transparent", border_spacing = 1)
        self.itemlevelTextbox.insert("0.0", "Insert character item level")
        self.itemlevelTextbox.tag_config("center", justify='center')
        self.itemlevelTextbox.insert(1.0, " ")
        self.itemlevelTextbox.tag_add("center", "1.0", "end")  
        self.itemlevelTextbox.configure(state = "disabled")
        self.itemlevelTextbox.grid(row = 7, column = 0, padx = 20, pady = 5)

        self.getItemlevel = customtkinter.CTkTextbox(self, height=1, width = 150, border_spacing = 1)
        self.getItemlevel.insert("0.0", "Insert item level")
        self.getItemlevel.grid(row = 8, column = 0, padx = 20, pady = 5)

        self.submitButton = customtkinter.CTkButton(master = self, text = "Submit Character", command = self.submit_character)
        self.submitButton.grid(row = 9, column = 0, padx = 20, pady = 5)

        self.footer = customtkinter.CTkFrame(self, fg_color = 'transparent', height = 20)
        self.footer.grid(row = 10, column = 0, padx = 20, pady = 2)

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
                    self.errorTextbox.tag_config("center", justify='center')
                    self.errorTextbox.insert(1.0, " ")
                    self.errorTextbox.tag_add("center", "1.0", "end")
                    self.errorTextbox.configure(state = "disabled")
                    return 0
                
        if characterName == "Character name" or characterName == "Character Name":
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", 'The character cannot be named "Character name"')
            self.errorTextbox.tag_config("center", justify='center')
            self.errorTextbox.insert(1.0, " ")
            self.errorTextbox.tag_add("center", "1.0", "end")
            self.errorTextbox.configure(state = "disabled")
            return 0

        if len(characterName) <= 2:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Character name length must be greater than 2")
            self.errorTextbox.tag_config("center", justify='center')
            self.errorTextbox.insert(1.0, " ")
            self.errorTextbox.tag_add("center", "1.0", "end")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        if self.subclassChosen.get() == "Select subclass":
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Please select your subclass!")
            self.errorTextbox.tag_config("center", justify='center')
            self.errorTextbox.insert(1.0, " ")
            self.errorTextbox.tag_add("center", "1.0", "end")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        characterItemLevel = self.getItemlevel.get("0.0", "end")
        try:
            characterItemLevel = int(characterItemLevel)
        except ValueError:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Item level must be a number!")
            self.errorTextbox.tag_config("center", justify='center')
            self.errorTextbox.insert(1.0, " ")
            self.errorTextbox.tag_add("center", "1.0", "end")
            self.errorTextbox.configure(state = "disabled")
            return 0
        if characterItemLevel < 0 or characterItemLevel > 9999:
            self.errorTextbox.configure(state = "normal")
            self.errorTextbox.delete("0.0", "end")
            self.errorTextbox.insert("0.0", "Item level must be between 0 and 9999")
            self.errorTextbox.tag_config("center", justify='center')
            self.errorTextbox.insert(1.0, " ")
            self.errorTextbox.tag_add("center", "1.0", "end")
            self.errorTextbox.configure(state = "disabled")
            return 0
        
        self.errorTextbox.configure(state = "normal")
        self.errorTextbox.delete("0.0", "end")
        self.errorTextbox.insert("0.0", "Character succesfuly created!")
        self.errorTextbox.tag_config("center", justify='center')
        self.errorTextbox.insert(1.0, " ")
        self.errorTextbox.tag_add("center", "1.0", "end")
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



