# -*- coding: utf-8 -*-
"""
Class for piece
"""



import math as m
import time

import numpy as np
import cv2
import functions as fn
import ctypes

class ePuzzle:
        def __init__(self, emptyIm, pieces):
            self.emptyIm = emptyIm
            self.pieces = pieces
            
        def corner(self, piece):
            mask = cv2.inRange(piece, 180, 255)
            corner = 0
            """Top left"""
            Ix1 = 50
            Iy1 = min( min(np.where(mask[:, Ix1] != 0)))
            ix1 = 62
            iy1 = min( min(np.where(mask[:, ix1] != 0)))
            ix2 = 75
            iy2 = min( min(np.where(mask[:, ix2] != 0)))
            ix3 = 87
            iy3 = min( min(np.where(mask[:, ix3] != 0)))
            IIx1 = 150
            IIy1 = min( min(np.where(mask[:, IIx1] != 0)))
            
            IIIy1 = 50 
            IIIx1 = min( min(np.where(mask[IIIy1, :] != 0)))
            iiiy1 = 62
            iiix1 = min( min(np.where(mask[iiiy1, :] != 0)))
            iiiy2 = 75
            iiix2 = min( min(np.where(mask[iiiy2, :] != 0)))
            iiiy3 = 87
            iiix3 = min( min(np.where(mask[iiiy3, :] != 0)))
            IVy1 = 100
            IVx1 =  min( min(np.where(mask[IVy1, :] != 0)))

            k11, b11 = (fn.linec(Ix1, Iy1, IIx1, IIy1))
            k21, b21 = (fn.linec(IVy1, IVx1, IIIy1, IIIx1))

            """Top right"""
            Ix2 = -151
            Iy2 = min( min(np.where(mask[:, Ix2] != 0)))
            ix1 = -63
            iy1 = min( min(np.where(mask[:, ix1] != 0)))
            ix2 = -76
            iy2 = min( min(np.where(mask[:, ix2] != 0)))
            ix3 = -88
            iy3 = min( min(np.where(mask[:, ix3] != 0)))
            IIx2 = -101
            IIy2 = min( min(np.where(mask[:, IIx2] != 0)))
            
            IIIy2 = 50 
            IIIx2 = max(max(np.where(mask[IIIy2, :] != 0)))
            iiiy1 = 62 
            iiix1 = max(max(np.where(mask[iiiy1, :] != 0)))
            iiiy2 = 75 
            iiix2 = max(max(np.where(mask[iiiy2, :] != 0)))
            iiiy3 = 87 
            iiix3 = max(max(np.where(mask[iiiy3, :] != 0)))
            IVy2 = 120
            IVx2 =  max(max(np.where(mask[IVy2, :] != 0)))
            
            k12, b12 = (fn.linec(Ix2, Iy2, IIx2, IIy2))
            k22, b22 = (fn.linec(IVy2, IVx2, IIIy2, IIIx2))

            """Bottom left"""
            Ix3 = 250
            Iy3 = max(max(np.where(mask[:, Ix3] != 0)))
            ix1 = 62
            iy1 = max(max(np.where(mask[:, ix1] != 0)))
            ix2 = 75
            iy2 = max(max(np.where(mask[:, ix2] != 0)))
            ix3 = 87
            iy3 = max(max(np.where(mask[:, ix3] != 0)))
            IIx3 = 200
            IIy3 = max(max(np.where(mask[:, IIx3] != 0)))
            
            IIIy3 = -51 
            IIIx3 = min(min(np.where(mask[IIIy3, :] != 0)))
            iiiy1 = -63
            iiix1 = min(min(np.where(mask[iiiy1, :] != 0)))
            iiiy2 = -76
            iiix2 = min(min(np.where(mask[iiiy2, :] != 0)))
            iiiy3 = -88
            iiix3 = min(min(np.where(mask[iiiy3, :] != 0)))
            IVy3 = -101
            IVx3 =  min(min(np.where(mask[IVy3, :] != 0)))
            
            k13, b13 = fn.linec(Ix3, Iy3, IIx3, IIy3)
            k23, b23 = fn.linec(IVy3, IVx3, IIIy3, IIIx3)
            
