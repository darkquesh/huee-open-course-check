from os import system, name

def clearScr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def mainMenu():
    print("** STUD - Student's Unique Depression **\n")
    print("- Select any! - (-1 to exit)")
    print("1. Open courses this term")
    print("2. Grade distributions over the years")

    sel = int(input("\n"))
    #print("Selection ", sel)

    return sel

def gradeDistrMenu():
    print("** Select any! ** (-1 to exit, 0 to return)\n")
    print("1. Display a single course")
    print("2. List all courses")

    sel = int(input("\n"))

    return sel

if __name__ == '__main__':
    mainMenu()
