import os
import requests
from pystyle import *
from time import sleep

def Send(username, avatar, content, webhook):
    res = requests.post(webhook, json={
        "username": username,
        "avatar_url": avatar,
        "content": content
    })
    if res.status_code == 200 or res.status_code == 204:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "\nMessage Sent! Status Code: 200"))
    elif res.status_code == 429:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "\nRate Limited! Status Code: 429"))
    else:
        exit()

def Menu1():
    webhook = Write.Input("Webhook: ", Colors.blue_to_cyan, interval=0.1)
    username = Write.Input("Username: ", Colors.blue_to_cyan, interval=0.1)
    avatar = Write.Input("Avatar Url (Blank for none): ", Colors.blue_to_cyan, interval=0.1)
    message = Write.Input("Message: ", Colors.blue_to_cyan, interval=0.1)
    amount = Write.Input("Amount: ", Colors.blue_to_cyan, interval=0.1)
    sent = int(amount) + 1
    for n in range(sent):
        Send(username, avatar, message, webhook)
    Write.Print("\nWebhook Spammed!", Colors.blue_to_cyan, 0.1)
    input()
    Main()

def Menu2():
    webhook = Write.Input("Webhook: ", Colors.blue_to_cyan, interval=0.1)
    res = requests.delete(webhook)
    if res.status_code == 200 or res.status_code == 204:
        Write.Print("\nWebhook Deleted!", Colors.blue_to_cyan, 0.1)
    elif res.status_code == 404:
        Write.Print("\nInvalid Webhook!", Colors.blue_to_cyan, 0.1)
    else:
        Write.Print("\nUnknown Error!", Colors.blue_to_cyan, 0.1)
    input()
    Main()

def Main():
    os.system("cls & title Orbit Spammer")
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter("""
              /$$$$$$            /$$       /$$   /$$    
             /$$__  $$          | $$      |__/  | $$    
            | $$  \ $$  /$$$$$$ | $$$$$$$  /$$ /$$$$$$  
            | $$  | $$ /$$__  $$| $$__  $$| $$|_  $$_/  
            | $$  | $$| $$  \__/| $$  \ $$| $$  | $$    
            | $$  | $$| $$      | $$  | $$| $$  | $$ /$$
            |  $$$$$$/| $$      | $$$$$$$/| $$  |  $$$$/
             \______/ |__/      |_______/ |__/   \___/    

                        [1] Webhook Spammer
                        [2] Webhook Deleter               
    """)))
    choice = Write.Input("Choice: ", Colors.blue_to_cyan, interval=0.1)
    if choice == "1":
        Menu1()
    elif choice == "2":
        Menu2()
    else:
        Main()

if __name__ == "__main__":
    Main()