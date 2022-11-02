from sys import argv
from os import rename, listdir
import re

def main():
    if len(argv) < 2:
        print("you fucked up")
        exit()
    directory = argv[1]
    name_list = []
    regexp = re.compile(r'S\d\d[\s.-]?E\d\d')
    regex_TG = re.compile(r'\[?\d?\d[xX]\d\d\]?')
    for file in listdir(directory):
        if file == argv[0]:
            continue
        #TODO: use regex to rename so it works on more than just dexter
        
        if regexp.search(file):
            print("Found correct formating for: " + file)
            continue
        if regex_TG.search(file):
            new_name = rename_topgear(file)
        #if "Top Gear" in file:
        #    new_name = rename_topgear(file)
        if "Dexter" in file:
            new_name = rename_dexter(file)
        name_list.append([file, new_name]) # type: ignore
        #rename(file, new_name)
    if checkprint(name_list):
        batch_rename(name_list)
    else:
        print("Exiting!")
        
def batch_rename(name_list):
    for item in name_list:
        rename(item[0], item[1])
    print("successfully finished")
    
def checkprint(name_list):
    for item in name_list:
        print(item)
    test = input("does everything look right? (y/n)? ")
    if test.lower() == 'y':
        return True
    elif test.lower() == 'n':
        for i in range(len(name_list)):
            print(i, name_list[i])
        
        wrong = input("Enter wrong indicies (eg, 1 3 8 10): ")
        wrong = wrong.split().sort()[::-1] # type: ignore
        #TODO: remove wrong values from list
    
def rename_dexter(file):
    file_holder = file.split()
    if int(file_holder[2]) < 10:
        file_holder[2] = 'S0'+file_holder[2]
    else: 
        file_holder[2] = 'S'+file_holder[2]
    # if int(file_holder[4]) < 10:
    #     file_holder[4] = 'E0'+file_holder[4]
    # else:
    file_holder[4] = 'E'+file_holder[4]
    file_holder[2] = file_holder[2] + file_holder[4]
    file_holder.pop(4)
    file_holder.pop(3)
    file_holder.pop(1)
    file_holder = ' '.join(file_holder)
    return file_holder

def rename_topgear(file):
    values = re.findall(r'\[?\d?\d[xX]\d\d\]?', file)
    print(values[0])
    values[0] = values[0].strip('[]').lower()
    new_values = values[0].split("x")
    final = 'S'+new_values[0]+'E'+new_values[1]
    finalfile = file.replace(values[0], final)
    return(finalfile)


if __name__ == "__main__":
    main()
    