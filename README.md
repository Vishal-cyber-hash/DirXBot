# Jarvis Assistant Project

## Overview
This project is a voice-controlled assistant, which integrates multiple features to offer users the ability to control their system, make calls, browse websites, and more. The system uses a combination of technologies such as Python, ADB (Android Debug Bridge), and web-based interfaces. The assistant is designed to function on both Android and PC platforms, utilizing voice recognition, face authentication, and system commands.

## Team Members
- **Vishal Paswan** - Team Leader
- **Jatin Megani** - UI/UX Designer
- **Vivek** - Software Developer
## Features:
- **Voice Control**: Uses voice commands to perform various actions like opening websites, making calls, sending messages, etc.
- **Face Authentication**: Verifies the user's identity using facial recognition before granting access.
- **Web Browsing**: Accesses and opens predefined websites from a CSV file.
- **System Commands**: Executes system-level commands such as opening applications or running scripts.
- **Contact Management**: Allows storing and managing contacts for sending messages and making calls.
- **Face Authentication**: Uses facial recognition for secure login.
- **Voice Commands**: Allows control over various system and web functions through voice commands.
- **System Commands**: Executes system commands and manipulates files and processes.
- **Web Interaction**: Automates interaction with websites like Google, YouTube, and Facebook.
- **Hotword Activation**: The assistant is always listening for the designated hotword to activate.


## Tools & Technologies:
- **Python**: Main programming language for backend functionalities.
- **ADB**: For connecting and controlling Android devices through Wi-Fi.
- **SQLite**: For storing and managing data such as contacts and commands.
- **Speech Recognition**: Converts speech into text for command execution.
- **pyttsx3**: Text-to-speech engine for feedback.
- **Eel**: A Python library to create web-based GUIs using HTML, CSS, and JavaScript.

## Files and Structure:
1. **Main Code**: Contains the main logic for starting the assistant, recognizing speech, and executing commands.
2. **Database (jarvis.db)**: Stores system commands, web commands, and contact information.
3. **CSV Files**: Used for storing the list of websites that can be accessed by the assistant.
4. **Batch Scripts**: Used for managing Android device connections over Wi-Fi.
5. **Web Interface (HTML/JS)**: A local web page for interacting with the assistant.

## Key Features of the Program:
- **Multi-Process Support**: Uses Python's multiprocessing to handle multiple tasks simultaneously (e.g., listening for hotwords and starting the assistant).
- **Hotword Detection**: Listens for specific commands (e.g., "Jarvis") to trigger the assistant.
- **Android Control**: Using ADB commands to perform tasks such as simulating key presses, taps, and input on an Android device.
- **Web-based UI**: Provides an interface for users to interact with the assistant.

## Achievements:
- **Hackathon Winner**: Vishal Paswan won the Hackathon in college with this program.

## Libraries Used:
- **eel**: A Python library for creating desktop web applications.
- **pyttsx3**: Text-to-speech conversion library.
- **speech_recognition**: Library for speech-to-text functionality.
- **sqlite3**: Database library for managing contacts and commands.
- **os**: Provides functions to interact with the operating system (e.g., execute commands, manipulate files).
- **multiprocessing**: Enables concurrent execution of tasks.
- **re**: Regular expression library used for extracting specific parts from commands.
- **time**: Provides time-related functions like sleeping between actions.

## Installation Requirements:
To run this project, you need to install the following libraries:



## Future Enhancements:
- Integration with more AI services for better voice recognition.
- Support for more system commands and interactions.
- Cloud synchronization for contacts and commands.
- Mobile app version of the assistant.

# Steps to Run the Program

## Step 1: Install Libraries

First, ensure that all necessary libraries are installed using the `requirements.txt` file. You can do this by running the following command in your terminal or command prompt:

1. **Navigate to your project directory** (where `requirements.txt` is located).
2. Run the following command:
   ```bash
   pip install -r requirements.txt

   python run.py


   
# Project Overview

This project was developed by **Vishal Paswan**, **Jatin Megani**, and **Vivek**. The objective was to build a voice assistant with various features.

## PowerPoint Presentation

You can view or download the PowerPoint presentation below:
<iframe src="[https://www.example.com/file.pdf](https://docs.google.com/presentation/d/1Yr9gHBQWnkiPxccAvg3sJipEmjzHjSV1pRm9GPUVz5E/edit?usp=sharing)" width="600" height="400"></iframe>


# My Project Overview
##logo
![Screenshot 1](www/assets/images/pngegg.ico)

## Screenshot 1
![Screenshot 1](www/assets/images/Screenshot%202024-11-10%20152235.png)

## Screenshot 2
![Screenshot 2](www/assets/images/Screenshot%202024-11-10%20152015.png)

## Final Version
![Final Version](www/assets/images/Screenshot%202024-11-10%20151947.png)