#            print('k3', k13, k23)
#            if (fn.on_line(k13, b13, [ix1, ix2, ix3], [iy1, iy2, iy3], Iy3) == 3
#                and fn.on_line(k23, b23, [iiix1, iiix2, iiix3], [iiiy1, iiiy2, iiiy3], IIIy3)) == 3:
#                corner = 'Bottom left'
##            print (abs(round(np.rad2deg(np.arctan(k13) - np.arctan(k23)), 0)))          
            """Bottom right"""
            Ix4 = -51
            Iy4 = max(max(np.where(mask[:, Ix4] != 0)))
            ix1 = -63
            iy1 = max(max(np.where(mask[:, ix1] != 0)))
            ix2 = -76
            iy2 = max(max(np.where(mask[:, ix2] != 0)))
            ix3 = -88
            iy3 = max(max(np.where(mask[:, ix3] != 0)))
            IIx4 = -101
            IIy4 = max(max(np.where(mask[:, IIx4] != 0)))
            
            IIIy4 = -171 
            IIIx4 = max(max(np.where(mask[IIIy4, :] != 0)))
            iiiy1 = -63
            iiix1 = max(max(np.where(mask[iiiy1, :] != 0)))
            iiiy2 = -76
            iiix2 = max(max(np.where(mask[iiiy2, :] != 0)))
            iiiy3 = -88
            iiix3 = max(max(np.where(mask[iiiy3, :] != 0)))
            IVy4 = -101
            IVx4 =  max(max(np.where(mask[IVy4, :] != 0)))
            
            k14, b14 = (fn.linec(Ix4, Iy4, IIx4, IIy4))
            k24, b24 = (fn.linec(IVy4, IVx4, IIIy4, IIIx4))

            if round(k14,2) == - round(k24,2):

                return 'Bottom right'
            
            elif round(k13,1) == - round(k23,1) or (round(k13,1)==0 and round(k13,1)==0):

                return 'Bottom left'
            
            elif round(k12,1) == - round(k22,1):

                return 'Top right'
            
            elif round(k11,1) == - round(k21,1):

                return 'Top left'
            
            else:
                if abs(round(k24,1)) == 0:
                    return 'Right'
                elif abs(round(k23,1)) == 0:
                    return 'Left'
                elif abs(round(k22,1)) == 0:
                    return 'Right'
                elif abs(round(k21,1)) == 0:
                    return 'Left'
                else:
                    return 'not corner'




        def assembly(self):
            for i in range(len(self.pieces)):

                if self.corner(self.pieces[i]) == 'Bottom left':
                    cv2.namedWindow('Im', 0)
#                    cv2.resizeWindow('Im', (700, 700))
                    while (1):
                        cv2.imshow('Im', self.pieces[i])
                        k = cv2.waitKey(1) & 0xFF
                        if k == 121:        ##yes
                            self.emptyIm[-self.pieces[i].shape[0]-1:-1, :self.pieces[i].shape[1]] = self.pieces[i]
                            cv2.destroyAllWindows()
                            last0 = self.pieces.pop(i)
                            first = last0
                            fill = int(max(np.where(self.emptyIm != 0)[1]))
                            break
                        elif k == 110:      ##no
                            cv2.destroyAllWindows()
                            break
                    if k == 121:
                        break
            placcce = ['Bottom right', 'Top left', 'Top right']
            j = 0
            t = 0
            if fill >= self.emptyIm.shape[1] - 200:
                h = 2
                fill = 0
            else: 
                h = 1
            

            fill10 = 0
            fill20 = 0
            step1 = 1
            step = 1
            pos3 = 0
            
            por1 = 20   #20 #20 # --
            por2 = 15   #12+90 #15+30 #30
            por3 = 20   #30 #20 # --
            check = 'Top right'
            
