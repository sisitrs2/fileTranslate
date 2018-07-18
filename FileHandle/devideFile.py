import os

def devideFile(path, jump_num = 3500): #3500 is usually working (under googles limit).
    try:
        #get file to devide.
        if path.find('.') != -1:
            parts = path.split('.')
            file_type = "." + parts[1] #.txt || .md ||
            path = parts[0]
            file = open(path + file_type, "r")
        else:
            file_type = ""
            file = open(path, "r")
    except IOError:
        print "No such file in direcory, Try again."
    data = unicode(file.read())
    i = 1
    while data:
        temp = open((path + "(" +  str(i) + ")") + file_type, "a")
        temp.write(data[:jump_num]) #append jump_num characters
        temp.close()
        data = data[jump_num:]
        i += 1
    file.close()
    os.remove(path + file_type)

if __name__ == '__main__':
    print "Hello, please enter file path:"
    path = raw_input()
    devideFile(path)
    print "File was devided successfuly."
