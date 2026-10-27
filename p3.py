import cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import time
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.6, maxHands= 1)


class Program():
    def __init__(self):
        self.flag = None
        self.last_f = None
        self.sx = None
        self.sy = None
        self.mouse_up_down = None
        
    def Hands(self):
        _, img = cap.read()
        self.hands, img = detector.findHands(img)
        if len(self.hands) == 0:
            self.flag = 0
        else:
            
            _, _, self.x2, self.y2 = self.hands[0]["bbox"]
            self.x, self.y = self.hands[0]["lmList"][0][0:2]
            hand1 = self.hands[0]
            self.fingers = detector.fingersUp(hand1)
            
            
            
            
            
    def upsempling(self):
        if len(self.hands) != 0:
            
            
            h = 9 * (self.x2* self.y2/864)
            w = 16 * (self.x2* self.y2/864)
                    
            if w < 480 and h < 270:
                w = 480
                h = 270
            
                    
            self.a = (int(self.x-(w/2)),int(self.y-(h/2)))
            
            self.c = (int(w),int(h))   
                
        
    def usloviay(self):
        if len(self.hands) != 0:
            
                
            if self.fingers in ([0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[1,1,0,0,0]):
                if self.flag == 0:
                    self.a1 = self.a
                    self.c1 = self.c
                    self.flag+=1



                if self.fingers == [0,1,0,0,0] or self.fingers == [1,1,0,0,0]:
                    
                    if self.last_f != self.fingers:
                        mouse.click(button='left')
                        self.start = time.time()
                                        
                    if time.time() - self.start > 0.3:
                        if self.last_time <= 0.3:                     
                            mouse.press(button='left')
                            self.mouse_up_down = True
                    self.last_time = time.time() - self.start
                                
                
                                   
                else:
                    if self.mouse_up_down:
                        self.mouse_up_down = False   
                        mouse.release(button='left') 
                        
            else:
                
                self.flag = 0
            self.last_f = self.fingers
        
    def control(self):
        
        if self.flag == 1:
                
            x_new = (self.x - self.a1[0]) * (1920 / self.c1[0])
            y_new = (self.y - self.a1[1]) * (1080 / self.c1[1])
            if self.sx is None:
                self.sx = x_new
                self.sy = y_new
            else:
                self.sx = 0.5 * x_new + 0.5 * self.sx
                self.sy = 0.5 * y_new + 0.5 * self.sy
            mouse.move(1920 - self.sx, self.sy, absolute=True)
                            
                
                        
       

main = Program()
while True:
    
    main.Hands()
    main.upsempling()
    main.usloviay()
    
    main.control()








    
