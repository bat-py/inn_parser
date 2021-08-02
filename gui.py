import tkinter as tk
from tkinter import ttk, Frame, filedialog
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

import multiprocessing as mp
#from . import parser
#from . import excel_writer


# Creating root window and setting themes and creating top menu
class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Creating and setting root window
        self.title("Парсер сайта https://pb.nalog.ru/")
        self.geometry('600x400')
        self.resizable(width=False, height=False)
        ico = ImageTk.PhotoImage(Image.open('images/icon.ico'))
        self.iconphoto(True, ico)

        # Setting theme for ttk
        self.style = ThemedStyle(self)
        self.style.set_theme('breeze')

        # Creating top menu and first page
        self.top_menu()
        self.firstpage()

        self.mainloop()

    # Top Menu Frame
    def top_menu(self):
        '''Creates top menu'''
        #Settings Top Menu
        top_menu = tk.Frame(self)
        top_menu.configure(bg='white', height=65, pady=5  )

        #Top Menu image
        my_image = Image.open('images/nalog_ru.png')
        my_image = my_image.resize((53, 53), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(my_image)
        tk_image_in_label = tk.Label(top_menu, image=self.tk_image)

        #DOC in the RIGHT side of Top Menu
        doc_style = ttk.Style().configure('top.TLabel', background='white')
        about_program = 'С помощью этой программы вы можете скачать данные из сайта https://pb.nalog.ru/\nДанные сохраняются в xlsx (Excel) формате'
        doc_label = ttk.Label(top_menu, text=about_program, style='top.TLabel')

        #Pack System
        top_menu.pack(fill=tk.X)
        top_menu.propagate(False)
        tk_image_in_label.grid(row=0, column=0, padx=7)
        doc_label.grid(row=0, column=1)

    # First Page
    def firstpage(self):
        self.first_window = Frame(self)

        # Get CSV file's path frame
        get_csv_file_label = ttk.Label(self.first_window,
                                 text='Пожалуйста выберите csv файл с INN:')
        get_csv_file_label.configure(font=('Calibri', 11))

        get_csv_file_frame = ttk.Frame(self.first_window)
        self.get_csv_file_entry = ttk.Entry(get_csv_file_frame, width=52)
        self.get_csv_file_entry.state(['disabled'])
        self.get_csv_file_button = ttk.Button(get_csv_file_frame,
                                    text='Обзор',
                                    command=self.get_csv_file_func,
                                    style='TButton'
                                    )


        #Get place to save
        place_to_save_label = ttk.Label(self.first_window,
                                        text='Выберите место сохранения Excel файла')
        place_to_save_label.configure(font=('Calibri', 11))
        place_to_save_frame = ttk.Frame(self.first_window)
        self.place_to_save_entry = ttk.Entry(place_to_save_frame, width=52)
        self.place_to_save_entry.state(['disabled'])
        self.place_to_save_button = ttk.Button(place_to_save_frame,
                                          text='Сохранить как',
                                          command=self.place_to_save_func,
                                          state='disabled',
                                          style='TButton'
                                          )


        # Button 'Далее'
        self.next_page_button = ttk.Button(self.first_window,
                                      text='Далее',
                                      #command=self.secondpage,
                                      state='disabled',
                                      style='TButton'
                                      )

        # firstpage's Pack System
        self.first_window.pack(fill=tk.BOTH, expand=1)
        get_csv_file_label.pack(fill=tk.X, padx=20, pady=(20, 5))
        get_csv_file_frame.pack(fill=tk.X)
        self.get_csv_file_entry.grid(row=0, column=0, padx=(40, 3))
        self.get_csv_file_button.grid(row=0, column=1, padx=3)

        place_to_save_label.pack(fill=tk.X, padx=20, pady=(40, 5))
        place_to_save_frame.pack(fill=tk.X)
        self.place_to_save_entry.grid(row=0, column=0, padx=(40, 3))
        self.place_to_save_button.grid(row=0, column=1, padx=3)

        self.next_page_button.place(x=465, y=265)

    # Second Page
    def secondpage(self):
        self.first_window.destroy()
        self.second_window = Frame(self)

        # secondpage's Pack System
        self.first_window.pack(fill=tk.BOTH, expand=1)




    # (firstpage) Opens filedialog, gets path and writes path to "self.csv_file_path"
    def get_csv_file_func(self):
        a = filedialog.askopenfilename(title='Select csv file', filetypes=(('csv file', '*.csv'), ))

        self.get_csv_file_entry.state(['!disabled'])
        self.get_csv_file_entry.delete(0, tk.END)
        self.get_csv_file_entry.insert(0, a)
        self.get_csv_file_entry.state(['disabled'])
        self.place_to_save_button.state(['!disabled'])

    # (firstpage) Opens filedialog, gets place to save parsed date
    def place_to_save_func(self):
        place = filedialog.asksaveasfilename(title='Куда вы хотите сохранить файл',
                                             initialfile = 'parsed_data',
                                             defaultextension = 'xlsx'
                                             )
        self.place_to_save_entry.state(['!disabled'])
        self.place_to_save_entry.delete(0, tk.END)
        self.place_to_save_entry.insert(0, place)
        self.place_to_save_entry.state(['disabled'])
        self.next_page_button.state(['!disabled'])