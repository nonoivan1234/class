from tkinter import *
from datetime import datetime
import login

classtable = [
    ['數學', '英文', '閱讀理解與表達', '閱讀理解與表達', '化學', '化學', '國文', '放學'],
    ['地理', '國文', '體育', '英文', '歷史', '生命教育', '數學', '放學'],
    ['國文', '音樂', '英文', '數學', '生物', '生物', '歷史', '放學'],
    ['資訊', '資訊', '多元選修', '多元選修', '英文', '地理', '體育', '放學'],
    ['國文', '數學', '自主學習', '自主學習', '班會', '彈性', '彈性', '放學']
]

classtime = [
    ['08:10', '09:00'],
    ['09:10', '10:00'],
    ['10:10', '11:00'],
    ['11:10', '12:00'],
    ['13:00', '13:50'],
    ['14:00', '14:50'],
    ['15:10', '16:00']
]


def timeout():
    current_show_label.config(text=datetime.now().strftime("%H:%M:%S"))
    for i in range (7):
        if datetime.now().strftime('%X') >= datetime.strptime(classtime[i][0], '%H:%M').strftime('%X') and datetime.now().strftime('%X') <= datetime.strptime(classtime[i][1], '%H:%M').strftime('%X'):
            class_ind = i

            now_text = classtable[datetime.today().weekday()][class_ind]
            
            next_text = classtable[datetime.today().weekday()][class_ind+1]
            
            now_show_label.config(text=now_text)
            next_show_label.config(text=next_text)
            
            subject = now_text
            go_login(subject, i)
    app.after(500, timeout)

def go_login(subject, class_ind):
    if log.readline()[-17::]=='Open the main.py\n':
        if subject=='英文' and int(datetime.now().strftime("%M"))>int(classtime[class_ind][3:4])+35:
            log.write(str(datetime.now())+' Try to login'+subject+'\n')
            # login.login('英文')
        elif subject != '放學了啦' or subject!='還沒上課':
            log.write(str(datetime.now())+' Try to login'+subject+'\n')
            print(subject)
            login.login(subject)


log = open('log.txt', 'r+', encoding='utf-8')

app = Tk()
app.title('防疫神器')

# Current Time
current_text = datetime.now().strftime("%H:%M:%S")
current_label = Label(app, text = '現在時間 :', font = ('微軟正黑體', 17), pady=25)
current_label.grid(row=0, column=0, sticky=W)
current_show_label = Label(app, text = current_text, font = ('微軟正黑體', 17), pady=25)
current_show_label.grid(row=0, column=1)

# Class now on
now_text = '還沒上課啦'
now_label = Label(app, text = '這一節課 :', font = ('微軟正黑體', 17), pady=25)
now_label.grid(row=1, column=0, sticky=W)
now_show_label = Label(app, text = now_text, font = ('微軟正黑體', 17), pady=25)
now_show_label.grid(row=1, column=1)

# Class next up
next_text = '還沒上課啦'
next_label = Label(app, text = '下一節課 :', font = ('微軟正黑體', 17), pady=25)
next_label.grid(row=2, column=0, sticky=W)
next_show_label = Label(app, text = next_text, font = ('微軟正黑體', 17), pady=25)
next_show_label.grid(row=2, column=1)

log.write(str(datetime.now())+' Open the main.py\n')

timeout()
app.geometry('250x250')

app.mainloop()