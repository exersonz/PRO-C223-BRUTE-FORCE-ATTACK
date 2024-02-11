import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath) # initializing ZipFile obj
global result
result = 0
global tried
tried = 0
c = 0

# checking if the zipped file has an encrypted password
if not zipf:
    print('The zipped file/folder is not password protected! You can successfully open it!')
else:
    starttime = time.time()
    wordlistFile = open('wordlist.txt', 'r')
    body = wordlistFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf8').strip()
        c += 1
        print(f'Trying to decode the password by using: {word}')
        try:
            with zipfile.ZipFile(folderpath, 'r') as zf:
                zf.extractall(pwd=password)
                print(f'Success! The password is: {word}')
                endtime = time.time()
                result = 1

                if result == 1:
                    duration = endtime - starttime
                    print(f'Congrats! Password found after trying {c} possible combinations in {duration} seconds')
                elif result == 0:
                    duration = endtime - starttime
                    print(f"Sorry, password not found. A total of {c} possible combinations tried in {duration} seconds. Password is not of 4 characters")
                break
        except:
            pass