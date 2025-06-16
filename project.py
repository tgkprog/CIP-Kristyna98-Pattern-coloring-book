import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageGrab


CANVAS_SIZE = 470
CANVAS_WIDTH = CANVAS_SIZE
CANVAS_HEIGHT = CANVAS_SIZE


root = tk.Tk()
root.geometry('850x650')
root.title("Coloring book")
canvas = tk.Canvas(root, width = CANVAS_WIDTH + 2, height = CANVAS_HEIGHT + 2, bg ="white")
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


color = "white"
coloring_line_width = 6
current_pattern = "initial_instructions"


def return_color(desired_color):
    #This function changes the global variable color, this variable is later used in the main coloring function. This function is called when presing the buttons with colors and various colors are given as arguments.
    global color
    color = desired_color


def return_coloring_line_width(desired_line_width):
    #This function changes the global variable coloring_line_width, this variable is later used in the main coloring function.This function is called when presing the buttons with  various lines-thickness and the number of pixels is passed to ths function as an argument.
    global coloring_line_width
    coloring_line_width = desired_line_width


def draw_pattern(pattern_number):
    #This function at first cleans the canvas and then calles the functions that creates the patterns. This function is connected to buttons and when each of the buttons are clicked, this function is called with the appropriate argument.
    if pattern_number == 1:
        canvas.delete('all')
        create_flower_pattern(canvas, 200 + 3, 200 + 3)

    elif pattern_number == 2:
        canvas.delete('all')
        create_scenery_pattern(canvas, 200 + 3, 200 + 3)

    elif pattern_number == 3:
        canvas.delete('all')
        create_geometry_pattern(canvas, 200 + 3, 200 + 3)

def reset_current_pattern():
    #This function at fist clears the canvas and then draws the same pattern that was there previously. We keep track of what is the current pattern through the global variable current_pattern. Each time a function that draws some pattern is called, that variable is re-written to keep it up-to-date.
    if current_pattern == "initial_instructions":
        canvas.delete('all')
        create_initial_instructions(canvas, 200 + 3, 200 + 3)

    elif current_pattern == "flower_pattern":
        canvas.delete('all')
        create_flower_pattern(canvas, 200 + 3, 200 + 3)

    elif current_pattern == "scenery_pattern" :
        canvas.delete('all')
        create_scenery_pattern(canvas, 200 + 3, 200 + 3)

    elif current_pattern == "geometry_pattern":
        canvas.delete('all')
        create_geometry_pattern(canvas, 200 + 3, 200 + 3)




