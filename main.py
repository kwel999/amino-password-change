#𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘤𝘩𝘢𝘯𝘨𝘦𝘳 𝘶𝘴𝘪𝘯𝘨 𝘬_𝘢𝘮𝘪𝘯𝘰.𝘱𝘺

import os
os.system("pip install -U k_amino.py")
os.system('clear')
import email
import k_amino, json, time
from concurrent.futures import ThreadPoolExecutor


print("\t\033[1;32m Change Password\033[1;36m https://youtube.com/c/KWELATEYOURPIZZA \n\n")

new = input("\nNew password >> ")


obj = "},"

accs = open("accounts.json")
acc = json.load(accs)

def log(client, email, password):
    try:
        client.login(email, password)
    except Exception as e:
        print(e)

def change(account: dict):
    email = account["email"]
    password = account["password"]
    device = account["deviceId"]
    client = k_amino.Client(deviceId=device)
    log(client = client, email=email, password=password)
    print(f"Changing Password >> {email}")
    try:
        client.change_password(password=password, newPassword=new)
        #time.sleep(4) #use time if you need
        print(f"Successfully Changed Password >>  {email}")
        with open("changed_accounts.json", 'a') as z:
            acc = f'{{"email": "{email}", "password": "{new}", "device": "{device}"{obj}\n'
            z.write(acc)
    except Exception as e:
        print(e)
    print("\n")

def main():
    for account in acc:
        ThreadPoolExecutor(max_workers=100).submit(change, account)
        time.sleep(2.5)


if __name__ == "__main__":
    main()
