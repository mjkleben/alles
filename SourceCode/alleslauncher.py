import urllib
import os, webbrowser,requests #for Google
import urllib.request, urllib.parse #for Youtube
import bs4
import smtplib #for emails
import sys
import time
import re
import subprocess
import threading
import inspect
from os import listdir
import shutil
#----------------------------------------------------------------------------------------------------------------------------

line_separator = "--------------------------------------------------------------------------------"
every_command = ["/g","/google", "/googler","/y", "/youtube", "/yt","/e", "/email", "/q", "/quit", "/music", "/m", "/video", "/v", '/cs', '/create', '/createscript', '/clear', '/es','/editscript', '/ds' ,'/delete', '/deletescript', '/startup', '/ss','/l', '/list', '/deleteemail', '/de', '/as', '/addscript','/open', '/os', '/sd', '/startupdelete', '/cc', '/changecolor', '/f', '/t', '/r', '/i']
def browser_commands(inputted_command):
    #Google caller
    google_commands = ["/g","/google", "/googler"]
    youtube_commands = ["/y", "/youtube", "/yt"]
    email_commands = ["/e", "/email"]
    edit_email_commands = ["/de", "/deleteemail"]
    music_commands = ["/music", "/m"]
    video_commands = ['/video','/v']
    create_macro_commands = ['/cs', '/create', '/createscript']
    edit_macro_commands = ['/es','/editscript']
    delete_macro_commands = ['/ds', '/delete', '/deletescript']
    help_commands = ["/help", "/h"]
    list_commands = ["/l", "/list"]
    add_commands = ['/as', '/addscript']
    open_macro = ['/open','/os']
    startup_delete = ['/sd', '/startupdelete']
    colors = ['/cc', '/changecolor']
    #print(inputted_command)
    if inputted_command.strip() in google_commands:
        print(line_separator)
        googler()
        enter_command()
    elif inputted_command in open_macro:
        command_user()
        enter_command()
    elif inputted_command in youtube_commands:
        print(line_separator)
        youtuber()
        enter_command()
    elif inputted_command in email_commands:
        print(line_separator)
        email_sender()
        enter_command()
    elif inputted_command in edit_email_commands:
        print(line_separator)
        edit_email()
        enter_command()
    elif inputted_command in video_commands:
        print(line_separator)
        video_downloader()
        enter_command()
    elif inputted_command in music_commands:
        print(line_separator)
        music_downloader()
        enter_command()
    elif inputted_command == "/quit" or inputted_command == "/q":
        print("Quitting alles..")
        time.sleep(2)
        sys.exit(0)
    elif inputted_command in create_macro_commands:
        print(line_separator)
        create_macro()
    elif inputted_command == "/clear":
        clear_screen()
    elif inputted_command in edit_macro_commands:
        print(line_separator)
        edit_macro()
        enter_command()
    elif inputted_command in delete_macro_commands:
        print(line_separator)
        delete_macro()
        enter_command()
    elif inputted_command == "/startup" or inputted_command == "/ss":
        print(line_separator)
        macro_startup()
        enter_command()
    elif inputted_command in list_commands:
        print(line_separator)
        show_commands()
        enter_command()
    elif inputted_command in edit_macro_commands:
        print(line_separator)
        edit_email()
        enter_command()
    elif inputted_command in add_commands:
        print(line_separator)
        add_to_macro()
        enter_command()
    elif inputted_command in startup_delete:
        print(line_separator)
        delete_from_startup()
        enter_command()
    elif inputted_command == "/f":
        print(line_separator)
        facebook()
        enter_command()
    elif inputted_command == "/t":
        print(line_separator)
        twitter()
        enter_command()
    elif inputted_command == "/i":
        print(line_separator)
        instagram()
        enter_command()
    elif inputted_command == "/r":
        print(line_separator)
        reddit()
        enter_command()
    #get rid of this
    elif inputted_command in colors:
        print(line_separator)
        change_color()
        enter_command()
    else:
        if inputted_command == "/help" or inputted_command == "/h":
            browser_helper()
        else:
            print("Please enter a valid command.\n")
            enter_command()

