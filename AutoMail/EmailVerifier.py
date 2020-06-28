from validate_email import validate_email

ifile = open("Emails.txt",'r')
print("The following are invalid emails:")
while 1:
    line = ifile.readline().rstrip('\n')
    if not line:
        ifile.close()
        break
    line = line.split("-")
    em = line[1].rstrip(" ")
    valid = validate_email(em,verify=True)
    if not valid:
        print(line)
