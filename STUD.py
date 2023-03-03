# STUD - Student's Unique Depression

import userInterface as ui
import checkCourse as cc
import gradeDistr as gd

def stud():
    sel = ui.mainMenu()
    #print("Selection:", sel)

    while sel != -1:
        ui.clearScr()

        if sel == -1:
            quit()
        elif sel == 1:      # 1. Check open courses
            cc.displayCourses()
        elif sel == 2:      # 2. Grade distributions
            gd_sel = ui.gradeDistrMenu()

            while gd_sel != 0:
                if gd_sel == -1:
                    quit()
                elif gd_sel == 1:       # Display a single course
                    gd.getFileName()
                elif gd_sel == 2:       # List all courses
                    gd.displayImg()
                else:
                    print("Enter a valid number!")

                input("\nPress ENTER to continue...\n")
                ui.clearScr()
                gd_sel = ui.gradeDistrMenu()
        else:
            print("Enter a valid number!")

        input("\nPress ENTER to continue...\n")
        ui.clearScr()
        sel = ui.mainMenu()

if __name__ == '__main__':
    stud()