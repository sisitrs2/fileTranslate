import os

def combineFile(path):
    #get file to combine.
    if path.find('.') != -1:
        parts = path.split('.')
        file_type = "." + parts[1] #.txt || .md ||
        path = parts[0]
    else:
        file_type = ""
    file = open(path + file_type, "a+")

    i = 1
    while True:
        try:
            temp = open(path + "(" + str(i) + ")" + file_type, "r") #file(1).txt 
            file.write(temp.read())
            temp.close()
            os.remove(path + "(" + str(i) + ")" + file_type)
            i += 1
        except IOError:
            break
    file.close()

if __name__ == '__main__':
    print "Hello, please enter file path"
    path = raw_input()
    combineFile(path)
    print "file was combine successfuly."