#-----------------------------------------CHANGE COLOR OF TERMINAL-------------------------------------
def change_color():
    try:
        list_colors = ['black', 'blue', 'green', 'aqua', 'red', 'purple', 'yellow', 'white', 'gray', 'light blue',
                       'light green', 'light aqua', 'light red', 'light purple', 'light yellow', 'bright white']
        color_path = os.path.dirname(os.getcwd())
        color_path = color_path + r"\alles" + "\setup\\" + "console_color.txt"
        f = open(color_path, "w")

        color_str = "color "
        console_color = ""
        #GET COLOR OF CONSOLE
        print("What color would you like your console to be?")
        print("Options: black, blue, green, aqua, red, purple, yellow, white, gray, light blue, light green, light aqua, light red, light purple, light yellow, bright white \n")

        desired_color = input("Console Color: ").strip().lower()
        while desired_color not in list_colors:
            desired_color = input("Please enter a valid color name: ")
            if desired_color in every_command:
                browser_commands(desired_color)
                #write original color

        if desired_color == "black":
            console_color = "0"
        elif desired_color == "blue":
            console_color = "1"
        elif desired_color == "green":
            console_color = "2"
        elif desired_color == "aqua":
            console_color = "3"
        elif desired_color == "red":
            console_color = "4"
        elif desired_color == "purple":
            console_color = "5"
        elif desired_color == "yellow":
            console_color = "6"
        elif desired_color == "white":
            console_color = "7"
        elif desired_color == "gray":
            console_color = "8"
        elif desired_color == "light blue":
            console_color = "9"
        elif desired_color == "light green":
            console_color = "A"
        elif desired_color == "light aqua":
            console_color = "B"
        elif desired_color == "light red":
            console_color = "C"
        elif desired_color == "light purple":
            console_color = "D"
        elif desired_color == "light yellow":
            console_color = "E"
        elif desired_color == "bright white":
            console_color = "F"

        color_str += console_color


        #NOW GET COLOR OF TEXT
        print("\n")
        print("What color would you like your text to be in the console?")
        print("Options: black, blue, green, aqua, red, purple, yellow, white, gray, light blue, light green, light aqua, light red, light purple, light yellow, bright white \n")
        desired_color = input("Text Color: ").strip().lower()
        while desired_color not in list_colors:
            desired_color = input("Please enter a valid color name: ")
            if desired_color in every_command:
                browser_commands(desired_color)
                #write original color

        if desired_color == "black":
            console_color = "0"
        elif desired_color == "blue":
            console_color = "1"
        elif desired_color == "green":
            console_color = "2"
        elif desired_color == "aqua":
            console_color = "3"
        elif desired_color == "red":
            console_color = "4"
        elif desired_color == "purple":
            console_color = "5"
        elif desired_color == "yellow":
            console_color = "6"
        elif desired_color == "white":
            console_color = "7"
        elif desired_color == "gray":
            console_color = "8"
        elif desired_color == "light blue":
            console_color = "9"
        elif desired_color == "light green":
            console_color = "A"
        elif desired_color == "light aqua":
            console_color = "B"
        elif desired_color == "light red":
            console_color = "C"
        elif desired_color == "light purple":
            console_color = "D"
        elif desired_color == "light yellow":
            console_color = "E"
        elif desired_color == "bright white":
            console_color = "F"

        color_str += console_color

        f.write(color_str)
        f.close()
        print("Color preferences saved! Restart alles to see the color changes.")
        print(line_separator)
        enter_command()

    except Exception as e:
        print(e)
        enter_command()


#-------------------------------------BROWSER HELPER-----------------------------------------------
def browser_helper():
    print("There is nothing to display for help here. Enter /l or /list to see all possible commands, /q or /quit to quit alles, or enter a command.")
    enter_command()
#--------------------------------------------CLEAR SCREEN-----------------------------------------
def clear_screen():
    os.system('cls')
    enter_command()

#----------------------------------------------GENERIC HELPER-----------------------------------------------
def helper():
    print("Welcome to alles, the script maker and performer! \nTo start using the program, type a command from the list of commands.")
    print("There are multiple options for a command; it doesn't matter which one you use.")
    print("\nYou can use the Clear, Help, or Quit commands at any time in the program. \nUsing the Help command on a command page will tell you more about that command.")
    print("\n")

    enter_command()

#-----------------------------------------SHOW ALL COMMANDS--------------------------------------------------------
def show_commands():
    print("************Welcome to alles, the Simple Script Maker and Performer!*************")
    print("--------------------------------Browser Commands--------------------------------")
    browser_commands_list = ["Google: '/g' '/google' '/googler'", "YouTube: '/y' '/yt' '/youtube'",
                             "Email: '/e' '/email'", "Delete Email Info: '/de' '/deleteemail'",
                             "Download Music: '/m' '/dm'", "Download Videos: '/v' '/video'"]
    for stuff in browser_commands_list:
        print(stuff)
    print("--------------------------------Script Commands----------------------------------")
    print("Create New Script: '/cs' '/create' '/createscript'")
    print("Open Script: '/os' '/open'")
    print("Add to Existing Script: '/as' '/addscript' ")
    print("Edit Existing Script: '/es' '/editscript'")
    print("Delete Existing Script: '/ds' '/deletescript' ")
    print("Start Script when Computer Starts: '/ss' '/startup' ")
    print("Delete Script from Startup: '/sd' '/startupdelete")
    print("------------------------------Additional Commands-------------------------------")
    print("List All Commands: '/l' '/list'")
    print("Clear Screen: '/clear'")
    print("Quit program: '/q' '/quit'")
    print("Help/About: '/h' '/help'")
    print("Change Color of Console and Text: '/cc' '/changecolor' ")
    print("Facebook: '/f' , Twitter: '/t' , Instagram: '/i' , Reddit: '/r'")
    print("--------------------------------------------------------------------------------\n")

    enter_command()
#----------------------------------------------------------SOCIAL MEDIA, ETC.---------------------------------------------------
def facebook():
    try:
        webbrowser.open_new_tab("https://www.facebook.com/")
        enter_command()
    except Exception as e:
        print(e)
        enter_command()

def twitter():
    try:
        webbrowser.open_new_tab("https://twitter.com/")
        enter_command()
    except Exception as e:
        print(e)
        enter_command()

def instagram():
    try:
        webbrowser.open_new_tab("https://www.instagram.com/")
        enter_command()
    except Exception as e:
        print(e)
        enter_command()

def reddit():
    try:
        webbrowser.open_new_tab("https://www.reddit.com/")
        enter_command()
    except Exception as e:
        print(e)
        enter_command()
#-----------------------------------------------------------------GOOGLE--------------------------------------------------------------
def googler(): #opens a google page in a new window
    search = input("Google: ").strip()

    if search.strip() in every_command:
        browser_commands(search.strip())
    elif search.strip() == "/help" or search.strip() == "/h":
        google_help()
    else:
        try:
            print("Searching on Google...")

            #How many tabs should be open? Code
            how_many_tabs = 1
            list = []
            if not re.findall(r'\+\+(\w+)', search):
                print("Finding top result for " + "'" + search + "'"+ " ...")
            if re.findall(r'\+\+(\w+)', search):
                list = re.findall(r'\+\+(\w+)', search)
                if int(list[0]):
                    how_many_tabs = int(list[0])
                    search, separator, old_string = search.partition('++' + list[0])
                    print("Finding top " + str(how_many_tabs) + " results for " + "'" + search + "'" + " ...")

            #Opening the tabs
            res = requests.get('https://google.com/search?q=' + search)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            links = soup.select('.r a')
            num_tabs = min(how_many_tabs, len(links))

            for i in range(num_tabs):
                webbrowser.open('https://google.com' + links[i].get('href'))

            browser_commands("/g")



        except Exception as e:
            print(e)
            enter_command()


