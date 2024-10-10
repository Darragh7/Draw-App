#122461902 - Darragh O'Keeffe
from tkinter import *
from app_custom_classes import *
#GUI layout 
config_c = Config(root,"Assignment 2",930,600,"grey")
left_frame = Frame(root, width=215, height=580, bg='light grey', border = 2)
left_frame.grid(row=0, column=0, padx=10, pady=10)
left_frame.grid_propagate(False)
right_frame = Frame(root, width=700, height=600, bg='white', border=2)
right_frame.grid(row=0, column=1)
right_frame.grid_propagate(False)

#Left frame
#Labels
lab1 = Label(left_frame, text="Colors" , background='light green' , font='Helvetica' , padx=22.5 , pady= 4).grid(column=0, row=0)
lab2 = Label(left_frame, text="Shapes", background='skyblue', font='Helvetica', padx=22.5 , pady= 4).grid(column=1, row=0)
#Buttons 
btn_col1_red = Button(left_frame, text="Red", background='red', border = 2 , padx=31 , pady= 5 , height=2, width=4)
btn_col1_red.grid(column=0, row=1 , padx=4 , pady=4)
btn_col1_blue = Button(left_frame, text="Blue", background='blue', border = 2 ,padx=31 , pady= 5 , height=2, width=4)
btn_col1_blue.grid(column=0, row=3 , padx=4 , pady=4)
btn3_col1_yellow  = Button(left_frame, text="Yellow", background='yellow', border = 2 ,padx=31 , pady= 5 , height=2, width=4)
btn3_col1_yellow.grid(column=0, row=5 , padx=4 , pady=4)
btn_col2_line = Button(left_frame, text="Line", background='chocolate', border = 2 , padx=31 , pady= 5 , height=2, width=4)
btn_col2_line.grid(column=1, row=1 , padx=4 , pady=4)
btn_col2_rect = Button(left_frame, text="Rectangle", background='chocolate', border = 2 ,padx=31 , pady= 5 , height=2, width=4)
btn_col2_rect.grid(column=1, row=3 , padx=4 , pady=4)
btn3_col2_oval = Button(left_frame, text="Oval", background='chocolate', border = 2 ,padx=31 , pady= 5 , height=2, width=4)
btn3_col2_oval.grid(column=1, row=5 , padx=4 , pady=4)

#Right frame
#Canvas
myCanvas = Canvas(right_frame, width=700, height=600, bg='white')

def draw_shape(event):
    global shape
    global start_x, start_y
    global event_click

    if event_click == True:
        #On the first click , store start coordinates as first corner
        start_x = event.x
        start_y = event.y
        event_click = False  #Waits for second click 
    else:
        if shape == "oval":
            myCanvas.create_oval(start_x, start_y, event.x, event.y, fill=color)
        elif shape == "rectangle":
            myCanvas.create_rectangle(start_x, start_y, event.x, event.y, fill=color)
        elif shape == "line":
            myCanvas.create_line(start_x, start_y, event.x, event.y, fill=color)
        event_click = True

def select_shape(selected_shape):
    global shape
    global event_click
    shape = selected_shape
    event_click = True

    # Update button colors based on selection
    btn_col2_line.config(bg='chocolate')
    btn_col2_rect.config(bg='chocolate')
    btn3_col2_oval.config(bg='chocolate')

    if shape == "line":
        btn_col2_line.config(bg='green')
    elif shape == "rectangle":
        btn_col2_rect.config(bg='green')
    elif shape == "oval":
        btn3_col2_oval.config(bg='green')

def select_color(selected_color):
    global color
    global event_click
    color = selected_color
    event_click = True

    # Update button colors based on selection
    btn_col1_red.config(bg='red')
    btn_col1_blue.config(bg='blue')
    btn3_col1_yellow.config(bg='yellow')

    if color == "red":
        btn_col1_red.config(bg='green')
    elif color == "blue":
        btn_col1_blue.config(bg='green')
    elif color == "yellow":
        btn3_col1_yellow.config(bg='green')

#Initialize global variables
shape = ""
color = ""
event_click = True

#Bind buttons to functions
def select_color_red(event):
    select_color("red")

def select_color_blue(event):
    select_color("blue")

def select_color_yellow(event):
    select_color("yellow")

def select_shape_line(event):
    select_shape("line")

def select_shape_rectangle(event):
    select_shape("rectangle")

def select_shape_oval(event):
    select_shape("oval")

btn_col1_red.bind("<Button-1>", select_color_red)
btn_col1_blue.bind("<Button-1>", select_color_blue)
btn3_col1_yellow.bind("<Button-1>", select_color_yellow)
btn_col2_line.bind("<Button-1>", select_shape_line)
btn_col2_rect.bind("<Button-1>", select_shape_rectangle)
btn3_col2_oval.bind("<Button-1>", select_shape_oval)

myCanvas.bind("<Button-1>", draw_shape)

#Event loop
myCanvas.pack()
try:
    root.mainloop()
except Exception as e:
    print("An error occurred:", str(e))
