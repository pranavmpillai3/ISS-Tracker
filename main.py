import requests
import smtplib
import datetime as dt

MY_LATITUDE = 0
MY_LONGITUDE = 0
mail = ""
# node to the connection
password = ""

response = requests.get("http://api.open-notify.org/iss-now.json")
isslong = response.json()['iss_position']['longitude']
isslati = response.json()['iss_position']['latitude']
print(isslati, isslong)

now = dt.datetime.now()
time = now.strftime('%H:%M:%S').split(':')
print(time)
if (float(float(isslati) + 5.0) <= float(MY_LATITUDE) <= float(float(isslati) - 5.0)) \
        and (float(isslong) + 5.0 <= MY_LONGITUDE <= float(isslong) - 5.0) \
        and (1 <= int(time[0]) >= 6 or 18 <= int(time[0]) <= 23):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        # connection to email server
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs='',
                            msg=f"LOOK  UP\n\nISS IS ABOVE YOUR HEAD")
