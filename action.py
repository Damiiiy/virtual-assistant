
# # import weather


# # import datetime
# # import webbrowser
# # import os
# # import time
# # import queue
# # import re
# # import pyttsx3
# # from threading import Thread, Event

# # # Initialize the TTS engine
# # engine = pyttsx3.init()
# # tts_queue = queue.Queue()

# # # Function to process TTS requests
# # def process_tts():
# #     while True:
# #         text = tts_queue.get()  # Wait for a new text to be added
# #         if text is None:  # Stop signal
# #             break
# #         engine.say(text)
# #         engine.runAndWait()

# # # Start the TTS processing thread
# # tts_thread = Thread(target=process_tts)
# # tts_thread.start()

# # # Dictionary to hold appointments and reminders
# # tasks = {
# #     'appointments': [],
# #     'reminders': []
# # }

# # # Function to add a task
# # def add_task(task_type, task_info):
# #     tasks.setdefault(task_type, []).append(task_info)
# #     return f"{task_type.capitalize()} added successfully!"

# # # Function to set a reminder
# # def set_reminder(reminder_time, message):
# #     tasks['reminders'].append({'time': reminder_time, 'message': message})
# #     return "Reminder set!"

# # # Function to check for due appointments and reminders
# # def check_due_tasks(stop_event):
# #     while not stop_event.is_set():
# #         current_time = datetime.datetime.now().replace(second=0, microsecond=0)  # Only check minute accuracy
        
# #         # Check for appointments
# #         for appointment in tasks['appointments'][:]:  # Iterate over a copy of the list
# #             if appointment['time'] == current_time:  # Exact match for appointment time
# #                 tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
# #                 tasks['appointments'].remove(appointment)  # Remove after notifying

# #         # Check for reminders
# #         for reminder in tasks['reminders'][:]:  # Iterate over a copy of the list
# #             if reminder['time'] == current_time:  # Exact match for reminder time
# #                 tts_queue.put(reminder['message'])
# #                 tasks['reminders'].remove(reminder)  # Remove after notifying

# #         time.sleep(1)  # Check every second

# # # Start the background thread to check for due tasks
# # stop_event = Event()
# # task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
# # task_checker_thread.start()

# # # Function to parse and schedule an appointment from user input in 24-hour format
# # def schedule_appointment(data_btn):
# #     try:
# #         time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
# #         appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info
# #         appointment_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
        
# #         # Adjust appointment time to today if it's not already in the future
# #         now = datetime.datetime.now()
# #         appointment_time = appointment_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)

# #         if appointment_time < now:
# #             appointment_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed

# #         return add_task('appointments', {'time': appointment_time, 'info': appointment_info})
# #     except ValueError:
# #         return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# # # Function to parse and set a reminder from user input in 24-hour format
# # def set_reminder_from_input(data_btn):
# #     try:
# #         # Extract time part in 24-hour format
# #         time_part = re.search(r'\b\d{1,2}:\d{2}\b', data_btn).group()  # Matches 'HH:MM'
# #         message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message
# #         reminder_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
        
# #         # Adjust reminder time to today if it's not already in the future
# #         now = datetime.datetime.now()
# #         reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)

# #         if reminder_time < now:
# #             reminder_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed

# #         return set_reminder(reminder_time, message)
# #     except (ValueError, AttributeError):
# #         return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# # # Function to clean up resources on exit
# # def cleanup():
# #     tts_queue.put(None)  # Signal to stop the TTS thread
# #     tts_thread.join()  # Wait for the TTS thread to finish
# #     stop_event.set()  # Stop the task checker thread before quitting

# # # Register cleanup function to be called on exit
# # import atexit
# # atexit.register(cleanup)

