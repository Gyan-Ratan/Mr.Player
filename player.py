from tkinter import *
from ctypes import windll


from  BlurWindow.blurWindow import blur

root = Tk()

root.config(bg='black')
root.iconbitmap('resources/images/icon.ico')
root.title("  MR. PLAYER")
root.wm_attributes("-transparent", '#010812')
root.geometry('1000x600')

root.update()

hWnd = windll.user32.GetForegroundWindow()
blur(hWnd)

hex='#192734756'
blur(hWnd,hexColor=hex)
'''
This for choosing your own color but careful ^_^
                                                                            # def color(hex):
                                                                            #     hWnd = windll.user32.GetForegroundWindow()
                                                                            #     blur(hWnd,hexColor=hex)


                                                                            # e = Entry(width=9)
                                                                            # e.insert(0,'#12121240')

                                                                            # e.pack()
                                                                            # b = Button(text='Apply',command=lambda:[color(e.get())])
                                                                            # b.pack()

'''
# LEFT PANE
leftFrame = Frame(root, bg='#010812',width=300,height=540)
leftFrame.pack_propagate(0)
leftFrame.pack(fill='both',side='left')
# LEFT PANE ELEMENTS
label1=Label(leftFrame,text="COOL")# To make the text orientation verticl use ,wraplength=1
label1.pack(ipadx=10,ipady=10,padx=100,pady=100)
# RIGHT PANE
rightFrame = Frame(root, bg='#152033',width=700,height=540)
rightFrame.pack_propagate(0)
rightFrame.pack(fill='both', side='right', expand='True')
# BOTTOM PANE Right
bottomFrame = Frame(rightFrame, width=700, height=60, bg='#0d1321')
bottomFrame.pack_propagate(0)
bottomFrame.pack(side='left', padx=0, pady=0, anchor='sw',expand='True')
# BOTTOM PANE left
bottomFrame = Frame(leftFrame, width=300, height=60, bg='#0d1321')
bottomFrame.pack_propagate(0)
bottomFrame.pack(side='left', padx=0, pady=0, anchor='sw',expand='True')






















'''
 THIS is Another window which will open with the existing window
            
            subroot =Tk()
            subroot.config(bg='green')
            subroot.geometry('100x600')
            subroot.update()
            subroot.mainloop()

'''
# Ending of main loop
root.mainloop()