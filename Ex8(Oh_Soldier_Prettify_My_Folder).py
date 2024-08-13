import os
from time import sleep

def soldier(path, exception, format):
    count = 0
    files = os.listdir(path)
    for item in files:
        f = open(item)
        f.close()
        r = open(exception)
        read = r.read()
        r.close()
        capital = item.capitalize()

        if item not in read and item != exception:
            os.rename(item, capital)

        if item.endswith(format):
            count += 1
            new_name = f"{str(count)}{format}"
            os.rename(item, new_name)

        elif item in read:
            pass


if __name__ == '__main__':
    print("Welcome! I am 'Soldier' the folder prettifier.")
    path1 = input("Enter the path of the folder.\n")
    if os.path.exists(path1) == False:
        print("No such path found.\n")

    else:
        os.chdir(path1)
        exception1 = input("Enter the file with the exceptions which are to be skipped(The file must be in the same folder).\n")

        if os.path.isfile(exception1) == False:
            print("No such file found.\n")

        else:
            format1 = input("Enter the file format you want to rename as ascending numbers.\n")

            if "." not in format1:
                print("Invalid file format/missing '.' keyword.\n")

            else:
                print("Prettifying your folder now...")
                sleep(2)
                soldier(path1,exception1,format1)
                print("I have prettified your folder!!!")
