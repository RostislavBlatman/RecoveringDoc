# -*- coding: utf-8 -*-
import cv2
import numpy as np
import ctypes
import datetime as dt
import time

def phi(k1, k2):
        if (abs(k2)== np.inf or abs(k1) == np.inf) and (abs(k2) == 0.0 or abs(k1) == -0.0):
            phi = np.pi/2
        elif k1 == np.inf and k2 != 0:
            k1 = 0
            tan_phi = abs((k2-k1)/(1+k2*k1))
            phi = np.arctan(tan_phi)
        elif k2 == np.inf and k1 != 0:
            k2 = 0
            tan_phi = abs((k2-k1)/(1+k2*k1))
            phi = np.arctan(tan_phi)
        elif (1+k2*k1) != 0:
            tan_phi = abs((k2-k1)/(1+k2*k1))
            phi = np.arctan(tan_phi)

        
        else:
            tan_phi = np.inf
            phi = np.arctan(tan_phi)


        return phi
    
def degree(angle):
    angle = angle*180/np.pi
    return angle

def radians(angle):
    angle = angle*np.pi/180
    return angle

def line(x0, y0, x1, y1):
    if x0!=x1 and y0!=y1:
        k = (y1-y0)/(x1-x0)
        b = y0-k*x0
    elif x1 == x0:
        k = 1
        b = 0
    elif y0 == y1:
        k=0
        b = y0-k*x0
    return k, b

def linec(x0, y0, x1, y1):
    if x1-x0 != 0:
#    if x0!=x1 and y0!=y1:
        k = (y1-y0)/(x1-x0)
        b = y0-k*x0
    elif x1 - x0 == 0:
        k = np.inf
        b=0
    elif y0 == y1:
        k=0
        b = y0-k*x0
    return k, b

def l_edge(x0, y0, x1, y1):
    if x0!=x1 and y0!=y1:
        k = (y1-y0)/(x1-x0)
    elif x0 ==x1 :
        k=1
    elif y0 == y1:
        k=0
    length = np.sqrt((x0-x1)**2 + (y0-y1)**2)
    return length, k
#
def inPolygon(x, y, xp, yp):
    c=0
    for i in range(len(xp)):
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and \
            (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])): c = 1 - c    
    return c

def on_line(k, b, x, y, Y):
    c = 0
    for i in range(len(x)):
        if k != np.inf:
            if y[i] - 15 <= x[i]*k + b <= y[i] + 15:
                c += 1
        else:
            if y[i] == Y or (Y-5 < y[i] < Y+5):
                c += 1
    return c

def rotate(event,x,y,flags, param):
    global img
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            param+=10
            M = cv2.getRotationMatrix2D((img.shape[0]/2, img.shape[1]/2), param, 1.0)
            img = cv2.warpAffine(img, M, (img.shape[0], img.shape[1]))
        elif flags < 0:
            param-=10
            M = cv2.getRotationMatrix2D((img.shape[0]/2, img.shape[1]/2), param, 1.0)
            img = cv2.warpAffine(img, M, (img.shape[0], img.shape[1]))
    return img

