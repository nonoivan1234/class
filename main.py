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
    '08:11', '09:11', '10:11', '11:11', '13:01', '14:01', '15:11'
]

def timeout():
    current_show_label.config(text=datetime.now().strftime("%H:%M:%S"))
    if datetime.now().strftime("%H:%M") in classtime:
        class_ind = classtime.index(datetime.now().strftime("%H:%M"))
        now_text = classtable[datetime.today().weekday()-1][class_ind]
        
        next_text = classtable[datetime.today().weekday()-1][class_ind+1]
        
        subject = now_text
        if subject=='英文' and int(datetime.now().strftime("%M"))>int(classtime[class_ind][3:4])+30:
            login('英文')
        elif subject != '放學了啦':
            login(subject)
    elif int(datetime.now().strftime("%H"))>=16 or int(datetime.now().strftime("%H"))<9:
        now_text = '放學了啦'
        next_text = '放學了啦'
    now_show_label.config(text=now_text)
    next_show_label.config(text=next_text)
    app.after(500, timeout)
    
app = Tk()
app.title('防疫神器')

# Current Time
current_text = datetime.now().strftime("%H:%M:%S")
current_label = Label(app, text = '現在時間 :', font = ('微軟正黑體', 17), pady=25)
current_label.grid(row=0, column=0, sticky=W)
current_show_label = Label(app, text = current_text, font = ('微軟正黑體', 17), pady=25)
current_show_label.grid(row=0, column=1)

# Class now on
now_text = '還沒上課喔'
now_label = Label(app, text = '這一節課 :', font = ('微軟正黑體', 17), pady=25)
now_label.grid(row=1, column=0, sticky=W)
now_show_label = Label(app, text = now_text, font = ('微軟正黑體', 17), pady=25)
now_show_label.grid(row=1, column=1)

# Class next up
next_text = '還沒上課喔'
next_label = Label(app, text = '下一節課 :', font = ('微軟正黑體', 17), pady=25)
next_label.grid(row=2, column=0, sticky=W)
next_show_label = Label(app, text = next_text, font = ('微軟正黑體', 17), pady=25)
next_show_label.grid(row=2, column=1)

timeout()
app.geometry('220x250')

app.mainloop()