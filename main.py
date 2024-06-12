import tkinter as tk
from tkinter import messagebox
import threading
import cv2
import mediapipe as mp
import pyautogui
import json
import fastdtw

# Function to run the virtual mouse application
def virtual_mouse_application():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()

    index_y = 0

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y

                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                        if abs(index_y - thumb_y) < 20:
                            pyautogui.click()
                            pyautogui.sleep(1)
                        elif abs(index_y - thumb_y) < 100:
                            pyautogui.moveTo(index_x, index_y)
        cv2.imshow('Virtual Mouse', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ##cut
    # Set threads
    show_camera_feed_thread = threading.Thread(target=show_camera_feed)
    handle_user_input_thread = threading.Thread(target=handle_user_input)

    # Start the threads
    show_camera_feed_thread.start()
    handle_user_input_thread.start()

    # Join the threads to the main thread
    show_camera_feed_thread.join()
    handle_user_input_thread.join()

def sinhala_sign_language_translator_application():
    # A class to recognize gestures
    class GestureRecognizer:
        def init(self, detection_confidence, tracking_confidence):
            # Define the mediapipe utilities for hands and drawing utilities
            self.mediapipe_hands = mp.solutions.hands
            self.mediapipe_draw = mp.solutions.drawing_utils
            # Define a single mediapipe hand and provide the detection and tracking confidence specified
            self.hands = self.mediapipe_hands.Hands(max_num_hands=1, min_detection_confidence=detection_confidence,
                                                    min_tracking_confidence=tracking_confidence)

        # Process the hands in an image
        def process_hands_from_image(self, image):
            # Convert the image to RGB format so that the hands can be processed
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Process the hands and get the landmarks
            processed_hands = self.hands.process(image_rgb).multi_hand_landmarks
            return processed_hands

        def get_hand_landmarks_from_image(self, image):
            # Process the hands from the image
            processed_hands = self.process_hands_from_image(image)
            # A list of the hand landmarks
            hand_landmarks = []
            # Check if any hands were actually in the image
            if processed_hands:
                # Get the landmarks of the first processed hand
                processed_hand = processed_hands[0]
                # The values to center the x and y coordinates
                x_to_center = None
                y_to_center = None
                # Loop through each landmark in the hand
                for index, landmark in enumerate(processed_hand.landmark):
                    # Get the height and width of the image
                    height, width, _ = image.shape
                    # Get the center points of the image
                    center_x = width / 2
                    center_y = height / 2
                    # Convert the floating point landmark positions into pixel values
                    x_pos = int(landmark.x * width)
                    y_pos = int(landmark.y * height)
                    # Check if this is the first landmark of the hand
                    if index == 0:
                        # Determine the values needed to center the x and y positions of the landmark
                        x_to_center = center_x - x_pos
                        y_to_center = center_y - y_pos
                    # Apply the centering values to the x and y positions of each landmark
                    x_pos += x_to_center
                    y_pos += y_to_center
                    # Add the pixel landmark positions to the list of landmarks
                    hand_landmarks.append([x_pos, y_pos])
            return hand_landmarks

        # Draw the landmarks and hand connections on an image
        def draw_hands_on_image(self, image):
            # Process the hands from the image
            processed_hands = self.process_hands_from_image(image)
            # Check if any hands were actually in the image
            if processed_hands:
                # Get the landmarks of the first processed hand
                processed_hand = processed_hands[0]
                # Draw the landmarks on the hand
                self.mediapipe_draw.draw_landmarks(image, processed_hand, self.mediapipe_hands.HAND_CONNECTIONS)
            return image



      
                                                                                  TRAINING_DATA_FILE_PATH)
                    if match == "a":
                        print("Match: මම")
                        print(f"Message: {message}")
                    elif match == "One":
                        print("Match: ඔබට")
                        print(f"Message: {message}")
                    elif match == "Two":
                        print("Match: මට")
                        print(f"Message: {message}")
                    elif match == "b":
                        print("Match: ආයුබෝවන්")
                        print(f"Message: {message}")
                    elif match == "c":
                        print("Match: ස්තූතියි")
                        print(f"Message: {message}")
                    elif match == "d":
                        print("Match: බඩගිනියි")
                        print(f"Message: {message}")
                    elif match == "e":
                        print("Match: කොහොමද")
                        print(f"Message: {message}")
                    elif match == "f":
                        print("Match: හොදින්")
                        print(f"Message: {message}")
                    elif match == "g":
                        print("Match: එහෙමද")
                        print(f"Message: {message}")
                    elif match == "h":
                        print("Match: ඔව්")
                        print(f"Message: {message}")
                    elif match == "i":
                        print("Match: නෑ")
                        print(f"Message: {message}")
                    elif match == "j":
                        print("Match: එපා")
                        print(f"Message: {message}")
                    elif match == "k":
                        print("Match: ඕනේ")
                        print(f"Message: {message}")
                    elif match == "l":
                        print("Match: එල")
                        print(f"Message: {message}")
                    elif match == "m":
                        print("Match: තිබහයි")
                        print(f"Message: {message}")
                    elif match == "n":
                        print("Match: ඇයි")
                        print(f"Message: {message}")
                    elif match == "o":
                        print("Match: බෑ")
                        print(f"Message: {message}")
                    elif match == "p":
                        print("Match: ගියා")
                        print(f"Message: {message}")
                    elif match == "q":
                        print("Match: කනවා")
                        print(f"Message: {message}")
                    elif match == "q":
                        print("Match: කනවා")
                        print(f"Message: {message}")
                    elif match == "r":
                        print("Match: හා")
                        print(f"Message: {message}")
                    elif match == "s":
                        print("Match: එනවා")
                        print(f"Message: {message}")
                    elif match == "t":
                        print("Match: බොනවා")
                        print(f"Message: {message}")
                    elif match == "u":
                        print("Match: කියන්න")
                        print(f"Message: {message}")
                    elif match == "v":
                        print("Match: අයියෝ")
                        print(f"Message: {message}")
                    elif match == "w":
                        print("Match: සුපිරි")
                        print(f"Message: {message}")
                    elif match == "x":
                        print("Match: ගැම්මක්")
                        print(f"Message: {message}")
                    elif match == "y":
                        print("Match: කොහෙද")
                        print(f"Message: {message}")
                    elif match == "z":
                        print("Match: අපි")
                        print(f"Message: {message}")
                    elif match == "aa":
                        print("Match: පැන්සල")
                        print(f"Message: {message}")
                    elif match == "ab":
                        print("Match: කීයද")
                        print(f"Message: {message}")
                    elif match == "ac":
                        print("Match: සමාවෙන්න")
                        print(f"Message: {message}")
                    elif match == "ad":
                        print("Match: මොකද්ද")
                        print(f"Message: {message}")
                    elif match == "ae":
                        print("Match: හදිස්සි")
                        print(f"Message: {message}")
                    elif match == "af":
                        print("Match: සල්ලි")
                        print(f"Message: {message}")
                    elif match == "ag":
                        print("Match: ආදරෙයි")
                        print(f"Message: {message}")
                    elif match == "ah":
                        print("Match: ගස්")
                        print(f"Message: {message}")
                    elif match == "ai":
                        print("Match: පෑන")
                        print(f"Message: {message}")
                    elif match == "aj":
                        print("Match: පාසල")
                        print(f"Message: {message}")
                    elif match == "ak":
                        print("Match: විශ්වවිද්‍යාලය")
                        print(f"Message: {message}")
                    elif match == "al":
                        print("Match: ගල")
                        print(f"Message: {message}")
                    elif match == "am":
                        print("Match: අම්මා ")
                        print(f"Message: {message}")
                    elif match == "an":
                        print("Match: තාත්තා")
                        print(f"Message: {message}")
                    elif match == "ao":
                        print("Match: අයියා")
                        print(f"Message: {message}")
                    elif match == "ap":
                        print("Match: අක්කා")
                        print(f"Message: {message}")
                    elif match == "aq":
                        print("Match: කම්මැලී")
                        print(f"Message: {message}")
                    elif match == "ar":
                        print("Match: තියනවා")
                        print(f"Message: {message}")
                    elif match == "as":
                        print("Match: යාලුවෝ")
                        print(f"Message: {message}")
                    elif match == "at":
                        print("Match: ගින්දර")
                        print(f"Message: {message}")
                    elif match == "au":
                        print("Match: දුවනවා")
                        print(f"Message: {message}")
                    elif match == "av":
                        print("Match: කාමරය")
                        print(f"Message: {message}")
                    elif match == "aw":
                        print("Match: ඔහුට")
                        print(f"Message: {message}")
                    elif match == "ax":
                        print("Match: උඩට")
                        print(f"Message: {message}")
                    elif match == "ay":
                        print("Match: වැස්ස")
                        print(f"Message: {message}")
                    elif match == "az":
                        print("Match: පියබා")
                        print(f"Message: {message}")
                    elif match == "ba":
                        print("Match: මල්")
                        print(f"Message: {message}")
                    elif match == "bb":
                        print("Match: තුවක්කුව")
                        print(f"Message: {message}")
                    elif match == "bc":
                        print("Match: පොඩි")
                        print(f"Message: {message}")
                    else:
                        print(f"Match: {match}")
                        print(f"Message: {message}")
                # If a name was provided, save the gesture to the training file
                else:
                    gesture_recognizer.save_image_as_training_data(captured_image, gesture_name,
                                                                   TRAINING_DATA_FILE_PATH)
                    print("The data was successfully registered.")
    # Set threads
    show_camera_feed_thread = threading.Thread(target=show_camera_feed)
    handle_user_input_thread = threading.Thread(target=handle_user_input)

    # Start the threads
    show_camera_feed_thread.start()
    handle_user_input_thread.start()

    # Join the threads to the main thread
    show_camera_feed_thread.join()
    handle_user_input_thread.join()

