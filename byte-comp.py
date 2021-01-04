import sys, os, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image to compare")
ap.add_argument("-s", "--second", required=True, help="second input image to compare")

args = vars(ap.parse_args())

f1 = args["first"]
f2 = args["second"]


with open(f1, 'rb') as f:
    str1 = f.read()

with open(f2, 'rb') as f2:
    str2 = f2.read()

file1 = str1
file2 = str2
str1 = str(str1)[2:]
str2 = str(str2)[2:]

# strip out the HEX prefix
pic1 = str(str1).split('\\x')
pic2 = str(str2).split('\\x')

#strip out any blanks
while "" in pic1: pic1.remove("")
while "" in pic2: pic2.remove("")

n = 0
in_a_row = 0
byte_string = ''
same_list = list()
no_match = 0
count_list = list()

# figure out which file is the larger of the two
if len(file1) > len(file2):
    bigger = pic1
    smaller = pic2
elif len(file1) < len(file2):
    bigger = pic2
    smaller = pic1
else:
    bigger = pic1
    smaller = pic2


for line in bigger:
    try:
        if line != smaller[n]:

            if (in_a_row > 2) and (no_match == 0):
                #print(byte_string)
                same_list.append(byte_string)
                count_list.append(str(n - in_a_row) + "_to_" + str(n))
                byte_string = ''

            n += 1
            in_a_row = 0
            no_match += 1

        else:
            no_match = 0
            in_a_row += 1
            byte_string += line + " "
            #print(in_a_row, "BYTE :", n + 1, f1, ":", line, "|", f2, ":", pic2[n])
            n += 1
    except IndexError:
        pass

c = 0
for i in same_list:
    print(count_list[c], ":", i)
    c += 1

