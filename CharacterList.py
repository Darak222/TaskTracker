import customtkinter
import tkinter as tk
import sqlite3 as sl

class CharacterListFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Character List", **kwargs):
        super().__init__(*args, **kwargs)

        self.testButton = customtkinter.CTkButton(self, text = "Character List Func", command = self.testCommand)
        self.testButton.grid(row = 0, column = 0, padx = 100, pady = 20)

    def testCommand(self):
        print("Character List")