def google_help():
    print("Welcome to the Googler!")
    print("\nEnter what you want to search to get the top search result on Google.")
    print("You can also add a '++#' after your search, where # is the number of top search results you want.")
    print("For example. Typing 'How to play the Guitar ++3' will open up the top 3 links of the Google search.")
    print("If you don't put a ++ followed by a number, then only the top link will be opened.")
    print("\n")
    enter_command()

#-------------------------------------------------YOUTUBE-------------------------------------------------
def youtuber(): #opens a youtube video
    youtube_commands = ["/y", "/youtube", "/yt"]
    print("Welcome to the YouTuber!")
    try:
        vid_search = input("What's the name of the video you'd like to search for?: ").strip()

        if vid_search in every_command:
            browser_commands(vid_search)
        elif vid_search == "/help" or vid_search =="/h":
            youtube_helper()
        else:
            query_string = urllib.parse.urlencode({"search_query": vid_search})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

            top_result = "http://www.youtube.com/watch?v=" + search_results[0]
            webbrowser.open_new_tab(top_result)

            correct_or_no = input("Is this video what you were looking for? Y or N: ").strip() #is the opened tab correct, if not then close it and open the whole YouTube page
            if correct_or_no == "y" or correct_or_no == "Y":
                browser_commands("/y")
            elif correct_or_no == "n" or correct_or_no == "N":
                webbrowser.open_new_tab("http://www.youtube.com/results?" + query_string)
            elif correct_or_no.strip() in every_command:
                browser_commands(correct_or_no)
            elif correct_or_no.strip() == "/help":
                youtube_helper()
            else:
                another_command = input("Enter a command: ").strip()
                browser_commands(another_command)

    except Exception as e:
        print(e)
        enter_command()



def youtube_helper():
    print("Welcome to the YouTuber! With this command, you can quickly search the top result of the video you want to see")
    print("on YouTube! If the video isn't what you wanted, then respond 'N' or 'n' when the program asks you to.")
    print("By responding 'N' or 'n', it will open up the whole page and let you select the video you want from there.")
    print("\n")
    command = input("Enter a command: ").strip()
    browser_commands(command)
#-------------------------------------------EMAIL----------------------------------------------------------------
def email_sender():
    try:
        print("Welcome to the Emailer!\n")
        #check if current directory is equal to this
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\setup\\"

        f_name = "email_setup.txt"
        email_path = path + f_name
        #print(real_path)

        if email_setup() == "dont setup":
            try:
                username = input("Email username : ").strip()
                if username in every_command:
                    browser_commands(username)
                if username == "/help" or username == '/h':
                    email_help()

                password = input("Email password: ").strip()
                if password in every_command:
                    browser_commands(password)
                if password == "/help" or password == '/h':
                    email_help()

                send_to = input("Send to: ").strip()
                if send_to in every_command:
                    browser_commands(send_to)
                if send_to == "/help" or send_to == '/h':
                    email_help()

                subject = input("Subject: ").strip()
                if subject in every_command:
                    browser_commands(subject)
                if subject == "/help" or subject == '/h':
                    email_help()

                content = input("Content: \n".strip())
                if content in every_command:
                    browser_commands(content)
                if content == "/help" or content == '/h':
                    email_help()


                message = 'Subject: {}\n\n{}'.format(subject, content)

                stmp_email = ""
                email_org = ""
                if "@hotmail.com" in username:
                    stmp_email = 'smtp.live.com'
                    email_org = "@hotmail.com"
                elif "@gmail.com" in username:
                    stmp_email = 'smtp.gmail.com'
                    email_org = '@gmail.com'


                email = smtplib.SMTP(stmp_email, 587)
                email.ehlo()
                email.starttls()
                email.login(username, password)

                email_address = username + email_org
                #email_outline(username, send_to, subject, content) #check to see if user wants to send mail or not

                if email_outline(username, send_to, subject, content)  == True:
                    email.sendmail(email_address, send_to, message)
                    email.quit()
                    print("Email sent!")
                    enter_command()
                elif email_outline(username, send_to, subject, content)  == False:
                    email.quit()
                    print("Email deleted.")
                    enter_command()
                else:
                    enter_command()

            except:
                print("Please check all email addresses and make sure everything is ty[ed correctly.")
                command = input("Type /help to see list of possible problems").strip()
                if command == "/help" or command == '/h':
                    email_help()
                else:
                    browser_commands(command)
        elif email_setup() == "not setup":
            print("Would you like to setup your email/password to this emailer?")
            response = input("Enter 'Y' or 'y' if yes, 'N' or 'n' if no: ").strip()
            if response in every_command:
                browser_commands(response)
            if response == "/help" or response == '/h':
                email_help()

            possible_response = ["Y", "y", "n", "N"]
            while(response not in possible_response):
                response = input("Please enter a valid response: ").strip()
            if response == "Y" or response == "y":
                f = open(email_path, "w")
                f.truncate()
                f.write("setup" + "\n")
                usr = input("Enter your username: ").strip()


                if usr in every_command:
                    browser_commands(usr)

                pwd = input("Enter your password: ").strip()
                if pwd in every_command:
                    browser_commands(pwd)

                f.write("Username: " + usr + "\n")
                f.write("Password: " + pwd)
                print("Setup Complete!")
                f.close()
            else:
                f = open(email_path, "w")
                f.truncate()
                f.write("dont setup")
                f.close()
        elif (email_setup() == "setup"):
            list_info = []
            f = open(email_path, "r")
            line = f.readline()
            while(line):
                list_info.append(line)
                line = f.readline()
            f.close()

            usr = list_info[1]
            usr = usr[10:].strip()
            pwd = list_info[2]
            pwd = pwd[10:].strip()
            try:
                username = usr
                print("From: " + username)
                if username in every_command:
                    browser_commands()

                password = pwd
                if password in every_command:
                    browser_commands(password)

                send_to = input("Send to: ").strip()
                if send_to in every_command:
                    browser_commands(send_to)

                subject = input("Subject: ").strip()
                if subject in every_command:
                    browser_commands(subject)

                content = input("Content: \n").strip()
                if content in every_command:
                    browser_commands(content)
                message = 'Subject: {}\n\n{}'.format(subject, content)

                stmp_email = ""
                email_org = ""
                if "@hotmail.com" in username:
                    stmp_email = 'smtp.live.com'
                    email_org = "@hotmail.com"
                elif "@gmail.com" in username:
                    stmp_email = 'smtp.gmail.com'
                    email_org = '@gmail.com'

                email = smtplib.SMTP(stmp_email, 587)
                email.ehlo()
                email.starttls()
                email.login(username, password)

                email_address = username + email_org

                if email_outline(username, send_to, subject, content) == True:
                    email.sendmail(email_address, send_to, message)
                    email.quit()
                    print("Email sent!")
                    enter_command()
                elif email_outline(username, send_to, subject, content) == False:
                    email.quit()
                    print("Email deleted.")
                    enter_command()
                else:
                    enter_command()

            except Exception as e:
                print("Please check all email addresses and make sure everything is typed correctly. For example, your username/password might be wrong.")
                command = input("Type /help to see list of possible problems").strip()
                if command == "/help" or command == '/h':
                    email_help()
                else:
                    browser_commands(command)
    except Exception as e:
        print(e)
        print("Please check all email addresses and make sure everything is typed correctly. For example, your username/password might be wrong.")
        command = input("Type /help to see list of possible problems").strip()
        if command == "/help" or command == '/h':
            email_help()
        else:
            browser_commands(command)

