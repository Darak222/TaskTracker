import customtkinter
import tkinter as tk
import sqlite3 as sl

class AddNewTaskFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Add New Task", **kwargs):
        super().__init__(*args, **kwargs)

        self.testButton = customtkinter.CTkButton(self, text = "Add New Task func", command = self.testCommand)
        self.testButton.grid(row = 0, column = 0, padx = 100, pady = 20)

    def testCommand(self):
        print("Add New Task")