# # # Action function to handle various commands
# # def action(send):
# #     data_btn = send.lower()
# #     responses = {
# #         "what is your name": "Hello, my name is Hardin, your computerized personal assistant.",
# #         "hello": "Hey there, how can I help you? You can ask me various questions.",
# #         "how are you": "I am doing great, how about you?",
# #         "thank you": "It's my pleasure to help you.",
# #         "good morning": "Good morning, do you need some help today?",
# #         "shutdown": "Goodbye!",
# #         "play music": "Gaana.com is now ready for you, enjoy your music.",
# #         "open google": "Google open.",
# #         "youtube": "YouTube opening.",
# #         "weather": "Checking the weather for you.",
# #         "music from my laptop": "Songs playing...",
# #         "schedule appointment": "Appointment scheduled.",
# #         "set reminder": "Reminder set.",
# #         "emergency response": "Emergency services are being contacted.",
# #     }
# #     if "what is your name" in data_btn:
# #         response = responses["what is your name"]
# #     elif any(greet in data_btn for greet in ["hello", "hey", "hi"]):
# #         response = responses["hello"]
# #     elif "how are you" in data_btn:
# #         response = responses["how are you"]
# #     elif any(thanks in data_btn for thanks in ["thank you", "thanks"]):
# #         response = responses["thank you"]
# #     elif "good morning" in data_btn:
# #         response = responses["good morning"]
# #     elif "what is the time now" in data_btn:
# #         current_time = datetime.datetime.now()
# #         response = f"{current_time.hour} Hour : {current_time.minute} Minute"
# #     elif "shutdown" in data_btn or "quit" in data_btn:
# #         stop_event.set()  # Stop the task checker thread before quitting
# #         response = responses["shutdown"]
# #     elif "play music" in data_btn or "song" in data_btn:
# #         webbrowser.open("https://gaana.com/")
# #         response = responses["play music"]
# #     elif "open google" in data_btn or "google" in data_btn:
# #         webbrowser.open('https://google.com/')
# #         response = responses["open google"]
# #     elif "youtube" in data_btn or "open youtube" in data_btn:
# #         webbrowser.open('https://youtube.com/')
# #         response = responses["youtube"]
# #     elif "weather" in data_btn:
# #         ans = weather.Weather()  # Ensure weather module is correctly set up
# #         response = ans
# #     elif "music from my laptop" in data_btn:
# #         url = 'D:\\music'
# #         songs = os.listdir(url)
# #         os.startfile(os.path.join(url, songs[0]))
# #         response = responses["music from my laptop"]
# #     elif "schedule appointment" in data_btn:
# #         response = schedule_appointment(data_btn)
# #     elif "set reminder" in data_btn:
# #         response = set_reminder_from_input(data_btn)
# #     elif "emergency response" in data_btn:
# #         tts_queue.put("Emergency services are being contacted.")
# #         webbrowser.open("https://www.redcrossnigeria.org/")  # Example emergency service link
# #         response = responses["emergency response"]
# #     else:
# #         response = "I am looking for possible answers to your request..."
# #     tts_queue.put(response)
# #     return response


# import weather
# import datetime
# import webbrowser
# import os
# import time
# import queue
# import re
# import pyttsx3
# from threading import Thread, Event
# from collections import deque

# # Initialize the TTS engine
# engine = pyttsx3.init()
# tts_queue = queue.Queue()

# # Function to process TTS requests
# def process_tts():
#     while True:
#         text = tts_queue.get()  # Wait for a new text to be added
#         if text is None:  # Stop signal
#             break
#         engine.say(text)
#         engine.runAndWait()

# # Start the TTS processing thread
# tts_thread = Thread(target=process_tts)
# tts_thread.start()

# # Dictionary to hold appointments and reminders
# tasks = {
#     'appointments': [],
#     'reminders': deque()  # Use deque for efficient pops from the front
# }

# # Function to add a task
# def add_task(task_type, task_info):
#     tasks.setdefault(task_type, []).append(task_info)
#     return f"{task_type.capitalize()} added successfully!"

# # Function to set a reminder
# def set_reminder(reminder_time, message):
#     tasks['reminders'].append({'time': reminder_time, 'message': message})
#     return "Reminder set!"

# # Function to check for due tasks
# def check_due_tasks(stop_event):
#     while not stop_event.is_set():
#         current_time = datetime.datetime.now().replace(second=0, microsecond=0)  # Only check minute accuracy
#         # Check for appointments
#         for appointment in tasks['appointments'][:]:  # Iterate over a copy of the list
#             if appointment['time'] == current_time:  # Exact match for appointment time
#                 tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
#                 tasks['appointments'].remove(appointment)  # Remove after notifying
#         # Check for reminders
#         while tasks['reminders'] and tasks['reminders'][0]['time'] <= current_time:  # Check all due reminders
#             reminder = tasks['reminders'].popleft()  # Get the first reminder
#             tts_queue.put(reminder['message'])  # Notify
#         time.sleep(1)  # Check every second

# # Start the background thread to check for due tasks
# stop_event = Event()
# task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
# task_checker_thread.start()

# # Function to parse and schedule an appointment from user input in 24-hour format
# def schedule_appointment(data_btn):
#     try:
#         time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
#         appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info
#         appointment_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
#         # Adjust appointment time to today if it's not already in the future
#         now = datetime.datetime.now()
#         appointment_time = appointment_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)
#         if appointment_time < now:
#             appointment_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed
#         return add_task('appointments', {'time': appointment_time, 'info': appointment_info})
#     except ValueError:
#         return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# # Function to parse and set a reminder from user input in 24-hour format
# def set_reminder_from_input(data_btn):
#     try:
#         # Extract time part in 24-hour format
#         time_part = re.search(r'\b\d{1,2}:\d{2}\b', data_btn).group()  # Matches 'HH:MM'
#         message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message
#         reminder_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
#         # Adjust reminder time to today if it's not already in the future
#         now = datetime.datetime.now()
#         reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)
#         if reminder_time < now:
#             reminder_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed
#         return set_reminder(reminder_time, message)
#     except (ValueError, AttributeError):
#         return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# # Function to clean up resources on exit
# def cleanup():
#     tts_queue.put(None)  # Signal to stop the TTS thread
#     tts_thread.join()  # Wait for the TTS thread to finish
#     stop_event.set()  # Stop the task checker thread before quitting

