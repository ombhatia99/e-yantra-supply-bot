import cv2
import numpy as np
import os

def partA():
    image_names=os.listdir('../Images')
    print(*image_names)
    image_attributes=[]
    middle_pixels=[]
    row=[]
    for image in image_names:
        attr=[]
        img=cv2.imread('../Images/{}'.format(image))
        dimensions=img.shape
        h=dimensions[0]
        w=dimensions[1]
        middle_pixels.append(img[h//2-1,w//2-1])
        image_attributes.append(dimensions)
        attr=[image]
        for dim in dimensions:
            attr.append(dim)
        for x in img[h//2-1,w//2-1].tolist():
            attr.append(x)
        row.append(attr)
    print(image_attributes)
    for pixel in middle_pixels:
        print(*pixel)
    print()
    for r in row:
        print(*r)


def partB():
    img=cv2.imread('../Images/cat.jpg')
    new_img=img.copy()
    new_img[:,:,0]=0
    new_img[:,:,1]=0
    cv2.imshow('img',new_img)
    
    cv2.imwrite('../Generated/cat_red.jpg',new_img)
    

        
def partC():
    i = cv2.imread('../Images/flowers.jpg')
    img = np.array(i, dtype=np.float)
    img /= 255.0
    #pre-multiplication
    a_channel = np.ones(img.shape, dtype=np.float)/2.0
    image = img*a_channel
    cv2.imwrite('../Generated/flowers_alpha.png',image)
    cv2.imshow('img',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
         

def partD():
    img=cv2.imread('../Images/horse.jpg')
    height,width,dimensions=img.shape
    b,g,r=cv2.split(img)
    
    new=0.3*r+0.59*g+0.11*b
    cv2.imshow('img',new)
    cv2.waitkey(0)
    cv2.imwrite('../Generated/horse_gray.jpg',new)
        

#partA()
partB()
partC()
partD()
