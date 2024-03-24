
#Caterina Ponti 
#CS110
#Project 2 Part 1 and 2 - Image Processing

from PIL import Image

import math

def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"

    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    imageWidth, imageHeight = inputImage.size

    copyImage(inputImage, imageWidth, imageHeight)

    while True: #Creating a menu to let the user choose what to do next
        print("Menu: ")
        print("1 - Flip the imagine.")
        print("2 - Find the secret pattern.")
        print("3 - Covert the imagine to black and white.")
        print("4 - Rotate the image 90 degrees.")
        print("5 - Swap corners of the image.")
        print("6 - Blur the image.")
        print("7 - Sharpen the image.")
        print("8 - Extract the edge from the image.")
        print("9 - Double the size.")
        print("10 - Exit.")

        

        choice = int(input("Enter your choiche (1/2/3/4/5/6/7/8/9/10):")) #Asking the user for an input chioce.

        try: #Menu
            if choice == 1:
                inputImage = flipVertical(imageWidth, imageHeight, inputImage)
                print("The image was flipped vertically.")
            elif choice == 2:
                findPattern()
                print("The mistery was solved.")
            elif choice == 3:
                makeGrayscale(imageWidth, imageHeight, inputImage)
                print("The image was converted to black and white.")
            elif choice == 4:
                rotate(inputImage, imageHeight, imageWidth)
                print("The image was rotated by 90 degrees.")
            elif choice == 5:
                swapCorners(inputImage, imageHeight, imageWidth)
                print("Corners of the image were swapped.")
            elif choice == 6:
                blur(inputImage, imageHeight, imageWidth)
                print("The image was blurred.")
            elif choice == 7:
                sharpenImage()
                print("The image was sharpened.")
            elif choice == 8:
                edgedetection(inputImage, imageHeight, imageWidth)
                print("The edges were extracted from the image.")
            elif choice == 9:
                factor = int(input("Enter a factor: ")) #Asking the user for an input
                scaleLarger(inputImage, imageHeight, imageWidth, factor)
                print(f"The image made {factor} times larger.")
            elif choice == 10:
                print("Goodbye!")
                break
            else:
                print("Error! Enter a value between 1 and 10.")


        except ValueError:
            print("Error! Enter a valid integer between 1 and 10.")


# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/copy.png")

def flipVertical(imageWidth, imageHeight, inputImage):
    verticalflipImage = Image.new('RGB', (imageWidth, imageHeight), 'white') #Creating a new image 

    for i in range(imageWidth): #Creating a nested loop 
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j)) 
            j = (imageHeight - 1) - j #Flipping the height values of the pixels
            verticalflipImage.putpixel((i, j), pixelColors)

    verticalflipImage.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/verticalflip.png") #Saving the image 
    
def findPattern():
    redImage = Image.open("/Users/caterinaponti/Desktop/PROJECTS/Project2/red-image.png")
    imageWidth, imageHeight = redImage.size

    for i in range(imageWidth): #Creating a nested loop 
        for j in range(imageHeight):
            pixelsColor = redImage.getpixel((i, j)) #Get the pixels' colors 
            if pixelsColor == (255, 0, 0) : #Getting rid of the red pixels
                pixelsColor = (255, 255, 255) #Set the pixels' colors to white
                redImage.putpixel((i, j), pixelsColor)

    redImage.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/mystery-solved.png") #Saving the image


def makeGrayscale(imageWidth, imageHeight, inputImage):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    grayImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth): # Creating a nested loop to modify the pixels
        for j in range(imageHeight):
            r, g, b = inputImage.getpixel((i,j)) #Getting the three RGB values from every pixel
            r = (r * 30)//100 + (g * 59)//100 + (b * 11)//100 #Setting the RGB values of the pixel to the same values
            g = (r * 30)//100 + (g * 59)//100 + (b * 11)//100
            b = (r * 30)//100 + (g * 59)//100 + (b * 11)//100
            pixelsColor = (r, g, b)
            grayImage.putpixel((i,j), pixelsColor) 

    grayImage.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/grayscale.png") #Saving the new image 



def rotate(inputImage, imageHeight, imageWidth):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    rotateImage = Image.new('RGB', (imageHeight, imageWidth), 'white')

    for i in range(imageHeight): # Creating a nested loop to modify the pixels
        for j in range(imageWidth):
            pixelsColor = inputImage.getpixel((j, i))
            rotateImage.putpixel((i, imageWidth - j - 1), pixelsColor) 

    rotateImage.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/rotate.png") #Saving the new image 

 
