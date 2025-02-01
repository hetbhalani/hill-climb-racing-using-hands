import cv2 as cv
from pynput.keyboard import Controller, Key
import mediapipe as mp

#initialize hands
mpHands = mp.solutions.hands 
mpDraw = mp.solutions.drawing_utils

# 50% confidence hovo joye
hands = mpHands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5)
Keyboard = Controller()

def isOpenHand(landmarks,hand_type):
    fingers = [] #ek list banavi for fingers detaction
    
    if hand_type == 'Right':
        fingers.append(landmarks[4].x > landmarks[3].x)
        #jo right hand no thumb open hse to aa true thse
    else:
        fingers.append(landmarks[4].x < landmarks[3].x) #for left
        
    for tip in [8,12,16,20]: #aa badha tips number 6
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y) #true if hand is open

    return sum(fingers) >= 4 #jo 4 finger khuli hoi to open

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 240) 
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

right_hand_close = False
left_hand_close = False

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    
    frame = cv.flip(frame,1)
    rgb_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
    result = hands.process(rgb_frame)
    # print(result.multi_hand_landmarks)
    
    #jo ek pn hand detact thai to if ma jai
    if result.multi_hand_landmarks and result.multi_handedness:
    
        #idx -> 0= first hand, 1= second hand
        #hand_landmarks = coordinates [x,y,z]
        for idx,hand_landmarks in enumerate(result.multi_hand_landmarks):
            #hand is left or right check kre
            hand_type = result.multi_handedness[idx].classification[0].label
            #hand pr lines banave
            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            if isOpenHand(hand_landmarks.landmark,hand_type):
                if hand_type == 'Right' and right_hand_close:
                    print("right open")
                    Keyboard.release(Key.right)
                    right_hand_close = False
                elif hand_type == 'Left' and left_hand_close:
                    print("left open")
                    Keyboard.release(Key.left)
                    left_hand_close = False
            else:
                if hand_type == 'Right' and not right_hand_close:
                    print("right close")
                    Keyboard.press(Key.right)
                    right_hand_close = True
                elif hand_type == 'Left' and not left_hand_close:
                    print("left close")
                    Keyboard.press(Key.left)
                    left_hand_close = True
                    
    cv.imshow("hand gesture",frame)

    if cv.waitKey(1) & 0xFF == 27: #27 is ascii for esc
        break

#badha resources relese krva mate
cap.release()
cv.destroyAllWindows()