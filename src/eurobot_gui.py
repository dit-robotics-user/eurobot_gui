#!/usr/bin/env python
import rospy
import Tkinter as tk
from Tkinter import *
import ttk
from std_msgs.msg import String

pub = rospy.Publisher('hit_wall', String, queue_size=10)

def talker():
    rospy.init_node('eurobot_gui', anonymous=True)
    rate = rospy.Rate(10)

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        self.title = tk.Label(self)
        self.title["text"] = "DIT Robotics\nEurobot 2020"
        self.title["width"] = 20
        self.title["height"] = 5
        self.title.pack()

        self.btn_HW = tk.Button(self)
        self.btn_HW["text"] = "Hit Wall"
        self.btn_HW["command"] = self.start
        self.btn_HW.pack()

    def start(self):
        pub.publish("hit wall")

root = tk.Tk()
root.geometry('800x600')
root.title('DIT Robotics Eurobot 2020')
app = Application(root)

if __name__ == '__main__':
    try:
        talker()
        root.mainloop()
    except rospy.ROSInterruptException:
        pass