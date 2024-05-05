#importing essential packages
import tkinter as tk
from tkinter import*
import googletrans
import customtkinter
from PIL import Image, ImageTk

#subprogram for GUI
def main_GUI():

    #subprogram for rescaling GUI
    def scaler(current):
        new_height=current.height
        new_width=current.width
        y_multi=new_height/1080
        x_multi=new_width/1920
        avg_size=(new_height+new_width)/2

        try:
            bg_image=bg_image.resize((new_width,new_height))
            bg_photoimage=ImageTk.PhotoImage(bg_image)
            bg.config(image=bg_photoimage)
            bg.image=bg_photoimage
        except:
            pass
    

   #subprogram for settings menu
    def settings():
        global root_settings
        
        #subprogram for closing settings
        def close_settings():
            root_settings.destroy()
        
        #defining background for settings
        root_settings=customtkinter.CTk()
        root_settings.title(settings_text)
        root_settings.geometry("300x400") 
        frame_settings=customtkinter.CTkFrame(master=root_settings, bg_color=bg_colour, corner_radius=30)
        frame_settings.pack(pady=10, padx=20, fill="both", expand=True)

        #importing languages for translator
        languages=googletrans.LANGUAGES
        language_list=list(languages.values())

        #defining settings menu elements
        translate_title=customtkinter.CTkLabel(root_settings,text=translator_text,font=("ariel",18),bg_color=bg_colour, corner_radius=6, width=150)
        translate_title.place(relx=0.5,rely=0.1,anchor=CENTER)

        translated_combo=customtkinter.CTkComboBox(root_settings, width=150, values=language_list, bg_color=bg_colour)
        translated_combo.set("english")
        translated_combo.place(relx=0.5,rely=0.2,anchor=CENTER)

        translate_button=customtkinter.CTkButton(root_settings,text=translate_text,font=("ariel",14),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=100)
        translate_button.place(relx=0.5,rely=0.3,anchor=CENTER)

        switch_theme_button=customtkinter.CTkRadioButton(root_settings,text=theme_text,font=("ariel",18),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=100)
        switch_theme_button.place(relx=0.5,rely=0.5,anchor=CENTER)

        exit_settings=customtkinter.CTkButton(root_settings,text=exit_text,font=("ariel",16),bg_color=bg_colour, corner_radius=6, width=80, command=close_settings)
        exit_settings.place(relx=0.5,rely=0.7,anchor=CENTER)

        root_settings.mainloop()

    #subprogram for exit button
    def close_main():
        root.destroy()
        root.destroy()
        
    #defining GUI
    root=customtkinter.CTk()                                                                               
    root.title(title_text)
    root.geometry("720x400") 

    #defining background
    bg_image=Image.open("Background image.png")
    bg_photoimage=ImageTk.PhotoImage(bg_image)
    bg=Label(root,image=bg_photoimage)
    bg.bind("<Configure>",scaler)
    bg.pack(fill=BOTH,expand=YES)

    #defining start menu elements
    title=customtkinter.CTkLabel(root,text=title_text,font=("ariel",30),bg_color=bg_colour, corner_radius=6, width=150)
    title.place(relx=0.5,rely=0.2,anchor=CENTER)

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=150)
    start_button.place(relx=0.5,rely=0.4,anchor=CENTER)

    settings_button=customtkinter.CTkButton(root,text=settings_text,font=("ariel",24),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=150, command=settings)
    settings_button.place(relx=0.5,rely=0.5,anchor=CENTER)

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),bg_color=bg_colour, corner_radius=6, width=150, command=close_main)
    exit_main.place(relx=0.5,rely=0.6,anchor=CENTER)

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