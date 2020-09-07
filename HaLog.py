from selenium import webdriver
from datetime import datetime
import mysql.connector
from mysql.connector import Error

rest = 0
day = 0
month = 0
year = 0


def main():
    print("Willkommen zum Hausaufgaben Log schreiber")
    mysqlConnection()
    print("Benutzername : " + name)
    print("Password: " + "************")
    getDay()
    print("Tag nach Doomsday Algorithem: " + str(rest))
    executeAction()


def mysqlConnection():
    global name, connection, cursor, password
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='logindata',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            cursor.execute("select * from logins")
            result = cursor.fetchall()
            for x in result:
                name = str(x[1])
                password = str(x[2])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def getDay():
    global year, month, day
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    numberOfWeek = 0
    jan = 3
    feb = 6
    mar = 6
    api = 2
    may = 4
    jun = 0
    jul = 2
    aug = 5
    sep = 1
    oct = 3
    nov = 6
    dec = 1
    theyear = year[2] + year[3]

    if theyear == "20":
        numberOfWeek = 20
        ab = numberOfWeek / 4
        numberOfWeek += ab
    elif theyear == "21":
        numberOfWeek = 21
        ab = numberOfWeek / 4
        numberOfWeek += ab
    elif theyear == "22":
        numberOfWeek = 22
        ab = numberOfWeek / 4
        numberOfWeek += ab

    numberOfWeek += 4
    if month == "01":
        numberOfWeek += jan
    if month == "02":
        numberOfWeek += feb
    if month == "03":
        numberOfWeek += mar
    if month == "04":
        numberOfWeek += api
    if month == "05":
        numberOfWeek += may
    if month == "06":
        numberOfWeek += jun
    if month == "07":
        numberOfWeek += jul
    if month == "08":
        numberOfWeek += aug
    if month == "09":
        numberOfWeek += sep
    if month == "10":
        numberOfWeek += oct
    if month == "11":
        numberOfWeek += nov
    if month == "12":
        numberOfWeek += dec

    numberOfWeek += int(day)
    rest = numberOfWeek % 7


def executeAction():
    if rest == 0:
        what_i_did = "Was habe ich gemacht?"
        theme = "Repetiert"
        how_long_did_take = "Wie lange habe ich gebraucht ?"
        time = input("Wie lange haben sie gebraucht: ")
        what_i_learned = "Was habe ich gelernt ?"
        txt1 = ""
        txt2 = ""

        ha_or_rep = input("Hausaufgabe(HA) oder Repetition(Rep) : ")
        first_theme = input("First Theme: ")
        second_theme = input("Second Theme: ")

        if ha_or_rep == "Rep" or ha_or_rep == "Repetition":
            txt1 = "Ich habe weiter Repetiert an dem Thema " + first_theme + ". Ausserdem habe besser verstanden wie "
            txt2 = second_theme + " funktioniert."
        elif ha_or_rep == "HA" or ha_or_rep == "Hausaufgabe":
            txt1 = "Ich habe meine Hausaufgaben zum Thema " + first_theme + " fertig gemacht."
            txt2 = "Ich bin ausserdem weiter gekommen im " + second_theme

        chrome_path = r"C:\Users\Andrei Oleniuc\Desktop\Code\Python Programms\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)

        driver.get("https://moodle.bbbaden.ch/")
        submit_btn = "#submit"
        user_field = "#inputName"
        pass_field = "#inputPassword"
        submit = driver.find_element_by_css_selector(submit_btn)
        user_fill = driver.find_element_by_css_selector(user_field)
        pass_fill = driver.find_element_by_css_selector(pass_field)
        user_fill.send_keys(name)
        pass_fill.send_keys(password)
        submit.click()
        driver.get("https://moodle.bbbaden.ch/mod/journal/edit.php?id=75819")

        textfield = driver.find_element_by_css_selector("#id_text_editoreditable > p")
        textfield.send_keys("-------------------------------------------------------------------------" +
                            "\n" +
                            "Andrei " + day + "." + month + "." + year
                            + "\n" + what_i_did
                            + "\n" + theme
                            + "\n" + how_long_did_take
                            + "\n" + time
                            + "\n" + what_i_learned
                            + "\n" + txt1
                            + txt2 + "\n" +
                            "-------------------------------------------------------------------------"
                            + '\n')
        btn = driver.find_element_by_css_selector("#id_submitbutton")
        btn.click()
    else:
        print("Heute ist nicht der Tag")


if __name__ == '__main__':
    main()
