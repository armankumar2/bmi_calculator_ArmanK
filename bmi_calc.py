'''MAKING A SIMPLE BMI CALCULATOR WITH THE HELP OF PYTHON Tkinter(GUI)'''
# Importing some modules
from tkinter import * # This will give the all modules of tkinter('*' --> indicates all)
import tkinter as tk
from tkinter import ttk # ttk --> This module provide classes to allow using Tk themed widget set
from tkinter import messagebox # This will help to import messagebox from tkinter module
from PIL import ImageTk, Image # This help to import Image and Image from Pillow(PIL) module

#Making a GUI BASED Window
window = tk.Tk() # Shows the screen(GUI based)
window.title("BMI CALCULATOR v.1.0") # Shows the given name in Title bar
window.geometry('370x525') # This helps to resize the window ('WxH') where, H= Height & W= Weight
window.resizable(False,False) # Window cannot be resizable coz. value is False--> (W,H)

# ICON
icon = PhotoImage(file="Photos_project/BMI_CALCULATOR_logo.ico") # getting the image through PhotoImage
icon_1 = window.iconphoto(False,icon) # It shows the icon in the Title Bar takes two arguements (bool,__image)

# STRUCTURE OF THE SOFTWARE 
#TOP
top_image = PhotoImage(file= "Photos_project/BMI_CALCULATOR.png")
top = Label(window, image= top_image).pack(side= TOP )

# Two-boxes
two_box = PhotoImage(file= "Photos_project/two_box.png")
Label(window, image = two_box).place(x= -5, y= 50)
Label(window, image = two_box).place(x= 180, y= 50)

# bottom-box
Label(window, width= 72, height= 18, bg= "light blue").pack(side= BOTTOM) # shows the bottom box

#Scale
scale = PhotoImage(file= "Photos_project/height_scale.png")
Label(window, image= scale , bg= "light blue").place(x= 5, y= 280)

# Height & Weight Slider

'''---------------------- Height_Slider-----------------------------'''

current_value = tk.DoubleVar() # DoubleVar --> Construct a float variable

def get_current_value():
    return '{0:.1f}'.format(current_value.get()) #{0:.1f} --> Here we specify 1 digits of precision and f is used to represent floating point number

def height_slider_changed(one_possible_arguement): #Define a function height_slider_changed and get the get_current_value
    Height_m.set(get_current_value())

    #straight_boy_height_slider_occur

    straight_boy_image = Label(window, bg= "light blue") # bg of the straight_boy_image is light blue
    size_r = int(float(get_current_value())) #converting float into int
    man_image_m = (Image.open("Photos_project/straight_boy.png")) # Module Image help to import images from desktop
    resized_img = man_image_m.resize((70,10 + size_r))
    straight_boy_img = ImageTk.PhotoImage(resized_img) #The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL(Pillow Module) images
    straight_boy_image.config(image= straight_boy_img)
    straight_boy_image.place(x= 30, y= 480 - size_r)
    straight_boy_image.image = straight_boy_img # it shows the image in the window

    


   

# command to change the background of slider
style = ttk.Style() # help to get the bg color
style.configure("TScale", background= "light gray")
# To control the height slider
height_slider = ttk.Scale(window, from_=0, to=200, orient="horizontal",style= "TScale",
command= height_slider_changed, variable= current_value, cursor= "double_arrow")
height_slider.place(x= 45, y= 150)

'''------------------------------------------------------------------------------------------'''

'''---------------------------Weight_Slider---------------------------------------------------'''
current_value_w = tk.DoubleVar() # DoubleVar --> Construct a float variable

def get_current_value_w():
    return '{0:.1f}'.format(current_value_w.get()) #{0:.1f} --> Here we specify 1 digits of precision and f is used to represent floating point number

def weight_slider_changed(one_possible_arguement): #Define a function weight_slider_changed and get the get_current_value_w
    #To globaly access
    global weight_slider
    Weight_m.set(get_current_value_w())

# command to change the background of slider
style_w = ttk.Style() # help to get the bg color
style_w.configure("TScale", background= "light gray")
# To control the weight slider
weight_slider = ttk.Scale(window, from_=0, to=200, orient="horizontal",style= "TScale",
command= weight_slider_changed, variable= current_value_w, cursor= "double_arrow") # "TScale" --> slider
weight_slider.place(x= 225, y= 150)


'''-------------------------------------------------------------------------------------------'''

#BMI calculation

