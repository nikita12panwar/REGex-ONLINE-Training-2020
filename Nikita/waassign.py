import requests as rq
import pyautogui as g
import webbrowser as wb
import time as t
import pyautogui as pg
number=[]
message=input("Enter your message: ")
count=int(input("How many person you want to send message(Limit 1 to 9): "))
numberMessage=int(input("How many message you want to send: "))
for i in range(count):
	num=int(input("Enter Contact Number followed by 91: "))
	number.append(num)
for a in range(count):
	t.sleep(2)
	link="https://web.whatsapp.com/send?phone={}&text={}".format(number[a],message)
wb.open(link)
t.sleep(15)
print("Page timeout")
pg.press("enter")
for x in range(numberMessage):
	pg.typewrite(message)
	pg.press("enter")
	t.sleep(2)
	pg.hotkey("ctrl","w")
	pg.press("enter")
	print("Mesage sent to {} message is {}".format(number[a],message))
print("Done")