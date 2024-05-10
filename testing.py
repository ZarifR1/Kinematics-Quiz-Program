#importing essential packages
import tkinter as tk
from tkinter import ttk
import googletrans
import customtkinter
from PIL import Image, ImageTk

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

def scaler_settings():
    pass

#subprogram for closing settings
def close_settings():
    root_settings.destroy()

#defining background for settings
root_settings=customtkinter.CTk()
root_settings.title(settings_text)
root_settings.geometry("300x400") 
bg_image2=Image.open("Images\Background image.png")
bg_image_copy2=bg_image2.copy()
bg_photoimage2=ImageTk.PhotoImage(bg_image_copy2)
bg_settings=customtkinter.CTkLabel(root_settings,image=bg_photoimage2)
bg_settings.bind("<Configure>",scaler_settings)
bg_settings.pack(fill='both',expand=True)
frame_settings=customtkinter.CTkFrame(master=root_settings,fg_color=fg_colour,bg_color=bg_colour,width=300,height=400,corner_radius=30)
frame_settings.place(relx=0.5,rely=0.5,in_=bg_settings, anchor="center")

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