# Function to run the main.py file of Virtual Mouse application
def run_virtual_mouse():
    try:
        # Run the virtual mouse application in a separate thread
        threading.Thread(target=virtual_mouse_application).start()
        root.destroy()  # Close the Tkinter window
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Virtual Mouse application:\n{e}")

def run_sinhala_sign_language_translator():
    try:
        threading.Thread(target=sinhala_sign_language_translator_application).start()
        root.destroy()  # Close the Tkinter window
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Sinhala Sign Language Translator application:\n{e}")
     
# Create the main window
root = tk.Tk()
root.title("SignSense")
root.attributes("-fullscreen", True)  # Fullscreen mode

# Set the background image
background_image = tk.PhotoImage(file="Img/WhatsApp Image 2024-06-09 at 00.53.16_d336f6db.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame for the text and buttons
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Title
title = tk.Label(frame, text="Gesture Recognition System", font=("Helvetica", 22, "bold"), bg="white")
title.grid(row=0, column=0, columnspan=2, pady=20)
    
# Sinhala Sign Language Translator
ssl_label = tk.Label(frame, text="Sinhala Sign Language Translator", font=("Helvetica", 24), bg="white")
ssl_label.grid(row=2, column=0, pady=10, padx=10)
ssl_button = tk.Button(frame, text="Run", command=run_sinhala_sign_language_translator, font=("Helvetica", 24), bg="black", fg="white")
ssl_button.grid(row=2, column=1, pady=10, padx=10)

# Virtual Mouse
vm_label = tk.Label(frame, text="Virtual Mouse", font=("Helvetica", 24), bg="white")
vm_label.grid(row=1, column=0, pady=10, padx=10)
vm_button = tk.Button(frame, text="Run", command=run_virtual_mouse, font=("Helvetica", 24), bg="black", fg="white")
vm_button.grid(row=1, column=1, pady=10, padx=10)

# Start the main loop
root.mainloop()