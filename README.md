# hand-gesture-recognition-system

This repository contains the following contents.
* Virtual mouse application
* Sinhala sign language recognition application
* English sign language recognition application
* Learning manage a dataset to train a model.(using roboflow)
* Learning data for finger gesture recognition and notebook for learning
* Learning how to enter custom dataset for hand gesture recognition.

# Requirements
* mediapipe 0.8.1
* OpenCV 3.4.2 or Later
* tkinter 3.9.19
* threading  4.2.0
* pyautogui 0.9.54
* json 2.7. 2
* fastdtw 0.3.4

# Installation process
* First extract all the file to your local machine.
* Install all the requirements from the list.
* For virtual_mouse and sinhala_sign_language application, you need to run main.py.

dataset :- Signs

* For english_sign_laguage application you need to train "english_sign_language_translator/Train_YOLONAS_Custom_Dataset_Sign_Language_Complete.ipynb" model using google colab and embed the ckpt_best.path file created in that model to the directory english_sign_language_translator/model_weights and copy the absolute path to english_sign_language_translator/main.py.

dataset :- https://public.roboflow.com/object-detection/american-sign-language-letters

# Directory
<pre>
├─main.py
│    
├─requirements.txt
│  
├─english_sign_language_translator
│  ├─Train_YOLONAS_Custom_Dataset_Sign_Language_Complete.ipynb
│  │_requirements.txt          
│  └─main.py
│          
├─sinhala_sign_language_translator
  ├─data.json
</pre>
