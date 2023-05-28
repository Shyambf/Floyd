import customtkinter
import tkinter
import math
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")  
import pprint

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Настройка")
        self.add("Флойд")
        self.add("Поиск")
        self.matrix_size = 0
        self.size = 0
        self.nev_matrix_size = 0
        

        # add widgets on tabs
        self.string_input_button = customtkinter.CTkButton(self.tab("Настройка"), text="Ввести размер матрицы", command=self.open_input_dialog_event)
        self.string_input_button.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.label = customtkinter.CTkLabel(self.tab("Настройка"), text=f"matrix size: {self.size}")
        self.label.grid(row=0, column=1, pady=10)

        self.size_button = customtkinter.CTkButton(self.tab("Настройка"), text='Создать матрицу', command=self.create_matrix)
        self.size_button.grid(row=2, column=0)

        self.matrix_frame = customtkinter.CTkFrame(self.tab("Настройка"))
        self.matrix_frame.grid(row=3, column=0)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tab("Настройка"), values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=1, padx=20, pady=(10, 10))
        
        self.submit_btn = customtkinter.CTkButton(self.tab("Флойд"), text='Рассчитать по флойду', command=self.algorithm)
        self.submit_btn.grid(row=0, column=0, pady=10)

        self.output_matrix = []
        self.output_matrix_frame = customtkinter.CTkFrame(self.tab("Флойд"))
        self.output_matrix_frame.grid(row=1, column=0)


        self.froms1 = customtkinter.CTkEntry(self.tab("Поиск"), width=100, placeholder_text='откуда')
        self.froms1.grid(row=0, column=0, sticky='s')

        self.froms = customtkinter.CTkEntry(self.tab("Поиск"), width=100, placeholder_text='куда')
        self.froms.grid(row=1, column=0, sticky='s')

        self.submit_btn = customtkinter.CTkButton(self.tab("Поиск"), text='поиск', command=self.get_len)
        self.submit_btn.grid(row=0, column=1, pady=10)

        self.label1 = customtkinter.CTkLabel(self.tab("Поиск"), text=f"len: ")
        self.label1.grid(row=3, column=0, pady=10)



    def create_matrix(self):
        size = self.size
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                self.matrix[i][j].destroy()

        self.matrix_size = int(size)
        self.matrix = []

        for i in range(self.matrix_size):
            self.matrix.append([])
            for j in range(self.matrix_size):
                self.matrix[i].append(customtkinter.CTkEntry(self.matrix_frame, width=35))
                if i == j: self.matrix[i][j].configure(state="disabled", corner_radius=50, fg_color="#FF0000")

                self.matrix[i][j].grid(row=i, column=j, padx=5, pady=5)


    def algorithm(self):
        self.nev_matrix_size = 0
        for i in range(self.nev_matrix_size):
            for j in range(self.nev_matrix_size):
                self.output_matrix[i][j].destroy()
            
        matrix = []
        for i in range(self.matrix_size):
            matrix.append([])
            for j in range(self.matrix_size):
                val = self.matrix[i][j].get()
                if i == j:
                    matrix[i].append(0)
                elif val.lower() == '0' or not val :
                    matrix[i].append(math.inf)
                else:
                    if (val.isnumeric()):
                        matrix[i].append(int(val))
                    else:
                        self.matrix[i][j].focus() 
                        return
        for k in range(self.matrix_size):
            prev = matrix.copy()
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    matrix[i][j] = min(prev[i][j], prev[i][k] + prev[k][j])
        self.nev_matrix_size = self.matrix_size
        for i in range(self.matrix_size):
            self.output_matrix.append([])
            for j in range(self.matrix_size):
                text = matrix[i][j]
                if i == j: text = '-1'
                elif (text == math.inf) or text == 0: text = '∞'
                self.output_matrix[i].append(customtkinter.CTkLabel(self.output_matrix_frame, text=text))
                self.output_matrix[i][j].grid(row=i, column=j, padx=7)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def get_len(self):
        x = self.froms1.get()
        y = self.froms.get()
        try:
            self.label1.configure(text = f'len: {self.output_matrix[int(x)-1][int(y)-1].cget("text")}')
        except BaseException:
            self.label1.configure(text = f'len: Такого нет')
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        self.size = dialog.get_input()
        self.label.configure(text=f"matrix size: {self.size}")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)



app = App()
app.mainloop()