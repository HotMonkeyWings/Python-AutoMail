import smtplib
from email.message import EmailMessage
import imghdr



ifile = open('Emails.txt','r')

while 1:
    msg = EmailMessage()
    msg['Subject'] = 'School Debutante 2019'
    msg['From'] = 'lndautomated@gmail.com'
    
    line = ifile.readline()
    if not line:
        ifile.close()
        break
    line = line.split('-')
    print(line)
    fname = line[0]+'.png'
    msg['To'] = line[1].rstrip('\n')
    m = str("Hello "+line[0]+",\nThis is from the Literary and Debating Club, NIT-Calicut.\nAttached to this mail is a certificate for your energetic participation in School Debutante 2019!\nWe hope you had a wonderful time!\n\nThe Literary and Debating Club,\nNIT Calicut,\nKerala\n\n Rai if u received this, that means the mail is a success! This is how it'll look like.")
    msg.set_content(m)

    with open(fname, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype ='image', subtype = file_type,filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('lndautomated@gmail.com','sfwibkqwtlatygxj')
        smtp.send_message(msg)
        print(line[0])
        

    