# # Register cleanup function to be called on exit
# import atexit
# atexit.register(cleanup)

# # Action function to handle various commands
# def Action(send):
#     data_btn = send.lower()
#     responses = {
#         "what is your name": "Hello, my name is Hardin, your computerized personal assistant.",
#         "hello": "Hey there, how can I help you? You can ask me various questions.",
#         "how are you": "I am doing great, how about you?",
#         "thank you": "It's my pleasure to help you.",
#         "good morning": "Good morning, do you need some help today?",
#         "shutdown": "Goodbye!",
#         "play music": "Gaana.com is now ready for you, enjoy your music.",
#         "open google": "Google open.",
#         "youtube": "YouTube opening please wait.",
#         "weather": "Checking the weather for you.",
#         "music from my laptop": "Songs playing...",
#         "schedule appointment": "Appointment scheduled.",
#         "set reminder": "Reminder set.",
#         "emergency response": "Emergency services are being contacted.",
#     }
#     response = "I am looking for possible answers to your request..."
    
#     if "what is your name" in data_btn:
#         response = responses["what is your name"]
#     elif any(greet in data_btn for greet in ["hello", "hey", "hi"]):
#         response = responses["hello"]
#     elif "how are you" in data_btn:
#         response = responses["how are you"]
#     elif any(thanks in data_btn for thanks in ["thank you", "thanks"]):
#         response = responses["thank you"]
#     elif "good morning" in data_btn:
#         response = responses["good morning"]
#     elif "what is the time now" in data_btn:
#         current_time = datetime.datetime.now()
#         response = f"{current_time.hour} Hour : {current_time.minute} Minute"
#     elif "shutdown" in data_btn or "quit" in data_btn:
#         stop_event.set()  # Stop the task checker thread before quitting
#         response = responses["shutdown"]
#     elif "play music" in data_btn or "song" in data_btn:
#         webbrowser.open("https://open.spotify.com/track/27tDoZsybt3KvJWTDoW9id?si=247a5a72e06045e7")
#         response = responses["play music"]
#     elif "open google" in data_btn or "google" in data_btn:
#         webbrowser.open('https://google.com/')
#         response = responses["open google"]
#     elif "youtube" in data_btn or "open youtube" in data_btn:
#         webbrowser.open('https://youtube.com/')
#         response = responses["youtube"]
#     elif "weather" in data_btn:
#         ans = weather.Weather()  # Ensure weather module is correctly set up
#         response = ans
#     elif "music from my laptop" in data_btn:
#         url = 'D:\\music'
#         songs = os.listdir(url)
#         os.startfile(os.path.join(url, songs[0]))
#         response = responses["music from my laptop"]
#     elif "schedule appointment" in data_btn:
#         response = schedule_appointment(data_btn)
#     elif "set reminder" in data_btn:
#         response = set_reminder_from_input(data_btn)
#     elif "emergency response" in data_btn:
#         tts_queue.put("Emergency services are being contacted.")
#         webbrowser.open("https://www.redcrossnigeria.org/")  # Example emergency service link
#         response = responses["emergency response"]

#     tts_queue.put(response)
#     return response



import weather
import datetime
import webbrowser
import os
import time
import queue
import re
import pyttsx3
from threading import Thread, Event
from collections import deque

# Initialize the TTS engine
engine = pyttsx3.init()
tts_queue = queue.Queue()

# Function to process TTS requests
def process_tts():
    while True:
        text = tts_queue.get()  # Wait for a new text to be added
        if text is None:  # Stop signal
            break
        engine.say(text)
        engine.runAndWait()

# Start the TTS processing thread
tts_thread = Thread(target=process_tts)
tts_thread.start()

# Dictionary to hold appointments and reminders
tasks = {
    'appointments': [],
    'reminders': deque()  # Use deque for efficient pops from the front
}

# Function to add a task
def add_task(task_type, task_info):
    tasks.setdefault(task_type, []).append(task_info)
    return f"{task_type.capitalize()} added successfully!"

# Function to schedule a reminder (now treated like an appointment)
def schedule_reminder(reminder_time, message):
    return add_task('reminders', {'time': reminder_time, 'message': message})

