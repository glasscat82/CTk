from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import tkinter as tk
import customtkinter as CTk
import secrets

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Generator password")
        self.resizable(False, False)
        
        # 1 label block row=0 column=0
        self.logo = CTk.CTkImage(dark_image=Image.open("img_green.png"), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)
        
        # 2 frame block row=1 column=0
        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))
        
        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100, command=self.set_password)
        self.btn_generate.grid(row=0, column=1)
        
        # 3 frame block row=2 column=0 -> the name settings_frame
        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # slider + input
        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_= 0, to=100, number_of_steps=100, command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        # input value
        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")
        
        # checkbox 1 -> in settings_frame
        self.cb_digits_var = tk.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)
        self.cb_digits.select()
        
        # checkbox 2 -> in settings_frame
        self.cb_lower_var = tk.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        # checkbox 3 -> in settings_frame
        self.cb_upper_var = tk.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        # checkbox 4 -> in settings_frame
        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbols_var,
                                          onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)

        # select 5 -> in settings_frame
        self.appearance_mode_option_menu = CTk.CTkOptionMenu(self.settings_frame,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        # set setting fest
        self.appearance_mode_option_menu.set("Dark")
        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, "12")
        self.toplevel_window = None
    
    def set_password(self):
        lenght_ = int(self.password_length_slider.get())
        g_ch_ = self.get_characters()
        
        if not g_ch_:
            self.open_toplevel()
        else:
            get_pass_ = "".join(secrets.choice(g_ch_) for _ in range(lenght_))        
            
            self.entry_password.delete(0, 'end')
            self.entry_password.insert(0, get_pass_)
    
    def slider_event(self, value):        
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        return "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbols_var.get())

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CTk.CTkToplevel()  # create window if its None or destroyed 
            self.toplevel_window.title('Message for you')
            self.toplevel_window.geometry("300x60")
            
            self.label = CTk.CTkLabel(master=self.toplevel_window, text="Please click checkbox")
            self.label.pack(padx=20, pady=20)
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == '__main__':
    app = App()
    app.mainloop()