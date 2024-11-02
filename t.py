import datetime
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)





# import datetime
# import webbrowser
# import os
# from threading import Thread, Event
# import time
# import queue
# import weather
# import pyttsx3
# import re

# # Initialize the TTS engine
# engine = pyttsx3.init()

# # Queue for TTS requests
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

# # Define a dictionary to hold appointments and reminders
# tasks = {
#     'appointments': [],
#     'reminders': []
# }

# # Function to add a task
# def add_task(task_type, task_info):
#     if task_type not in tasks:
#         tasks[task_type] = []
#     tasks[task_type].append(task_info)
#     return f"{task_type.capitalize()} added successfully!"

# # Function to set a reminder
# def set_reminder(reminder_time, message):
#     tasks['reminders'].append({'time': reminder_time, 'message': message})
#     return "Reminder set!"

# # Function to check for due appointments and reminders
# def check_due_tasks(stop_event):
#     while not stop_event.is_set():
#         current_time = datetime.datetime.now()

#         # Check for appointments
#         for appointment in tasks['appointments']:
#             if appointment['time'] <= current_time:
#                 tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
#                 tasks['appointments'].remove(appointment)  # Remove after notifying

#         # Check for reminders
#         for reminder in tasks['reminders']:
#             if reminder['time'] <= current_time:
#                 tts_queue.put(reminder['message'])
#                 tasks['reminders'].remove(reminder)  # Remove after notifying

#         time.sleep(30)  # Check every 30 seconds

# # Start the background thread to check for due tasks
# stop_event = Event()
# task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
# task_checker_thread.start()

# def Action(send):
#     data_btn = send.lower()

#     if "what is your name" in data_btn:
#         tts_queue.put("Hello, my name is Hardin, your computerized personal assistant.")
#         return "Hello, my name is Hardin, your computerized personal assistant."

#     elif "hello" in data_btn or "hey" in data_btn or "hi" in data_btn:
#         response = (
#             "Hey there, how can I help you? You can ask me the following: "
#             "1. What is your name? "
#             "2. How are you? "
#             "3. Thank you or thanks. "
#             "4. Good morning. "
#             "5. What is the time now? "
#             "6. Shutdown or quit. "
#             "7. Play music. "
#             "8. Open Google. "
#             "9. Open YouTube. "
#             "10. Weather. "
#             "11. Music from my laptop. "
#             "12. Schedule an appointment. "
#             "13. Set a reminder. "
#             "14. Emergency response."
#         )
#         tts_queue.put(response)
#         return response

#     elif "how are you" in data_btn:
#         tts_queue.put("I am doing great, how about you?")
#         return "I am doing great, how about you?"

#     elif "thank you" in data_btn or "thanks" in data_btn:
#         tts_queue.put("It's my pleasure to help you.")
#         return "It's my pleasure to help you."

#     elif "good morning" in data_btn:
#         tts_queue.put("Good morning, do you need some help today?")
#         return "Good morning, do you need some help today?"

#     elif "what is the time now" in data_btn:
#         current_time = datetime.datetime.now()
#         time_str = f"{current_time.hour} Hour : {current_time.minute} Minute"
#         tts_queue.put(time_str)
#         return time_str

#     elif "shutdown" in data_btn or "quit" in data_btn:
#         stop_event.set()  # Stop the task checker thread before quitting
#         tts_queue.put("Goodbye!")
#         return "Goodbye!"

#     elif "play music" in data_btn or "song" in data_btn:
#         webbrowser.open("https://gaana.com/")
#         tts_queue.put("Gaana.com is now ready for you, enjoy your music.")
#         return "Gaana.com is now ready for you, enjoy your music."

#     elif 'open google' in data_btn or 'google' in data_btn:
#         url = 'https://google.com/'
#         webbrowser.get().open(url)
#         tts_queue.put("Google open.")
#         return "Google open."

#     elif 'youtube' in data_btn or "open youtube" in data_btn:
#         url = 'https://youtube.com/'
#         webbrowser.get().open(url)
#         tts_queue.put("YouTube open.")
#         return "YouTube open."

#     elif 'weather' in data_btn:
#         ans = weather.Weather()  # Ensure weather module is correctly set up
#         tts_queue.put(ans)
#         return ans

#     elif 'music from my laptop' in data_btn:
#         url = 'D:\\music'
#         songs = os.listdir(url)
#         os.startfile(os.path.join(url, songs[0]))
#         tts_queue.put("Songs playing...")
#         return "Songs playing..."

