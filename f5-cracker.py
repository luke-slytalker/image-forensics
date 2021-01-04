import os, sys, subprocess, math, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image to try to crack")
ap.add_argument("-p", "--pass", required=True, help="list of passwords to try")

args = vars(ap.parse_args())

img = args["image"]
pwlist = args["pass"]


with open(pwlist) as pw:  # open the file
    pword = pw.readline().strip()  # read a line in
    cnt = 1  # set our COUNTER to the 1st position

    while pword:
        # while we have a password to try, we keep trying.

        # build our command as an array of values
        comm = ['java', '-jar', 'f5.jar', 'x', '-p', pword, img]

        # output the progress to our user
        print("Try # {}: Password:  {}".format(cnt, pword.strip()))

        # run our command and pipe the output back to a variable we'll call RESULT
        result = subprocess.Popen(comm, stdout=subprocess.PIPE).communicate()[0]

        if str(result).find("only") > 0:
            # print("wrong password.")
            pword = pw.readline().strip()  # set the next line
            cnt += 1  # increase the counter

        else:
            # holy crap, we found something!!
            with open('output.txt', 'r') as f:
                file_check = f.read()

            print("")
            print("------- !!!FOUND PASSWORD!!! -------")
            print("")
            print("Password:    [  " + str(pword) + "  ]")
            print("Try # " + str(cnt))
            print("")
            print(str(file_check))
            print("")
            pword = ""  # clear this variable and break out of our loop.

print("------- CRACKING COMPLETE -------")