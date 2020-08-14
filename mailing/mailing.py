# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:44:55 2020

@author: noelp
"""

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template


def create_conection(user,passwd):
        smtp = smtplib.SMTP("smtp.live.com", 587)
        smtp.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        smtp.starttls() #Puts connection to SMTP server in TLS mode
        smtp.ehlo()
        smtp.login(user, passwd)
        return smtp


def send_mail(send_from, send_to, subject, mail, arg, smtp, files=None):
    '''
    mail.html example
    <html>
    Something
    ...
    Hi {{name}}
    ....
    Something
    </html>
    
    where {{name}} is the parameter to be render
    '''
    
      
    ## creo mi clase mensaje
    msg = MIMEMultipart("alternative") 
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = subject
    
    ## html mail body

    template = Template(open(mail,'r').read())
    temp_rend = template.render(arg) ### change body parameters, arg: 'dict'
    body = MIMEText(temp_rend, "html")
    msg.attach(body)
    
    ### attachments  
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    ### create connection
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    