#     elif 'schedule appointment' in data_btn:
#         try:
#             time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
#             appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info

#             if ':' in time_part:
#                 appointment_time = datetime.datetime.strptime(time_part, '%I:%M%p')  # For formats like '2:30pm'
#             else:
#                 appointment_time = datetime.datetime.strptime(time_part, '%I%p')  # For formats like '3pm'

#             result = add_task('appointments', {'time': appointment_time, 'info': appointment_info})
#             tts_queue.put(result)
#             return result
#         except ValueError:
#             tts_queue.put("I'm sorry, I couldn't understand the time format. Please use formats like '3pm' or '2:30pm'.")
#             return "I'm sorry, I couldn't understand the time format."

#     elif 'set reminder' in data_btn:

#         try:

#             # Extract the time part using regex (looks for formats like "12:07pm")

#             time_part = re.search(r'\d{1,2}:\d{2}[ap]m|\d{1,2}[ap]m', data_btn).group()

#             message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message

#             # Convert the time string to a datetime object

#             reminder_time = datetime.datetime.strptime(time_part, '%I:%M%p' if ':' in time_part else '%I%p')

#             # Set the reminder

#             result = set_reminder(reminder_time, message)

#             tts_queue.put(result)

#             return result

#         except ValueError:

#             tts_queue.put("I'm sorry, I couldn't understand the time format. Please use formats like '2:30pm'.")

#             return "I'm sorry, I couldn't understand the time format."

#         except AttributeError:

#             tts_queue.put("I couldn't find a valid time in your input. Please try again with a valid time format.")

#             return "I couldn't find a valid time in your input. Please try again with a valid time format."

#     elif 'emergency response' in data_btn:
#         tts_queue.put("Emergency services are being contacted.")
#         webbrowser.open("https://www.redcrossnigeria.org/")  # Example emergency service link
#         return "Emergency services are being contacted."

#     else:
#         tts_queue.put("I am looking for possible answers to your request...")
#         return "I am looking for possible answers to your request..."

# # Clean up resources when exiting
# def cleanup():
#     tts_queue.put(None)  # Signal to stop the TTS thread
#     tts_thread.join()  # Wait for the TTS thread to finish
#     stop_event.set()  # Stop the task checker thread before quitting

# # Call cleanup before exiting your program
# import atexit
# atexit.register(cleanup)


# import datetime
# import webbrowser
# import os
# import time
# import queue
# import re
# import weather
# import pyttsx3
# from threading import Thread, Event

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
#     'reminders': []
# }

# # Function to add a task
# def add_task(task_type, task_info):
#     tasks.setdefault(task_type, []).append(task_info)
#     return f"{task_type.capitalize()} added successfully!"

# # Function to set a reminder
# def set_reminder(reminder_time, message):
#     tasks['reminders'].append({'time': reminder_time, 'message': message})
#     return "Reminder set!"

# # Function to check for due appointments and reminders
# def check_due_tasks(stop_event):
#     while not stop_event.is_set():
#         current_time = datetime.datetime.now()
#         # Check for appointments
#         for appointment in tasks['appointments']:
#             if appointment['time'] <= current_time:
#                 tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
#                 tasks['appointments'].remove(appointment)  # Remove after notifying
#         # Check for reminders
#         for reminder in tasks['reminders']:
#             if reminder['time'] <= current_time:
#                 tts_queue.put(reminder['message'])
#                 tasks['reminders'].remove(reminder)  # Remove after notifying
#         time.sleep(30)  # Check every 30 seconds

# # Start the background thread to check for due tasks
# stop_event = Event()
# task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
# task_checker_thread.start()

# def action(send):
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
#         "youtube": "YouTube open.",
#         "weather": "Checking the weather for you.",
#         "music from my laptop": "Songs playing...",
#         "schedule appointment": "Appointment scheduled.",
#         "set reminder": "Reminder set.",
#         "emergency response": "Emergency services are being contacted.",
#     }

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
#         webbrowser.open("https://gaana.com/")
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
#     else:
#         response = "I am looking for possible answers to your request..."

#     tts_queue.put(response)
#     return response

# def schedule_appointment(data_btn):
#     try:
#         time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
#         appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info
#         appointment_time = datetime.datetime.strptime(time_part, '%I:%M%p') if ':' in time_part else datetime.datetime.strptime(time_part, '%I%p')
#         return add_task('appointments', {'time': appointment_time, 'info': appointment_info})
#     except ValueError:
#         return "I'm sorry, I couldn't understand the time format. Please use formats like '3pm' or '2:30pm'."

