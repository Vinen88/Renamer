from sys import argv
from os import rename, listdir, path
import re

def main():
    if len(argv) < 2:
        print("you fucked up")
        exit()
    directory = argv[1]
    name_list = []
    regexp = re.compile(r'S\d\d[\s.-]?E\d\d')
    regex_TG = re.compile(r'\[?\d?\d[xX]\d\d\]?')
    media_regex = re.compile(r'^.*\.(mov|wmv|flv|mp4|avi|mkv)$')
    for file in listdir(directory):
        new_name = None
        if file == argv[0]:
            continue
        #TODO: use regex to rename so it works on more than just dexter
        if not media_regex.search(file):
            print(f"non-media file - {file}")
            continue
        if regexp.search(file):
            print(f"Found correct formating for: {file}")
            continue
        if regex_TG.search(file):
            new_name = rename_topgear(file)
        elif "Dexter" in file:
            new_name = rename_dexter(file)
        if name_list is not None:
            name_list.append([file, new_name]) 
    checkprint(name_list, directory)
        
def batch_rename(name_list, dir):
    for item in name_list:
        rename(path.join(dir, item[0]), path.join(dir, item[1]))
    print("successfully finished")
    
def checkprint(name_list, dir):
    for item in name_list:
        print(item)
    test = input("does everything look right? (y/n)? ")
    if test.lower() == 'y':
        batch_rename(name_list, dir)
    elif test.lower() == 'n':
        while True:
            for i in range(len(name_list)):
                print(i, name_list[i])
            wrong = input("Enter wrong indicies(eg, 1 3 8 10)(y if all are correct): ")
            if wrong.lower() == 'y':
                break
            if wrong is not None:
                wrong = wrong.split()
                wrong.sort()
                wrong = wrong[::-1]
                print(f"removing {wrong} indicies")
                for ind in wrong:
                    del name_list[int(ind)]
        batch_rename(name_list, dir)
            
        
        
    
def rename_dexter(file):
    file_holder = file.split()
    if int(file_holder[2]) < 10:
        file_holder[2] = 'S0'+file_holder[2]
    else: 
        file_holder[2] = 'S'+file_holder[2]
    file_holder[4] = 'E'+file_holder[4]
    file_holder[2] = file_holder[2] + file_holder[4]
    file_holder.pop(4)
    file_holder.pop(3)
    file_holder.pop(1)
    file_holder = ' '.join(file_holder)
    return file_holder

def rename_topgear(file):
    values = re.findall(r'\[?\d?\d[xX]\d\d\]?', file)
    values[0] = values[0].strip('[]').lower()
    new_values = values[0].split("x")
    final = 'S'+new_values[0]+'E'+new_values[1]
    finalfile = file.replace(values[0], final)
    return(finalfile)


if __name__ == "__main__":
    main()
    