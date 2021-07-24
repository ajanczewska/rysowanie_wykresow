#-*- coding: utf-8 -*-
#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from matplotlib import rc
import numpy as np
import matplotlib.figure
import matplotlib.backends.backend_tkagg
import sympy
import re
class Application(tk.Frame):
    def __init__(self, master=None):
        """Metoda generuje głowne okno GUI i wywołuje metody, które tworzą elementy w nim zawarte"""
        super().__init__(master)
        self.master = master
        self.master.title("Rysowanie wykresu funkcji")
        
        self.master.geometry('950x650')
        self.pack()

        self.created_labels()
        self.created_text_fields()
        self.created_calculator()
        self.created_legend()
        self.created_draw_btn()
        self.created_button_quit()

    def created_labels(self):
        """Metoda tworzy widgety, które odpowiadają za wyświetlanie tekstu"""
        self.wz_label = tk.Label(self.master, text="Podaj wzór funkcji (jako zmienną przyjmij 'x')", font=('Arial', 14, 'bold'))
        self.wz_label.pack()
        self.wz_label.place(x=70, y=40)
        
        self.x_label = tk.Label(self.master, text="Zakres x", font=('bold'))
        self.x_label.pack()
        self.x_label.place(x=70, y=230)


        self.od_x = tk.Label(self.master, text="od")
        self.od_x.pack()
        self.od_x.place(x=70, y=260)

        self.do_x = tk.Label(self.master, text="do")
        self.do_x.pack()
        self.do_x.place(x=170, y=260)

        self.etykieta_x = tk.Label(self.master, text="Etykieta na osi x", font=('bold'))
        self.etykieta_x.pack()
        self.etykieta_x.place(x=210, y=395)

        self.etykieta_y = tk.Label(self.master, text="Etykieta na osi y", font=('bold'))
        self.etykieta_y.pack()
        self.etykieta_y.place(x=360, y=395)

        self.y_label = tk.Label(self.master, text="Zakres y", font=('bold'))
        self.y_label.pack()
        self.y_label.place(x=70, y=315)

        self.od_y = tk.Label(self.master, text="od")
        self.od_y.pack()
        self.od_y.place(x=70, y=345)

        self.do_y = tk.Label(self.master, text="do")
        self.do_y.pack()
        self.do_y.place(x=170, y=345)

        self.title_label = tk.Label(self.master, text="Tytuł", font=('bold'))
        self.title_label.pack()
        self.title_label.place(x=70, y=395)

    def created_text_fields(self):
        """
        Metoda tworzy pola, w których użytkownik może wpisać tekst(wzór funkcji, zakresy, tytyuł wykresu i etykiet)
        Metoda tworzy również pola, w których są wyświetlane komunikaty dotyczące podanych zakresów
        """
        self.equation = tk.StringVar()
        self.wz_text = tk.Entry(self.master, width=21, textvariable=self.equation)
        self.wz_text.pack()
        self.wz_text.place(x=70, y=75)

        self.mgs_empty_wz = tk.Label(self.master, text='', font=('Arial', 8, 'italic'))
        self.mgs_empty_wz.pack()
        self.mgs_empty_wz.place(x=70, y=95)
        
        self.zakres_odx = tk.Entry(self.master, width=10)
        self.zakres_odx.pack()
        self.zakres_odx.place(x=100, y=260)

        self.zakres_msg = tk.Label(self.master, text='', font=('Arial', 8, 'italic'))
        self.zakres_msg.pack()
        self.zakres_msg.place(x=100, y=280)

        self.zakres_ody = tk.Entry(self.master, width=10)
        self.zakres_ody.pack()
        self.zakres_ody.place(x=100, y=345)

        self.zakres_ymsg = tk.Label(self.master, text='', font=('Arial', 8, 'italic'))
        self.zakres_ymsg.pack()
        self.zakres_ymsg.place(x=100, y=365)

        self.zakres_dox = tk.Entry(self.master, width=10)
        self.zakres_dox.pack()
        self.zakres_dox.place(x=200, y=260)

        self.zakres_doy = tk.Entry(self.master, width=10)
        self.zakres_doy.pack()
        self.zakres_doy.place(x=200, y=345)

        self.title_entry = tk.Entry(self.master)
        self.title_entry.pack()
        self.title_entry.place(x=70, y=425)

        self.osx_entry = tk.Entry(self.master)
        self.osx_entry.pack()
        self.osx_entry.place(x=210, y=425)

        self.osy_entry = tk.Entry(self.master)
        self.osy_entry.pack()
        self.osy_entry.place(x=360, y=425)

    def created_calculator(self):
        """Metoda tworzy przyciski, które służą do budowania wzoru funkcji"""
        self.op1_btn= tk.Button(root, text='x', height=1, width=5, command=lambda: self.press('x'))
        self.op1_btn.pack()
        self.op1_btn.place(x=70, y=130)
        
        self.op2_btn = tk.Button(root, text='1/x', height=1, width=5, command=lambda: self.press('1/x'))
        self.op2_btn.pack()
        self.op2_btn.place(x=114, y=130)
        
        self.op3_btn = tk.Button(root, text='sqrt(x)', height=1, width=5, command=lambda: self.press('sqrt(x)'))
        self.op3_btn.pack()
        self.op3_btn.place(x=156, y=130)
        
        self.op4_btn = tk.Button(root, text='x^2', height=1, width=5, command=lambda: self.press('x^2') )
        self.op4_btn.pack()
        self.op4_btn.place(x=198, y=130)
        
        self.op5_btn = tk.Button(root, text='+', height=1, width=5, command=lambda: self.press('+'))
        self.op5_btn.pack()
        self.op5_btn.place(x=70, y=156)
        
        self.op6_btn = tk.Button(root, text='-', height=1, width=5, command=lambda: self.press('-'))
        self.op6_btn.pack()
        self.op6_btn.place(x=114, y=156)

        self.op7_btn = tk.Button(root, text='*', height=1, width=5, command=lambda: self.press('*'))
        self.op7_btn.pack()
        self.op7_btn.place(x=156, y=156)
    
        self.op8_btn = tk.Button(root, text='/', height=1, width=5, command=lambda: self.press('/'))
        self.op8_btn.pack()
        self.op8_btn.place(x=198, y=156)

        self.op9_btn = tk.Button(root, text='(', height=1, width=5, command=lambda: self.press('('))
        self.op9_btn.pack()
        self.op9_btn.place(x=70, y=182)
        
        self.op10_btn = tk.Button(root, text=')', height=1, width=5, command=lambda: self.press(')'))
        self.op10_btn.pack()
        self.op10_btn.place(x=114, y=182)

        self.op11_btn = tk.Button(root, text='sin(x)', height=1, width=5, command=lambda: self.press('sin(x)'))
        self.op11_btn.pack()
        self.op11_btn.place(x=156, y=182)

        self.op12_btn = tk.Button(root, text='cos(x)', height=1, width=5, command=lambda: self.press('cos(x)'))
        self.op12_btn.pack()
        self.op12_btn.place(x=198, y=182)

    def created_legend(self):
        """Metoda tworzy przycisk, który pozwala użytkownikowi wybrać legendę"""
        s = ttk.Style()
        s.configure('TCheckbutton', font=(10))
        self.var = tk.IntVar()
        self.check_btn = ttk.Checkbutton(self.master, text="Legenda na wykresie",takefocus=0, style='TCheckbutton', variable=self.var)
        self.check_btn.pack()
        self.check_btn.place(x=70, y=480)

    def created_draw_btn(self):
        """Metoda tworzy przycisk, który uruchami proces tworzenia wykresu funkcji"""
        self.draw_btn = tk.Button(self.master, text="RYSUJ", font=('Roboto', 12, 'bold'), foreground='#442963', background='#CEC9C9')
        self.draw_btn.pack()
        self.draw_btn.place(x=70, y=520)
        self.draw_btn.bind('<Button-1>', self.created_canvas_figure)

    def created_button_quit(self):
        """Metoda tworzy przycisk kończący program"""
        self.bn_quit = tk.Button(text='ZAKOŃCZ', command=root.quit, font=('Roboto', 8, 'bold'), foreground='#F02420', background='#CEC9C9')
        self.bn_quit.pack()
        self.bn_quit.place(x=770, y=530)

    def press(self, num):
        """
        Metoda przyjmuje wartości z przycisków
        Tworzy zmienną expresion, do której przypisuje zawartość pola, w którym użytkownik podaje wzór funkcji, a nastepnie wartość z klikniętego przycisku
        Ustawia wartość zmiennej expresion na zmiennej equation
        """
        self.expresion = str(self.wz_text.get())
        self.expresion = self.expresion + str(num)
        self.equation.set(self.expresion)

    def created_canvas_figure(self, event):
        """
        Metoda jest wywoływana po kliknięciu przez użytkownika na przycisk 'rysuj'
        Tworzy ona figurę, na której dodaje wykres z podanymi parametrami
        Obsługuje błędy dla zakresów, które nie są liczbami
        Wyświtla wykres na 'płótnie'
        """
        self.wz_text.config(background='white')
        func_string = str(self.wz_text.get())
        f = matplotlib.figure.Figure(figsize=(4, 3), dpi=100, tight_layout=(10,5,5))
        fig = f.add_subplot()
        fig.set_xlabel('')
        fig.set_ylabel('')
        fig.set_title('')
        try:
            zakres_odx = float(self.zakres_odx.get())
            zakres_dox = float(self.zakres_dox.get())
            x = np.arange(zakres_odx, zakres_dox, 0.1)
            self.zakres_msg.config(text='')
        except ValueError:
            self.zakres_msg.config(text="Proszę podać zakres jako liczbę", foreground='red')
        
        def string2func(string):
            """
            Metoda przyjmuje wzór funkcji z pola, w którym użytkownik go podaje
            Sprawdza czy podany wzór znajduje się na liście symboli i funkcji, które mogą być częścią matematycznego wzoru
            Jeśli nie jest na liście przerywa program
            W przeciwnym wypadku zwraca funkcję func
            """
            allowed_words = ['x', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp']
            replacements = {'sin':'np.sin', 'cos':'np.cos', 'tan':'np.tan', 'sqrt':'np.sqrt', 'log':'np.log', 'exp':'np.exp', '^':'**'}
            for word in re.findall('[a-zA-Z_=@$&#,]+', string):
                if word not in allowed_words:
                    self.wz_text.config(background='#F9CBC1')
                    break
            for old, new in replacements.items():
                string = string.replace(old, new)
                def func(x):
                    """Konwertuje string na wzór matematyczny po czym go zwraca"""
                    return eval(string)
            return func     

        if func_string != '':
            self.mgs_empty_wz.config(text='')
            try:
                for string in func_string.split(';'):
                    func = string2func(string)
                    x = np.arange(zakres_odx, zakres_dox, 0.1)
                    fig.set_xlabel(str(self.osx_entry.get()))
                    fig.set_ylabel(str(self.osy_entry.get()))

                    fig.set_xlim([zakres_odx, zakres_dox])
                    
                    title = str(self.title_entry.get())
                    fig.set_title(title)

                    fig.plot(x, func(x))
                try:
                    zakres_ody = float(self.zakres_ody.get())
                    zakres_doy = float(self.zakres_doy.get())
                    fig.set_ylim([zakres_ody, zakres_doy])
                    self.zakres_ymsg.config(text='')
                except ValueError:
                    self.zakres_ymsg.config(text="Możesz również wybrać zakres liczbowy na osi y", foreground='red')
                    fig.set_ylim()


                if self.var.get() == 1:
                    fig.legend(func_string.split(';'))
                else:
                    fig.legend('')
                
            except:
                self.wz_text.config(background='#F9CBC1')

        else:
            self.mgs_empty_wz.config(text='Proszę podać wzór funkcji', foreground='red')

        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(f)
        self.canvas.get_tk_widget().pack()
        self.canvas.get_tk_widget().place(x=450, y=55)
        
        self.toolbar = matplotlib.backends.backend_tkagg.NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.update()
        self.toolbar.pack()
        self.toolbar.place(x=600, y=395)        

if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()