def BMI():
    def msg():
        messagebox.showinfo("BMI CALCULATOR v.1.0","Click on CLEAR REPORT") # it shows the msg box of info
    # To globally access
    global view_report_txt
    global advice_bmi
    global advice_bmi_2
    w = int(Weight_m.get())
    # Converting height(h) cm to m , 1m = 100cm ---> 1cm = 1/100 m
    h = int(Height_m.get()) / 100 # Dividing height(h) with 100
    # BMI formula = weight(w) / height(h²)(**2 --> raise to power of 2 )
    bmi_c = w/(h**2) 
    # round a number into decimal digits
    bmi = round(bmi_c, 1)
    view_report_txt = Label(window, font= ("Arial Bold",60) , fg= "white", bg= "light blue", justify= RIGHT)
    view_report_txt.place(x= 100, y= 250)
    view_report_txt.config(text= bmi)
    view_report_b.config(command= msg) # Double click on VIEW REPORT it will show an info-msg



    # BMI --> DATA TAKEN by --> https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
    advice_bmi = Label(window, font= ("Arial Italic", 30), bg= "light blue")
    advice_bmi_2 = Label(window, font=("Poppins Italic", 10), bg= "light blue", fg= "black")
    advice_bmi.place(x= 125, y= 332)
    advice_bmi_2.place(x= 115, y= 382)
    if bmi <= 18.5 :
        advice_bmi.config(text= "Underweight!", fg= "yellow")
        advice_bmi_2.config(text= "It indicates \n you have to gain some calories") # \n indicates escape seq. of new line
    elif bmi > 18.5 and bmi <= 25:
         advice_bmi.config(text= "Normal!", fg= "green")
         advice_bmi_2.config(text= "It indicates \n that you are healthy")
    elif bmi > 25 and bmi <= 30:
        advice_bmi.config(text= "Overweight!" , fg= "orange") 
        advice_bmi_2.config(text= """It indicates that you are slightly overweight \n A doctor may advice \n to lose some weight for health reasons!""") # \n indicates escape seq. of new line
    else:
        advice_bmi.config(text= "Obes!", fg= "red")
        advice_bmi_2.config(text= """Health may be at risk, burn some calories""") # \n indicates escape seq. of new line

#Height_show_box
height_show_box = PhotoImage(file= "Photos_project/height_show.png")
Label(window, image= height_show_box).place(x= 27, y= 210)

#Height_show_box
weight_show_box = PhotoImage(file= "Photos_project/weight_show.png")
Label(window, image= weight_show_box).place(x= 212, y= 210)


#Entry_Height_Weight
Height_m = IntVar() # IntVar --> Construct a int variable
Weight_m = IntVar() # IntVar --> Construct a int variable

#For measuring Height
height_m = Entry(window, textvariable= Height_m, width= 5, font=("Arial",28), bg= "light gray", fg= "black",bd=0, justify = CENTER) #    to align text in
height_m.place(x= 35, y= 100)
Height_m.set(get_current_value()) # set converts  variable into value

#For Measuring Weight
weight_m = Entry(window, textvariable= Weight_m, width= 5, font=("Arial",28), bg= "light gray", fg= "black",bd=0, justify = CENTER) #    to align text in
weight_m.place(x= 225, y= 100)
Weight_m.set(get_current_value_w())

#BMI CALCULATOR to view report

view_report = PhotoImage(file= "Photos_project/view_report.png")
view_report_b = Button(window, image= view_report , bg= "light blue", bd= 0 , cursor= "hand2", command= BMI) # Button helps to create a button
view_report_b.place(x= 97, y= 459)
view_report_b.config(activebackground= "light blue") # Clicking the button it didn't show any bg

# BMI CALCULATOR to clear report 
'''--------------------CLEAR REPORT------------------------------'''
def clear():
    view_report_txt.place_forget() # It will delete previous record
    advice_bmi.place_forget() # It will delete previous record
    advice_bmi_2.place_forget() # It will delete previous record
    view_report_b.config(command= BMI) # Clicking on clear button it will run BMI function
    

'''--------------------------------------------------------------'''

clear_report = PhotoImage(file= "Photos_project/clear_btn.png")
clear_report_b = Button(window, image= clear_report , bg= "light blue", bd= 0, cursor= "hand2", command= clear) # Button helps to create a button
clear_report_b.place(x= 230, y= 464)
clear_report_b.config(activebackground= "light blue") # Clicking the button it didn't show any bg

#copywright_trademark
copywright = Label(window, text= "© Arman Tech. All rights reserved" , font= ("Poppins",5), fg= "black", bg= "light blue")
copywright.place(x= 250, y= 508)

# To run the program
window.mainloop()

# CODE COMPLETION ------->>>> 100%
