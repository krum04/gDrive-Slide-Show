# main.py
import tkinter
from PIL import Image, ImageTk, ImageFilter
from folderSync import folderSync 

# create a Tkinter window
root = tkinter.Tk()

# get the screen dimensions
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# set window properties
root.overrideredirect(1) 
root.geometry(f"{w}x{h}+0+0") 
root.focus_set()  

# create a canvas to draw on
canvas = tkinter.Canvas(root, width=w, height=h, highlightthickness=0)
canvas.pack()
canvas.configure(background='black')  

# set up an infinite loop to display images
running = True

# seconds to display each image
delay = 10  

while running:

    # get a list of image files from the specified folder
    images = folderSync()

    # loop through the images and display each one
    for image in images:

        # attempt to open the image
        try:
            pilImage = Image.open(image)
        except Exception as e:
            print(e)
            continue  # skip to the next image if there's an error

        # resize the image to fit the screen while preserving aspect ratio
        imgWidth, imgHeight = pilImage.size
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)

        # create a blurred version of the image and paste the original onto it
        bluredImage = pilImage.resize((4000, 4000), Image.ANTIALIAS).filter(ImageFilter.GaussianBlur(radius=30))
        pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)
        bluredImage.paste(pilImage, (int(2000-(imgWidth/2)), int(2000-(imgHeight/2))))

        # convert the image to a Tkinter-compatible format and display it
        imageTk = ImageTk.PhotoImage(bluredImage)
        imagesprite = canvas.create_image(w/2, h/2, image=imageTk)

        # update the window and wait for 10 seconds before displaying the next image
        root.update()
        root.after(delay*1000)