def main():
    #This is the main function. At first a function that writes the initial instruction is called. Then there are defined all the buttons which are connected to the functions above (i.e. they call these function). At the end we also have the canvas.bind which is basically the main functionality that enables us to do the coloring.

    create_initial_instructions(canvas, 200 + 3, 200 + 3)

    #Buttons for reseting the pattern (i.e. it removes any coloring from the current pattern)
    BOTTOM_BUTTON_Y = 568
    reset = tk.Button(root, text="Reset", width=5, command=lambda: reset_current_pattern())
    reset.place(x=525, y=BOTTOM_BUTTON_Y)

    save_button = tk.Button(root, text="Save", width=5, command=save_canvas_as_image)
    save_button.place(x=600, y=BOTTOM_BUTTON_Y)    
  
    #Buttons for color picking
    red = tk.Button(root, text="Red", width=5, bg="#e83838", command=lambda: return_color("#e83838"))
    red.place(x=20, y=40)
    blue = tk.Button(root, text="Blue", width=5, bg="#0095ff", command=lambda: return_color("#0095ff"))
    blue.place(x=20, y=80)
    yellow = tk.Button(root, text="Yellow", width=5, bg="#EEEE11", command=lambda: return_color("#eeee11"))
    yellow.place(x=20, y=120)
    green = tk.Button(root, text="Green", width=5, bg="#1eba4a", command=lambda: return_color("#1eba4a"))
    green.place(x=20, y=160)
    pink = tk.Button(root, text="Pink", width=5, bg="#fc8de4", command=lambda: return_color("#fc8de4"))
    pink.place(x=20, y=200)
    beige = tk.Button(root, text="Beige", bg="#eed9c4", width=5, command=lambda: return_color("#eed9c4"))
    beige.place(x=20, y=240)
    brown = tk.Button(root, text="Brown", width=5, bg="#804205", command=lambda: return_color("#804205"))
    brown.place(x=20, y=280)
    emerald = tk.Button(root, text="Emerald", width=5, bg="#007d54", command=lambda: return_color("#007d54"))
    emerald.place(x=20, y=320)
    levander = tk.Button(root, text="Levander", width=5, bg="#D3D3FF", command=lambda: return_color("#D3D3FF"))
    levander.place(x=20, y=360)
    mustard = tk.Button(root, text="Mustard", width=5, bg="#FFCE1B", command=lambda: return_color("#FFCE1B"))
    mustard.place(x=20, y=400)
    turquoise = tk.Button(root, text="Turquoise", width=5, bg="#40E0D0", command=lambda: return_color("#40E0D0"))
    turquoise.place(x=20, y=440)
    black = tk.Button(root, text="Black", width=5, command=lambda: return_color("#000000"))
    black.place(x=20, y=480)
    white = tk.Button(root, text="White", width=5, command=lambda: return_color("#FFFFFF"))
    white.place(x=20, y=520)

    # Buttons for line thickness picking
    RIGHT_LINE = 675
    thick = tk.Button(root, text="Thick line", width=10, command=lambda: return_coloring_line_width(14))
    thick.place(x=RIGHT_LINE, y=250)
    medium = tk.Button(root, text="Medium-thick line", width=15, command=lambda: return_coloring_line_width(8))
    medium.place(x=RIGHT_LINE, y=290)
    thin = tk.Button(root, text="Thin line", width=10, command=lambda: return_coloring_line_width(3))
    thin.place(x=RIGHT_LINE, y=330)

    # Buttons for pattern picking
    pattern_flower = tk.Button(root, text="Patern 1 - Flower", width=15, command=lambda: draw_pattern(1))
    pattern_flower.place(x=150, y=40)
    pattern_scenery = tk.Button(root, text="Patern 2 - Scenery", width=15,command=lambda: draw_pattern(2))
    pattern_scenery.place(x=320, y=40)
    pattern_geometry = tk.Button(root, text="Patern 3 - Geometry",width=15, command=lambda: draw_pattern(3))
    pattern_geometry.place(x=490, y=40)
    




    canvas.bind("<B1-Motion>", on_mouse_dragged)
    root.mainloop()






def create_flower_pattern(canvas, starting_x, starting_y):
    #This function draws a flower on the canvas, starting_x and starting_y are the coordinates for the canvas centre. Here we also change the global variable current pattern to keep the current pattern up-to-date so we can use the reset function.

    global current_pattern
    current_pattern = "flower_pattern"

    canvas.create_oval(starting_x - 200,starting_y - 200,starting_x + 200,starting_y + 200,width=3,outline ='black')

    canvas.create_oval(starting_x - 20,starting_y - CANVAS_SIZE / 2,starting_x + 20,starting_y,width=3,outline ='black')
    canvas.create_oval(starting_x - 40,starting_y - CANVAS_SIZE / 2,starting_x + 40,starting_y,width=3,outline ='black')
    canvas.create_oval(starting_x - 60,starting_y - CANVAS_SIZE / 2,starting_x + 60,starting_y,width=3,outline ='black')

    canvas.create_oval(starting_x - 20,starting_y,starting_x + 20,starting_y + CANVAS_SIZE / 2, width=3, outline ='black')
    canvas.create_oval(starting_x - 40,starting_y,starting_x + 40,starting_y + CANVAS_SIZE / 2, width=3, outline ='black')
    canvas.create_oval(starting_x - 60,starting_y,starting_x + 60,starting_y + CANVAS_SIZE / 2, width=3, outline ='black')

    canvas.create_oval(starting_x - CANVAS_SIZE / 2,starting_y - 20,starting_x,starting_y + 20, width=3,outline ='black')
    canvas.create_oval(starting_x - CANVAS_SIZE / 2,starting_y - 40,starting_x,starting_y + 40, width=3,outline ='black')
    canvas.create_oval(starting_x - CANVAS_SIZE / 2,starting_y - 60,starting_x,starting_y + 60, width=3,outline ='black')

    canvas.create_oval(starting_x,starting_y - 20,starting_x + CANVAS_SIZE / 2,starting_y + 20,width=3,outline ='black')
    canvas.create_oval(starting_x,starting_y - 40,starting_x + CANVAS_SIZE / 2,starting_y + 40,width=3,outline ='black')
    canvas.create_oval(starting_x,starting_y - 60,starting_x + CANVAS_SIZE / 2,starting_y + 60,width=3,outline ='black')

    canvas.create_oval(starting_x - 20,starting_y - 20,starting_x + 20,starting_y + 20,fill='white',width=3, outline ='black')

