# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
from PIL import Image
import imageio
import numpy as np
import skimage.color

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def checkBinaryAdd(pixel):
    sum=0
    pixel=str(pixel)
    pixel1=pixel[4:]
    for i in pixel1:
        sum=sum+int(i)
    return f'{sum:02b}'


def findAdder(data,pixel):
    b00=[0,15]
    b01=[1,2,4,8]
    b10=[3,5,6,9,10,12]
    b11=[7,11,13,14]
    if(data=='00'):
        return f'{b00[min(range(len(b00)), key=lambda i: abs(b00[i] - pixel))]:04b}'
    if(data =='01'):
        return f'{b01[min(range(len(b01)), key=lambda i: abs(b01[i] - pixel))]:04b}'
    if (data == '10'):
        return f'{b10[min(range(len(b10)), key=lambda i: abs(b10[i] - pixel))]:04b}'
    if (data == '11'):
        return f'{b11[min(range(len(b11)), key=lambda i: abs(b11[i] - pixel))]:04b}'

def last4lsbToDic(pixel):
    pixel=str(pixel)
    newpixel=pixel[4:]
    number=int(newpixel,2)
    return number
def change4lsb(pixel,lsb):
    pixel=str(pixel)
    lsb=str(lsb)
    newpixel=pixel[:4]+lsb
    return newpixel

def binaryAdd(newimg, data):
    n=int(f'{len(data):08b}')
    n=len(str(n))
    if(n%2==1):
        n=n+1
    if(((len(data)*8)/2)+(n/2)+n>newimg.shape[0]*newimg.shape[1]):
        return err
    else:
        b=(f'{n:08b}')
        n_binary=(f'{len(data):08b}')
        if(len(n_binary)%2!=0):
            n_binary='0'+n_binary
        data.insert(0, n_binary)
        data.insert(0,b)
        row = newimg.shape[0]
        col = newimg.shape[1]
        i=0
        j=0
        for k in data:
            while(k!=""):
                 z=k[:2]
                 k=k[2:]
                 if(j==col):
                    j=0
                    i=i+1
                 pixel=checkBinaryAdd(newimg[i][j])
                 if(z!=pixel):
                    new_pixel=findAdder(z,last4lsbToDic(newimg[i][j]))
                    newimg[i][j]=change4lsb(newimg[i][j],new_pixel)
                    j=j+1
                 else:
                     j=j+1




        return newimg













def convert_to_gray(image):
    return skimage.color.rgb2gray(image)
def is_grayscale(image):
    if (len(image.shape) == 3):
        return False
    return True
def read_image(filename, representation: int):
    """converts an image to some representation. does not perform gray->rgb!!!!
     :param filename - the filename of an image on disk (could be grayscale or RGB).
     :param representation - representation code, either 1 or 2 defining whether the output should be a grayscale
     image (1) or an RGB image (2).
    :return: the image in the requested representation
    """
    image = imageio.imread(filename).astype(np.float64)
    if(not(is_grayscale(image))): #image has color
        if(representation != 2):
            image = convert_to_gray(image)
    else: #image is gray
        if(representation != 1):#great, do nothing
            print("Error - this function does not support gray to rgb conversion")
            return None
    return normalize_image(image).astype(np.float64)
def binaryToDec(bin):
    bin1=str(bin)
    return int(bin1,2)
def encode():
    img = input("Enter image name(with extension) : ")
    image = imageio.imread(img).astype(np.float64)
    newimg=convert_to_gray(image).astype(np.int64)
    row=newimg.shape[0]
    col = newimg.shape[1]
    for i in range(row):
        for j in range(col):
            newimg[i][j]=f'{newimg[i][j]:08b}'

    data = input("Enter data to be encoded : ")
    if (len(data) == 0):
        raise ValueError('Data is empty')
    newdata=genData(data)
    enPic=binaryAdd(newimg,newdata)
    for i in range(row):
        for j in range(col):
            enPic[i][j]=binaryToDec(enPic[i][j])
    PIL_image = Image.fromarray(np.uint8(enPic))
    new_img_name = input("Enter the name of new image(with extension) : ")
    PIL_image.save( new_img_name,str(new_img_name.split(".")[1].upper()))















    new_img_name = input("Enter the name of new image(with extension) : ")



# Decode the data in the image
def decode():


    return


# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()

    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")


# Driver Code
if __name__ == '__main__':
    # Calling main function
    main()