# def set_reminder_from_input(data_btn):
#     try:
#         time_part = re.search(r'\d{1,2}:\d{2}[ap]m|\d{1,2}[ap]m', data_btn).group()
#         message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message
#         reminder_time = datetime.datetime.strptime(time_part, '%I:%M%p' if ':' in time_part else '%I%p')
#         return set_reminder(reminder_time, message)
#     except (ValueError, AttributeError):
#         return "I'm sorry, I couldn't understand the time format. Please use formats like '2:30pm'."

# # Clean up resources when exiting
# def cleanup():
#     tts_queue.put(None)  # Signal to stop the TTS thread
#     tts_thread.join()  # Wait for the TTS thread to finish
#     stop_event.set()  # Stop the task checker thread before quitting

# # Register cleanup function to be called on exit
# # import atexit
# # atexit.register(cleanup)


# ###########################################
# #############################################




# import datetime
# import webbrowser
# import os
# import time
# import queue
# import re
# import weather
# import pyttsx3
# from threading import Thread, Event

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
#     'reminders': []
# }

# # Function to add a task
# def add_task(task_type, task_info):
#     tasks.setdefault(task_type, []).append(task_info)
#     return f"{task_type.capitalize()} added successfully!"

# # Function to set a reminder
# def set_reminder(reminder_time, message):
#     tasks['reminders'].append({'time': reminder_time, 'message': message})
#     return "Reminder set!"

# # Function to check for due appointments and reminders
# def check_due_tasks(stop_event):
#     while not stop_event.is_set():
#         current_time = datetime.datetime.now()
#         # Check for appointments
#         for appointment in tasks['appointments']:
#             if appointment['time'] <= current_time:
#                 tts_queue.put(f"It's time for your appointment: {appointment['info']}.")
#                 tasks['appointments'].remove(appointment)  # Remove after notifying
#         # Check for reminders
#         for reminder in tasks['reminders']:
#             if reminder['time'] <= current_time:
#                 tts_queue.put(reminder['message'])
#                 tasks['reminders'].remove(reminder)  # Remove after notifying
#         time.sleep(30)  # Check every 30 seconds

# # Start the background thread to check for due tasks
# stop_event = Event()
# task_checker_thread = Thread(target=check_due_tasks, args=(stop_event,))
# task_checker_thread.start()

# def action(send):
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
#         "youtube": "YouTube open.",
#         "weather": "Checking the weather for you.",
#         "music from my laptop": "Songs playing...",
#         "schedule appointment": "Appointment scheduled.",
#         "set reminder": "Reminder set.",
#         "emergency response": "Emergency services are being contacted.",
#     }
    
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
#         webbrowser.open("https://gaana.com/")
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
#     else:
#         response = "I am looking for possible answers to your request..."
    
#     tts_queue.put(response)
#     return response

# def schedule_appointment(data_btn):
#     try:
#         time_part = data_btn.split("at")[-1].strip().split(" ")[0]  # Extract the time part after "at"
#         appointment_info = " ".join(data_btn.split(" ")[3:])  # Extract appointment info
#         appointment_time = datetime.datetime.strptime(time_part, '%I:%M%p') if ':' in time_part else datetime.datetime.strptime(time_part, '%I%p')
#         return add_task('appointments', {'time': appointment_time, 'info': appointment_info})
#     except ValueError:
#         return "I'm sorry, I couldn't understand the time format. Please use formats like '3pm' or '2:30pm'."

# def set_reminder_from_input(data_btn):
#     try:
#         time_part = re.search(r'\d{1,2}:\d{2}[ap]m|\d{1,2}[ap]m', data_btn).group()
#         message = " ".join(data_btn.split(" ")[3:])  # Extract reminder message
#         reminder_time = datetime.datetime.strptime(time_part, '%I:%M%p' if ':' in time_part else '%I%p')
#         return set_reminder(reminder_time, message)
#     except (ValueError, AttributeError):
#         return "I'm sorry, I couldn't understand the time format. Please use formats like '2:30pm'."

# # Clean up resources when exiting
# def cleanup():
#     tts_queue.put(None)  # Signal to stop the TTS thread
#     tts_thread.join()  # Wait for the TTS thread to finish
#     stop_event.set()  # Stop the task checker thread before quitting

# # Register cleanup function to be called on exit
# import atexit
# atexit.register(cleanup)




#################################