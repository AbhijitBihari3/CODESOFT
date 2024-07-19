from datetime import datetime
import webbrowser
import os
def chatbot_response(command):
    command = command.lower()
    #greeting from the chatbot
    if 'hi' in command or 'hello' in command or 'start' in command:
        return "Hello! How can i help you today?"
    #resonse for any help
    elif 'help' in command :
        return "Sure, How can i assit you."
    #redirect to linkedin
    elif 'go to linkedin' in command:
        return webbrowser.open("https://www.linkedin.com")
    #it will give the current date  
    elif 'date' in command:
        today_date= datetime.now().strftime('%Y-%m-%d')
        return f"The Date is {today_date}"
    #it will give the current time
    elif 'time' in command:
        time_now=datetime.now().strftime('%H:%M')
        return f"Time is {time_now}"
    #response to who are you
    elif 'who are you?' in command:
        return "Iam a chatbot"
    #it will open google    
    elif 'go to google' in command:
        return webbrowser.open("http://www.google.com")
    #for youtube  
    elif 'go to youtube' in command:
        return webbrowser.open("http://www.youtube.com")
    #for geeksforgeeks  
    elif 'go to gfg' in command:
        return webbrowser.open("https://www.geeksforgeeks.org/")
    #redirect to notepad
    elif 'go to notepad' in command:
        return os.system('notepad')("opening notepad..")
    # exit
    elif 'bye' in command:
        return "You're welcome! Glad i could help. Bye! "
    #invalid command
    else:
        return "sorry, i don't understand"

def main():    
    print("Welcome to the chat,'exit' to end the conversation")
    while True: #untill the user type exit
        command = input("you: ")
        if command == 'exit':
         print("Chatbot: Goodbye, it was nice chatting with you.")
         break  #break after "exit"
        bot_response=chatbot_response(command) 
        print(f"Chatbot: {bot_response}")
# main fucntion is only executed if the script runs directly, not imported as module.
if __name__ == "__main__":
    main() 
