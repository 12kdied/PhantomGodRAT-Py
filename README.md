#PhantomGod RAT

Description
PhantomGod RAT is an open-source project that functions as a Remote Access Trojan developed in Python. This code allows you to control and gather information from a remote system through commands sent from a Telegram server.

Prerequisites
Python 3.x
Python libraries: telebot, requests, psutil, pyautogui, opencv-python, pyaudio, keyboard, pillow, pywin32, numpy, zipfile36, pycryptodome, python-telegram-bot
Configuration
Before using PhantomGod, follow these steps to set up the project:

Open the main.py file.

Configure the Telegram token and target chat ID on the following lines:

python
Copy code
token = 'YOUR_TOKEN_HERE'  # Replace 'YOUR_TOKEN_HERE' with your Telegram token
id_chat = 'YOUR_CHAT_ID_HERE'  # Replace 'YOUR_CHAT_ID_HERE' with the target chat ID
Ensure that all required libraries are installed using the following command:

bash
Copy code
pip install -r requirements.txt
Telegram Commands
PhantomGod RAT is controlled through commands sent from a Telegram server. Here are some of the available commands:

/help: Display the list of available commands.
/start: Start PhantomGod RAT.
/owner: Show information about the project's founder.
/readme: Display the project's README file.
/update: Update the bot with a new version (you need to provide the download link).
/restart_program: Restart the PhantomGod program.
/screenshot: Capture a screenshot of the desktop.
/info: Display information about the target system.
/webcam: Capture a photo from the target's webcam.
/videocam <duration>: Record a video from the webcam for the specified duration (in seconds).
/microphone <duration>: Record audio from the microphone for the specified duration (in seconds).
/shut_down: Shut down the target system.
/terminal <command>: Execute a command in the target system's terminal.
/msgbox <message>: Display a message box on the target system with the provided message.
/download <URL>: Download a file in the background from the specified URL.
/keylogger: Start the keylogger to record pressed keys.
/keylogger_stop: Stop the keylogger.
/record_screen <duration>: Record the screen for the specified duration (in seconds).
/passwords: Retrieve stored passwords from web browsers.
/desktop <name> <content> <num_files>: Create files on the target system's desktop.
/task: List active processes on the target system.
/task_stop <name>: Stop a specific process on the target system.
Important Notes
This project is in a testing and development phase. Use it responsibly and in accordance with local laws.
The project is open-source, and any attempt to edit or impersonate the creator may have legal consequences.
It is recommended to have only one bot per victim, as receiving multiple victims can cause issues.
Ensure that PhantomGod is up-to-date to take advantage of the latest features and security fixes.
Versions
Current Version: 0.1.0
Credits
Developed by the PhantomGod team.
License
This project is licensed under the MIT License.

Thank you for using PhantomGod RAT! If you have any questions or suggestions, feel free to contact us.