def email_setup():
    path = os.path.dirname(os.getcwd())
    path = path + r"\alles" + "\setup\\"

    f_name = "email_setup.txt"
    email_path = path + f_name
    try:
        f = open(email_path, "r")

        line = f.read()
        line = line.split('\n', 1)[0]

        if(line == "not setup"):
            return "not setup"
        elif(line == "dont setup"):
            return "dont setup"
        elif(line == "setup"):
            return "setup"
        f.close()

    except Exception as e:
        print(e)
        enter_command()


def email_help():
    print("Welcome to the Emailer! For now, only Gmail and Hotmail/Live is available. \nIf you are experiencing problems with this, then follow these directions:\n")

    print("1. If using Gmail -> My Account -> Sign-in & security. Make 'Allow less secure apps: ON'")
    print("2. Make sure you wrote the full email address. Example: 'foo@gmail.com' instead of just 'foo'.")
    print("3. Check to see if you typed your password, all emails, etc. correctly.\n")

    print("If your problem still hasn't been resolved, please contact using the alles website.")

    enter_command()

def email_outline(email_address, send_to, subject, content ):
    print("------------------EMAIL PREVIEW------------------")
    print("From: " + email_address)
    print("To: " + send_to)
    print("Subject: " + subject)
    print("Content: " + content)
    print("-------------------------------------------------")

    answer = input("Send Email? Y or N: ").strip()
    if answer in every_command:
        browser_commands(answer)

    response = ["y", "Y", "n", "N"]

    while(answer not in response):
        answer = input("Enter a valid response or Enter a command..").strip()
        if answer in every_command:
            browser_commands(answer)

    if answer == "Y" or answer == "y":
        return True
    elif answer == "N" or answer == "n":
        return False
    else:
        enter_command()
def edit_email():
    try:
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\setup\\"

        f_name = "email_setup.txt"
        email_path = path + f_name
        try:
            f = open(email_path, "w")
            f.truncate()
            f.write("not setup")
            f.close()
            print("Email info deleted! Use the email command if you'd like to setup another email..\n")
            enter_command()
        except Exception as e:
            print(e)
            enter_command()
    except Exception as c:
        print(c)
        enter_command()

#---------------------------------------------------------------------------------------------------------------------
def vid_opener():
    path = os.path.dirname(os.getcwd())
    path = path + r"\alles" + "\\"
    path = path + "video_script.py"
    os.system(r"python " + path)

def video_downloader():
    try:
        path1 = os.path.dirname(os.getcwd())
        path1 = path1 + r"\alles" +"\\"

        all_files = os.listdir(path1)
        if "video_script.py" in all_files:
            os.remove(path1 + "video_script.py")

        url = input("Enter the url of the YouTube video you'd like to download: ").strip()
        # open the download file
        if url in every_command:
            browser_commands(url)
        if url == "/helper" or url == "/help":
            video_helper()

        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\\" + r"setup\videodownloader.txt"

        f = open(path, "r")

        # make a script to download the file
        video_script = open(path1 + "video_script.py", "w")

        file_line = f.readline()
        while file_line:
            if "foo" in file_line:
                video_script.write(file_line.replace("foo", "'" + url + "'"))
                file_line = f.readline()
            else:
                video_script.write(file_line)
                file_line = f.readline()

        video_script.close()

        download_thread = threading.Thread(target=vid_opener, args=())
        download_thread.start()

        while True:
            another = input("Enter a command while your video downloads: ").strip()
            browser_commands(another)

    except Exception as e:
        print(e)
        command = input("Your video cannot be downloaded. Type '/h' or '/help' to see possible reasons as to why.").strip()
        if command == "/help" or command == "/h":
            video_helper()
        else:
            browser_commands(command)