#            self.pieces.reverse()
            time.sleep(10)
            k = 0
            while self.pieces:
                cv2.namedWindow('Result',0)
                cv2.resizeWindow('Result', (700, 700))
                cv2.imshow('Result', self.emptyIm)
                cv2.waitKey(10)
#                ex = input('continue?')
#                if ex == 'y':
#                    pass
#                elif ex == 'n':
#                    raise SystemError('left the program')
                hand = True
                if h == 1:
                    for piece in self.pieces:
                        if k == 0 :
                            time.sleep(10)
                            k+=1
                        if last0.shape[0] >= piece.shape[0]:
                            blur = cv2.GaussianBlur(piece, (7,7), 0)
                            mask = cv2.inRange(blur, 220, 255)
#                            cv2.namedWindow('part', 0)
#                            cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                            cv2.imshow('part', mask)
#                            cv2.waitKey(0)
#                            print('1')
                            delta = last0.shape[0] - piece.shape[0]
    #                        print(max(np.where(last[delta:, :] != 0)))
                            s = last0.shape[0] - delta
#                            print ('s',s)
                            I = [max(max(np.where(last0[delta+int(s/2) - int(s/2.5) + k, :] != 0))) for k in range(1,2*int(s/2.5))]
    #                        print( I)
                            last_l = [last0.shape[1] - u for u in I]
    #                        print(last_l)
    #                        I = min(min(np.where(piece[20 + int(s/6), :] != 0)))
                            I = [min(min(np.where(mask[20 + int(s/2) - int(s/2.5) + k, :] != 0))) for k in range(1,2*int(s/2.5))]
                            piece_l =  I
    #                        print(piece_l)
                            d = np.array(last_l) + np.array(piece_l)
#                            print ('d',np.mean(d))
                            sko = np.std(d)
#                            print('sko',sko)
#                            print(self.corner(piece))
                            if round(sko,0) <= por1 or (self.corner(piece)=='Bottom right' and round(sko, 0) <= 50):# and (self.corner(piece) != 'Top right' and self.corner(piece) != 'Top left' and self.corner(piece)!= 'Left' and self.corner(piece) != 'Right'):
#                                print('fill', fill)
#                                print(fill-int(np.mean(d)))
#                                print(fill-int(np.mean(d)) + piece.shape[1])
                                self.emptyIm[-piece.shape[0]-1:-1, fill-int(np.mean(d)):fill-int(np.mean(d)) + piece.shape[1]] += piece
                                fill = int(max(np.where(self.emptyIm != 0)[1]))
#                                print('fill', fill)
                                hand = False
                                if fill >= self.emptyIm.shape[1] - 200 or self.corner(piece) == 'Bottom right':
                                    h = 2
                                    fill = 0
                                    fill1 = min(np.where(self.emptyIm[:, :first.shape[1]] != 0)[1])
                                    fill2 = min(np.where(self.emptyIm[:, piece.shape[1]:] != 0)[1])
                                    last0 = piece
                                    self.pieces.remove(piece)
                                    placcce.append(placcce.pop(0))
                                    break
                                last0 = piece
                                self.pieces.remove(piece)
                                break
                                placcce.append(placcce.pop(0))
                                
                        elif last0.shape[0] < piece.shape[0]:
                            blur = cv2.GaussianBlur(piece, (7,7),0)
                            mask = cv2.inRange(blur, 220, 255)
#                            cv2.namedWindow('part', 0)
#                            cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                            cv2.imshow('part', mask)
#                            cv2.waitKey(0)
#                            print('0')
                            delta =  piece.shape[0] - last0.shape[0]
    #                        print(max(np.where(last[delta:, :] != 0)))
                            s = piece.shape[0] - delta