# Function to check for due tasks
def check_due_tasks(stop_event):
    while not stop_event.is_set():
        current_time = datetime.datetime.now().replace(second=0, microsecond=0)  # Only check minute accuracy
        # Check for appointments
        for appointment in tasks['appointments'][:]:  # Iterate over a copy of the list
            if appointment['time'] == current_time:  # Exact match for appointment time
                tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
                tasks['appointments'].remove(appointment)  # Remove after notifying
        # Check for reminders
        while tasks['reminders'] and tasks['reminders'][0]['time'] <= current_time:  # Check all due reminders
            reminder = tasks['reminders'].popleft()  # Get the first reminder
            tts_queue.put(reminder['message'])  # Notify
        time.sleep(1)  # Check every second

# Start the background thread to check for due tasks
stop_event = Event()
task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
task_checker_thread.start()

# Function to parse and schedule an appointment from user input in 24-hour format
def schedule_appointment(data_btn):
    try:
        time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
        appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info
        appointment_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
        # Adjust appointment time to today if it's not already in the future
        now = datetime.datetime.now()
        appointment_time = appointment_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)
        if appointment_time < now:
            appointment_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed
        return add_task('appointments', {'time': appointment_time, 'info': appointment_info})
    except ValueError:
        return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# Function to parse and set a reminder from user input in 24-hour format
def set_reminder_from_input(data_btn):
    try:
        # Extract time part in 24-hour format
        time_part = re.search(r'\b\d{1,2}:\d{2}\b', data_btn).group()  # Matches 'HH:MM'
        message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message
        reminder_time = datetime.datetime.strptime(time_part, '%H:%M')  # 24-hour time format
        # Adjust reminder time to today if it's not already in the future
        now = datetime.datetime.now()
        reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day, second=0, microsecond=0)
        if reminder_time < now:
            reminder_time += datetime.timedelta(days=1)  # Schedule for next day if time has passed
        return schedule_reminder(reminder_time, message)
    except (ValueError, AttributeError):
        return "I'm sorry, I couldn't understand the time format. Please use 24-hour format like '14:30'."

# Function to clean up resources on exit
def cleanup():
    tts_queue.put(None)  # Signal to stop the TTS thread
    tts_thread.join()  # Wait for the TTS thread to finish
    stop_event.set()  # Stop the task checker thread before quitting

# Register cleanup function to be called on exit
import atexit
atexit.register(cleanup)

# Action function to handle various commands
def Action(send):
    data_btn = send.lower()
    responses = {
        "what is your name": "Hello, my name is Alvis, your computerized personal assistant.",
        "hello": "Hey there, how can I help you? You can ask me various questions.",
        "how are you": "I am doing great, how about you?",
        "thank you": "It's my pleasure to help you.",
        "good morning": "Good morning, do you need some help today?",
        "shutdown": "Goodbye!",
        "play music": "Spotify is now ready for you, enjoy your music.",
        "open google": "Google is opening please wait.",
        "youtube": "YouTube opening please wait.",
        "weather": "Checking the weather for you.",
        "music from my laptop": "Songs playing...",
        "schedule appointment": "Appointment scheduled.",
        "set reminder": "Reminder set.",
        "emergency response": "Emergency services are being contacted.",
    }
    response = "I am looking for possible answers to your request..."
    if "what is your name" in data_btn:
        response = responses["what is your name"]
    elif any(greet in data_btn for greet in ["hello", "hey", "hi"]):
        response = responses["hello"]
    elif "how are you" in data_btn:
        response = responses["how are you"]
    elif any(thanks in data_btn for thanks in ["thank you", "thanks"]):
        response = responses["thank you"]
    elif "good morning" in data_btn:
        response = responses["good morning"]
    elif "what is the time now" in data_btn:
        current_time = datetime.datetime.now()
        response = f"{current_time.hour} Hour : {current_time.minute} Minute"
    elif "shutdown" in data_btn or "quit" in data_btn:
        stop_event.set()  # Stop the task checker thread before quitting
        response = responses["shutdown"]
    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")
        response = responses["play music"]
    elif "open google" in data_btn or "google" in data_btn:
        webbrowser.open('https://google.com/')
        response = responses["open google"]
    elif "youtube" in data_btn or "open youtube" in data_btn:
        webbrowser.open('https://youtube.com/')
        response = responses["youtube"]
    elif "weather" in data_btn:
        ans = weather.Weather()  # Ensure weather module is correctly set up
        response = ans
    elif "music from my laptop" in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        response = responses["music from my laptop"]
    elif "schedule appointment" in data_btn:
        response = schedule_appointment(data_btn)
    elif "set reminder" in data_btn:
        response = set_reminder_from_input(data_btn)
    elif "emergency response" in data_btn:
        tts_queue.put("Emergency services are being contacted.")
        webbrowser.open("https://www.redcrossnigeria.org/")  # Example emergency service link
        response = responses["emergency response"]
    
    tts_queue.put(response)
    return response