import tkinter as tk
import os

name = 'Your name'

try:
    f = open(os.path.join('D:\\', "Clock File.txt"), "r")
    name = f.read()
    f.close()
except:
    f = open(os.path.join('D:\\', "Clock File.txt"),"w+")
    f.write('there !')
    name = f.read()
    f.close()
    
    
running = False
i = 0
lm, ln = 60, 0
resume = False
prev = 0
durations = []

def second(a, b):

    def counter_(p, q=0):

        def count(n, m):
            if running:
                if str(m) == '0':
                    m, n = 59, n-1
                    tim = str(n)+' , ' + str(m)
                else:
                    m = m-1
                    tim = str(n)+' , ' + str(m)
                label['text'] = tim
                label.after(1000, count, n, m)
            else:
                global lm
                global ln
                lm, ln = n, m
                print("Not running")
        count(p, q)

    def beg():
        s['state'] = tk.DISABLED
        d['state'] = tk.NORMAL
        o['state'] = tk.NORMAL
        r['state'] = tk.DISABLED
        progressbar['text'] = '_'*18
        l2['text'] = '0%'
        global running
        running = True
        counter_(b)

    def done():
        print(label['text'])
        global i
        i = i + 1
        if(i<=int(a)):
            l = int((i * 18) / int(a))
            l2['text'] = str(int((i * 100) / int(a))) + '%'
            progressbar['text'] = '█'*l + '_'*(18-l)
            global prev
            durations.append(str(prev - int(label['text'].split()[0])))
            prev = int(label['text'].split()[0])
            

    def finish():
        o['state'] = tk.DISABLED
        d['text'] = 'Report'
        s['state'] = tk.NORMAL
        r['state'] = tk.NORMAL
        s['text'] = 'Resume'
        global resume
        resume = True
        global running
        running = False
        print(label['text'])

    def reset():
        s['state'] = tk.NORMAL
        d['state'] = tk.DISABLED
        d['text'] = 'Done'
        o['state'] = tk.DISABLED
        global i
        i = 0
        l2['text'] = '0%'
        global resume
        resume = False
        s['text'] = 'Start'
        label['text'] = str(b)+' , 0'
        progressbar['text'] = '_'*18

    def choose():
        if resume :
            cont()
        else:
            beg()

    def cont():
        global running
        running = True
        counter_(lm, ln)
        d['state'] = tk.NORMAL
        d['text'] = 'Done'
        o['state'] = tk.NORMAL
        s['state'] = tk.DISABLED
        r['state'] = tk.DISABLED

    def done_():
        if d['text'] == 'Done':
            done()
        else:
            Report()

    def Report():
        rep = tk.Tk()
        rep.title('Report')
        heading = tk.Label(rep, text=" Time taken :", fg='Blue', font='Times 20 italic', width=18, height=1)
        heading.pack()
        data = tk.Label(rep, text=", ". join(durations), fg='Blue', font='Times 20 italic', width=18, height=1)
        data.pack()
        rep.minsize(width=750, height=100)
        rep.maxsize(width=750, height=100)
        rep.mainloop()
        

    global prev
    main = tk.Tk()
    main.title("Clock")
    l2 = tk.Label(main, text='0%', fg='Green', font='Times 20 italic', width=18, height=1)
    l2.grid(row=0, column=4)
    progressbar = tk.Label(main, text='_'*18, fg='Green', font='Times 15 bold', width=15)
    progressbar.grid(row=2, column=4)
    label = tk.Label(main, text=str(b), fg='Green', font='Times 12 bold', width=7, height=2)
    label.grid(row=1, column=2)
    r = tk.Button(main, text="Reset", width=10, height=2, command=lambda: reset())
    r.grid(row=0, column=3)
    s = tk.Button(main, text="Start", width=10, height=2, command=lambda: choose())
    s.grid(row=0, column=0)
    d = tk.Button(main, text="Done", width=10, height=2, command=lambda: done_(), state=tk.DISABLED)
    d.grid(row=0, column=1)
    o = tk.Button(main, text="Finish", width=10, height=2, command=lambda: finish(), state=tk.DISABLED)
    o.grid(row=0, column=2)
    prev = b
    main.minsize(width=750, height=150)
    main.maxsize(width=750, height=150)
    main.mainloop()


def go(a, b, boot):
    boot.destroy()
    second(a, b)


def first():
    boot = tk.Tk()
    boot.title("Welcome")
    tk.Label(boot, text=" Hi " + name, fg="blue", font="Courier 30 bold").grid(row=0, column=0)
    tk.Label(boot, text="# Questions", font="Times 12 bold").grid(row=1, column=1)
    tk.Label(boot, text="Hours", font="Times 12 bold").grid(row=2, column=1)
    tk.Label(boot, text="Minutes", font="Times 12 bold").grid(row=3, column=1)
    n = tk.Entry(boot)
    t1 = tk.Entry(boot)
    t2 = tk.Entry(boot)
    t2.insert(0, "0")
    n.grid(row=1, column=3)
    t1.grid(row=2, column=3)
    t2.grid(row=3, column=3)
    tk.Button(boot, text="Go", font="Times 12 bold", width=5, height=1, command=lambda: go(n.get(), int(float(t1.get()) * 60 + int(t2.get())), boot)).place(x=600, y=91)
    boot.minsize(width=750, height=150)
    boot.maxsize(width=750, height=150)
    boot.mainloop()


first()