#                            print(s)
                            I = [max(max(np.where(last0[-25-k, :] != 0))) for k in range(1,int(s)-25)] 
#                            print(I)
                            last_l = [last0.shape[1] - u for u in I]
    #                        print(last_l)
                            I = [min(min(np.where(mask[25+k, :] != 0))) for k in range(1,int(s)-25)]
    
                            piece_l =  I
    #                        print(piece_l)
                            d = np.array(last_l) + np.array(piece_l)
#                            print ('d',np.mean(d))
                            sko = np.std(d)
#                            print('sko',sko)
#                            print(self.corner(piece))
                            if round(sko,0) <= por1 or (self.corner(piece)=='Bottom right' and round(sko,0) <= 50):#  and (self.corner(piece) != 'Top right' and self.corner(piece) != 'Top left' and self.corner(piece)!= 'Left' and self.corner(piece) != 'Right'):
#                                print(fill-int(np.mean(d)))
#                                print(fill-int(np.mean(d)) + piece.shape[1])
                                self.emptyIm[-piece.shape[0]-1:-1,  fill-int(np.mean(d)):fill-int(np.mean(d)) + piece.shape[1]] += piece 
                                fill = max(np.where(self.emptyIm != 0)[1])
#                                print('fill', fill)
                                hand = False
                                if fill >= self.emptyIm.shape[1]-200 or self.corner(piece) == 'Bottom right':
                                    h = 2
                                    fill = 0
                                    fill1 = min(np.where(self.emptyIm[:, :first.shape[1]] != 0)[1])
                                    fill2 = min(np.where(self.emptyIm[:, -piece.shape[1]-1:-1] != 0)[1]) ##убрать 1200
                                    last0 = piece
                                    self.pieces.remove(piece)
                                    placcce.append(placcce.pop(0))
#                                cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                                cv2.imshow('part', mask)
#                                cv2.waitKey(0)
                                    break
                                last0 = piece
                                self.pieces.remove(piece)
                                break
                                placcce.append(placcce.pop(0))
                    if sko > por1 and hand == True:
                        for piece in self.pieces:
                            if last0.shape[0] >= piece.shape[0]:
                                
                                blur = cv2.GaussianBlur(piece, (7,7), 0)
                                mask = cv2.inRange(blur, 220, 255)
                                cv2.n
    #                            print('1')
                                delta = last0.shape[0] - piece.shape[0]
        #                        print(max(np.where(last[delta:, :] != 0)))
                                s = last0.shape[0] - delta
    #                            print ('s',s)
                                I = [max(max(np.where(last0[delta+int(s/2) - int(s/2.5) + k, :] != 0))) for k in range(1,2*int(s/2.5))]
        #                        print( I)
                                last_l = [last0.shape[1] - u for u in I]
        #                        print(last_l)
        #                        I = min(min(np.where(piece[20 + int(s/6), :] != 0)))
                                I = [min(min(np.where(mask[20 + int(s/2) - int(s/2.5) + k, :] != 0))) for k in range(1,2*int(s/2.5))]
                                piece_l =  I
        #                        print(piece_l)
                                d = np.array(last_l) + np.array(piece_l)
        #                        print ('d',d)
                                sko = np.std(d)
                                while (1):
                                    cv2.imshow('part', mask)
                                    k = cv2.waitKey(1) & 0xFF
                                    if k == 121:  
#                                        print('sko',sko)
            #                            print(self.corner(piece))
                                        self.emptyIm[-piece.shape[0]-1:-1, fill-int(np.mean(d)):fill-int(np.mean(d)) + piece.shape[1]] += piece
                                        fill = int(max(np.where(self.emptyIm != 0)[1]))
        #                                print('fill', fill)
                                        if fill >= self.emptyIm.shape[1]-400 or self.corner(piece) == 'Bottom right':
                                            h = 2
                                            fill = 0
                                            fill1 = min(np.where(self.emptyIm[:, :first.shape[1]] != 0)[1])
                                            fill2 = min(np.where(self.emptyIm[:, piece.shape[1]:] != 0)[1])
                                            last0 = piece
                                            self.pieces.remove(piece)
                                            placcce.append(placcce.pop(0))
                                            break
                                        last0 = piece
                                        self.pieces.remove(piece)
                                        placcce.append(placcce.pop(0))
                                        break
                                    elif k == 110:      ##no