def create_scenery_pattern(canvas, starting_x, starting_y):
    #This function draws a scenery on the canvas, starting_x and starting_y are the coordinates for the canvas centre. Here we also change the global variable current pattern to keep the current pattern up-to-date so we can use the reset function.

    global current_pattern
    current_pattern = "scenery_pattern"
    
    # house
    canvas.create_rectangle(starting_x - 80, starting_y + 40, starting_x + 80, CANVAS_HEIGHT, width=3, outline ='black')
    canvas.create_line(starting_x - 80, starting_y + 40, starting_x, starting_y - 50, width=3)
    canvas.create_line(starting_x + 80, starting_y + 40, starting_x, starting_y - 50, width=3)

    # left window
    canvas.create_rectangle(starting_x - 50, starting_y + 70, starting_x - 35, starting_y + 85, width=3, outline ='black')
    canvas.create_rectangle(starting_x - 35, starting_y + 70, starting_x - 20, starting_y + 85, width=3, outline ='black')
    canvas.create_rectangle(starting_x - 50, starting_y + 85, starting_x - 35, starting_y + 100, width=3, outline ='black')
    canvas.create_rectangle(starting_x - 35, starting_y + 85, starting_x - 20, starting_y + 100, width=3, outline ='black')

    # right window
    canvas.create_rectangle(starting_x + 20, starting_y + 70, starting_x + 35, starting_y + 85, width=3, outline ='black')
    canvas.create_rectangle(starting_x + 35, starting_y + 70, starting_x + 50, starting_y + 85, width=3, outline ='black')
    canvas.create_rectangle(starting_x + 20, starting_y + 85, starting_x + 35, starting_y + 100, width=3, outline ='black')
    canvas.create_rectangle(starting_x + 35, starting_y + 85, starting_x + 50, starting_y + 100, width=3, outline ='black')

    # door
    canvas.create_rectangle(starting_x - 10, CANVAS_HEIGHT - 40, starting_x + 10, CANVAS_HEIGHT, width=3, outline ='black')
    canvas.create_line(starting_x + 10, CANVAS_HEIGHT - 20, starting_x + 5, CANVAS_HEIGHT - 20, width=3)

    # sun
    canvas.create_oval(starting_x + 90, starting_y - 150, starting_x + 150, starting_y - 90, width=3, outline ='black')
    canvas.create_line(starting_x + 85, starting_y - 120, starting_x + 60, starting_y - 120,  width=3)
    canvas.create_line(starting_x + 155, starting_y - 120, starting_x + 180, starting_y - 120,  width=3)
    canvas.create_line(starting_x + 120, starting_y - 155, starting_x + 120, starting_y - 180,  width=3)
    canvas.create_line(starting_x + 120, starting_y - 85, starting_x + 120, starting_y - 60,  width=3)
    canvas.create_line(starting_x + 120, starting_y - 85, starting_x + 120, starting_y - 60,  width=3)
    canvas.create_line(starting_x + 95, starting_y - 145, starting_x + 84, starting_y - 156,  width=3)
    canvas.create_line(starting_x + 145, starting_y - 145, starting_x + 156, starting_y - 156,  width=3)
    canvas.create_line(starting_x + 95, starting_y - 95, starting_x + 84, starting_y - 84,  width=3)
    canvas.create_line(starting_x + 145, starting_y - 95, starting_x + 156, starting_y - 84,  width=3)

    # cloud

    canvas.create_oval(starting_x - 160, starting_y - 125, starting_x - 130, starting_y - 95, width=3, outline ='black')
    canvas.create_oval(starting_x - 100, starting_y - 125, starting_x - 70, starting_y - 95, width=3, outline ='black')
    canvas.create_oval(starting_x - 145, starting_y - 155, starting_x - 85, starting_y - 95, width=3, outline ='black')
    canvas.create_oval(starting_x - 152, starting_y - 134, starting_x - 80, starting_y - 93, width=3, fill = 'white', outline ='')
    canvas.create_line(starting_x - 150, starting_y - 95, starting_x - 80, starting_y - 95, width=3)



