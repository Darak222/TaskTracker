import customtkinter
import tkinter as tk
import sqlite3 as sl

class TaskListFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Task List", **kwargs):
        super().__init__(*args, **kwargs)
        self.connect = sl.connect('testbase.db')

        self.errorTextbox = customtkinter.CTkTextbox(self, height = 1, width = 400, fg_color = "transparent", border_spacing = 1)
        self.errorTextbox.insert("0.0", "")
        self.errorTextbox.configure(state = "disabled")
        self.errorTextbox.grid(row = 0, column = 0, padx = 20, pady = 1)

        self.testButton = customtkinter.CTkButton(self, text = "Task List Func", command = self.testCommand)
        self.testButton.grid(row = 0, column = 0, padx = 100, pady = 20)


    def testCommand(self):
        print("Test")




        
