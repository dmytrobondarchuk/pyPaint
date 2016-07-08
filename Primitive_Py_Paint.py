from tkinter import *
#this simple and primitive paint app is created by Dmytro Bondarchuk
class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self):
        self.brush_size = self.brush_slider.get()

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Simple PyPaint")  # set the name of the window
        self.pack(fill=BOTH, expand=1)  # host active elements on the parent window

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")  # create the field for painting and set white background
        self.canv.grid(row=2, column=0, columnspan=11, padx=5, pady=5, sticky=E+W+S+N)  # Attach the canvas by grid method. It will be located in the 3rd row, first column, and will occupy 7 columns, set the margins for X and Y in the 5 pixels, and forced to be stretched when stretching the entire window
        self.canv.bind("<B1-Motion>", self.draw) # Bind a handler to the canvas. <B1-Motion> means "motion while holding left mouse button" to call draw function

        color_lab = Label(self, text="Color: ") # Create a label for the buttons to change the color of the brush
        color_lab.grid(row=0, column=0, padx=6) # Set created tag in the first row and the first column, set the horizontal spacing to 6 pixels

        red_btn = Button(self, text="Red", width=8, bg="red", command=lambda: self.set_color("red")) # Create a button: set button text, set the width of the button (10 characters), the function to be called when the button is pressed.
        red_btn.grid(row=0, column=1) # set button

        green_btn = Button(self, text="Green", width=8, bg="green", command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=8, bg="blue", command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=8, bg="grey", command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        yellow_btn = Button(self, text="Yellow", width=8, bg="yellow", command=lambda: self.set_color("yellow"))
        yellow_btn.grid(row=0, column=5)

        
        clear_btn = Button(self, text="Clear all", width=8, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=0, column=8, padx=6)
       
        self.brush_slider=Scale(self, from_=1, to = 30, orient = HORIZONTAL, length = 75)
        self.brush_slider.grid(row=0, column=9)

        #self.brush_slider_item=self.brush_slider.get()
                       
        app_button = Button(self, text="Apply brush size", width=20, command = lambda: self.set_brush_size()).grid(row=0, column=10)

def main():
    root = Tk()
    root.geometry("850x500+200+30") #set window geometry (850x500) and window location
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()