def create_geometry_pattern(canvas, starting_x, starting_y):
    #This function draws a geometrical pattern on the canvas, starting_x and starting_y are the coordinates for the canvas centre. Here we also change the global variable current pattern to keep the current pattern up-to-date so we can use the reset function.

    global current_pattern
    current_pattern = "geometry_pattern"

    for i in range(1, 7):
        k = 2 ** i
        x_1 = starting_x - (CANVAS_WIDTH / k)
        y_1 = starting_y - (CANVAS_HEIGHT / k)
        x_2 = starting_x + (CANVAS_WIDTH / k)
        y_2 = starting_y + (CANVAS_HEIGHT / k)

        canvas.create_rectangle(x_1, y_1, x_2, y_2,width=3, outline ='black')
        canvas.create_line(x_1, starting_y, starting_x, y_2, width=3)
        canvas.create_line(starting_x, y_2, x_2, starting_y, width=3)
        canvas.create_line(starting_x, y_1, x_2, starting_y, width=3)
        canvas.create_line(x_1, starting_y, starting_x, y_1, width=3)

    canvas.create_line(starting_x, 0, starting_x, CANVAS_HEIGHT)
    canvas.create_line(0, starting_y, CANVAS_WIDTH, starting_y)


def create_initial_instructions(canvas, starting_x, starting_y):
    #This function writes the initial instructions to use the program. This function is called at the beginning. Here we don't change the global variable as this is it's pre-set value and the user cannot call this function any later after letting some pattenrs to be drawn on the canvas.
    starting_x = starting_x + 23
    canvas.create_text(starting_x , starting_y - 180, text='WELCOME to the pattern coloring book!', font=('Arial, 17 bold'), fill='#7f65ad')
    canvas.create_text(starting_x, starting_y - 130, text="To start coloring please follow these steps:",font=('Arial, 16 '), fill='#7f65ad')

    canvas.create_text(starting_x , starting_y - 110, text="1. Pick a  desired pattern - click on one of the buttons above",font=('Arial, 10 bold'), fill='black')
    canvas.create_text(starting_x , starting_y - 90, text="2. Pick a  desired color - click one of the buttons on the left",font=('Arial, 10 bold'), fill='black')
    canvas.create_text(starting_x, starting_y - 70,text="3. Pick a line thickness - click one of the buttons on the right", font=('Arial, 10 bold'), fill='black')
    canvas.create_text(starting_x, starting_y - 50,text="4. Start coloring! Just press a mouse and start dragging it around.", font=('Arial, 10 bold'), fill='black')

    canvas.create_text(starting_x , starting_y - 10, text="And that's it! At any time, you can change the color,",font=('Arial, 14'), fill='#7f65ad')
    canvas.create_text(starting_x , starting_y + 10, text="line-thickness or even the pattern, just click the ",font=('Arial, 14'), fill='#7f65ad')
    canvas.create_text(starting_x , starting_y + 30, text="corresponding button. White colored line can work as ",font=('Arial, 14'), fill='#7f65ad')
    canvas.create_text(starting_x , starting_y + 50, text="an erasor but be careful, it can erase the pattern too! ", font=('Arial, 14'),fill='#7f65ad')
    canvas.create_text(starting_x , starting_y + 70,text="If you want to start coloring the current pattern from ", font=('Arial, 14'),fill='#7f65ad')
    canvas.create_text(starting_x , starting_y + 90, text="the beginning, you can use the reset button.",font=('Arial, 14'),fill='#7f65ad')

    canvas.create_text(starting_x, starting_y + 140, text="HAVE FUN!!!", font=('Arial, 23 bold'),fill='#7f65ad')


def color_pattern(canvas, x, y):
    #This function is the function responsible for the coloring prosess. We do it with drwaing ovals. As the function is called repeatedly it then creates an illusion of drawing a line. Here we use the variables color and coloring_line_width.
    
    canvas.create_oval(
        x - 1,
        y - 1,
        x + coloring_line_width,
        y + coloring_line_width,
        fill = color,
        outline = ""
    )


def on_mouse_dragged(event):
    #This function collects the coordinates of the event that is in our case basically the mouse dragging and then it calles the coloring function eith these coordinates. This function is being repeatedly called when the mouse is being pressed via the 'canvas.bind("<B1-Motion>", on_mouse_dragged)' which we have in the main function.
    
    x = event.x
    y = event.y
    color_pattern(canvas, x, y)

def save_canvas_as_image():
    if current_pattern == "initial_instructions":
        messagebox.showinfo("Info", "Draw an image first")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)


if __name__ == '__main__':
    main()