#                                    cv2.destroyWindow('part')
                                        break
                                if k == 121:
                                    break
                                            
                                    
                            elif last0.shape[0] < piece.shape[0]:
                                blur = cv2.GaussianBlur(piece, (7,7),0)
                                mask = cv2.inRange(blur, 220, 255)
#                                cv2.namedWindow('part', 0)
#                                cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                                cv2.imshow('part', mask)
#                                cv2.waitKey(0)
    #                            print('0')
                                delta =  piece.shape[0] - last0.shape[0]
        #                        print(max(np.where(last[delta:, :] != 0)))
                                s = piece.shape[0] - delta
    #                            print(s)
                                I = [max(max(np.where(last0[-25-k, :] != 0))) for k in range(1,int(s)-25)] 
    #                            print(I)
                                last_l = [last0.shape[1] - u for u in I]
        #                        print(last_l)
                                I = [min(min(np.where(mask[25+k, :] != 0))) for k in range(1,int(s)-25)]
        
                                piece_l =  I
        #                        print(piece_l)
                                d = np.array(last_l) + np.array(piece_l)
        #                        print (d)
                                sko = np.std(d)
                                print('sko',sko)
    #                            print(self.corner(piece))
                                while (1):
                                    cv2.imshow('part', mask)
                                    k = cv2.waitKey(1) & 0xFF
                                    if k == 121:  
#                                        print('sko',sko)
            #                            print(self.corner(piece))
                                        self.emptyIm[-piece.shape[0]-1:-1, fill-int(np.mean(d)):fill-int(np.mean(d)) + piece.shape[1]] += piece
                                        fill = int(max(np.where(self.emptyIm != 0)[1]))
        #                                print('fill', fill)
                                        if fill >= self.emptyIm.shape[1]-200:
                                            h = 2
                                            fill = 0
                                            fill1 = min(np.where(self.emptyIm[:, :first.shape[1]] != 0)[1])
                                            fill2 = min(np.where(self.emptyIm[:, piece.shape[1]:] != 0)[1])
                                            last0 = piece
                                            self.pieces.remove(piece)
                                            placcce.append(placcce.pop(0))
                                            break
                                        last0 = piece
                                        self.pieces.remove(piece)
                                        placcce.append(placcce.pop(0))
                                        break
                                    elif k == 110:      ##no
#                                    cv2.destroyWindow('part')
                                        break
                                    if k == 121:
                                        break

                elif h == 2:
                    sizes = []
                    for piece in self.pieces:
                        sizes.append(piece.shape[1])
                    for piece in self.pieces:
                        blur = cv2.GaussianBlur(piece, (7,7),0)
                        mask = cv2.inRange(blur, 220, 255)
#                        cv2.namedWindow('part', 0)
#                        cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                        cv2.imshow('part', mask)
#                        cv2.waitKey(0)
#                        print('3')
                        
#                        s = piece.shape[1]
                        s = min(sizes)
                        I = [max(max(np.where(mask[:, 30+k] != 0))) for k in range(int(s-45))]
                        piece_l = [piece.shape[0] - u for u in I]
                        II = [min(min(np.where(self.emptyIm[:, fill10+30+k] != 0))) for k in range(int(s-45))]
                        last_l = II
                        d = np.array(last_l) + np.array(piece_l)
                        sko = np.std(d)
#                        print('sko', sko)
#                        print(self.corner(piece))
                        if (round(sko,0) <= por2 and self.corner(piece) != 'Top right') or ((self.corner(piece) == 'Left' or self.corner(piece) == 'Top left') and round(sko,0) <= 30):# or self.corner(piece) == 'Left':