def video_helper():
    print("Welcome to the video downloader! Download a YouTube video by simply entering its url. Videos will automatically be downloaded to your Desktop.")
    print("If you're experiencing problems downloading your video, make sure the link is correct. Videos in a playlist may not be downloaded. You'll have to")
    print("find the original video on its own and use that url.")

    enter_command()
#--------------------------------------------------------------------------------------------------------------------
def music_opener():
    path = os.path.dirname(os.getcwd())
    path = path + r"\alles" + "\\"
    path = path + r"\music_script.py"

    os.system(r"python " + path)


def music_downloader():
    try:
        path1 = os.path.dirname(os.getcwd())
        path1 = path1 + r"\alles" + "\\"

        url = input("Enter the url of the YouTube video you'd like to convert to mp3: ").strip()
        if url in every_command:
            browser_commands(url)
        if url == "/help" or url == "/h":
            music_helper()

        # open the download file
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + r"\setup\musicdownloader.txt"
        f = open(path, "r")

        # make a script to download the file
        music_script = open(path1 + "music_script.py", "w+")

        file_line = f.readline()
        while file_line:
            if "foo" in file_line:
                music_script.write(file_line.replace("foo", "'" + url + "'"))
                file_line = f.readline()
            else:
                music_script.write(file_line)
                file_line = f.readline()

        f.close()
        music_script.close()

        download_thread = threading.Thread(target=music_opener, args=())
        download_thread.start()

        #py_opener("music_script.py")

    except Exception as e:
        print(e)
        enter_command()


def music_helper():
    print("Welcome to the music downloader! Here you can download music by simply entering a YouTube video's url. The mp3 files will be downloaded to your Desktop.")

    browser_commands("/y")
#---------------------------------------------------------------------------------------------------------------------
def enter_command():
    command = input("Enter a command: ").strip()
    if command == "/h" or command == "/help":
        browser_helper()
    else:
        browser_commands(command)

#----------------------CREATE MACRO------------------------------------------------------------------------
def create_macro(): #creates personal macro
    print("Welcome to the Script Creator!")
    print("Here are your current scripts: ")

    try:
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_scripts\\"
        #print(os.path.dirname(os.path.realpath(sys.argv[0])))

        all_files = os.listdir(path)

        numberer = 1
        for file in all_files:
            print(str(numberer) + ". " + file.replace(".txt", ""))
            numberer += 1

        print("\n")
        file_name = input("What would you like to name your new script?: ").strip()
        if file_name in every_command:
            browser_commands(file_name.strip())

        _continue = "true"
        while _continue != "false":
            if file_name + ".txt" in all_files:
                print("A file with that name already exists")
                file_name = input("Please enter another file name: ").strip()
            else:
                _continue = "false"


        file_name_actual = file_name + ".txt"
        print("What would you like your script to do? (You can add several commands to one script):")
        #open a file to create macro commands


        file_in_path = os.path.join(path, file_name_actual)

        f = open(file_in_path, "w")
        while_loop = "Y"

        while(while_loop == "y" or while_loop == "Y"):
            print("1. Open a website page")
            print("2. Open an application")
            print("3. Open a file")
            response = input("I choose option: ").strip()
            if response in every_command:
                browser_commands(response.strip())

            if(response == "1" or response =="1."):
                website_link = input("Enter the website link: ").strip()
                if website_link.strip() in every_command:
                    browser_commands(website_link.strip())
                f.write("Website: " + website_link + "\n")
                while_loop = input("Keep going? Y to continue, anything else to stop: ").strip()

            elif (response == "2" or response == "2."):
                application = input("Enter the application's PATH: ").strip()
                if application.strip() in every_command:
                    browser_commands(application.strip())
                f.write("Application: " + application + "\n")
                while_loop = input("Keep going? Y to continue, anything else to stop: ").strip()
            elif (response == "3" or response == "3."):
                file = input("Enter the file's PATH: ").strip()
                if file.strip() in every_command:
                    browser_commands(file.strip())
                f.write("File: " + file + "\n")
                while_loop = input("Keep going? Y to continue, anything else to stop: ").strip()

            else:
                print("Please choose a valid option. ")
            print('\n')
        f.close()
    except Exception as e:
        print(e)


