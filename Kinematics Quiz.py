#importing essential packages
import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
import googletrans
import customtkinter
from PIL import Image, ImageTk
import textblob

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
        if main_theme=="dark":
            bg_image=Image.open("Images\Dark Background image.png")
        else:
            bg_image=Image.open("Images\Light Background image.png")
        bg_photoimage=ImageTk.PhotoImage(bg_image)
        bg.configure(image=bg_photoimage)
        bg.image=bg_photoimage
    

        #resizing main_GUI elements
        frame.configure(width=new_width*0.6,height=new_height*0.6)
        settings_image=settings_image_copy.resize((int(70*avg_size),int(70*avg_size)))
        settings_button.configure(image=ImageTk.PhotoImage(settings_image),height=30*y_multi,width=50*x_multi)
        #selection statement for immediate changes in scaling of existing widgets
        try:
            exit_main.configure(font=("ariel",36*avg_size),height=30*y_multi, width=100*x_multi)
            if title.winfo_exists():
                title.configure(font=("ariel",46*avg_size), height=30*y_multi,width=150*x_multi)
                start_button.configure(font=("ariel",36*avg_size),height=30*y_multi, width=100*x_multi)
            if question.winfo_exists():
                question.configure(font=("ariel",36*avg_size), height=150*y_multi,width=new_width*0.3)
                next_button.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
            if option_A.winfo_exists():
                option_A.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_B.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_C.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_D.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
            if input_entry.winfo_exists():
                input_entry.configure(font=("ariel",36*avg_size), height=80*y_multi,width=200*x_multi)
            if score_title.winfo_exists():
                score_title.configure(font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
                final_score.configure(font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
                restart_button.configure(font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
        except:
            pass

    #subprogram for translating GUI
    def translate():
        global current_language
        try:                                                                                
            #determining the language keys for translation
            global from_language_key, to_language_key
            for key, value in languages.items():                                            
                if (value == current_language):
                    from_language_key=key
            for key,value in languages.items():                                             
                if (value ==translated_combo.get()):
                    to_language_key=key

            #subprogram for translating each text variable to new language
            def translator(text):
                try:
                    translated_text=str(textblob.TextBlob(text).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_text=text
                return translated_text
            
            #iteration which produces new list of questions in translated language
            global translated_questions,translated_A, translated_B, translated_C, translated_D
            translated_questions=[]
            for i in range(0,8):
                try:
                    translated_question=str(textblob.TextBlob(questions[i]).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_question=questions[i]
                translated_questions.append(translated_question)
            
            #iteration which produces new lists of MCQ options in translated language
            translated_A=[]
            translated_B=[]
            translated_C=[]
            translated_D=[]
            for i in range(0,4):
                try:
                    translated_A_text=str(textblob.TextBlob(A[i]).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_A_text=A[i]
                translated_A.append(translated_A_text)

                try:
                    translated_B_text=str(textblob.TextBlob(B[i]).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_B_text=B[i]
                translated_B.append(translated_B_text)

                try:
                    translated_C_text=str(textblob.TextBlob(C[i]).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_C_text=C[i]
                translated_C.append(translated_C_text)

                try:
                    translated_D_text=str(textblob.TextBlob(D[i]).translate(from_lang=from_language_key,to=to_language_key))
                except:
                    translated_D_text=D[i]
                translated_D.append(translated_D_text)

            #immediately translates any existing widget into translated language
            exit_main.configure(text=translator(exit_text))
            current_language=translated_combo.get()
            
            try:
                if start_button.winfo_exists():
                    title.configure(text=translator(title_text))
                    start_button.configure(text=translator(start_text))
            except:
                pass
            try:
                if question.winfo_exists():
                    question.configure(text=translated_questions[current_q])
                    next_button.configure(text=translator(next_text))
            except:
                pass
            try:
                if option_A.winfo_exists():
                    option_A_text="A) "+translated_A[current_q]
                    option_A.configure(text=option_A_text)
                    option_B_text="B) "+translated_B[current_q]
                    option_B.configure(text=option_B_text)
                    option_C_text="C) "+translated_C[current_q]
                    option_C.configure(text=option_C_text)
                    option_D_text="D) "+translated_D[current_q]
                    option_D.configure(text=option_D_text)
            except:
                pass
            try:
                if score_title.winfo_exists():
                    score_title.configure(text=translator(score_text))
                    restart_button.configure(text=translator(restart_text))
                    root_settings.destroy()
                    settings()
            except:
                pass
            root_settings.destroy()
            settings()

        except:
            pass

    #subprogram for switching theme of GUI
    def switch_theme():
         global main_theme,current_theme, theme_accent, bg_colour, fg_colour, text_colour
         current_theme=main_theme
         #fetches current theme of GUI and alters it
         if current_theme=="dark":
              bg_image=Image.open("Images\Light Background image.png")
              bg_image_copy=bg_image.copy()
              bg_photoimage=ImageTk.PhotoImage(bg_image_copy)
              bg.configure(image=bg_photoimage)
              bg.bind("<Configure>",scaler)
              customtkinter.set_appearance_mode("light")                                                                       
              bg_colour = "grey86"
              fg_colour = "grey70"
              text_colour = "black"
              main_theme="light"
         if current_theme=="light":
              bg_image=Image.open("Images\Dark Background image.png")
              bg_image_copy=bg_image.copy()
              bg_photoimage=ImageTk.PhotoImage(bg_image_copy)
              bg.configure(image=bg_photoimage)
              bg.bind("<Configure>",scaler)
              customtkinter.set_appearance_mode("dark")   
              bg_colour = "grey17"
              fg_colour = "#363636"
              text_colour = "white"
              main_theme="dark"
        
        #immediately switches existing widgets into new theme
         frame.configure(fg_color=fg_colour,bg_color=bg_colour)
         frame.place(relx=0.5,rely=0.5,in_=bg, anchor="center")
         exit_main.configure(bg_color=bg_colour,text_color=text_colour)
         settings_button.configure(bg_color=bg_colour,text_color=text_colour)
         try:
            if title.winfo_exists():
                title.configure(fg_color=fg_colour,text_color=text_colour)
                start_button.configure(bg_color=bg_colour,text_color=text_colour)
         except:
            pass
         try:
            if question.winfo_exists():
                question.configure(fg_color=fg_colour,text_color=text_colour)
                next_button.configure(bg_color=bg_colour,text_color=text_colour)
         except:
            pass
         try:
            if option_A.winfo_exists():
                option_A.configure(bg_color=bg_colour,text_color=text_colour)
                option_B.configure(bg_color=bg_colour,text_color=text_colour)
                option_C.configure(bg_color=bg_colour,text_color=text_colour)
                option_D.configure(bg_color=bg_colour,text_color=text_colour)
         except:
            pass
         try:
            if input_entry.winfo_exists():
                input_entry.configure(fg_color=fg_colour,bg_color=bg_colour,text_color=text_colour)
         except:
            pass
         try:
            if score_title.winfo_exists():
                score_title.configure(fg_color=fg_colour,bg_color=bg_colour,text_color=text_colour)
                final_score.configure(fg_color=fg_colour,bg_color=bg_colour,text_color=text_colour)
                restart_button.configure(bg_color=bg_colour,text_color=text_colour)
         except:
            pass
         root_settings.destroy()
         settings()
         
    #subprogram for starting quiz
    def start(position):
        global current_q
        current_q=position
        #clearing GUI elements for quiz
        if position == 0:
            title.destroy()               
            start_button.destroy()

        #restarts quiz
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
             #iteration which compares user answers with the true answers, incrementing the score when they match
             for i in range(0,len(mcq_solutions)):
                  if user_mcq_answers[i]==mcq_solutions[i]:
                       score+=1
                  if user_entry_answers[i]==entry_solutions[i]:
                       score+=1

             global score_title,final_score,restart_button
             
             #defining widgets for final screen
             try:
                score_title_text=str(textblob.TextBlob(score_text).translate(from_lang=from_language_key,to=to_language_key))
             except:
                score_title_text=score_text
             score_title=customtkinter.CTkLabel(root,text_color=text_colour,text=score_title_text,bg_color=bg_colour,fg_color=fg_colour, font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
             score_title.place(relx=0.5,rely=0.2,anchor='center')
            
             final_score=customtkinter.CTkLabel(root,text_color=text_colour,text=(score,"/8"),bg_color=bg_colour,fg_color=fg_colour, font=("ariel",50*avg_size), height=50*y_multi,width=180*x_multi)
             final_score.place(relx=0.5,rely=0.5,anchor='center')

             try:
                restart_button_text=str(textblob.TextBlob(restart_text).translate(from_lang=from_language_key,to=to_language_key))
             except:
                restart_button_text=restart_text
             restart_button=customtkinter.CTkButton(root,text_color=text_colour,text=restart_button_text,bg_color=bg_colour,command=restart, font=("ariel",36*avg_size), height=60*y_multi,width=200*x_multi)
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
                          
        
               
        #selection statement for clearing the existing question, options, entry and leaving it clear for the next ones to be placed
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
            global input_entry
            question.destroy()
            user_entry_answers.append(float(input_entry.get()))
            input_entry.destroy()
            next_button.destroy()
        
        #condition for running through quiz
        if position < len(questions):
            
            #shows questions on main GUI
            if current_language=="english":
                question_text=questions[position]
            else:
                question_text=translated_questions[position]
            question=customtkinter.CTkLabel(root,text_color=text_colour,text=question_text,fg_color=fg_colour,wraplength=root.winfo_width()*0.5,font=("ariel",36*avg_size), height=150*y_multi,width=new_width*0.3)
            question.place(relx=0.5,rely=0.2,anchor='center')

            #next button for moving to next question
            try:
                next_button_text=str(textblob.TextBlob(next_text).translate(from_lang=from_language_key,to=to_language_key))
            except:
                next_button_text=next_text
            next_button=customtkinter.CTkButton(root,text_color=text_colour,text=next_button_text,bg_color=bg_colour,state="disabled",command=lambda:start(position+1),font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
            next_button.place(relx=0.5,rely=0.85,anchor='center')

            #condition for showing MCQ options
            if position < len(A):
                
                #placing options A, B, C, D on root
                if current_language=="english":
                    option_A_text="A) "+A[position]
                else:
                    option_A_text="A) "+translated_A[position]
                option_A=customtkinter.CTkButton(root,text="",bg_color=bg_colour,text_color=text_colour,state="normal",command=lambda:answer_select("A"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_A.configure(text=option_A_text)
                option_A.place(relx=0.35,rely=0.4,anchor='center')

                if current_language=="english":
                    option_B_text="B) "+B[position]
                else:
                    option_B_text="B) "+translated_B[position]
                option_B=customtkinter.CTkButton(root,text="",bg_color=bg_colour,text_color=text_colour,state="normal",command=lambda:answer_select("B"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_B.configure(text=option_B_text)
                option_B.place(relx=0.35,rely=0.5,anchor='center')

                if current_language=="english":
                    option_C_text="C) "+C[position]
                else:
                    option_C_text="C) "+translated_C[position]
                option_C=customtkinter.CTkButton(root,text="",bg_color=bg_colour,text_color=text_colour,state="normal",command=lambda:answer_select("C"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_C.configure(text=option_C_text)
                option_C.place(relx=0.35,rely=0.6,anchor='center')

                if current_language=="english":
                    option_D_text="D) "+D[position]
                else:
                    option_D_text="D) "+translated_D[position]
                option_D=customtkinter.CTkButton(root,text="",bg_color=bg_colour,text_color=text_colour,state="normal",command=lambda:answer_select("D"), font=("ariel",36*avg_size), height=50*y_multi,width=180*x_multi)
                option_D.configure(text=option_D_text)
                option_D.place(relx=0.35,rely=0.7,anchor='center')

            else:
                #placing input entry on root
                input_entry=customtkinter.CTkEntry(master=root,font=('ariel',36*avg_size),text_color=text_colour,bg_color=bg_colour,fg_color=fg_colour, height=60*y_multi,width=200*x_multi)
                input_entry.bind("<KeyRelease>",entry_detection)
                input_entry.place(relx=0.5,rely=0.6,anchor='center')
                
        else:
             #calls subprogram after quiz has finished
             answer_check()
    


   #subprogram for settings menu
    def settings():

        def settings_exist():
            try:
                if root_settings.winfo_exists():
                    settings_button.configure(state="disabled")
            except:
                settings_button.configure(state="normal")
        
        #rescales settings menu
        def scaler_settings(current):
            #sets scalar multiples for all screen elements
            new_height=current.height
            new_width=current.width
            y_multi=new_height/1080
            x_multi=new_width/1920
            avg_size=(x_multi+y_multi)/2
        
            #resizing GUI background
            if main_theme=="dark":
                bg_image2=Image.open("Images\Dark Settings Background.png")
            else:
                bg_image2=Image.open("Images\Light Settings Background.png")
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
        global root_settings,frame_settings,translate_title,switch_theme_button,exit_settings
        settings_button.configure(state="disabled")
        root_settings=Toplevel(bg=bg_colour)
        root_settings.title(settings_text)
        root_settings.geometry("300x400") 
        bg_image2=Image.open("Images\Dark Settings Background.png")
        bg_image_copy2=bg_image2.copy()
        bg_photoimage2=ImageTk.PhotoImage(bg_image_copy2)
        bg_settings=customtkinter.CTkLabel(root_settings,image=bg_photoimage2)
        bg_settings.bind("<Configure>",scaler_settings)
        bg_settings.pack(fill='both',expand=True)
        frame_settings=customtkinter.CTkFrame(master=root_settings,fg_color=fg_colour,bg_color=bg_colour,width=300,height=400,corner_radius=30)
        frame_settings.place(relx=0.5,rely=0.5,in_=bg_settings, anchor="center")

        #importing languages for translator
        global languages, language_list,translated_combo
        languages=googletrans.LANGUAGES
        language_list=list(languages.values())

        try:
            translate_title_text=str(textblob.TextBlob(translator_text).translate(from_lang=from_language_key,to=to_language_key))
        except:
            translate_title_text=translator_text
        #defining settings menu elements
        translate_title=customtkinter.CTkLabel(root_settings,text_color=text_colour,text=translate_title_text,font=("ariel",18),fg_color=fg_colour, height=20,width=100)
        translate_title.place(relx=0.5,rely=0.1,anchor='center')

        translated_combo=customtkinter.CTkComboBox(root_settings, width=150, values=language_list, bg_color=bg_colour, height=20)
        translated_combo.set("english")
        translated_combo.place(relx=0.5,rely=0.2,anchor='center')

        try:
            translate_button_text=str(textblob.TextBlob(translate_text).translate(from_lang=from_language_key,to=to_language_key))
        except:
            translate_button_text=translate_text
        translate_button=customtkinter.CTkButton(root_settings,text_color=text_colour,text=translate_button_text,font=("ariel",14),bg_color=bg_colour,corner_radius=6, width=100, height=30,command=translate)
        translate_button.place(relx=0.5,rely=0.35,anchor='center')

        try:
            theme_button_text=str(textblob.TextBlob(theme_text).translate(from_lang=from_language_key,to=to_language_key))
        except:
            theme_button_text=theme_text
        switch_theme_button=customtkinter.CTkSwitch(root_settings,text_color=text_colour,text=theme_button_text,font=("ariel",18),fg_color=fg_colour, corner_radius=6, width=100, height=20, command=switch_theme)
        switch_theme_button.place(relx=0.5,rely=0.5,anchor='center')


        try:
            exit_settings_text=str(textblob.TextBlob(exit_text).translate(from_lang=from_language_key,to=to_language_key))
        except:
            exit_settings_text=exit_text
        exit_settings=customtkinter.CTkButton(root_settings,text_color=text_colour,text=exit_settings_text,font=("ariel",16),bg_color=bg_colour, corner_radius=6, width=80, height=30, command=close_settings)
        exit_settings.place(relx=0.5,rely=0.7,anchor='center')
        
        
        settings_exist()
        root_settings.mainloop()

    #subprogram for exit button
    def close_main():
        root.destroy()

        
    #defining GUI
    customtkinter.set_appearance_mode("dark") 
    root=customtkinter.CTk()                                                                               
    root.title(title_text)
    root.geometry("720x480")                         

    #defining background
    bg_image=Image.open("Images\Dark Background image.png")
    bg_image_copy=bg_image.copy()
    bg_photoimage=ImageTk.PhotoImage(bg_image_copy)
    bg=customtkinter.CTkLabel(root,image=bg_photoimage)
    bg.bind("<Configure>",scaler)
    bg.pack(fill='both',expand=True)
    frame=customtkinter.CTkFrame(master=root,fg_color=fg_colour,bg_color=bg_colour,width=720,height=480,corner_radius=30)
    frame.place(relx=0.5,rely=0.5,in_=bg, anchor="center")

    #defining start menu elements
    title=customtkinter.CTkLabel(root,text=title_text,font=("ariel",30),text_color=text_colour,fg_color=fg_colour,height=20,width=150)
    title.place(relx=0.5,rely=0.2,anchor='center')

    start_button=customtkinter.CTkButton(root,text=start_text,font=("ariel",24),bg_color=bg_colour,text_color=text_colour, width=150, command=lambda:start(0))
    start_button.place(relx=0.5,rely=0.4,anchor='center')

    #creating image for settings button
    settings_image=Image.open("Images\settings symbol.png")
    settings_image_copy=settings_image.copy()
    settings_image=settings_image_copy.resize((50,50))

    settings_button=customtkinter.CTkButton(root,text="",state="normal",image=ImageTk.PhotoImage(settings_image),font=("ariel",24),text_color=text_colour,width=50, command=settings)
    settings_button.place(relx=0.15,rely=0.85,anchor='center')

    exit_main=customtkinter.CTkButton(root,text=exit_text,font=("ariel",24),text_color=text_colour,bg_color=bg_colour, width=50, command=close_main)
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
score_text="Score"
main_theme="dark"
current_language="english"
user_mcq_answers=[]
user_entry_answers=[]

#questions and mcq options for the quiz
questions = ["Which of the following is the equation for average velocity (v is average velocity).", "If an object is acceleration uniformly, how would its displacement time graph appear?","If a ball is thrown vertically up, what is its instantaneous velocity when it reaches its max height?","What does the gradient of a velocity time graph represent?","A car stopped from 200 m/s over a distance of 1 km. What is the magnitude of acceleration that the car experienced over this time?","An object moves at a constant velocity of 108 km/h. What is its displacement over 11s?"," A train accelerates from 10 m/s to 60 m/s in 20 s. What is the acceleration of the train?","A ball is dropped from a height of 5 m/s at a speed of 10 m/s. How long does it take to hit the ground to 2 decimal places?"]
A=["v=s/t","Straight line with positive gradient","Not enough information","acceleration"]
B=["v=u+at","Straight line with negative gradient","Less than initial velocity but not zero","displacement"]
C=["v=u+a/t","Curve with positive gradient","More than initial velocity","distance"]
D=["v=st","Curve with negative gradient","Zero","Force"]

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