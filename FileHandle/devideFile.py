import os

def devideFile(path):
    jump_num = 3500 #seem to not cause any troubles. (3850 did, depends on the file) 
    while True:
        try:
            #get file to devide.
            parts = path.split('.')
            file_type = parts[1] #.txt || .md ||
            path = parts[0]
            file = open(path + "." + file_type, "r")
            break
        except IOError:
            print "No such file in direcory, Try again."
    data = unicode(file.read())
    i = 1
    while data:
        temp = open((path + "(" +  str(i) + ")") + "." + file_type, "a")
        temp.write(data[:jump_num]) #append jump_num characters
        temp.close()
        data = data[jump_num:]
        i += 1
    file.close()
    os.remove(path + "." + file_type)


