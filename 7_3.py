# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    if fname == "na na boo boo":
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        print("file doesn't exist" ,fname)
        quit()

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    position = line.find(':')
    number = float(line[position+1:])
    count = count + 1
    total = total + number

average = total/count
print("Average spam confidence:", average)
