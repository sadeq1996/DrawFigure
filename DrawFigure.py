ask= input("ٌWich figurer do you want draw: ? (1:rectangle | 2:circle):  ")

def draw(event,x,y,flags, param):
    
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
            if ask== "1":
            
                cv2.rectangle(img2,(x-50, y-50),(x+50,y +50),(0,0,255),3)
                
            elif  ask== "2":
                cv2.circle(img2,(x,y),30,(0,255,0),4)
            
            
img2= np.zeros((512,512,3),np.uint8)
cv2.namedWindow("draw")
cv2.setMouseCallback('draw',draw)
while(1):
    cv2.imshow('draw',img2)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()