# 👋 Hand Gesture Keyboard Controller

A Python-based computer vision project that allows you to control keyboard inputs using hand gestures captured through your webcam.just for fun and learning!😉

## ✨ Features

- 🎥 Real-time hand tracking using MediaPipe
- 👆 Detects open and closed hand positions
- ⌨️ Controls left and right arrow keys based on hand gestures
- 🤚 Supports both left and right hand detection

## 🛠️ Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- pynput

## 📦 Installation

```bash
pip install opencv-python
pip install mediapipe
pip install pynput
```

## 🚀 Usage

1. Run the script:
```bash
python main.py
```

2. Position yourself in front of the webcam
3. Use hand gestures to control:
   - 👉 Close right hand to press right arrow key
   - 👈 Close left hand to press left arrow key
   - ✋ Open hands to release keys

4. Press `ESC` to exit the program

## 🎮 How It Works

The program uses MediaPipe's hand tracking to:
1. Detect hand landmarks in real-time (plot 21-points on hand)
2. Determine if each hand is open or closed based on finger positions
3. Trigger keyboard events accordingly:
   - Closed hand = Key press
   - Open hand = Key release


## 🤝 Contributing

Fell free to Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if you like this project!😉