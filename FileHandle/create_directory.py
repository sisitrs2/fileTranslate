import os, sys

def create_directory(path):
    parts = path.split('.')
    file_type = parts[1] #.txt || .md ||
    path = parts[0] #dir1/dir2/file
    path_parts = path.split('/')
    file_name = path_parts[-1]
    path_to_file = path_parts[:-1] # add path up until file name
    path_to_file = '/'.join(path_to_file)
    if not os.path.exists("translated-english"):
        os.makedirs("translated-english")
    return path_to_file + "translated-english/" + file_name + "." + file_type

