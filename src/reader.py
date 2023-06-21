# Reads a shopping list and parses it into a list of items
def read_file(file_path):
    f = open(file_path, "r")
    file_contents = f.read()
    file_contents_list = file_contents.split('\n')
    f.close()
    return file_contents_list
