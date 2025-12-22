## Virtual Mouse Using Hand Gestures (Python)

A computer vision–based Virtual Mouse that enables hands-free control of the system cursor using real-time hand gestures captured through a webcam.
The project leverages MediaPipe Hand Tracking and PyAutoGUI to replace traditional mouse input.

## ✨ Key Features

Real-time hand landmark detection

Cursor movement via index finger tracking

Pinch gesture (index + thumb) for left-click

Smooth and stable cursor motion

Touch-free and hardware-independent solution

## 🧰 Tech Stack

Python 3.11

OpenCV – Video capture & processing

MediaPipe – Hand landmark detection

PyAutoGUI – Mouse control

## 📁 Project Structure
VirtualMouseai/
├── virtual_mouse.py
├── README.md
├── .venv/
└── .idea/

## ⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/shreyanshpatel302623/VirtualMouse.git
cd virtual-mouse-python

2. Create Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install opencv-python mediapipe pyautogui

## 🔐 Required macOS Permissions

Mandatory for proper execution

Camera Access
System Settings → Privacy & Security → Camera → Allow Terminal / PyCharm

Accessibility Access
System Settings → Privacy & Security → Accessibility → Allow Terminal / PyCharm

## ▶️ Run the Application
python virtual_mouse.py

Gesture Controls
Gesture	Action
Index finger movement	Cursor movement
Index + Thumb pinch	Left click
ESC key	Exit program
## 🧠 Working Principle

Webcam captures live video frames

MediaPipe detects 21 hand landmarks

Index finger coordinates are mapped to screen resolution

Cursor position is updated in real time

Pinch gesture triggers mouse click event

## 🎯 Use Cases

Touchless human-computer interaction

Assistive technology

AI & Computer Vision learning projects

Gesture-controlled interfaces

## 🚀 Future Enhancements

Right-click & scroll gestures

Drag-and-drop support

GUI toggle for enable/disable

Accuracy improvements with advanced filtering

## 👤 Author

Shreyansh Patel

