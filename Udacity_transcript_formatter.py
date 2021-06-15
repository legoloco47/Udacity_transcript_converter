import sys
import os

print(sys.argv[1])
lecture = sys.argv[1]

if lecture.endswith("/"):
        lecture = lecture[:-1]

newfile = open(lecture + ".doc", "w+")
print("newfile: ", newfile)
# Needs slash at the end of folder name
if not lecture.endswith("/"):
	lecture += '/'

directory = os.getcwd() +'/' + lecture

os_directory = os.listdir(directory)

for fn in os.listdir(directory):
        if fn[1] == ' ':
                src = directory + "/" + fn
                dst = directory + "/0" + fn
                os.rename(src, dst)

for filename in sorted(os.listdir(directory)):
        if filename[0] == '.': continue
        lecture_name = filename.split(" - ")
        lecture_name_edited = lecture_name[0] + " - " + lecture_name[1]
        newfile.write("\n\n------------------------------------\n"+lecture_name_edited)
        newfile.write("\n------------------------------------\n")
        # print ("This is the file: ", filename)
        with open(lecture + "/" +filename) as f:
                for content in f:
                        if not content[:-1].isdigit():
                                if content[0].isdigit() and content[1].isdigit() and content[2] == ':':
                                        continue
                                else:
                                        if content[0] != '\n':
                                                if (content[len(content)-2] != "."):
                                                        s = list(content)
                                                        s[len(content)-1] = " "
                                                        content = "".join(s)
                                                newfile.write(content)
        print("Written file " + lecture_name_edited)
        f.close()

newfile.close()