def edit_macro():
    print("Welcome to the Script Editor!")
    print("Here are your current scripts: ")

    numberer = 1
    try:
        list_of_files = []
        file_without_txt = []
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_scripts\\"
        all_files = os.listdir(path)

        for file in all_files:
            list_of_files.append(file)
            file = file.replace(".txt", "")
            file_without_txt.append(file)
            print(str(numberer) + ". " + file)
            numberer += 1

        print("\n")
        chosen_request = input("Which script would you like to edit? Enter the script name: ").strip()
        if chosen_request.strip() in every_command:
            browser_commands(chosen_request.strip())
        while chosen_request not in file_without_txt:
            chosen_request = input("Please enter a valid script name: ").strip()
            if chosen_request in every_command:
                browser_commands(chosen_request.strip())

        keep_going = "y"
        while keep_going == "y" or keep_going == "Y":
            macro = []
            if(chosen_request in file_without_txt):
                index = file_without_txt.index(chosen_request)
                print(line_separator)
                print("Script commands for the file" + " '" + chosen_request + "': ")

                file_in_path = os.path.join(path, chosen_request + ".txt")
                f = open(file_in_path, "r")

                line = f.readline()
                line_counter = 1

                while line:
                    if line.strip() != "":
                        print(str(line_counter) + ": " + line)
                        macro.append(line)
                        line = f.readline()
                        line_counter += 1
                    else:
                        line = f.readline()
                f.close()

                print(line_separator)
                macro_selection = input("Second, which command would you like to edit? Enter the corresponding number: ").strip()
                if macro_selection.strip() in every_command:
                    browser_commands(macro_selection.strip())

                macro_selection = int(macro_selection)
                #make sure the choice is valid
                while macro_selection not in range(1, line_counter + 1):
                    macro_selection = input("Please enter a valid number: ").strip()
                    if macro_selection.strip() in every_command:
                        browser_commands(macro_selection.strip())
                    macro_selection = int(macro_selection)
                    if macro_selection in every_command:
                        browser_commands(macro_selection)

                print(("Previous " + macro[macro_selection - 1]))
                if("Website:" in macro[macro_selection - 1]):
                    new_website = input("New Website Link: ").strip()
                    macro[macro_selection - 1] = "Website: " + new_website
                if "Application: " in macro[macro_selection - 1]:
                    new_app = input("New Application PATH: ").strip()
                    macro[macro_selection - 1] = "Application: " + new_app
                if("File: " in macro[macro_selection - 1]):
                    new_file = input("New File PATH: ").strip()
                    macro[macro_selection - 1] = "File: " + new_file


                #delete everything in the file and rewrite it
                file_in_path = os.path.join(path, list_of_files[index])
                #f = open(list_of_files[index], "w")
                f = open(file_in_path, "w")

                for m in macro:
                    f.write(m + "\n")
                f.close()
                print(macro[macro_selection - 1] + " has been updated! ")
                keep_going = input("Edit another script? Enter Y to keep going or anything else to stop.. : ").strip()
                if keep_going in every_command:
                    browser_commands(keep_going)
            else:
                print("Script file not found.")
    except Exception as e:
        print(e)
        enter_command()

def add_to_macro():
    print("Add more commands to a script!")
    print("Here are your current scripts: ")

    numberer = 1
    try:
        list_of_files = []
        file_without_txt = []
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_scripts\\"

        all_files = os.listdir(path)
        for file in all_files:
            list_of_files.append(file)
            file = file.replace(".txt", "")
            file_without_txt.append(file)
            print(str(numberer) + ". " + file)
            numberer += 1

        print("\n")
        chosen_request = input("Which script would you like to add commands to? Enter the script name: ").strip()
        if chosen_request.strip() in every_command:
            browser_commands(chosen_request.strip())

        while chosen_request.strip() not in file_without_txt:
            chosen_request = input("Please enter a valid script name: ").strip()
            if chosen_request in every_command:
                browser_commands(chosen_request.strip())

        keep_going = "y"
        while keep_going == "y" or keep_going == "Y":
            macro = []
            if (chosen_request in file_without_txt):
                index = file_without_txt.index(chosen_request)
                print(line_separator)
                print("Current commands for script" + " '" + chosen_request + "': ")

                file_in_path = os.path.join(path, chosen_request + ".txt")
                f = open(file_in_path, "r")

                line = f.readline()
                line_counter = 1

                while line:
                    if line.strip() != "":
                        print(str(line_counter) + ": " + line)
                        macro.append(line)
                        line = f.readline()
                        line_counter += 1
                    else:
                        line = f.readline()
                f.close()

                print("What command would you like to add? ")
                print("1. Open a website")
                print("2. Open an application")
                print("3. Open a file")

                print("\n")
                desired_command = int(input("Enter the corresponding number to the desired option: ").strip())
                while desired_command not in range(1,4):
                    if desired_command in every_command:
                        browser_commands(desired_command)
                    else:
                        desired_command = int(input("Please enter a valid corresponding number: ").strip())

                desired_command = str(desired_command)

                if(desired_command == "1"):
                    website = input("Enter the Website URL: ").strip()
                    if website in every_command:
                        browser_commands(website)
                    add_website = "Website: " + website.strip()
                    macro.append(add_website)

                elif desired_command == "2":
                    application = input("Enter the application's PATH: ").strip()
                    if application in every_command:
                        browser_commands(application)
                    add_app = "Application: " + application.strip()
                    macro.append(add_app)

                elif desired_command == "3":
                    file = input("Enter the file's PATH: ").strip()
                    if file in every_command:
                        browser_commands(file)
                    add_file = "File: " + file
                    macro.append(add_file)

                # delete everything in the file and rewrite it
                file_in_path = os.path.join(path, list_of_files[index])
                # f = open(list_of_files[index], "w")
                f = open(file_in_path, "w")

                for m in macro:
                    f.write(m + "\n")
                f.close()
                print("Command added!")
                keep_going = input("Add another command? Enter Y to keep going or anything else to stop.. ").strip()
                if keep_going in every_command:
                    browser_commands(keep_going)
                elif keep_going.lower() != "y":
                    print(line_separator)
                    enter_command()

            else:
                print("Script file not found.")
    except Exception as e:
        print(e)
        enter_command()

def delete_macro():
    try:
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_scripts\\"

        print("Welcome to the Script Deleter!")
        print("Here are your current scripts: ")
        numberer = 1

        all_files = os.listdir(path)

        list_of_files = []
        file_without_txt = []
        for file in all_files:
            list_of_files.append(file)
            file = file.replace(".txt", "")
            file_without_txt.append(file)
            print(str(numberer) + ". " + file)
            numberer += 1

        print(line_separator)

        chosen_request = input("Which script would you like to delete? Enter the script name: ").strip()
        if chosen_request.strip() in every_command:
            browser_commands(chosen_request.strip())
        while chosen_request not in file_without_txt:
            chosen_request = input("Please enter a valid script name: ").strip()
            if chosen_request in every_command:
                browser_commands(chosen_request)
        try:
            os.remove(path + chosen_request + ".txt")
            print("Script successfully deleted")

        except Exception as e:
            print(e)
            enter_command()
    except Exception as excep:
        print(excep)
        enter_command()