def swapCorners(inputImage, imageHeight, imageWidth):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    swap_corners_image = Image.new('RGB', (imageWidth, imageHeight), 'white')

    # Splitting the image in 4 quadrants
    halfWidth = imageWidth // 2 
    halfHeight = imageHeight // 2

    for i in range(imageWidth//2): #Iterating through the pixels of the upper left quadrant 
        for j in range(imageHeight//2):
            pixelsColor = inputImage.getpixel((i, j))
            swap_corners_image.putpixel((i + halfWidth, j + halfHeight), pixelsColor) #Positioning the pixels in the lower right corner

    for i in range(imageWidth//2, imageWidth): #Iterating through the pixels of the upper right quadrant 
        for j in range(imageHeight//2):
            pixelsColor = inputImage.getpixel((i, j))
            swap_corners_image.putpixel((i - halfWidth, j + halfHeight), pixelsColor) #Positioning the pixels in the lower left corner

    for i in range(imageWidth//2): #Iterating through the pixels of the lower left quadrant 
        for j in range(imageHeight//2, imageHeight):
            pixelsColor = inputImage.getpixel((i, j))
            swap_corners_image.putpixel((i + halfWidth, j - halfHeight), pixelsColor) #Positioning the pixels in the upper right corner

    for i in range(imageWidth//2, imageWidth): #Iterating through the pixels of the lower right quadrant 
        for j in range(imageHeight//2, imageHeight):
            pixelsColor = inputImage.getpixel((i, j))
            swap_corners_image.putpixel((i - halfWidth, j - halfHeight), pixelsColor) #Positioning the pixels in the upper left corner


    swap_corners_image.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/cornerswap.png") #Saving the new image 


def blur(inputImage, imageHeight, imageWidth):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    blur_Image = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth): #Iterating throught the image pixels
        for j in range(imageHeight):
            
            pixel_grid = [] #Creating an empty list for the pixel grid values

            for x in range(i - 1, i + 2): #creating the grid around the pixel
                for y in range(j - 1, j + 2):

                    if 0 <= x < imageWidth and 0 <= y < imageHeight: #Taking care of the pixels who are on the edge of the image
                        pixel_grid.append(inputImage.getpixel((x, y)))

            avg_rgb = ( #averaging the pixel colors of the pixel of the grid
                sum([px[0] for px in pixel_grid]) // len(pixel_grid),
                sum([px[1] for px in pixel_grid]) // len(pixel_grid),
                sum([px[2] for px in pixel_grid]) // len(pixel_grid)

            )

            blur_Image.putpixel((i, j), avg_rgb)



    blur_Image.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/blurred.png") #Saving the new image 



def sharpenImage():
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usf-campus.jpg')
    imageWidth, imageHeight = inputImage.size

    sharpenImage = Image.new('RGB', (imageWidth, imageHeight), 'white')
    blur_Image = Image.new('RGB', (imageWidth, imageHeight), 'white')


    for i in range(imageWidth): #Iterating the image pixels
        for j in range(imageHeight):

            original_pixel = inputImage.getpixel((i, j)) #Getting the original pixels of the input Image 

            pixel_grid = [] #Creating an empty list for the pixel grid values

            for x in range(i - 1, i + 2): #creating the grid around the pixel
                for y in range(j - 1, j + 2):

                    if 0 <= x < imageWidth and 0 <= y < imageHeight: #Taking care of the pixels who are on the edge of the image
                        pixel_grid.append(inputImage.getpixel((x, y)))

            avg_rgb = ( #averaging the sum of the colors of the pixel of the grid
                sum([pixel[0] for pixel in pixel_grid]) // len(pixel_grid),
                sum([pixel[1] for pixel in pixel_grid]) // len(pixel_grid),
                sum([pixel[2] for pixel in pixel_grid]) //len(pixel_grid)

            )

            blur_Image.putpixel((i, j), avg_rgb) 
            blurred_pixel = blur_Image.getpixel((i, j))


            sharpened_pixel = ( #Calculating the sharpened pixels with the formula 
                original_pixel[0] + int((original_pixel[0] - blurred_pixel[0]) * 5),
                original_pixel[1] + int((original_pixel[1] - blurred_pixel[1]) * 5),
                original_pixel[2] + int((original_pixel[2] - blurred_pixel[2]) * 5)
            )

            sharpenImage.putpixel((i, j), sharpened_pixel)

    sharpenImage.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/sharpened.png") #Saving the new image 


def edgedetection(inputImage, imageHeight, imageWidth):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')
    edgedetection.Image = Image.new('RGB', (imageWidth, imageHeight), 'white')

    Gx = [
        [+1 , 0, -1],
        [+2 , 0 , -2],
        [+1, 0, -1]
    ]

    Gy = [
        [+1 , +2, +1],
        [0 , 0 , 0],
        [-1, -2, -1]
    ]
    
    for i in range(imageWidth): # Creating a nested loop to modify the pixels
        for j in range(imageHeight):

            pixel_grid = []

            for x in range(i - 1, i + 2): #creating the grid around the pixel
                for y in range(j - 1, j + 2):

                    if 0 <= x < imageWidth and 0 <= y < imageHeight: #Taking care of the pixels who are on the edge of the image
                        r, g, b = inputImage.getpixel((x,y)) #Getting the three RGB values from every pixel
                        grayScale = (r + g + b) // 3
                        pixel_grid.append(grayScale)

            if len(pixel_grid) == 9:     
                totalx = 0 
                totaly = 0

                for k in range(3): #Iterate the values of the pixel grid
                    for t in range(3):
                        totalx += pixel_grid[k * 3 + t] * Gx[k][t] #Multiply each value in the Gx and Gy and add all the values together 
                        totaly += pixel_grid[k * 3 + t] * Gy[k][t]


                output = int(math.sqrt(totalx ** 2 + totaly ** 2)) #Calculate gradient magnitude
                output = max(0, min(255, output))

                edgedetection.Image.putpixel((i, j), (output, output, output))

    edgedetection.Image.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/sobel.png") #Saving the new image



def scaleLarger(inputImage, imageHeight, imageWidth, factor):
    inputImage = Image.open('/Users/caterinaponti/Desktop/PROJECTS/Project2/usfca_logo.png')

    new_Width = imageWidth * factor #Defining the new width
    new_Height = imageHeight * factor #Defining the new height

    scaleLarger.Image = Image.new('RGB', (new_Width, new_Height), 'white')

    for i in range(new_Width): #Iterating the pixels of the new sized image
        for j in range(new_Height):
            original_i = i // factor #Original size pixels
            original_j = j // factor

            pixel = inputImage.getpixel((original_i, original_j)) #Get the pixels of the Input image pixels
            scaleLarger.Image.putpixel((i, j), pixel) #put the pixels in the new sized picture



    scaleLarger.Image.save("/Users/caterinaponti/Desktop/PROJECTS/Project2/scaled.png") #Saving the new image














main()