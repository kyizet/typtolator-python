try:
        import tkinter as tk
        from tkinter import ttk
        from tkinter.font import Font
except:   #2.x
        import Tkinter as tk
        from Tkinter import ttk
        from Tkinter.font import Font
from PIL import ImageTk, Image
from random import shuffle
import random
import pickle

usr_choice = 1

class typtolator(tk.Tk): # main class copied from sentdex (Harrison Kinseley)
        
        def __init__(self, *args, **kwargs):
        
                tk.Tk.__init__(self, *args, **kwargs)
                tk.Tk.wm_title(self, "Typtolator")
                self.geometry("720x480+360+240")
                self.resizable(False, False)

                container = tk.Frame(self)
                container.pack(side="top", fill="both", expand = True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                self.frames = {}
                pages = (MainMenu, startPage, AboutPage, AppPage)
                for F in pages:

                    frame = F(container, self)
                    self.frames[F] = frame
                    frame.grid(row=0, column=0, sticky="nsew")

                self.show_frame(MainMenu)

        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()
        
class MainMenu(tk.Frame): #main menu window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open("img/mm_bg.jpg")
        photo = ImageTk.PhotoImage(image)
        bg_img = tk.Label(self, image=photo)
        bg_img.image = photo
        bg_img.pack()

        #start button
        start_btn = tk.Button(self,
                                       text = "Start",
                                       padx = 70,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground="#858585",
                                      activeforeground="#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: controller.show_frame(startPage))
        start_btn.place(x = 280, y = 200)

        #about button
        about_btn = tk.Button(self,
                                      text = "About",
                                      padx = 66,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: controller.show_frame(AboutPage))
        about_btn.place(x = 280, y = 260)

        #exit button
        exit_btn = tk.Button(self,
                                        text = "Exit",
                                        padx = 30,
                                        pady = 10,
                                        bg = "#45453c",
                                        fg = "#fff",
                                        activebackground = "#858585",
                                        activeforeground = "#000",
                                        cursor = "hand1",
                                        bd = 0,
                                        command = quit)
        exit_btn.place(x = 600, y = 400)



class startPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                image = Image.open("img/start_bg.jpg")
                photo = ImageTk.PhotoImage(image)
                bg_img = tk.Label(self, image=photo)
                bg_img.image = photo
                bg_img.pack()

                def deliverValue(x):
                        usr_choice = x
                        controller.show_frame(AppPage)

                #back button
                back_btn = tk.Button(self,
                                     text = "Back",
                                     width = 10,
                                      padx = 30,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: controller.show_frame(MainMenu))
                back_btn.place(x = 10, y = 10)

                #easy button
                btn_easy = tk.Button(self,
                                      text = "Easy",
                                      padx = 77,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: deliverValue(1))
                btn_easy.place(x = 400, y = 260)

                #normal button
                btn_normal = tk.Button(self,
                                      text = "Medium",
                                      padx = 66,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: deliverValue(2))
                btn_normal.place(x = 400, y = 310)

                #hard button
                btn_easy = tk.Button(self,
                                      text = "Hard",
                                      padx = 77,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: deliverValue(3))
                btn_easy.place(x = 400, y = 360)

class AppPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                image = Image.open("img/app_bg.jpg")
                photo = ImageTk.PhotoImage(image)
                bg_img = tk.Label(self, image = photo)
                bg_img.image = photo
                bg_img.pack()

                #failed implementation
                if usr_choice == 1:
                        file = open("data/easy_data.txt", "r", encoding="utf-8-sig")
                        data = file.read()
                        lst = data.split()
                elif usr_choice == 2:
                        file = open("data/medium_data.txt", "r", encoding="utf-8-sig")
                        data = file.read()
                        lst = data.split()
                elif usr_choice == 3:
                        file = open("data/hard_data.txt", "r", encoding="utf-8-sig")
                        data = file.read()
                        lst = data.split()
                var1 = "Press"
                var2 = "Start"
                running = False
                usr_data = []
                history_data = []

                #result popup frame
                def popupResult(x,y):
                        window = tk.Toplevel()

                        background_img = tk.PhotoImage(file = "img/result_bg.png")

                        bg_img = tk.Label(window, image = background_img)
                        bg_img.pack()
                        
                        window.geometry("360x240+500+350")
                        window.title("Result")

                        wpm = len(x)

                        #accuracy calculation
                        a = len(x)
                        b = len(y)
                        try:
                                if a < 100:
                                        accuracy = 100*(b/a)
                                elif a > 100:
                                        accuracy = b*(a/100)
                        except ZeroDivisionError:
                                wpm = "Zero Division Error"
                                accuracy = "Zero Division Error"
                        
                        wpm_lbl = tk.Label(window,
                                            text = "WPM: ",
                                            bg = "#455a64",
                                            fg = "#000",
                                           font = ("Arial", "16"))
                        wpm_lbl.place(x = 70, y = 30)

                        accuracy_lbl = tk.Label(window,
                                                text = "Accuracy: ",
                                                bg = "#455a64",
                                                fg = "#000",
                                                font = ("Arial", "16"))
                        accuracy_lbl = tk.Label(window,
                                                text = "Accuracy: ",
                                                bg = "#455a64",
                                                fg = "#000",
                                                font = ("Arial", "16"))
                        accuracy_lbl.place(x = 85, y = 60)

                        wpm_value = tk.Label(window,
                                             text = wpm,
                                             bg = "#455a64",
                                             fg = "#000",
                                             font = ("Arial", "16"))
                        wpm_value.place(x = 140, y = 30)

                        accuracy_value = tk.Label(window,
                                                text = accuracy,
                                                bg = "#455a64",
                                                fg = "#000",
                                                font = ("Arial", "14"))
                        accuracy_value.place(x = 185, y = 60)
                        window.configure(background = "white")
                        window.mainloop()

                #start button function
                def start():
                        running = True
                                
                        def set_count():
                                global timecount
                                if running == True:
                                        timecount = 60
                                        timer.after(0, refresh)

                        def refresh():
                                global timecount
                                if timecount != 0 and running == True:
                                        timecount -= 1
                                        start_btn.configure(state = "disabled")
                                        timer.configure(text = timecount)
                                        timer.after(1000, refresh)
                                elif timecount == 0 and running == True:
                                        popupResult(usr_data, history_data)
                                        
                        set_count()
                        assign_value1()
                        assign_value2()
                        usr_input.configure(state = "normal")
                        usr_input.focus()
                        
                #receiving/determining inputs
                def input_value(event):
                        value = usr_input.get("1.0", tk.END)
                        if not usr_data:
                                value = value[:-1]
                        else:
                                value = value[:-1]
                                value = value[1:]
                        lbl1_value = lbl1.cget("text")
                        lbl2_value = lbl2.cget("text")
                        if value == lbl1_value:
                                assign_value1()
                                history_data.append(lbl1_value)
                        elif value == lbl2_value:
                                assign_value2()
                                history_data.append(lbl2_value)
                        usr_data.append(value)
                        usr_input.delete("1.0", tk.END)

                #reset
                def reset():
                        global timecount
                        running = False
                        usr_data.clear()
                        history_data.clear()
                        timecount = "60"
                        start_btn.configure(state = "active")
                        timer.configure(text = timecount)
                        lbl1.configure(text = "Press")
                        lbl2.configure(text = "Start")
                        usr_input.configure(state = "disabled")

                #outputting data1
                def assign_value1():
                        random.shuffle(lst)
                        var1 = lst[random.randint(1, (len(lst)-1))]
                        lbl1.configure(text = var1)

                #outputting data2
                def assign_value2():
                        random.shuffle(lst)
                        var2 = lst[random.randint(1, (len(lst)-1))]
                        lbl2.configure(text = var2)

                #back button
                back_btn = tk.Button(self,
                                     text = "Back",
                                     width = 10,
                                      padx = 30,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: controller.show_frame(startPage))
                back_btn.place(x = 10, y = 10)

                #time count
                timecount = 0
                timer = tk.Label(self,
                                 text = timecount,
                                 width = 10,
                                 padx = 0,
                                 pady = 10,
                                 font = ("Arial", 12),
                                 bd = 0,
                                 bg = "#c1bd7d",
                                 relief = "groove")
                timer.place(x = 330)

                #reset button
                reset_btn = tk.Button(self,
                                        text = "Reset",
                                        cursor = "hand1",
                                        bd = 0,
                                        bg = "#543525",
                                        fg = "#fff",
                                        activebackground = "#966650",
                                        padx = 16,
                                        pady = 10,
                                        command = reset)
                reset_btn.place(x = 580, y = 15)

                #start button
                start_btn = tk.Button(self,
                                        text = "Start",
                                        cursor = "hand1",
                                        bd = 0,
                                        bg = "#543525",
                                        fg = "#fff",
                                        activebackground = "#966650",
                                        padx = 20,
                                        pady = 10,
                                        command = start)
                start_btn.place(x = 500, y = 15)

                #first word
                lbl1 = tk.Label(self,
                                text = var1,
                                padx = 60,
                                pady = 13,
                                font = ("Arial", 18),
                                bd = 0,
                                bg = "#a69a03")
                lbl1.place(x = 80, y = 100)

                #second word
                lbl2 = tk.Label(self,
                                text = var2,
                                padx = 60,
                                pady = 13,
                                font = ("Arial", 18),
                                bd = 0,
                                bg = "#a69a03")
                lbl2.place(x = 430, y = 100)

                #selecting input
                def select(value):
                                usr_input.insert(tk.END, value)

                #User inputting area   
                usr_input = tk.Text(self,
                                    height = 1,
                                    width = 88,
                                     cursor = "hand1",
                                    font = ("Arial", 20),
                                    spacing1 = 8,
                                    spacing3 = 8,
                                    bg = "#988a72",
                                    fg = "#001a36",
                                    bd = 0)
                usr_input.place(x = 4, y = 220)


                #defining virtual keyboard start
                firstrow = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                secondrow = ['q','w','e', 'r', 'y', 'u', 'i', 'o', 'p', '\' ', '(']
                thirdrow = ['a', 's', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', ';']
                fourthrow = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', ')']
                
                corX = 4
                for button in firstrow:
                    tk.Button(self,
                              text = button,
                              padx = 25,
                              pady = 5,
                              bg = "#2a1d08",
                              fg = "#d4b9cc",
                              bd = 0,
                              activebackground = "#988a72",
                                     cursor = "hand1",
                              command = lambda x=button: select(x)).place(x = corX, y = 300)
                    corX += 65

                clear = tk.Button(self,
                                text = "clear",
                                    padx = 10,
                                    pady = 4,
                                      bd = 0,
                                      bg = "#2a1d08",
                                      fg = "#d4b9cc",
                                      activebackground = "#988a72",
                                     cursor = "hand1",
                              command = lambda: usr_input.delete("1.0", tk.END))
                clear.place(x = 655, y = 300)

                corX = 4
                for button in secondrow:
                    tk.Button(self,
                              text = button,
                              padx = 25,
                              pady = 5,
                              bd = 0,
                              bg = "#2a1d08",
                              fg = "#d4b9cc",
                              activebackground = "#988a72",
                                     cursor = "hand1",
                              command = lambda x=button: select(x)).place(x = corX, y = 335)
                    corX += 65

                corX = 4
                for button in thirdrow:
                        tk.Button(self,
                              text = button,
                              padx = 25,
                              pady = 5,
                              bd = 0,
                              bg = "#2a1d08",
                              fg = "#d4b9cc",
                              activebackground = "#988a72",
                                     cursor = "hand1",
                              command = lambda x=button: select(x)).place(x = corX, y = 370)
                        corX += 65

                corX = 4
                for button in fourthrow:
                            tk.Button(self,
                                      text = button,
                                      padx = 25,
                                      pady = 5,
                                      bd = 0,
                                      bg = "#2a1d08",
                                      fg = "#d4b9cc",
                                      activebackground = "#988a72",
                                     cursor = "hand1",
                              command = lambda x=button: select(x)).place(x = corX, y = 405)
                            corX += 65
                            
                spaceKey = tk.Button(self,
                                     text = "space",
                                     padx = 100,
                                     pady = 5,
                              bd = 0,
                              bg = "#2a1d08",
                              fg = "#d4b9cc",
                              activebackground = "#988a72",
                                     cursor = "hand1",
                                     command = lambda: usr_input.insert(tk.INSERT, " "))
                spaceKey.place(x = 230, y = 440)
                usr_input.bind('<Return>', input_value)
                #defining virtual keyboard end
                

class AboutPage(tk.Frame): #about page
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                image = Image.open("img/abt_bg.jpg")
                photo = ImageTk.PhotoImage(image)
                bg_img = tk.Label(self, image=photo)
                bg_img.image = photo
                bg_img.pack()

                #back button
                back_btn = tk.Button(self,
                                     text = "Back",
                                     width = 10,
                                      padx = 30,
                                      pady = 10,
                                      bg = "#45453c",
                                      fg = "#fff",
                                      activebackground = "#858585",
                                      activeforeground = "#000",
                                      cursor = "hand1",
                                      bd = 0,
                                      command = lambda: controller.show_frame(MainMenu))
                back_btn.place(x = 10, y = 10)

                #about button
                abt_font = ("Arial", 12, "bold")
                text = """ Sorry to not include your favorite white color,
                                grey is the brightest color
                                        the creator of the app can see

                                                Created by Zet
                                                For Python Project (3rd Year LAP)"""
                lbl = ttk.Label(self, text = text,
                               background = "#eae9e7",
                                font = abt_font,
                                cursor = "heart")
                lbl.place(x = 30, y = 130)
                                     
        

def main():
        app = typtolator()
        app.mainloop()
        
if __name__ == "__main__":
        main()
