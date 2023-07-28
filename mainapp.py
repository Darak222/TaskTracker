import customtkinter
import tkinter as tk
import sqlite3 as sl
from CreateCharacter import CreateCharacterFrame
from CreateDB import createDB
from TaskList import TaskListFrame
from CharacterList import CharacterListFrame
from AddNewTask import AddNewTaskFrame
from RaidList import RaidListFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        createDB()

        self.geometry("1000x1000")
        self.title("Task Tracker")

        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure(0, weight = 1)

        self.grid_rowconfigure(1, weight = 0)

        self.create_menu_frame = customtkinter.CTkFrame(self)
        self.create_menu_frame.grid(row = 0, column = 0)

        self.taskListButton = customtkinter.CTkButton(master = self.create_menu_frame, text = "Task List", command = self.TaskListSelected)
        self.taskListButton.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.createCharacterButton = customtkinter.CTkButton(master = self.create_menu_frame, text = "Create Character", command = self.CreateCharacterSelected)
        self.createCharacterButton.grid(row = 0, column = 1, padx = 20, pady = 20)

        self.CharacterListButton = customtkinter.CTkButton(master = self.create_menu_frame, text = "Character List", command = self.CharacterListSelected)
        self.CharacterListButton.grid(row = 0, column = 2, padx = 20, pady = 20)

        self.AddNewTaskButton = customtkinter.CTkButton(master = self.create_menu_frame, text = "Add New Task", command = self.AddNewTaskSelected)
        self.AddNewTaskButton.grid(row = 0, column = 3, padx = 20, pady = 20)

        self.RaidListButton = customtkinter.CTkButton(master = self.create_menu_frame, text = "Raid List", command = self.RaidListSelected)
        self.RaidListButton.grid(row = 0, column = 4, padx = 20, pady = 20)

        self.select_mainframe = TaskListFrame(self, header_name = "Task List 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        

    def TaskListSelected(self):
        self.select_mainframe.destroy()
        self.select_mainframe = TaskListFrame(self, header_name = "Task List 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        print("Task List")

    def CreateCharacterSelected(self):
        self.select_mainframe.destroy()
        self.select_mainframe = CreateCharacterFrame(self, header_name = "Create Character 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        print("Create Character")

    def CharacterListSelected(self):
        self.select_mainframe.destroy()
        self.select_mainframe = CharacterListFrame(self, header_name = "Character List 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        print("Character List")

    def AddNewTaskSelected(self):
        self.select_mainframe.destroy()
        self.select_mainframe = AddNewTaskFrame(self, header_name = "Add New Task 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        print("Add New Task")

    def RaidListSelected(self):
        self.select_mainframe.destroy()
        self.select_mainframe = RaidListFrame(self, header_name = "Raid List 1")
        self.select_mainframe.grid(row = 1, column = 0, padx = 20, pady = 20)
        print("Raid List")

app = App()
app.mainloop()