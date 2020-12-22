import os
import mysql.connector
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypassvault.settings')

import django

django.setup()
from mydb.models import Topic, Account, AccessRecord


def read_db():
    con = mysql.connector.connect(
        user="root",
        password="24firehit",
        host="127.0.0.1",
        database="accounts"
    )

    cursor = con.cursor()

    query = cursor.execute("SELECT * FROM account")
    results = cursor.fetchall()

    # # print(results)
    # for x in results:
    #     print(x)
    return results


dataframe = read_db()


def add_topic(topic):
    t = Topic.objects.get_or_create(topic_name=topic)[0]
    t.save()
    return t


def populate_db(dt):
    for x in dt:
        aux = []
        for i in range(0, 11):
            if x[i] is None or x[i] == '':
                if i == 7:
                    aux.append("Other")
                else:
                    aux.append(" ")
            else:
                aux.append(x[i])


        # Getting data from the list
        email = aux[1]
        username = aux[2]
        password = aux[3]
        url = aux[4]
        website_name = aux[5]
        comment = aux[6]
        top = add_topic(aux[7])
        Name = aux[8]
        Address = aux[9]
        Phone_Number = aux[10]
        day = datetime.now()
        print(x[0], email, username, password, url, website_name)
        account = \
            Account.objects.get_or_create(topic=top, Email=email, website_name=website_name, url=url, password=password,
                                          userName=username, comment=comment, Name=Name, Address=Address,
                                          Phone_Number=Phone_Number)[0]
        acc_re = AccessRecord.objects.get_or_create(name=account, date=day)


if __name__ == '__main__':
    print("pupulating from mydb in SQL 127.0.0.1")
    populate_db(dataframe)
    print("Finished Populating!!")
