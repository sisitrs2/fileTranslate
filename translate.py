# -*- coding: utf-8 -*-
from googletrans import Translator
from time import sleep
import requests
from FileHandle.devideFile import devideFile
from FileHandle.combineFile import combineFile
from FileHandle.create_directory import create_directory
import sys 


def translate_all(path):
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
    reload(sys)  
    sys.setdefaultencoding('utf8')
    trans = Translator()
    
    path = raw_input("Hello user, \nEnter file to translate  path: \n")
    file = open(path, "r")
    string = file.read()
    if len(string) > 3500: #5k maximum google server can translate (less in unicode)
        file.close()
        devideFile(path)
        print "Large file, please wait (this can take a minute).."
        output = translate_all(path)
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