#--------------------------------MACRO WHEN COMPUTER STARTS---------------------------------------------
def macro_startup():
    print("Have a script startup when your computer starts!")
    print("Your current scripts are: ")
    try:
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_scripts\\"

        #print(macro_path)
        all_files = os.listdir(path)
        if all_files == []:
            print("You do not have any scripts.")
            command = input("Please enter a command.").strip()
            browser_commands(command)

        numberer = 1

        list_of_files = []
        for f in all_files:
            print(str(numberer) + ". " + f.replace(".txt", ""))
            list_of_files.append(f.replace(".txt", ""))
            numberer += 1

        file_choice = input("Enter the script you'd like to startup: ").strip()
        if file_choice in every_command:
            browser_commands(file_choice)

        while file_choice not in list_of_files:
            file_choice = input("Please enter a correct script name: ").strip()
            if file_choice in every_command:
                browser_commands(file_choice)

        chosen_macro_path = path + file_choice + ".txt"
        chosen_macro = open(chosen_macro_path, "r")

        line = chosen_macro.readline()
        macro_commands = []
        while line:
            if line != "":
                macro_commands.append(line.rstrip("\n"))
                line = chosen_macro.readline()
            else:
                line = chosen_macro.readline()

        # put corresponding file name in the start path
        start_path = os.path.dirname(os.getcwd())
        start_path = start_path + r"\alles" + "\my_startup_scripts\\"

        add_to_start = os.path.join(start_path, file_choice + ".py")

        startup_macro = open(add_to_start, "a+")

        #Macro that the user wants to put in Startup
        path3 = os.path.dirname(os.getcwd())
        path3 = path3 + r"\alles" + "\my_scripts\\"
        original_macro = open(path3 + file_choice + ".txt", "r")
        #Template to copy to new macro

        startup_path = str(os.path.dirname(os.getcwd())) + r"\alles"  + r"\startup\\"

        template = open(startup_path + "template.txt", "r")

        #copy the tempplate first
        temp_line = template.readline()
        while temp_line:
            startup_macro.write(temp_line)
            temp_line = template.readline()
        template.close()

        # add a space between the writings
        startup_macro.write("\n")
        startup_macro.write("\n")

        line = original_macro.readline()
        while line:
            if "Website:" in line:
                url = line[8:]
                url = url.strip()
                #open the website_opener, copy it to the new file, and then replace FILLER with actual url
                file_temp = open(startup_path + "webpage_opener.txt", "r")

                webpage_opener_line = file_temp.readline()
                while webpage_opener_line:
                    if"FILLER" in webpage_opener_line:
                        startup_macro.write(webpage_opener_line.replace("FILLER", "'" + url + "'"))
                        webpage_opener_line = file_temp.readline()
                    else:
                        startup_macro.write(webpage_opener_line)
                        webpage_opener_line = file_temp.readline()
                file_temp.close()

            #---------------------IF APPLICATION------------------
            if "Application:" in line:
                app_name = line[12:]
                app_name= app_name.strip()

                # open the website_opener, copy it to the new file, and then replace FILLER with actual url
                file_temp = open(startup_path+ "app_opener.txt", "r")
                app_opener_line = file_temp.readline()

                #make space for new command
                startup_macro.write("\n")
                startup_macro.write("\n")
                while app_opener_line:
                    if "FILLER" in app_opener_line:
                        startup_macro.write(app_opener_line.replace("FILLER", "'" + url + "'"))
                        app_opener_line = file_temp.readline()
                    else:
                        startup_macro.write(app_opener_line)
                        app_opener_line = file_temp.readline()
                file_temp.close()


            #---------------------------FILE----------------------------------------
            if "File:" in line:
                url = line[5:]
                url = url.strip()

                # add a space between the writings
                startup_macro.write("\n")
                startup_macro.write("\n")

                # open the website_opener, copy it to the new file, and then replace FILLER with actual url
                file_temp = open(startup_path + "file_opener.txt", "r")

                file_opener_line = file_temp.readline()
                while file_opener_line:
                    if "FILLER" in file_opener_line:
                        startup_macro.write(file_opener_line.replace("FILLER", "'" + url + "'"))
                        file_opener_line = file_temp.readline()
                    else:
                        startup_macro.write(file_opener_line)
                        file_opener_line = file_temp.readline()

                file_temp.close()
            #move to next line
            line = original_macro.readline()

        startup_macro.close()
        original_macro.close()
        print("Added script to startup!")
        enter_command()

    except Exception as e:
        print(e)
        enter_command()

#-----------------DELETE FROM STARTUP------------------------------------
def delete_from_startup():
    try:
        # put corresponding file name in the start path
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\my_startup_scripts\\"

        print("Delete a script from your startup")
        print("Here are your current scripts: ")
        numberer = 1

        all_files = os.listdir(path)

        list_of_files = []
        file_without_txt = []
        for file in all_files:
            if ".py" in file:
                list_of_files.append(file)
                file = file.replace(".py", "")
                file_without_txt.append(file)
                print(str(numberer) + ". " + file)
                numberer += 1

        print(line_separator)

        chosen_request = input("Which script would you like to delete? Enter the script name: ").strip()
        if chosen_request.strip() in every_command:
            browser_commands(chosen_request.strip())
        while chosen_request not in file_without_txt:
            chosen_request = input("Please enter a valid script name: ").strip()
            if chosen_request in every_command:
                browser_commands(chosen_request)
        try:
            os.remove(path + chosen_request + ".py")
            print("Script successfully deleted")

        except Exception as e:
            print(e)
            enter_command()
    except Exception as excep:
        print(excep)
        enter_command()

