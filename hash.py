from passlib.hash import nthash, lmhash
import hashlib

print(r"                                                                                    ,----,") 
print(r"        ,--,                                 ,--,         ,--.                    ,/   .`| ")
print(r"      ,--.'|   ,---,       .--.--.         ,--.'|       ,--.'|   ,---,          ,`   .'  : ") 
print(r"   ,--,  | :  '  .' \     /  /    '.    ,--,  | :   ,--,:  : |  '  .' \       ;    ;     / ")
print(r",---.'|  : ' /  ;    '.  |  :  /`. / ,---.'|  : ',`--.'`|  ' : /  ;    '.   .'___,/    ,'  ")
print(r"|   | : _' |:  :       \ ;  |  |--`  |   | : _' ||   :  :  | |:  :       \  |    :     |   ")
print(r":   : |.'  |:  |   /\   \|  :  ;_    :   : |.'  |:   |   \ | ::  |   /\   \ ;    |.';  ;   ")
print(r"|   ' '  ; :|  :  ' ;.   :\  \    `. |   ' '  ; :|   : '  '; ||  :  ' ;.   :`----'  |  |   ")
print(r"'   |  .'. ||  |  ;/  \   \`----.   \'   |  .'. |'   ' ;.    ;|  |  ;/  \   \   '   :  ;   ")
print(r"|   | :  | ''  :  | \  \ ,'__ \  \  ||   | :  | '|   | | \   |'  :  | \  \ ,'   |   |  '   ")
print(r"'   : |  : ;|  |  '  '--' /  /`--'  /'   : |  : ;'   : |  ; .'|  |  '  '--'     '   :  |   ")
print(r"|   | '  ,/ |  :  :      '--'.     / |   | '  ,/ |   | '`--'  |  :  :           ;   |.'    ")
print(r";   : ;--'  |  | ,'        `--'---'  ;   : ;--'  '   : |      |  | ,'           '---'      ")
print(r"|   ,/      `--''                    |   ,/      ;   |.'      `--''                        ")
print(r"'---'                                '---'       '---'                                     ")

print()

print(r"               .__                                  __           .__                  .__                   __  ._.")
print(r"__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____   |  |__ _____    _____|  |__   ____ _____ _/  |_| |")
print(r"\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  |  |  \\__  \  /  ___/  |  \ /    \\__  \\   __\ |")
print(r" \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> ) |   Y  \/ __ \_\___ \|   Y  \   |  \/ __ \|  |  \|")
print(r"  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/  |___|  (____  /____  >___|  /___|  (____  /__|  __")
print(r"             \/          \/            \/     \/                      \/     \/     \/     \/     \/     \/      \/")

print()
print()

print("💩 What type of hash are you planning on using: ") 
print("1. LM (Lan manager)" )
print("2. NTLM (NT Lan manager)")
print("3. MD5")
print("4. SHA-1")
print("5. SHA-256")
hash_type = int(input("6. SHA-512 : "))

print()

def ntlm():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = nthash.hash(lines[i].strip())
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break
        


def lm():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = lmhash.hash(lines[i].strip())
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break

def MD5():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = hashlib.md5(lines[i].strip().encode()).hexdigest()
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break

def sha1():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = hashlib.sha1(lines[i].strip().encode()).hexdigest()
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break

def sha256():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = hashlib.sha256(lines[i].strip().encode()).hexdigest()
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break


def sha512():
    text = input("Enter your hashed text: ")
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lines = [line.strip() for line in file]
    
    for i in range(len(lines)):
        x = hashlib.sha512(lines[i].strip().encode()).hexdigest()
        if x == text:
            print("Your hashed password is:", lines[i].strip())
            break
        elif x == len(lines):
            print("Sorry! your password has not been found.")
            break


if hash_type == 1:
    lm()
elif hash_type == 2:
    ntlm()
elif hash_type == 3:
    MD5()
elif hash_type == 4:
    sha1()
elif hash_type == 5:
    sha256()
elif hash_type == 6:
    sha512()
else:
    print("Wrong input!")
