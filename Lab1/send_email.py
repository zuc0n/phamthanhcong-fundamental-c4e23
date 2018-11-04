from gmail import GMail, Message

gmail = GMail("zuc0nc4e23@gmail.com", "zuc0n1996")

loi_noi_list = ["Aye", 'anh nho em', 'a muon ']
from random import choice
k = choice(loi_noi_list)

template = '''<p>Ch&agrave;o em,</p>
<p>H&ocirc;m nay anh dậy sớm, l&ograve;ng anh nhớ em v&ocirc; c&ugrave;ng, Anh đo&aacute;n l&agrave; anh y&ecirc;u em mất rồi.</p>
<p>Thế n&ecirc;n l&agrave; m&igrave;nh cưới nhau đi&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
<p>Anh y&ecirc;u của em&nbsp;</p>
'''


moi = template.replace("{{sick}}", k)
msg = Message("Giay Cau hon", to="qhuydtvt@gmail.com", html=moi)

gmail.send(msg)



