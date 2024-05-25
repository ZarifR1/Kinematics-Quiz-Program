# Setting up quiz questions to be displayed
questions = ["Which of the following is the equation for average velocity (v is average velocity).", "If an object is acceleration uniformly, how would its displacement time graph appear?","If a ball is thrown vertically up, what is its instantaneous velocity when it reaches its max height?","What does the gradient of a velocity time graph represent?","A car stopped from 200 m/s over a distance of 1 km. What is the magnitude of acceleration that the car experienced over this time?","An object moves at a constant velocity of 108 km/h. What is its displacement over 11s?"," A train accelerates from 10 m/s to 60 m/s in 20 s. What is the acceleration of the train?","A ball is dropped from a height of 5 m/s at a speed of 10 m/s. How long does it take to hit the ground to 2 decimal places?"]
A=["v=s/t","Straight line with positive gradient","Not enough information","acceleration"]
B=["v=u+at","Straight line with negative gradient","Less than initial velocity but not zero","displacement"]
C=["v=u+a/t","Curve with positive gradient","More than initial velocity","distance"]
D=["v=st","Curve with negative gradient","Zero","Force"]

#shows questions on main GUI
question=customtkinter.CTkLabel(root,text=questions[position],fg_color=fg_colour,wraplength=root.winfo_width()*0.5,font=(int("ariel",36*avg_size)), height=150*y_multi,width=new_width*0.3)
next_button=customtkinter.CTkButton(root,text=next_text,bg_color=bg_colour,state="disabled",command=lambda:start(position+1),font=(int("ariel",36*avg_size)), height=50*y_multi,width=180*x_multi)
