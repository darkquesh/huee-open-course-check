from PIL import Image
from pathlib import *
import glob
import os

def displayImg():
    image = Image.open('grade_distr/ELE203_21-22_Fall_AY.jpeg')
    image.show()

def getFileName():
    fdir = os.listdir('grade_distr')        # File directory, ensure that you have 'grade_distr' directory
    filenames = [os.path.splitext(f)[0] for f in fdir]

    for c in range(len(filenames)):
        fileName = filenames[c]
        #print(filenames[c])

        dist = fileName.split("_")
        
        course = dist[0]
        term = "20" + dist[1] + " " + dist[2]
        instr = dist[3]
        
        print(course, "\n", end='')
        print(term, "\n", end='')
        print(instr, "\n", end='')
        print("")

if __name__ == '__main__':
    getFileName()