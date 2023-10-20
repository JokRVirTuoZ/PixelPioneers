from scripts._class.Map import *



def exemple():
    source_file = open("acsii/loc/menu", "r")
    m = Map(40, 15)
    valid_map = m.check_file(source_file)
    if valid_map:
        m.file_read(source_file)
        m.display()


if __name__ == '__main__':
    testclick()
