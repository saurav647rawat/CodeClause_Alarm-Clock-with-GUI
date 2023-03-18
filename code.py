import tkinter as tk
import datetime as dt
import time


class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        self.alarm_time = dt.datetime.now()

        # create time labels
        self.current_time_label = tk.Label(
            master, text="", font=("Helvetica", 24))
        self.current_time_label.pack(pady=10)

        self.alarm_time_label = tk.Label(
            master, text=self.alarm_time.strftime("%H:%M:%S"), font=("Helvetica", 18))
        self.alarm_time_label.pack()

        # create time spinners
        self.hour_spinner = tk.Spinbox(
            master, from_=0, to=23, width=2, font=("Helvetica", 16))
        self.minute_spinner = tk.Spinbox(
            master, from_=0, to=59, width=2, font=("Helvetica", 16))
        self.second_spinner = tk.Spinbox(
            master, from_=0, to=59, width=2, font=("Helvetica", 16))
        self.hour_spinner.pack()
        self.minute_spinner.pack()
        self.second_spinner.pack()

        # create set alarm button
        self.set_alarm_button = tk.Button(
            master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        # create alarm status label
        self.alarm_status_label = tk.Label(
            master, text="", font=("Helvetica", 18))
        self.alarm_status_label.pack(pady=10)

        # start clock
        self.update_clock()

    def update_clock(self):
        # update current time label
        self.current_time_label.configure(text=time.strftime("%H:%M:%S"))
        # check if alarm time is reached
        if self.alarm_time <= dt.datetime.now():
            self.alarm_status_label.configure(text="Alarm!", fg="red")
        # update alarm time label
        self.alarm_time_label.configure(
            text=self.alarm_time.strftime("%H:%M:%S"))
        # update every second
        self.master.after(1000, self.update_clock)

    def set_alarm(self):
        # get alarm time from spinners
        alarm_hour = int(self.hour_spinner.get())
        alarm_minute = int(self.minute_spinner.get())
        alarm_second = int(self.second_spinner.get())
        # create datetime object for alarm time
        self.alarm_time = dt.datetime.now().replace(
            hour=alarm_hour, minute=alarm_minute, second=alarm_second, microsecond=0)
        # clear alarm status label
        self.alarm_status_label.configure(text="", fg="black")


root = tk.Tk()
clock = AlarmClock(root)
root.mainloop()