def pieces(g, image):
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray1, (5, 5), 0)

    mask_im = cv2.inRange(gray, 100, 255)

    dialated = cv2.dilate(mask_im, cv2.getStructuringElement(cv2.MORPH_CROSS,(35,35)), iterations = 1)
    eroded = cv2.erode(dialated, cv2.getStructuringElement(cv2.MORPH_CROSS,(35,35)), iterations = 1) 
    _, contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.namedWindow('res', 0)
    cv2.imshow('res', eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pieces = []
    area = []
    for contour in contours:
        area.append(cv2.contourArea(contour))
    j=0
    ex = 0
    while j<int(g) and ex<100000:
        for i in range(len(contours)):
            if area[i]==max(area):
                rect = cv2.minAreaRect(contours[i])
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                cv2.drawContours(image,[box],0,(0,0,255),10)            
                cv2.drawContours(image, contours[i], -1, (0,255,0), 10)
                k_pos = []
                b_pos = []
                k_neg = []
                b_neg = []
                x = (box[0][0] + box[2][0])/2
                y = (box[0][1] + box[2][1])/2
                center = [x,y]
                for t in range(-1,len(box)-1):
                    k, b = line(box[t][0], box[t][1], box[t+1][0], box[t+1][1])
                    if k >0:
                        k_pos.append(k)
                        b_pos.append(b)
                    else:
                        k_neg.append(k)
                        b_neg.append(b)
                # print(k_neg, k_pos)
                im1 = np.zeros(image.shape[0:2], dtype='uint8')
                ind = np.array(np.where(mask_im != 0))
                if (k_pos[0] == 1 or k_neg[0] == 1) and (box[0][0] == box [1][0] and box [1][1] == box[2][1]):
                    mask1 = ind[0] <= max([box[z][1] for z in range(len(box))])
                    mask2 = ind[0] >= min([box[z][1] for z in range(len(box))])
                    mask01 = (mask1 * mask2)
                    mask1 = ind[1] <= max([box[z][0] for z in range(len(box))])
                    mask2 = ind[1] >= min([box[z][0] for z in range(len(box))])
                    mask02 =  (mask1 * mask2)
                    mask = (mask01 * mask02)
                    X = ind[:, mask]
                    im1[X[0], X[1]] = 1
                    im1 = im1 * gray1
                else:
                    mask1 = ind[0] <= k_pos[0] * ind[1] + b_pos[0]
                    mask2 = ind[0] >= k_pos[1] * ind[1] + b_pos[1]
                    mask12 = (mask1 * mask2)
                    mask3 = ind[0] >= k_pos[0] * ind[1] + b_pos[0]
                    mask4 = ind[0] <= k_pos[1] * ind[1] + b_pos[1]
                    mask34 = (mask3 * mask4)
                    mask5 = ind[0] <= k_neg[0] * ind[1] + b_neg[0]
                    mask6 = ind[0] >= k_neg[1] * ind[1] + b_neg[1]
                    mask56 = (mask5 * mask6) 
                    mask7 = ind[0] >= k_neg[0] * ind[1] + b_neg[0]
                    mask8 = ind[0] <= k_neg[1] * ind[1] + b_neg[1]
                    mask78 = (mask7 * mask8)
                    mask1234 = mask12 + mask34
                    mask5678 = mask56 + mask78 
                    mask = mask1234 * mask5678
                    X = ind[:, mask]
                    im1[X[0], X[1]] = 1
                    im1 = im1 * gray1
#                
                if center[1] < image.shape[0]/2:
                    M = np.float32([[1, 0, 0], [0, 1, round(image.shape[0]/2 - center[1], 0)]])
                    im1 = cv2.warpAffine(im1, M, (im1.shape[1], im1.shape[0]))
#                    print (round(image.shape[0]/2 - center[1], 0))
                elif center[1] > image.shape[0]/2:                     # Y #
                    M = np.float32([[1, 0, 0], [0, 1, -round(center[1] - image.shape[0]/2, 0)]])
                    im1 = cv2.warpAffine(im1, M, (im1.shape[1], im1.shape[0]))
#                    print (round(-(center[1] - image.shape[0]/2, 0)))
                if center[0] < image.shape[1]/2:
                    M = np.float32([[1, 0, round(image.shape[1]/2 - center[0], 0)], [0, 1, 0]])
                    im1 = cv2.warpAffine(im1, M, (im1.shape[1], im1.shape[0]))                    # X #
#                    print(round(image.shape[1]/2 - center[0], 0))
                elif center[0] > image.shape[1]/2:
                    M = np.float32([[1, 0, -round(center[0] - image.shape[1]/2, 0)], [0, 1, 0]])
                    im1 = cv2.warpAffine(im1, M, (im1.shape[1], im1.shape[0]))

                filename = 'img' + str(j+1) + '.png'
                cv2.imwrite(filename, im1)
                print ('Piece ', j+1, 'has been written')
                j+=1
                area[i] = 0
#                cropped = image[y:y+H, x:x+W]
                pieces.append(im1)
                break
            else:
                ex += 1
            
    return pieces



def orient(image):

    gray = cv2.GaussianBlur(image, (5, 5), 0)
    mask = cv2.inRange(gray, 200, 255)
    eroded = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_CROSS,(5,9)), iterations = 1)
    _, contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    area = []
    for contour in contours:
        area.append(cv2.contourArea(contour))
    ex = 0
    if len(contours) == 0:
        raise SystemExit("all is black")
    u = 0
    k = []
    same = []
    while u < 4 and ex < 1000:
        for i in range(len(contours)):
            if area[i]==max(area):
                ex += 1
                if area[i] < 3000:
                    u += 1
                    break
                else:

                    length = []
                    

                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    

                    
                    if u > 0:
                        length.append(l_edge(box[0][0], box[0][1], box[1][0], box[1][1])[0])
                        length.append(l_edge(box[1][0], box[1][1], box[2][0], box[2][1])[0])
                        for t in range(len(length)):
                            if length[t] == max(length):
                                if l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1] >= 0:
                                    k.append(l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1])
                                else:
                                    k.append(l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1])
                                if box[t][0] == box[t+1][0]:
                                    same.append(1)
                    else:
                        length.append(l_edge(box[0][0], box[0][1], box[1][0], box[1][1])[0])
                        length.append(l_edge(box[1][0], box[1][1], box[2][0], box[2][1])[0])
                        for t in range(len(length)):
                            if length[t] == max(length):
                                if l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1] >= 0:
                                    k_zip = (l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1])
                                else:
                                    k_zip = (l_edge(box[t][0], box[t][1], box[t+1][0], box[t+1][1])[1] )
                    area[i] = 0        
                    u += 1
                    break
