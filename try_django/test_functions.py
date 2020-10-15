from django.core.mail import send_mail
from django.http import HttpResponse
import os
from dotenv import load_dotenv
load_dotenv()

def test_mail_OLD(request):
    send_mail('Example Subject-5:42pm 3/7/2020', 'Example Message ABC 5:42pm 3/7/2020', 'smilingideas@gmail.com', ['davidtang@hengbao.com','heydudde@gmail.com'])
    return HttpResponse('email sent at 5:42pm 3/7/2020!')

def test_mail(request):
    send_mail('Example Subject - Send from HBI email', 'Example Message sent on 7:29am 5th July - Send from HBI email', 'davidtang@hengbao.com', ['cryptocoinwiz@gmail.com','heydudde@gmail.com'])
    return HttpResponse('email Send from HBI ABC email')

def test_getenviron(request):
    sendgridapi1 = os.environ.get('SENDGRID_API_KEY')
    awskeyid1 = os.environ.get('AWS_ACCESS_KEY_ID')
    awsaccesskey1 = os.environ.get('AWS_SECRET_ACCESS_KEY')
    awss3bucket1 = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    secretkey1 = os.environ.get('SECRET_KEY')

    sqlengine1 = os.environ.get('SQL_ENGINE')
    sqldb1 = os.environ.get('SQL_DATABASE')
    sqluser1 = os.environ.get('SQL_USER')
    sqlpassword1 = os.environ.get('SQL_PASSWORD')
    sqlhost1 = os.environ.get('SQL_HOST')
    sqlport1 = os.environ.get('SQL_PORT')
    sqldebug1 = os.environ.get('DEBUG')

    print('sendgridapi1=', sendgridapi1)
    print('awskeyid1=', awskeyid1)
    print('awsaccesskey1=', awsaccesskey1)
    print('awss3bucket1=', awss3bucket1)
    print('secretkey1=', secretkey1)

    print('sqlengine1=', sqlengine1)
    print('sqldb1=', sqldb1)
    print('sqluser1=', sqluser1)
    print('sqlpassword1=', sqlpassword1)
    print('sqlhost1=', sqlhost1)
    print('sqlport1=', sqlport1)
    print('sqldebug1=', sqldebug1)





    return HttpResponse('ok done!')