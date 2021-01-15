# Description

includeMergerP is a Python script to merge many included files in one file. It takes an input files and an output file name. At the end of the script, the output files will contain the input filese with "include" lines replaced with the included file's content.

It can be used recursively

# How to use it:

Input must be formatted as:

python includeMergerP.py fileDaLeggere fileDestinazione [options]

The content of the readFile is copied in the output, replacing "include.." lines with the respective file's content

OPTIONS

--recursive -> the script is executed also on the included files recursively
