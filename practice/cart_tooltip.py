import tkinter as tk
from tkinter import messagebox

class ToolTip:
    """Проста підказка для кнопки"""
    def __init__(self, widget, text_func):
        self.widget = widget
        self.text_func = text_func
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        text = self.text_func()
        if self.tip_window or not text:
            return
        x, y, cx, cy = self.widget.bbox("insert")  # координати курсора
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # прибрати рамку
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", "10", "normal"))
        label.pack(ipadx=5, ipady=3)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Магазин")

        # Дані кошика: список кортежів (назва, ціна)
        self.cart_items = [("Товар1", 500), ("Товар2", 300), ("Товар3", 600)]  # можна змінювати
        # self.cart_items = []  # перевірка порожнього кошика

        self.cart_button = tk.Button(root, text="Кошик", command=self.checkout)
        self.cart_button.pack(padx=50, pady=50)

        # Підказка
        ToolTip(self.cart_button, self.get_cart_tooltip)

    def get_cart_tooltip(self):
        if not self.cart_items:
            return "У кошику немає товарів"
        count = len(self.cart_items)
        total = sum(item[1] for item in self.cart_items)
        return f"У вашому кошику позицій - {count} товарів\nНа загальну суму {total}\n(натисніть для оформлення)"

    def checkout(self):
        if not self.cart_items:
            messagebox.showinfo("Кошик", "У кошику немає товарів")
        else:
            count = len(self.cart_items)
            total = sum(item[1] for item in self.cart_items)
            messagebox.showinfo("Оформлення", f"Ви оформляєте {count} товарів на суму {total} грн")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
