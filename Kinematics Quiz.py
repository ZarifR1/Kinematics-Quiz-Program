#importing essential packages
import tkinter as tk
from tkinter import ttk
import googletrans
import customtkinter
from PIL import Image, ImageTk

#subprogram for GUI
def main_GUI():

    #subprogram for rescaling GUI
    def scaler(current):
        #sets scalar multiples for all screen elements
        new_height=current.height
        new_width=current.width
        y_multi=new_height/1080
        x_multi=new_width/1920
        avg_size=(x_multi+y_multi)/2

    
        #resizing GUI background
        bg_image=bg_image_copy.resize((new_width,new_height))
        bg_photoimage=ImageTk.PhotoImage(bg_image)
        bg.configure(image=bg_photoimage)
        bg.image=bg_photoimage
    

        #resizing main_GUI elements
        frame.configure(width=new_width*0.6,height=new_height*0.6)
        title.configure(font=("ariel",46*avg_size), height=30*y_multi,width=150*x_multi)
        start_button.configure(font=("ariel",36*avg_size),height=30*y_multi, width=100*x_multi)
        settings_image=settings_image_copy.resize((int(70*avg_size),int(70*avg_size)))
        settings_button.configure(image=ImageTk.PhotoImage(settings_image),height=30*y_multi,width=50*x_multi)
        exit_main.configure(font=("ariel",36*avg_size),height=30*y_multi, width=100*x_multi)




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
        translate_title.place(relx=0.5,rely=0.1,anchor='center')

        translated_combo=customtkinter.CTkComboBox(root_settings, width=150, values=language_list, bg_color=bg_colour)
        translated_combo.set("english")
        translated_combo.place(relx=0.5,rely=0.2,anchor='center')

        translate_button=customtkinter.CTkButton(root_settings,text=translate_text,font=("ariel",14),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=100)
        translate_button.place(relx=0.5,rely=0.3,anchor='center')

        switch_theme_button=customtkinter.CTkRadioButton(root_settings,text=theme_text,font=("ariel",18),fg_color=fg_colour,bg_color=bg_colour,  corner_radius=6, width=100)
        switch_theme_button.place(relx=0.5,rely=0.5,anchor='center')

        exit_settings=customtkinter.CTkButton(root_settings,text=exit_text,font=("ariel",16),bg_color=bg_colour, corner_radius=6, width=80, command=close_settings)
        exit_settings.place(relx=0.5,rely=0.7,anchor='center')

        root_settings.mainloop()

    #subprogram for exit button
    def close_main():
        root.destroy()
        root.destroy()
        
    #defining GUI
    root=customtkinter.CTk()                                                                               
    root.title(title_text)
    root.geometry("720x480")                         

    #defining background
    global bg_image, bg_photoimage, bg, frame
    bg_image=Image.open("Background image.png")
    bg_image_copy=bg_image.copy()
    bg_photoimage=ImageTk.PhotoImage(bg_image_copy)
    bg=customtkinter.CTkLabel(root,image=bg_photoimage)
    bg.bind("<Configure>",scaler)
    bg.pack(fill='both',expand=True)
    frame=customtkinter.CTkFrame(master=root,fg_color=fg_colour,bg_color=bg_colour,width=720,height=480,corner_radius=30)
    frame.place(relx=0.5,rely=0.5,in_=bg, anchor="center")

    #defining start menu elements
    title=customtkinter.CTkLabel(root,text=title_text,font=("ariel",30),fg_color=fg_colour,height=20,width=150)
    title.place(relx=0.5,rely=0.2,anchor='center')

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24), width=150)
    start_button.place(relx=0.5,rely=0.4,anchor='center')

    #creating image for settings button
    settings_image=Image.open("settings symbol.png")
    settings_image_copy=settings_image.copy()
    settings_image=settings_image_copy.resize((50,50))

    settings_button=customtkinter.CTkButton(root,text="",image=ImageTk.PhotoImage(settings_image),font=("ariel",24),width=50, command=settings)
    settings_button.place(relx=0.15,rely=0.85,anchor='center')

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),bg_color=bg_colour, width=50, command=close_main)
    exit_main.place(relx=0.85,rely=0.85,anchor='center')

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
    fg_colour = "#363636"
    text_colour = "white"

main_GUI()