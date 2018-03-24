import os

def main():
    #get file to combine.
    path = raw_input("Enter file path: ")
    parts = path.split('.')
    file_type = parts[1] #.txt || .md ||
    path = parts[0]
    file = open(path + "." + file_type, "a+")
    i = 1
    while True:
        try:
            temp = open(path + "(" + str(i) + ")" + "." + file_type, "r") #file(1).txt 
            file.write(temp.read())
            temp.close()
            os.remove(path + "(" + str(i) + ")" + "." + file_type)
            i += 1
        except IOError:
            break
    file.close()

main()

