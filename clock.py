from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    l_hr.config(text=hr)
    l_min.config(text=mi)
    l_sec.config(text=sec)
    l_am.config(text=am)

    l_date.config(text=date)
    l_mon.config(text=month)
    l_year.config(text=year)
    l_day.config(text=day)

    l_hr.after(200,date_time)

clock = Tk()
clock.title("        Digital Clock")
clock.geometry("1000x500")
clock.config(bg="grey")

#time

l_hr=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_hr.place(x=120,y=50,height=110,width=100)

l_hr_t=Label(clock, text="Hour", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_hr_t.place(x=120,y=190,height=40,width=100)

l_min=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_min.place(x=340,y=50,height=110,width=100)

l_min_t=Label(clock, text="Min.", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_min_t.place(x=340,y=190,height=40,width=100)

l_sec=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_sec.place(x=560,y=50,height=110,width=100)

l_sec_t=Label(clock, text="Sec.", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_sec_t.place(x=560,y=190,height=40,width=100)

l_am=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_am.place(x=780,y=50,height=110,width=100)

l_am_t=Label(clock, text="AM/PM", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_am_t.place(x=780,y=190,height=40,width=100)

# date

l_date=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_date.place(x=120,y=270,height=110,width=100)

l_date_t=Label(clock, text="Date", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_date_t.place(x=120,y=410,height=40,width=100)

l_mon=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_mon.place(x=340,y=270,height=110,width=100)

l_mon_t=Label(clock, text="Month", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_mon_t.place(x=340,y=410,height=40,width=100)

l_year=Label(clock, text="00", font = "SCIENTIFIC 50", bg="dark grey", fg="white")
l_year.place(x=560,y=270,height=110,width=100)

l_year_t=Label(clock, text="Year", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_year_t.place(x=560,y=410,height=40,width=100)

l_day=Label(clock, text="00", font = "SCIENTIFIC 40", bg="dark grey", fg="white")
l_day.place(x=780,y=270,height=110,width=100)

l_day_t=Label(clock, text="Day", font = "SCIENTIFIC 22", bg="dark grey", fg="white")
l_day_t.place(x=780,y=410,height=40,width=100)

date_time()

clock.mainloop()