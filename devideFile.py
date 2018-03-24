import os

def main():
    jump_num = 15000
    while True:
        try:
            #get file to devide.
            path = raw_input("Enter file path: ")
            parts = path.split('.')
            file_type = parts[1] #.txt || .md ||
            path = parts[0]
            print file_type
            file = open(path + "." + file_type, "r")
            break
        except IOError:
            print "No such file in direcory, Try again."
    data = file.read()
    i = 1
    while data:
        temp = open((path + "(" +  str(i) + ")") + "." + file_type, "a")
        temp.write(data[:jump_num]) #append jump_num characters
        temp.close()
        data = data[jump_num:]
        i += 1
    file.close()
    os.remove(path + "." + file_type)

main()