#    print(k)
#    print(np.mean(k))
    if k.count(1) != len(k) and k.count(1) == 1:
        k.remove(1)
    if k.count(1) != len(k) and k.count(1) == 2:
        k[k!=1] = 1   
#    print('k', np.mean(k))
    if len(k) != 0:  
        if np.mean(k) <= 0:
            alpha =   np.rad2deg(np.arctan(np.mean(k)))
        else:
            alpha =  np.rad2deg(np.arctan(np.mean(k)))
        if np.mean(k) == 1 and k.count(1) == 2 and len(same) != 0:
            alpha = 90
    
    else:
        if k_zip <=0:
            alpha =  np.rad2deg(np.arctan(k_zip))
        else:
            alpha =  np.rad2deg(np.arctan(k_zip))
#    print ('angle is', alpha)
    (H, W) = image.shape[:2]
    center = (W / 2, H / 2)
    
    if alpha >= 0:
        M = cv2.getRotationMatrix2D(center, alpha, 1.0)
    elif alpha < 0:
        M = cv2.getRotationMatrix2D(center, alpha, 1.0)
    im = cv2.warpAffine(image, M, (W, H))
    return im
    
def crop(image):

    mask = cv2.inRange(image, 100, 255)
    dialated = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_CROSS,(9,9)), iterations = 1)
    eroded = cv2.erode(dialated, cv2.getStructuringElement(cv2.MORPH_CROSS,(9,9)), iterations = 1)
    _, contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    area = []
    for contour in contours:
        area.append(cv2.contourArea(contour))
    for i in range(len(contours)):
        if area[i] == max(area):
            r_rect = x,y,W,H = cv2.boundingRect(contours[i])
#            cv2.rectangle(image,(x,y),(x+W,y+H),(255,255,255),1)
    crop = image[y:y+H, x:x+W]
    return crop





