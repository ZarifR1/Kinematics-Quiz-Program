import tkinter as tk
from tkinter import ttk
import googletrans
import customtkinter
from PIL import Image, ImageTk

def main_GUI():
    def scaler(current):
        #sets scalar multiples for all screen elements
        new_height=current.height
        new_width=current.width
        y_multi=new_height/1080
        x_multi=new_width/1920
        avg_size=(new_height+new_width)/2

    
        try:
            #resizing GUI background
            bg_image=bg_image.resize((new_width,new_height))
            bg_photoimage=ImageTk.PhotoImage(bg_image)
            bg.configure(image=bg_photoimage)
            bg.image=bg_photoimage
        except:
            pass
        
        try:
            #resizing main_GUI elements
            frame.configure(width=new_width*0.9,height=new_height*0.9)
            title.configure(font=("ariel",30*avg_size), width=150*x_multi)
            start_button.configure(font=("ariel",24*avg_size), width=150*x_multi)
            settings_button.configure(font=("ariel",24*avg_size), width=150*x_multi)
            exit_main.configure(font=("ariel",24*avg_size), width=150*x_multi)
            print(new_width*0.9)
        except:
            pass


    # Subprogram for exit button
    def close_main():
        root.destroy()

    # Defining GUI
    root = customtkinter.CTk()
    root.title(title_text)
    root.geometry("720x480")

    # Defining background
    global bg_image
    bg_image = Image.open("Background image.png")
    bg_photoimage = ImageTk.PhotoImage(bg_image)
    bg = customtkinter.CTkLabel(root, image=bg_photoimage)
    bg.bind("<Configure>", scaler)
    bg.pack(fill='none', expand=True)
    frame = customtkinter.CTkFrame(master=root, width=720, height=480, corner_radius=30)
    frame.place(relx=0.5, rely=0.5, in_=bg, anchor="c")

     #defining start menu elements
    title=customtkinter.CTkLabel(root,text=title_text,font=("ariel",30),bg_color=bg_colour, corner_radius=6, width=150)
    title.place(relx=0.5,rely=0.2,anchor='center')

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=150)
    start_button.place(relx=0.5,rely=0.4,anchor='center')

    settings_button=customtkinter.CTkButton(root,text=settings_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=50)
    settings_button.place(relx=0.1,rely=0.9,anchor='center')

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),bg_color=bg_colour, corner_radius=6, width=50, command=close_main)
    exit_main.place(relx=0.9,rely=0.9,anchor='center')
    root.mainloop()
    
#defining text variables, theme and language
title_text="Kinematics Quiz"
start_text="Start Quiz"
settings_text="Settings"
exit_text="Exit"
translator_text="Translator"
translate_text="Translate"
theme_text="Switch theme"
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