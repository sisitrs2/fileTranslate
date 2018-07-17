# -*- coding: utf-8 -*-
from googletrans import Translator
from time import sleep
import requests
from FileHandle.devideFile import devideFile
from FileHandle.combineFile import combineFile
from FileHandle.create_directory import create_directory
import sys 


def translate_all(path, jump_num = 3500):
    trans = Translator()
    parts = path.split('.')
    file_type = parts[1] #.txt || .md ||
    path = parts[0]
    output = ""
    string = ""
    i = 1
    while True: #run as long as there are files left.
        try:
            temp = open(path + "(" + str(i) + ")" + "." + file_type, "r") #file(1).txt 
            string = unicode(temp.read()) #for code readability
            try:
                translated = trans.translate(string) #for code readability (temp.read() => string)
		output += translated.text
            except requests.exceptions.ConnectionError:
                print "Connection refused"
                print "You might not have internet connection"
                print "Or there's a problem with google translate server."
            temp.close()
            i += 1
        except IOError:
            break
        sleep(0.2) #just so google wouldn't block client.
    return output


def main():
    jump_num = 3500
    not_work = True
    file_not_exist = True
    reload(sys)  
    sys.setdefaultencoding('utf8')
    trans = Translator()
    
    print "Hello user, "
    while file_not_exist: 
        path = raw_input("Enter file to translate  path: \n")
        try:
            file = open(path, "r")
            file_not_exist = False
        except IOError:
           print "File does not exist, try again\n" 
    string = file.read()
    if len(string) > jump_num: #5k maximum google server can translate (less in unicode)
        file.close()
        devideFile(path, jump_num)
        print "Large file, please wait (this can take a minute).."
	while not_work:
            try:
                output = translate_all(path, jump_num)
                print "Worked fine"
                not_work = False
            except ValueError:
                print "Fixing JSON problems.."
		combineFile(path)
                jump_num -= 100
		devideFile(path, jump_num)
                continue
        combineFile(path)
    else:
        file.close()
        try:
            output = trans.translate(string).text
        except requests.exceptions.ConnectionError:
            print "Connection refused"
            print "You might not have internet connection"
            print "Or there's a problem with google translate server."
    path = create_directory(path)#creates a directory named translate-english and returns path with directory
    trans_file = open(path, "a+")  #translated file
    trans_file.write(output)
    print "File was translated successfully."
    print "You can find your file under the: " + path + " directory." 


main()
