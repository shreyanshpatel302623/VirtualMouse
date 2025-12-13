import cv2
import mediapipe as mp
import pyautogui
import time
import math
SMOOTHING = 7
CLICK_DISTANCE_PX = 40
CLICK_COOLDOWN = 0.6
CAM_INDEX = 0
MIRROR_X = False
DEBUG_PRINT_EVERY_SEC = 2.0
cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open camera index {CAM_INDEX}")
hand_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0.0, 0.0
last_click_time = 0.0
_last_debug = 0.0
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame.")
            break
        frame = cv2.flip(frame, 1)
        frame_h, frame_w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand_detector.process(rgb)
        hands = results.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(
                    frame, hand, mp.solutions.hands.HAND_CONNECTIONS
                )
                lmks = hand.landmark
                index_x = index_y = thumb_x = thumb_y = None
                for idx, lm in enumerate(lmks):
                    px = int(lm.x * frame_w)
                    py = int(lm.y * frame_h)
                    if idx == 8:
                        cv2.circle(frame, (px, py), 8, (0, 255, 255), cv2.FILLED)
                        mapped_x = lm.x * screen_width
                        if MIRROR_X:
                            mapped_x = screen_width - mapped_x
                        index_x = mapped_x
                        index_y = lm.y * screen_height
                    if idx == 4:
                        cv2.circle(frame, (px, py), 8, (0, 255, 255), cv2.FILLED)
                        t_x = lm.x * screen_width
                        if MIRROR_X:
                            t_x = screen_width - t_x
                        thumb_x = t_x
                        thumb_y = lm.y * screen_height
                if index_x is not None and index_y is not None:
                    cur_x = prev_x + (index_x - prev_x) / SMOOTHING
                    cur_y = prev_y + (index_y - prev_y) / SMOOTHING
                    prev_x, prev_y = cur_x, cur_y
                    tgt_x = int(max(0, min(screen_width - 1, round(cur_x))))
                    tgt_y = int(max(0, min(screen_height - 1, round(cur_y))))
                    if time.time() - _last_debug > DEBUG_PRINT_EVERY_SEC:
                        print(f"[DEBUG] X={tgt_x}, Y={tgt_y}")
                        _last_debug = time.time()
                    try:
                        pyautogui.moveTo(tgt_x, tgt_y, _pause=False)
                    except Exception as e:
                        print("Move error:", e)
                if index_x is not None and thumb_x is not None:
                    dist = math.hypot(index_x - thumb_x, index_y - thumb_y)
                    if dist < CLICK_DISTANCE_PX:
                        now = time.time()
                        if now - last_click_time > CLICK_COOLDOWN:
                            pyautogui.click()
                            last_click_time = now
        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    hand_detector.close()