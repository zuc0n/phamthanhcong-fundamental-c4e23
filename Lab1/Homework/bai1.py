from gmail import GMail, Message
import datetime

gmail = GMail("zuc0nc4e23@gmail.com", "zuc0n1996")

ly_do = "Entschuldigung, ich bin heute {{sick}} sein, sodass kann ich nicht mein Haus verlassen. I werde mich einen Tag freinehmen"
benh_tat = ["krank", "Grippe", "Kopfschmerzen"]

from random import choice
ngau_nhien = choice(benh_tat)
msg = Message('Don xin nghi', to='theonlyone1511@gmail.com', text= ly_do.replace("{{sick}}", ngau_nhien))
now = datetime.datetime.now().strftime('%I:%M %p')
while True:
     if now == "07:00 AM":
        gmail.send(msg)
