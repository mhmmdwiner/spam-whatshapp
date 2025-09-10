import pyautogui as spam
import time

msg = input("Pesan yang ingin dikirim : ")

count = 0
limit = int(input("masukan jumlah pesan : "))

time.sleep(5)

# while i<int(limit):
while count<int(limit):
    count+=1
    if count > limit:
        break
    spam.typewrite(msg)
    spam.press('Enter')