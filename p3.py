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
        self.flag = 0
        self.last_f = 0
        self.start = 0
        self.flag2 = False
        self.a = 0
        self.c = 0
    def Hands(self):
        _, img = cap.read()
        self.hands, img = detector.findHands(img)
        if len(self.hands) == 0:
            self.flag = 0
        else:
            _, _, self.x2, self.y2 = self.hands[0]["bbox"]
            self.x, self.y = self.hands[0]["center"]
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
            
                
            if self.fingers == [0,0,0,0,0] or self.fingers == [1,0,0,0,0] or self.fingers == [0,1,0,0,0] or self.fingers == [1,1,0,0,0]: 
                if self.flag == 0:
                    self.a1 = self.a
                    self.c1 = self.c
                    self.flag+=1
                
                                
                if self.fingers == [0,1,0,0,0] or self.fingers == [1,1,0,0,0]:
                    self.y = self.y + abs(self.x2-self.y2)/4
                    if self.last_f != self.fingers:
                        self.start = time.time()
                        mouse.press(button='left')
                        self.flag2 = True
                        
                else:
                    
                    if self.flag2 == True: 
                        elapsed = time.time() - self.start 
                        
                        if elapsed < 0.5 : 
                            mouse.click(button='left')
                          
                    mouse.release(button='left') 
                    self.flag2 = False    
            else:
                mouse.release(button='left')
                self.flag = 0
            self.last_f = self.fingers
        
    def control(self):
        try:
            if self.flag == 1:
                
                x_new = (self.x - self.a1[0]) * (1920 / self.c1[0])
                y_new = (self.y - self.a1[1]) * (1080 / self.c1[1])
                
                mouse.move(1920-x_new, y_new, absolute=True) 
                
                
                        
        except:
            pass
    

main = Program()
while True:
    
    main.Hands()
    main.usloviay()
    main.upsempling()
    main.control()


    
