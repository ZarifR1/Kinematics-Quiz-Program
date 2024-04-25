#importing essential packages
import tkinter as tk
from tkinter import*
import googletrans
import customtkinter

#subprogram for GUI
def main_GUI():
    #defining background
    root=customtkinter.CTk()                                                                               
    root.title("Summing Series")
    root.geometry("800x600") 
    frame=customtkinter.CTkFrame(master=root, bg_color=bg_colour, corner_radius=30)
    frame.pack(pady=20, padx=50, fill="both", expand=True)
    customtkinter.set_appearance_mode(main_theme)

    #defining start menu elements
    title=customtkinter.CTkLabel(root,text=title_text,font=("ariel",30),bg_color=bg_colour, corner_radius=6, width=150)
    title.place(relx=0.5,rely=0.2,anchor=CENTER)

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=150)
    start_button.place(relx=0.5,rely=0.4,anchor=CENTER)

    settings_button=customtkinter.CTkButton(root,text=settings_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=150)
    settings_button.place(relx=0.5,rely=0.5,anchor=CENTER)

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),bg_color=bg_colour, corner_radius=6, width=150)
    exit_main.place(relx=0.5,rely=0.6,anchor=CENTER)

    root.mainloop()

#defining text variables, theme and language
title_text="Kinematics Quiz"
start_text="Start Quiz"
settings_text="Settings"
exit_text="Exit"
main_theme="dark"
current_language="english"

#information to change theme
if main_theme == "light":
    theme_accent = "gray92"                                                                        
    bg_colour = "grey86"
    fg_colour = "grey70"
    text_colour = "black"
if main_theme == "dark":
    theme_accent = "gray14"
    bg_colour = "grey17"
    fg_colour = "grey35"
    text_colour = "white"

main_GUI()