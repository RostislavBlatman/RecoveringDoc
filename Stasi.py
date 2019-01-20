# -*- coding: utf-8 -*-
"""
    Stasi - semi-automatic program to restore a torn document.
    In first window you must count the pieces of document, press any key and input their number in console.
    On window "res" you can see black and white mask of document. Press any key.
    On "original" window result of search is displayed. Press any key.
    The next few windows display the pieces individually. You must correct their orientation by double-click
        on right and left mouse button, and rotate by mouse wheel. If correct - press space-button.
    And now press "Y" if first piece is correct.
    Show some magic...
    Your recover document is ready to read :)
"""
import ctypes

import cv2
import numpy as np
import functions as fn
import datetime as dt
import Piece as P

def rotate(event,x,y,flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        img = img[-1:0:-1, :]
    if event == cv2.EVENT_RBUTTONDBLCLK:
        img = img[:, -1:0:-1]
    if event == cv2.EVENT_MBUTTONDBLCLK:
        M = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 90, 1.0)
        img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            param+=1
            M = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), param, 1.0)
            img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
        elif flags < 0:
            param-=1
            M = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), param, 1.0)
            img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return img
#input('ARE YOU SURE?!\a')
START = dt.datetime.now()

image1  = cv2.imread("6.png")
image2 = cv2.imread("7.png")
image3 = cv2.imread("9.png")

image = np.concatenate((image1, image2, image3), axis=1)

cv2.namedWindow ('original', 0)
cv2.resizeWindow('original', (ctypes.windll.user32.GetSystemMetrics(0)-100, ctypes.windll.user32.GetSystemMetrics(1)-200))
cv2.imshow('original', image)
cv2.waitKey(0)
cv2.destroyWindow('original')
g = input('How many  pieces?\n>>>')

pieces = fn.pieces(g, image)
j=0
cv2.namedWindow('Original', 0)
cv2.resizeWindow('Original', (ctypes.windll.user32.GetSystemMetrics(0)-100, ctypes.windll.user32.GetSystemMetrics(1)-200))
cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyWindow('Original')
cv2.imwrite('Original.jpg', image)
fragments = []
for img in pieces:

    img = fn.orient(img)
    filename = "img" + str(j) + ".png"
#    cv2.imwrite(filename, img)
    param = 0
    cv2.namedWindow('image', 0)
    cv2.resizeWindow('image', (ctypes.windll.user32.GetSystemMetrics(0)-100, ctypes.windll.user32.GetSystemMetrics(1)-200))
    cv2.setMouseCallback('image', rotate, param)
    while(1):
       cv2.imshow('image',img)
       k = cv2.waitKey(1) & 0xFF
       if k == 32:

           break
       if k == 27:
           cv2.destroyAllWindows()
           raise SystemError("You left the program")
    cv2.destroyAllWindows()    
    img = fn.crop(img)
    filename = "Piece" + str(j+1) + ".png"
    cv2.imwrite(filename, img)
    fragments.append(img)
#    P.ePuzzle.corner(img)
    j+=1
place = np.zeros((image1.shape[0]+300, image1.shape[1]), dtype='uint8')
fff = fragments[:]
puzzle = P.ePuzzle(place, fff)
l1 = puzzle.assembly()

I = list(np.where(place != 0))
[X1,Y1] = [min(I[0])+150, min(I[1])+150]
[X2,Y2] = [max(I[0])-150, max(I[1])-150]
place = place[X1:X2, Y1:Y2] 
eroded = cv2.erode(place, cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)), iterations = 1)
cv2.destroyAllWindows()
cv2.namedWindow('Image', 0)
cv2.resizeWindow('Image', (700, 700))
cv2.imshow('Image', place)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('puzzle.png', place)
FINISH = dt.datetime.now()
print('Work is done, timeworks: ', FINISH-START, '\a')