import time
from datetime import datetime as dt

host_temp= 'hosts'
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com', 'www.pocket.com','pocket.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) >= dt.now() >= dt(dt.now().year, dt.now().month, dt.now().day, 8):
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("{} {}\r".format(redirect, website))
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


    time.sleep(5)