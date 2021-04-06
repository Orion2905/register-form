import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime as dt

class Register:
    def __init__(self, root):
        root.grid_columnconfigure(0, weight=1)
        root.geometry("600x640")
        root.resizable(False, False)
        root.title("Registration form")
        root.configure(background="#dff9fb")

        font = ("Bebas",20, "bold")
        font_2 = ("Consolas", 16, "bold")
        font_3 = ("Candara", 14)
        font_4 = ("Bebas", 10)

        self.v = tk.StringVar(root)
        v_2 = tk.StringVar(root, "0")

        self.img_1 = ImageTk.PhotoImage(file="img/reg.png")
        
        image = tk.Label(root, image=self.img_1, bg="#c7ecee")
        image.grid(sticky="WE")
        # Titolo della pagina
        title = tk.Label(
            root,
            text="Registration form",
            font = font,
            bg="#c7ecee"
        )
        title.grid(sticky="WE")
        # dati inseriti dall'utente
        name = tk.Label(
            root,
            text="Name",
            font=font_2,
            bg="#dff9fb"
        )
        name.grid(row=2, column=0)
        self.name_entry = tk.Entry(
            root,
            justify="center"
        )
        self.name_entry.grid(row=3, column=0, ipady=5, sticky="WE", padx="100")

        surname = tk.Label(
            root,
            text="Surname",
            font=font_2,
            bg="#dff9fb"
        )
        surname.grid(row=4, column=0)
        self.surname_entry = tk.Entry(
            root,
            justify="center"
        )
        self.surname_entry.grid(row=5, column=0, ipady=5, sticky="WE", padx="100")

        email = tk.Label(
            root,
            text="Email",
            font=font_2,
            bg="#dff9fb"
        )
        email.grid(row=6, column=0)

        self.email_entry = tk.Entry(
            root,
            justify="center"
        )
        self.email_entry.grid(row=7, column=0, ipady=5, sticky="WE", padx="100")

        gender = tk.Label(
            root,
            text="Gender",
            font=font_2,
            bg="#dff9fb"
        )
        gender.grid(row=8, column=0)

        frame = tk.Frame(
            root,
            bg="#dff9fb"
        )
        frame.grid()

        self.male_entry = tk.Radiobutton(
            frame,
            text="Male",
            value="male",
            variable=self.v,
            font = font_3,
            bg="#dff9fb"
        )
        self.male_entry.grid(row=0, column=0)

        self.famale_entry = tk.Radiobutton(
            frame,
            text="Famale",
            value="famale",
            variable=self.v,
            font = font_3,
            bg="#dff9fb"
        )
        self.famale_entry.grid(row=0, column=1, ipady=5)

        password = tk.Label(
            root,
            text="Password",
            font=font_2,
            bg="#dff9fb"
        )
        password.grid(row=11, column=0)

        self.password_entry = tk.Entry(
            root,
            show="⬤",
            justify="center"
        )
        self.password_entry.grid(row=12, column=0, ipady=5, sticky="WE", padx="100")

        rep_password = tk.Label(
            root,
            text="Repeat Password",
            font=font_2,
            bg="#dff9fb"
        )
        rep_password.grid(row=13, column=0)

        self.rep_password_entry = tk.Entry(
            root,
            show="⬤",
            justify="center"
        )
        self.rep_password_entry.grid(row=14, column=0, ipady=5, sticky="WE", padx="100")

        self.submit = tk.Button(
            root,
            text="Submit",
            command=self.submit,
            width=30,
            height=2,
            bg="#badc58",
            font=font_4
        )
        self.submit.grid(pady=15)

        footer = tk.Label(
            root,
            text = "Copyright © " + str(dt.datetime.now().strftime("%Y")) + " OrionDev"
        )
        footer.grid(pady=0)

    def submit(self):
        values = {
            "Name" : self.name_entry.get(),
            "Surname" : self.surname_entry.get(),
            "Email" : self.email_entry.get(),
            "Gender" : self.v.get(),
            "Password" : self.password_entry.get(),
            "Repeated Password" : self.rep_password_entry.get()
        }
        values = self.check(values)
        if "is missing." in values:
            self.submit['bg'] = "#eb4d4b"
            messagebox.showerror(title="Error", message=values)
        elif " is not allowed" in values:
            self.submit['bg'] = "#eb4d4b"
            messagebox.showerror(title="Error", message=values)
        elif "Invalid Email" in values:
            self.submit['bg'] = "#eb4d4b"
            messagebox.showerror(title="Error", message=values)
        elif "Passwords do not match" in values:
            self.submit['bg'] = "#eb4d4b"
            messagebox.showerror(title="Error", message=values)
        elif "The password requires" in values:
            self.submit['bg'] = "#eb4d4b"
            messagebox.showerror(title="Error", message=values)
        else:

            success_message = f'Successfully registered!\nWelcome {values["Name"], values["Surname"]};\n' \
                              f'Your gender is {values["Gender"]};' \
                              f'\nYour email is {values["Email"]};' \
                              f'\nYour password is {values["Password"]}'

            self.submit['bg'] = "#dff9fb"
            messagebox.showinfo(title="Success!", message=success_message)
            # print("successfully registered",values)
            # print("Welcome", values["Name"], values["Surname"])
            # print(
            #     "Your email is " + values["Email"] +
            #     "\nYour gender is " + values["Gender"] +
            #     "\nYour password is " + values["Password"]
            # )


    def check(self, values):
        results = values
        not_allowed = [
            "-", "+", ".", "#", '"', "'", "!", "£", "$", "%", "&", "/", "(", ")", "=", "?", "^", ">", "<",
            "[", "]", "*", ";", ",", ":", "_", "°", "ç", "§", "@", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        ]
        for value in values:
            if len(values[value]) <= 0: #Controlla se il campo è stato compilato
                results = "The " + str(value) + " is missing."
                break
            else:
                #Controllo del nome
                for i in not_allowed:
                    if i in values["Name"]:
                        results = i + " is not allowed in the Name"
                        break
                    elif i in values["Surname"]:
                        results = i + " is not allowed in the Surname"
                        break

            #Controllo della mail
            if "@" not in values["Email"]:
                results = "Invalid Email"
                break

            #controllo della password
            if values["Password"] != values["Repeated Password"]:
                results = "Passwords do not match"
                break
            elif len(values["Password"]) < 8:
                results = "The password requires at least 8 characters"
                break

        return results

if __name__ == '__main__':
    root = tk.Tk()
    reg = Register(root)
    root.mainloop()