#                            print('sko',sko)
#                            print('pos3', pos3)
                            self.emptyIm[-piece.shape[0]+int(np.mean(d)+sko):int(np.mean(d)+sko), fill10-pos3:fill10-pos3+piece.shape[1] ] += piece
                            h = 3
                            hand = False
                            last0 = piece
                            fill += int(max(np.where(self.emptyIm != 0)[0]))
                            fill1  = fill1  = int(min(np.where(self.emptyIm[:, fill10:fill10+piece.shape[1]] > 200)[0]))
#                            print('fill1', fill1)
                            if fill1 <= 350:
                                fill10 = int((max(np.where(self.emptyIm[:piece.shape[1]+5, :] != 0)[0])))

                                pos3 = 150
                                por2 = 40
                                check = 0
                                step1 = -1
#                                print('fill10', fill10, por)
                            self.pieces.remove(piece)
                            placcce.append(placcce.pop(0))
                            break
                    if sko > por2 and hand == True:
                        for piece in self.pieces:
                            blur = cv2.GaussianBlur(piece, (7,7),0)
                            mask = cv2.inRange(blur, 220, 255)
                            cv2.namedWindow('part', 0)
                            cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
                            I = [max(max(np.where(mask[:, 30+k] != 0))) for k in range(int(s-45))]
                            piece_l = [piece.shape[0] - u for u in I]
                            II = [min(min(np.where(self.emptyIm[:, fill10+30+k] != 0))) for k in range(int(s-45))]
                            last_l = II
                            d = np.array(last_l) + np.array(piece_l)
                            sko = np.std(d)
#                            print('sko', sko)
                            while (1):
                                cv2.imshow('part', mask)
                                k = cv2.waitKey(1) & 0xFF
                                if k == 121:        ##yes
                                    self.emptyIm[-piece.shape[0]+int(np.mean(d)-sko/1.5):int(np.mean(d)-sko/1.5), fill10-pos3:fill10-pos3+piece.shape[1] ] += piece
                                    h = 3
                                    last0 = piece
                                    fill += int(max(np.where(self.emptyIm != 0)[0]))
                                    fill1  = int(min(np.where(self.emptyIm[:, fill10:fill10+piece.shape[1]] > 200)[0]))
#                                    print('fill1', fill1)
                                    if fill1 <= 350:
                                        fill10 = int((max(np.where(self.emptyIm[:piece.shape[1]+5, :] != 0)[0])))
                                        pos1 = int(min(min(np.where(self.emptyIm[:, piece.shape[1]+5] != 0))))
                                        pos2 = int(max(max(np.where(self.emptyIm[pos1, :piece.shape[1]+5] != 0))))
                                        pos3 = 150
                                        por2 = 40
                                        check = 0
                                        step1 = -1
        #                                print('fill10', fill10, por)
                                    self.pieces.remove(piece)
                                    placcce.append(placcce.pop(0))
                                    break
                                elif k == 110:      ##no
#                                    cv2.destroyWindow('part')
                                    break
                            if k == 121:
                                break
                            elif k == 110:
                                h = 3
                                
                elif h == 3:
                    sizes = []
                    for piece in self.pieces:
                        sizes.append(piece.shape[1])
                    for piece in self.pieces:
                        blur = cv2.GaussianBlur(piece, (7,7),0)
                        mask = cv2.inRange(blur, 220, 255)
#                        cv2.namedWindow('part', 0)
#                        cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
#                        cv2.imshow('part', mask)
#                        cv2.waitKey(0)
#                        print('4')
                        s = min(sizes)
                        I = [max(max(np.where(mask[:, -40-k] != 0))) for k in range(50,int(s-60))]
                        piece_l = [piece.shape[0] - u for u in I]
                        II = [min(min(np.where(self.emptyIm[fill20: : step, -40-k] != 0))) for k in range(50,int(s-60))]
                        last_l = II
                        d = np.array(last_l) + np.array(piece_l)
                        sko = np.std(d)
