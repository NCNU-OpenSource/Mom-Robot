#!/usr/bin/python
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Which email address want to send
# 明文的帳密
to = 'liawyuzher99@gmail.com'

# Using specific mail account
user = 'liawyuzher99@gmail.com'
password = 'igcbatwyyltqpsjk'
# SMTP command
smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpserver.login(user, password)
today = datetime.date.today()

# Linux Specific shell command
arg='hostname -I'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[0].decode("utf-8")
my_ip = 'Your ip is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = user
msg['To'] = to
smtpserver.sendmail(user, [to], msg.as_string())
smtpserver.quit()