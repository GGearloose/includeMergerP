import os
import sys

# 
# Input must be formatted as:
#
# python componiInclude.py fileDaLeggere fileDestinazione [options]
#
# The content of the readFile is copied in the output, replacing "include.." lines with the respective file's content
#
# OPTIONS
#
# --recursive -> the script is executed also on the included files recursively
#

instructions = "        Usage: python componiInclude.py fileDaLeggere fileDestinazione [options]\n\n\
        OPTIONS:\n\n\
        --recursive: the script is executed also on the included files recursively\n\n"



if len(sys.argv) <= 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print(instructions)
    exit()

# File to read initially
fileToRead = sys.argv[1]

if len(sys.argv) == 2:
    print("Destination file missing\n")
    print(instructions)
    exit()
else:
    # Output file
    fileToWrite = open(sys.argv[2], "w")

# Taking flag option
option = None
if len(sys.argv) > 3:
    option = sys.argv[3]

# Various parameters declaration
numberOfIncluded = 0
includedFilesList = []

# Read name of the included file
def readNameIncluded(stringa):
    global includedFilesList
    fileToInclude = ''
    start = False
    end = False
    for c in stringa:
        if end:
            break
        if not start and (c == "\"" or c == "\'"):
            start = True
        else:
            if start and (c == "\"" or c == "\'"):
                end = True
            else:
                if start and c != "\"" and c != "\'":
                    fileToInclude = fileToInclude+c
    includedFilesList.append(fileToInclude)
    return fileToInclude

# Copy input file in the specified output
def unwrap(inputFile):
    global numberOfIncluded
    inputFileOpened = open(inputFile, 'r')
    for readLine in inputFileOpened:
        if readLine.count('include') > 0:
            numberOfIncluded += 1
            fileToInclude = readNameIncluded(readLine)
            fileToIncludeOpened = open(fileToInclude, "r")
            fileToWrite.write("\n//START AUTO-INCLUDE -- "+fileToInclude+"\n\n")
            if option == '--recursive':
                unwrap(fileToInclude)
            else:
                openNotRecursive = open(fileToInclude)
                for line in openNotRecursive:
                    fileToWrite.write(line)
                openNotRecursive.close()
            fileToWrite.write("\n//END AUTO-INCLUDE -- "+fileToInclude+"\n\n")
        else:
            fileToWrite.write(readLine)
    inputFileOpened.close()

unwrap(fileToRead)


fileToWrite.close()

print("\nDone\n")
print("Number of included files unwrapped: "+str(numberOfIncluded))

if len(includedFilesList) > 0:
    print("Included files unwrapped: ")
    for included in includedFilesList:
        print("    - "+included)
else:
    print("Included files unwrapped: none")
print("\nOutput file: "+str(sys.argv[2]))
print('\n')

exit()
