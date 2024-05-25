#importing essential packages
import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
import googletrans
import customtkinter
from PIL import Image, ImageTk

#subprogram for GUI
def main_GUI():

    #subprogram for rescaling GUI
    def scaler(current):
        #sets scalar multiples for all screen elements
        global avg_size, new_height, new_width, x_multi, y_multi,avg_size
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
        

        
    
    #subprogram for starting quiz
    def start(position):

        def scaler_quiz(current):
            #sets scalar multiples for all screen elements
            new_height=current.height
            new_width=current.width
            y_multi=new_height/1080
            x_multi=new_width/1920
            avg_size=(x_multi+y_multi)/2

        
            #resizing GUI background
            bg_image3=bg_image_copy.resize((new_width,new_height))
            bg_photoimage3=ImageTk.PhotoImage(bg_image3)
            bg.configure(image=bg_photoimage3)
            bg.image=bg_photoimage3

            #resizing main_GUI elements
            frame.configure(width=new_width*0.6,height=new_height*0.6)
            try:
                question.configure(font=("ariel",36*avg_size), height=150*y_multi,width=new_width*0.3)
                next_button.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                settings_image=settings_image_copy.resize((int(70*avg_size),int(70*avg_size)))
                settings_button.configure(image=ImageTk.PhotoImage(settings_image),height=30*y_multi,width=50*x_multi)
                exit_main.configure(font=("ariel",36*avg_size),height=30*y_multi, width=100*x_multi)
                if position < 5:
                    option_A.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                    option_B.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                    option_C.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                    option_D.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                if position > 4 and entry_exists==True:
                    input_entry.configure(font=("ariel",36*avg_size), height=80*y_multi,width=200*x_multi)
                if position == 8:
                    score_title.configure(font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
                    final_score.configure(font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
                    restart_button.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                
            except Exception as e:
                pass

        #clearing GUI elements for quiz
        if position == 0:
            title.destroy()               
            start_button.destroy()
            bg.bind("<Configure>",scaler_quiz)

        def restart():
            score_title.destroy()
            final_score.destroy()
            restart_button.destroy()

            start(0)
            
        #subprogram for calculating final score
        def answer_check():
             mcq_solutions=["A","C","D","A"]
             entry_solutions=[20,330,2.5,0.42]
             score=0
             for i in range(0,len(mcq_solutions)):
                  if user_mcq_answers[i]==mcq_solutions[i]:
                       score+=1
                  if user_entry_answers[i]==entry_solutions[i]:
                       score+=1

             global score_title,final_score,restart_button
             score_title=customtkinter.CTkLabel(root,text=score_text,bg_color=bg_colour,fg_color=fg_colour, font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
             score_title.place(relx=0.5,rely=0.2,anchor='center')
            
             final_score=customtkinter.CTkLabel(root,text=(score,"/8"),bg_color=bg_colour,fg_color=fg_colour, font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
             final_score.place(relx=0.5,rely=0.5,anchor='center')

             restart_button=customtkinter.CTkButton(root,text=restart_text,bg_color=bg_colour,command=restart, font=("ariel",36*avg_size), height=60*y_multi,width=200*x_multi)
             restart_button.place(relx=0.5,rely=0.85,anchor='center')




        #subprogram to detect user input into the entry
        def entry_detection(event):
            if (input_entry.get()).isalpha()==False:
                next_button.configure(state="normal")
            else:
                next_button.configure(state="disabled")
                             


        #subprogram for selecting user's mcq answers
        def answer_select(answer):
            if position < len(A):
                if answer=="A":
                        option_A.configure(state="disabled")
                        option_B.configure(state="normal")
                        option_C.configure(state="normal")
                        option_D.configure(state="normal")
                if answer=="B":
                        option_A.configure(state="normal")
                        option_B.configure(state="disabled")
                        option_C.configure(state="normal")
                        option_D.configure(state="normal")
                if answer=="C":
                        option_A.configure(state="normal")
                        option_B.configure(state="normal")
                        option_C.configure(state="disabled")
                        option_D.configure(state="normal")
                if answer=="D":
                        option_A.configure(state="normal")
                        option_B.configure(state="normal")
                        option_C.configure(state="normal")
                        option_D.configure(state="disabled")
                next_button.configure(state="normal")
                          
        
               
        
        if position != 0 and position < 5:
            global question,next_button,option_A,option_B,option_C,option_D
            question.destroy()
            if option_A._state == 'disabled':
                 user_mcq_answers.append("A")
            if option_B._state == 'disabled':
                 user_mcq_answers.append("B")
            if option_C._state == 'disabled':
                 user_mcq_answers.append("C")
            if option_D._state == 'disabled':
                 user_mcq_answers.append("D")
            option_A.destroy()
            option_B.destroy()
            option_C.destroy()
            option_D.destroy()
            next_button.destroy()
        if position > 4:
            global input_entry,entry_exists
            question.destroy()
            user_entry_answers.append(float(input_entry.get()))
            input_entry.destroy()
            next_button.destroy()
            entry_exists=False

        # Setting up quiz questions to be displayed
        questions = ["Which of the following is the equation for average velocity (v is average velocity).", "If an object is acceleration uniformly, how would its displacement time graph appear?","If a ball is thrown vertically up, what is its instantaneous velocity when it reaches its max height?","What does the gradient of a velocity time graph represent?","A car stopped from 200 m/s over a distance of 1 km. What is the magnitude of acceleration that the car experienced over this time?","An object moves at a constant velocity of 108 km/h. What is its displacement over 11s?"," A train accelerates from 10 m/s to 60 m/s in 20 s. What is the acceleration of the train?","A ball is dropped from a height of 5 m/s at a speed of 10 m/s. How long does it take to hit the ground to 2 decimal places?"]
        A=["v=s/t","Straight line with positive gradient","Not enough information","acceleration"]
        B=["v=u+at","Straight line with negative gradient","Less than initial velocity but not zero","displacement"]
        C=["v=u+a/t","Curve with positive gradient","More than initial velocity","distance"]
        D=["v=st","Curve with negative gradient","Zero","Force"]
        

        if position < len(questions):
            
            #shows questions on main GUI
            question=customtkinter.CTkLabel(root,text=questions[position],fg_color=fg_colour,wraplength=root.winfo_width()*0.5,font=("ariel",36*avg_size), height=150*y_multi,width=new_width*0.3)
            question.place(relx=0.5,rely=0.2,anchor='center')

            #next button for moving to next question
            next_button=customtkinter.CTkButton(root,text=next_text,bg_color=bg_colour,state="disabled",command=lambda:start(position+1),font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
            next_button.place(relx=0.5,rely=0.85,anchor='center')


            if position < len(A):

                option_A_text="A) "+A[position]
                option_A=customtkinter.CTkButton(root,text="",state="normal",command=lambda:answer_select("A"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_A.configure(text=option_A_text)
                option_A.place(relx=0.35,rely=0.4,anchor='center')

                option_B_text="B) "+B[position]
                option_B=customtkinter.CTkButton(root,text="",state="normal",command=lambda:answer_select("B"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_B.configure(text=option_B_text)
                option_B.place(relx=0.35,rely=0.5,anchor='center')

                option_C_text="C) "+C[position]
                option_C=customtkinter.CTkButton(root,text="",state="normal",command=lambda:answer_select("C"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_C.configure(text=option_C_text)
                option_C.place(relx=0.35,rely=0.6,anchor='center')

                option_D_text="D) "+D[position]
                option_D=customtkinter.CTkButton(root,text="",state="normal",command=lambda:answer_select("D"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_D.configure(text=option_D_text)
                option_D.place(relx=0.35,rely=0.7,anchor='center')

            else:
                input_entry=customtkinter.CTkEntry(master=root,font=('ariel',36*avg_size), height=60*y_multi,width=200*x_multi)
                input_entry.bind("<KeyRelease>",entry_detection)
                input_entry.place(relx=0.5,rely=0.6,anchor='center')
                entry_exists=True
            
        else:
             answer_check()
    
        
                
            
            
   #subprogram for settings menu
    def settings():
        
        #rescales settings menu
        def scaler_settings(current):
            #sets scalar multiples for all screen elements
            new_height=current.height
            new_width=current.width
            y_multi=new_height/1080
            x_multi=new_width/1920
            avg_size=(x_multi+y_multi)/2
        
            #resizing GUI background
            bg_image2=bg_image_copy2.resize((new_width,new_height))
            bg_photoimage2=ImageTk.PhotoImage(bg_image2)
            bg_settings.configure(image=bg_photoimage2)
            bg_settings.image=bg_photoimage2

            #resizing settings elements
            frame_settings.configure(width=new_width*0.6,height=new_height*0.6)
            translate_title.configure(font=("ariel",48*avg_size),width=100*x_multi,height=60*y_multi)
            translated_combo.configure(width=700*x_multi,height=60*y_multi)
            translate_button.configure(font=("ariel",48*avg_size),width=100*x_multi,height=90*y_multi)
            switch_theme_button.configure(font=("ariel",48*avg_size),width=100*x_multi,height=60*y_multi)
            exit_settings.configure(font=("ariel",48*avg_size),height=90*y_multi,width=280*x_multi)
        
        #subprogram for closing settings
        def close_settings():
            settings_button.configure(state="normal")
            root_settings.destroy()
        
        #defining background for settings
        global root_settings
        settings_button.configure(state="disabled")
        root_settings=Toplevel(bg=bg_colour)
        root_settings.title(settings_text)
        root_settings.geometry("300x400") 
        bg_image2=Image.open("Images\Settings background.png")
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
        translate_title=customtkinter.CTkLabel(root_settings,text=translator_text,font=("ariel",18),fg_color=fg_colour, height=20,width=100)
        translate_title.place(relx=0.5,rely=0.1,anchor='center')

        translated_combo=customtkinter.CTkComboBox(root_settings, width=150, values=language_list, bg_color=bg_colour, height=20)
        translated_combo.set("english")
        translated_combo.place(relx=0.5,rely=0.2,anchor='center')

        translate_button=customtkinter.CTkButton(root_settings,text=translate_text,font=("ariel",14),bg_color=bg_colour,corner_radius=6, width=100, height=30)
        translate_button.place(relx=0.5,rely=0.35,anchor='center')

        switch_theme_button=customtkinter.CTkRadioButton(root_settings,text=theme_text,font=("ariel",18),fg_color=fg_colour, corner_radius=6, width=100, height=20)
        switch_theme_button.place(relx=0.5,rely=0.5,anchor='center')

        exit_settings=customtkinter.CTkButton(root_settings,text=exit_text,font=("ariel",16),bg_color=bg_colour, corner_radius=6, width=80, height=30, command=close_settings)
        exit_settings.place(relx=0.5,rely=0.7,anchor='center')

        root_settings.mainloop()

    #subprogram for exit button
    def close_main():
        root.destroy()
        
    #defining GUI
    root=customtkinter.CTk()                                                                               
    root.title(title_text)
    root.geometry("720x480")                         

    #defining background
    global bg_image, bg_photoimage, bg, frame
    bg_image=Image.open("Images\Background image.png")
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

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24), width=150, command=lambda:start(0))
    start_button.place(relx=0.5,rely=0.4,anchor='center')

    #creating image for settings button
    settings_image=Image.open("Images\settings symbol.png")
    settings_image_copy=settings_image.copy()
    settings_image=settings_image_copy.resize((50,50))

    settings_button=customtkinter.CTkButton(root,text="",state="normal",image=ImageTk.PhotoImage(settings_image),font=("ariel",24),width=50, command=settings)
    settings_button.place(relx=0.15,rely=0.85,anchor='center')

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),bg_color=bg_colour, width=50, command=close_main)
    exit_main.place(relx=0.85,rely=0.85,anchor='center')

    root.mainloop()

#defining text variables, theme and language and score
title_text="Kinematics Quiz"
start_text="Start Quiz"
settings_text="Settings"
exit_text="Exit"
translator_text="Translator"
translate_text="Translate"
theme_text="Switch theme"
next_text="Next"
restart_text="Restart Quiz"
main_theme="dark"
score_text="Score"
current_language="english"
user_mcq_answers=[]
user_entry_answers=[]

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