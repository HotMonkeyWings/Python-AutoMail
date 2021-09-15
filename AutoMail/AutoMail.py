import smtplib
from email.message import EmailMessage
import imghdr



ifile = open('Emails.txt','r')  # Save in the format of name-email (separated by '-')

while 1:
    msg = EmailMessage()
    msg['Subject'] = 'School Debutante 2019'
    msg['From'] = 'dev_b180297cs@nitc.ac.in'
    
    line = ifile.readline()     # Reads the names and emails
    if not line:
        ifile.close()
        break
    line = line.split('-')
    print("Sending mail to", line[0])
    msg['To'] = line[1].rstrip('\n')        # Sets the recipient's mail       
    m = str("Hello "+line[0]+",\nThis is from the Literary and Debating Club, NIT-Calicut.\nAttached to this mail is a certificate for your energetic participation in School Debutante 2019!\nWe hope you had a wonderful time!\n\nThe Literary and Debating Club,\nNIT Calicut,\nKerala\n\n Rai if u received this, that means the mail is a success! This is how it'll look like.")
    msg.set_content(m)

    # Attachments
    fname = line[0]+'.png'              # File name here
    with open(fname, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype ='image', subtype = file_type,filename = file_name)      # Specify file name, rest is taken care of

    # Login details (Use ENV variables if necessary)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('email','password')      # Enable access on https://myaccount.google.com/lesssecureapps
        smtp.send_message(msg)
        print('Mail has been sent to',line[0])
        

    