#                        print('sko', sko)
                        if round(sko,0) <= por3 or (self.corner(piece) == 'Right' and round(sko,0) <= 80) or (self.corner(piece) == 'Top right' and round(sko,0) <= 42):
#                            print('sko',sko)
                            self.emptyIm[-piece.shape[0]+int(np.mean(d)+sko):int(np.mean(d)+sko), fill20-piece.shape[1]-30:fill20-30 ] += piece
                            h = 2
                            hand = False
                            last0 = piece
#                            fill = int(max(np.where(self.emptyIm != 0)[0]))
                            fill2  = int(min(np.where(self.emptyIm[:, -piece.shape[1]-1:-1] > 200)[0]))
#                            print('fill2', fill2)
                            if fill2 <=350:
#                                fill2 = int(min(min(np.where(self.emptyIm[:, -piece.shape[1]-10:-10] != 0))))
                                fill20 -= piece.shape[1]
#                                print('fill20', fill20)
                                step = -1
                            self.pieces.remove(piece)
                            placcce.append(placcce.pop(0))
                            break
                    if sko > por3 and hand == True:
                        for piece in self.pieces:
                                blur = cv2.GaussianBlur(piece, (7,7),0)
                                mask = cv2.inRange(blur, 180, 255)
                                cv2.namedWindow('part', 0)
                                cv2.resizeWindow('part', (ctypes.windll.user32.GetSystemMetrics(0)-700, ctypes.windll.user32.GetSystemMetrics(1)-200))
                                I = [max(max(np.where(mask[:, -40-k] != 0))) for k in range(50,int(s-60))]
                                piece_l = [piece.shape[0] - u for u in I]
                                II = [min(min(np.where(self.emptyIm[fill20: : step, -40-k] != 0))) for k in range(50,int(s-60))]
                                last_l = II
                                d = np.array(last_l) + np.array(piece_l)
                                sko = np.std(d)
#                                print('sko', sko)
                                while (1):
                                    cv2.imshow('part', mask)
                                    k = cv2.waitKey(1) & 0xFF
                                    if k == 121:        ##yes
                                        self.emptyIm[-piece.shape[0]+int(np.mean(d)-sko/2):int(np.mean(d)-sko/2), fill20-piece.shape[1]-50:fill20-50 ] += piece
                                        h = 2
                                        last0 = piece
            #                            fill = int(max(np.where(self.emptyIm != 0)[0]))
                                        fill2  = int(min(np.where(self.emptyIm[:, -piece.shape[1]-1:-1] > 200)[0]))
#                                        print('fill2', fill2)
                                        if fill2 <=350:
            #                                fill2 = int(min(min(np.where(self.emptyIm[:, -piece.shape[1]-10:-10] != 0))))
                                            fill20 -= piece.shape[1]
#                                            print('fill20', fill20)
                                            step = -1
                                        self.pieces.remove(piece)
                                        placcce.append(placcce.pop(0))
                                        break
                                    elif k == 110:      ##no
#                                        cv2.destroyWindow('part')
                                        break
                                if k == 121:
                                    break
                                elif k == 110:
                                    h = 2
                                    
                
                if np.array(np.where(self.emptyIm[450] == 0)).size <=90:
                    break
                t+=1
            if self.pieces and np.array(np.where(self.emptyIm[450] == 0)).size <=90:
                
                mask1 = cv2.inRange(self.emptyIm, 150, 255)
                I = list(np.where(mask1 != 0))
                [X1,Y1] = [min(I[0])+150, min(I[1])+150]
                [X2,Y2] = [max(I[0])-150, max(I[1])-150]
                self.emptyIm = self.emptyIm[X1:X2, Y1:Y2]