#-------------------------MACRO USER--------------------------------------
def command_user():
    print("Your current scripts are: ")
    try:
        path1 = os.path.dirname(os.getcwd())
        path1 = path1 + r"\alles" + "\\my_scriptss\\"
        #print(path1)
        all_files = os.listdir(path1)

        if all_files == []:
            print("You do not have any personal scripts.")
            command = input("Enter a command: ").strip()
            browser_commands(command)

        numberer = 1

        list_of_files = []
        for f in all_files:
            print(str(numberer) + ". " + f.replace(".txt", ""))
            list_of_files.append(f.replace(".txt", ""))
            numberer += 1

        #print(list_of_files)
        print("\n")
        file_choice = input("Enter the script you'd like to use: ").strip()
        if file_choice in every_command:
            browser_commands(file_choice)

        while file_choice not in list_of_files:
            file_choice = input("Please enter a correct file name: ").strip()
            if file_choice in every_command:
                browser_commands(file_choice)

        chosen_macro_path = path1 + file_choice + ".txt"
        chosen_macro = open(chosen_macro_path, "r")

        line = chosen_macro.readline()
        macro_commands = []
        while line:
            if "Website" in line:
                webpage_opener(line[8:].strip())
                #thread = threading.Thread(target=webpage_opener(line[8:].strip()))
                #thread.start()
                line = chosen_macro.readline()
            elif "Application" in line:
                app_opener(line[12:].strip())
                #thread = threading.Thread(target=app_opener(line[12:].strip()))
                #thread.start()
                line = chosen_macro.readline()
            elif "File" in line:
                file_opener(line[5:].strip())
                #thread = threading.Thread(target=file_opener(line[5:].strip()))
                #thread.start()
                line = chosen_macro.readline()
            else:
                line = chosen_macro.readline()

        chosen_macro.close()

    except Exception as e:
        print(e)
        enter_command()


#------------------------FUNCTIONS FOR SETUP------------------------------------------------------------------
def webpage_opener(website_url):
    try:
        webbrowser.open(website_url)
    except:
        print("Something is not working with the url: " + website_url )

def file_opener(file_path):
    try:
        os.startfile(file_path)
    except:
        print("Something is not working with the file PATH: " + file_path)

def app_opener(app_path):
    try:
        subprocess.call(app_path.strip())
    except:
        print("Something is not working with the application PATH: " + app_path)


#-----------------------------------MOVE STARTUPPATH-------------------------------------------------
def check_StartPath_file():
    s_path = str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split("\\")
    string1 = r"C:\Users"
    string2 = r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    start_path = string1 + "\\" + str(s_path[2]) + string2 + "\\"
    list = listdir(start_path)

    if "StartUpPath.exe" in list:
        return True
    else:
        return False
#------------------------------------PACKAGE INSTALLATIONS---------------------------------------------
def install_packages():
    try:
        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\setup\\"

        os.system(path + "Installation.exe")

        path = os.path.dirname(os.getcwd())
        path = path + r"\alles" + "\setup\\" + "installation_status.txt"
        f = open(path, "w")
        f.write("successfully installed packages")

    except Exception as e:
        print(e)


#-------------------------------------------HOME PAGE----------------------------------------------------
def home():
    print("************Welcome to alles, the Simple Script Maker and Performer!*************")
    print("--------------------------------Browser Commands--------------------------------")
    browser_commands_list = ["Google: '/g' '/google' '/googler'", "YouTube: '/y' '/yt' '/youtube'",
                             "Email: '/e' '/email'", "Delete Email Info: '/de' '/deleteemail'",
                             "Download Music: '/m' '/dm'", "Download Videos: '/v' '/video'"]
    for stuff in browser_commands_list:
        print(stuff)
    print("--------------------------------Script Commands----------------------------------")
    print("Create New Script: '/cs' '/create' '/createscript'")
    print("Open Script: '/os' '/open'")
    print("Add to Existing Script: '/as' '/addscript' ")
    print("Edit Existing Script: '/es' '/editscript'")
    print("Delete Existing Script: '/ds' '/deletescript' ")
    print("Start Script when Computer Starts: '/ss' '/startup' ")
    print("Delete Script from Startup: '/sd' '/startupdelete")
    print("------------------------------Additional Commands-------------------------------")
    print("List All Commands: '/l' '/list'")
    print("Clear Screen: '/clear'")
    print("Quit program: '/q' '/quit'")
    print("Help/About: '/h' '/help'")
    print("Change Color of Console and Text: '/cc' '/changecolor' ")
    print("Facebook: '/f' , Twitter: '/t' , Instagram: '/i' , Reddit: '/r'")
    print("--------------------------------------------------------------------------------\n")


    option_answer = input("Enter a command: ").strip()
    if option_answer == "/help" or option_answer == "/h":
        helper()
        user_input = input("Enter a command: ").strip()
        browser_commands(user_input)
    else:
        while(option_answer.strip() != "/q") or (option_answer.strip() != "/quit"):
            browser_commands(option_answer.strip())


#----------CHANGE COLOR OF TERMINAL
os.system('mode con: cols=85 lines=33')

try:
    color_path = os.path.dirname(os.getcwd())
    color_path = color_path + r"\alles" + "\setup\\" + "console_color.txt"
    f = open(color_path, "r")
    line = str(f.readline())
    os.system(line)
except Exception as e:
    print(e)

home()

#-----------------------------------

input('Press ENTER to exit')



