import tkinter as tk
from tkinter import messagebox, filedialog
from crud import add_client, add_order, add_payment
from reports import export_csv, export_json, export_excel

class CRMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini CRM")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Добавить клиента", command=self.add_client_window).pack(pady=5)
        tk.Button(self, text="Добавить заказ", command=self.add_order_window).pack(pady=5)
        tk.Button(self, text="Добавить платёж", command=self.add_payment_window).pack(pady=5)
        tk.Button(self, text="Экспорт CSV", command=lambda: self.export_data("csv")).pack(pady=5)
        tk.Button(self, text="Экспорт JSON", command=lambda: self.export_data("json")).pack(pady=5)
        tk.Button(self, text="Экспорт EXCEL", command=lambda: self.export_data("xlsx")).pack(pady=5)

    def add_client_window(self):
        win = tk.Toplevel(self)
        win.title("Добавить клиента")

        tk.Label(win, text="Имя").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()

        tk.Label(win, text="Email").pack()
        email_entry = tk.Entry(win)
        email_entry.pack()

        tk.Label(win, text="Телефон").pack()
        phone_entry = tk.Entry(win)
        phone_entry.pack()

        def save():
            name = name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            if name and email and phone:
                add_client(name, email, phone)
                messagebox.showinfo("Успех", "Клиент добавлен")
                win.destroy()
            else:
                messagebox.showwarning("Ошибка", "Заполните все поля")

        tk.Button(win, text="Сохранить", command=save).pack(pady=5)

    def add_order_window(self):
        win = tk.Toplevel(self)
        win.title("Добавить заказ")

        tk.Label(win, text="ID клиента").pack()
        client_id_entry = tk.Entry(win)
        client_id_entry.pack()

        tk.Label(win, text="Название проекта").pack()
        project_entry = tk.Entry(win)
        project_entry.pack()

        tk.Label(win, text="Статус").pack()
        status_entry = tk.Entry(win)
        status_entry.pack()

        tk.Label(win, text="Дедлайн (YYYY-MM-DD)").pack()
        deadline_entry = tk.Entry(win)
        deadline_entry.pack()

        def save():
            try:
                client_id = int(client_id_entry.get())
                project = project_entry.get()
                status = status_entry.get()
                deadline = deadline_entry.get()
                if project and status and deadline:
                    add_order(client_id, project, status, deadline)
                    messagebox.showinfo("Успех", "Заказ добавлен")
                    win.destroy()
                else:
                    messagebox.showwarning("Ошибка", "Заполните все поля")
            except ValueError:
                messagebox.showerror("Ошибка", "ID клиента должен быть числом")

        tk.Button(win, text="Сохранить", command=save).pack(pady=5)

    def add_payment_window(self):
        win = tk.Toplevel(self)
        win.title("Добавить платеж")

        tk.Label(win, text="ID заказа").pack()
        order_id_entry = tk.Entry(win)
        order_id_entry.pack()

        tk.Label(win, text="Сумма").pack()
        amount_entry = tk.Entry(win)
        amount_entry.pack()

        def save():
            try:
                order_id = int(order_id_entry.get())
                amount = float(amount_entry.get())
                add_payment(order_id, amount)
                messagebox.showinfo("Успех", "Платеж добавлен")
                win.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректные данные")

        tk.Button(win, text="Сохранить", command=save).pack(pady=5)

    def export_data(self, formatt):
        filename = filedialog.asksaveasfilename(defaultextension=f".{formatt}",
                                                filetypes=[(f"{formatt.upper()} файлы", f"*.{formatt}")])
        if filename:
            try:
                if formatt == "csv":
                    export_csv(filename)
                elif formatt == "json":
                    export_json(filename)
                else:
                    export_excel(filename)

                messagebox.showinfo("Успех", f"Данные экспортированы в {filename}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при экспорте:\n{e}")

if __name__ == "__main__":
    app = CRMApp()
    app.mainloop()
