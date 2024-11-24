# 1.
from tkinter import *
GARUMS = 500
PLATUMS = 800
logs = Tk()
logs.title('Burbuļu spridzinātājs')
a = Canvas(logs, width=PLATUMS, height=GARUMS, bg='darkblue')
a.pack()

# 2.
kuģa_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
kuģa_id2 = a.create_oval(0, 0, 30, 30, outline='red')
KUĢA_R = 15
VID_X = PLATUMS / 2
VID_Y = GARUMS / 2
a.move(kuģa_id, VID_X, VID_Y)
a.move(kuģa_id2, VID_X, VID_Y)

# 3.
KUĢA_ĀTR = 10
def pārvietot_kuģi(notikums):
    if notikums.keysym == 'Up':
        a.move(kuģa_id, 0, -KUĢA_ĀTR)
        a.move(kuģa_id2, 0, -KUĢA_ĀTR)
    elif notikums.keysym == 'Down':
        a.move(kuģa_id, 0, KUĢA_ĀTR)
        a.move(kuģa_id2, 0, KUĢA_ĀTR)
    elif notikums.keysym == 'Left':
        a.move(kuģa_id, -KUĢA_ĀTR, 0)
        a.move(kuģa_id2, -KUĢA_ĀTR, 0)
    elif notikums.keysym == 'Right':
        a.move(kuģa_id, KUĢA_ĀTR, 0)
        a.move(kuģa_id2, KUĢA_ĀTR, 0)
a.bind_all('<Key>', pārvietot_kuģi)

# 4. 
from random import randint
burb_id = list()
burb_r = list()
burb_ātrums = list()
MIN_BURB_R = 10
MAX_BURB_R = 30
MAX_BURB_ĀTR = 10
ATSTARPE = 100
def izveidot_burbuli():
    x = PLATUMS + ATSTARPE
    y = randint(0, GARUMS)
    r = randint(MIN_BURB_R, MAX_BURB_R)
    id1 = a.create_oval(x - r, y - r, x + r, y + r, outline='white')
    burb_id.append(id1)
    burb_r.append(r)
    burb_ātrums.append(randint(1, MAX_BURB_ĀTR))

# 5.