#                mask1 = cv2.inRange(self.emptyIm, 150, 255)
#                dil = cv2.dilate(mask1, cv2.getStructuringElement(cv2.MORPH_RECT,(105,105)), iterations = 1)
#                er = cv2.erode(dil, cv2.getStructuringElement(cv2.MORPH_RECT,(105,105)), iterations = 1)
                
                sizes = []
                while self.pieces:
                    cv2.imshow('Result', self.emptyIm)
                    cv2.waitKey(10)
                    for piece in self.pieces:
                        sizes.append(piece.shape[1])
    #                zero[-self.pieces[0].shape[0]-1:-1, :self.pieces[0].shape[1]] += self.pieces[0]
                    for piece in self.pieces:
                        s = min(sizes)
                        mask1 = cv2.inRange(self.emptyIm, 150, 255)
                        dil = cv2.dilate(mask1, cv2.getStructuringElement(cv2.MORPH_RECT,(85,85)), iterations = 1)
                        er = cv2.erode(dil, cv2.getStructuringElement(cv2.MORPH_RECT,(85,85)), iterations = 1)
#                        cv2.namedWindow('er', 0)
#                        cv2.imshow('er', er)
#                        cv2.waitKey(0)
                        er = 255 - er
#                        cv2.namedWindow('er', 0)
#                        cv2.imshow('er', er)
#                        cv2.waitKey(0)
                        i = (min(np.where(er==255)[1]))
                        i2 = (max(np.where(er==255)[1]))
                        ii = i2-i
                        I = [max(max(np.where(piece[:, k] != 0))) for k in range(int(ii-55))]
                        piece_l = [piece.shape[0] - u for u in I]
                        
#                        print(i, i2)
#                        print('s', s)
                        II = [max(max(np.where(er[:, i+k] == 255))) for k in range(int(ii-55))]
                        last_l = II
                        d = np.array(last_l) + np.array(piece_l)
                        sko = np.std(d)
                        
#                        print('skooo', sko)
#                        print (-piece.shape[0]+int(np.mean(d)-sko)-int(np.mean(d)-sko))
#                        print(i-i+piece.shape[1])
                        if sko <= 350:
                            self.emptyIm[-piece.shape[0]+int(np.mean(d)+sko/2):int(np.mean(d)+sko/2), i:i+piece.shape[1] ] += piece
                            self.pieces.remove(piece)
                            hand = False
                            break
                    if sko > 350 and hand:
                        for piece in self.pieces:
                    
                            mask1 = cv2.inRange(self.emptyIm, 150, 255)
                            dil = cv2.dilate(mask1, cv2.getStructuringElement(cv2.MORPH_RECT,(85,85)), iterations = 1)
                            er = cv2.erode(dil, cv2.getStructuringElement(cv2.MORPH_RECT,(85,85)), iterations = 1)
                            cv2.namedWindow('part', 0)
                            er = 255 - er
                            i = (min(np.where(er==255)[1]))
                            i2 = (max(np.where(er==255)[1]))
                            ii = i2-i
                            I = [max(max(np.where(piece[:, k] != 0))) for k in range(int(ii-55))]
                            piece_l = [piece.shape[0] - u for u in I]
                            II = [max(max(np.where(er[:, i+k] == 255))) for k in range(int(ii-55))]
                            last_l = II
                            d = np.array(last_l) + np.array(piece_l)
                            sko = np.std(d)
                            while (1):
                                cv2.imshow('part', piece)
                                k = cv2.waitKey(1) & 0xFF
                                if k == 121:        ##yes
                                    self.emptyIm[-piece.shape[0]+int(np.mean(d)+sko/2):int(np.mean(d)+sko/2), i:i+piece.shape[1] ] += piece
                                    self.pieces.remove(piece)
                                    break
                                elif k == 110:      ##no
                                    break
                            if k == 121:
                                    break
                       
            return self.emptyIm
    
                
                        
                        
                    