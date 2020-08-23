from selenium import webdriver
from datetime import datetime

# Data for Site
now = datetime.now()
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)

what_i_did = "Was habe ich gemacht?"
theme = "Repetiert"
how_long_did_take = "Wie lange habe ich gebraucht ?"
time = input("Time taken: ")
what_i_learned = "Was habe ich gelernt ?"
txt1 = ""
txt2 = ""

ha_or_rep = input("HA or Rep: ")
first_theme = input("First Theme: ")
second_theme = input("Second Theme: ")

if ha_or_rep == "Rep":
    txt1 = "Ich habe weiter Repetiert an dem Thema " + first_theme + ". Ausserdem habe besser verstanden wie "
    txt2 = second_theme + " funktioniert."
elif ha_or_rep == "HA":
    txt1 = "Ich habe meine Hausaufgaben zum Thema " + first_theme + " fertig gemacht."
    txt2 = "Ich bin ausserdem weiter gekommen im " + second_theme

chrome_path = r"C:\Users\Andrei Oleniuc\Desktop\Python Programms\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

user = "Andrei.Oleniuc4"
password = "Asdfqwer1234"

driver.get("https://moodle.bbbaden.ch/")

submit_btn = "#submit"
user_field = "#inputName"
pass_field = "#inputPassword"

submit = driver.find_element_by_css_selector(submit_btn)
user_fill = driver.find_element_by_css_selector(user_field)
pass_fill = driver.find_element_by_css_selector(pass_field)

user_fill.send_keys(user)
pass_fill.send_keys(password)
submit.click()

driver.get("https://moodle.bbbaden.ch/mod/journal/edit.php?id=62613")
textbox1 = "#id_text_editoreditable > p:nth-child(1)"
nameField = driver.find_element_by_css_selector(textbox1)
nameField.send_keys("Andrei Oleniuc " + day + "." + month + "." + year
                    + "\n" + what_i_did
                    + "\n" + theme
                    + "\n" + how_long_did_take
                    + "\n" + time
                    + "\n" + what_i_learned
                    + "\n" + txt1 + txt2
                    + "\n")
nameField.submit()





