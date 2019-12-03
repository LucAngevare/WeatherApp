import tkinter as tk
from tkinter import font
import requests
import json

HEIGHT = 500
WIDTH = 600

def formatResponse(weather):
  try:
    name = str(weather['name'])
    desc = str(weather["weather"][0]["description"])
    temp = str(weather['main']['temp'])

    final_str = "City: %s\nConditions: %s\nTemperature: %s" % (name, desc, temp)
    str(name + ' ' + desc + ' ' + temp)
  except:
    final_str = "No valid input shithead"
  return final_str


def Test_Function(entry):
  api_address='http://api.openweathermap.org/data/2.5/weather?appid=34f0968e5b315c84a6a6cbbe4ec9f1bf&q='
  city = entry
  url = api_address + city + '&units=metric'
  json_data = requests.get(url).json()
  realtime_weather = json_data["weather"][0]["description"]
  temp = int(json_data['main']['temp'])
  label['text'] = formatResponse(json_data)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backgroundIMG = tk.PhotoImage(file='file.gif')
backgroundLBL = tk.Label(root, image=backgroundIMG)
backgroundLBL.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", bg='white',font=40, command=lambda: Test_Function(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

otherShittyFrame = tk.Frame(root, bg="#80c1ff", bd=15)
otherShittyFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(otherShittyFrame, bg='white',font=('Courier', 15))
label.place(relwidth=1, relheight=1)

root.mainloop()