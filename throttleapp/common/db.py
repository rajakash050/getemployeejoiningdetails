
import os
import base64
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.conf import settings
import mysql.connector


def query(sql):
    mydb = mysql.connector.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        database=settings.DATABASES['default']['NAME']
    )

    print(sql)
    # print(val)
    mycursor = mydb.cursor()

    mycursor.execute(str(sql))

    mydb.commit()

    mycursor.close()
    mydb.close()

    print(mycursor.rowcount, "record inserted.")
    return True

def getquery(qe):
    print(qe)
    mydb = mysql.connector.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        database=settings.DATABASES['default']['NAME']
    )
    mycursor = mydb.cursor(dictionary=True)

    # mycursor.execute(sql, val)
    mycursor.execute(qe)

    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    # for x in myresult:
    #     print(x)
    print(myresult)
    return list(myresult)

def authentication_check (request): 
    user_password = []   
    if request.META.has_key("HTTP_AUTHORIZATION"):
        encoded_user_password =  request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        user_password  = base64.b64decode(encoded_user_password).split(":")
        user_name = user_password[0]
        password = user_password[1]
    return user_password



