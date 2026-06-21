from qr_generator import QRGenerator
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class GUIQR(QRGenerator):
    def __init__(self):
        super().__init__()

        self.root = tk.Tk()
        self.root.title("QR Code Generator")

        tk.Label(self.root, text="Enter text or URL:").pack(pady=5)
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        self.fill_color = tk.StringVar(value="black")
        self.back_color = tk.StringVar(value="white")
        self.logo_path = tk.StringVar(value="")

        tk.Button(self.root, text="Pick Fill Color", command=lambda: self.choose_color(self.fill_color)).pack(pady=2)
        tk.Button(self.root, text="Pick Background Color", command=lambda: self.choose_color(self.back_color)).pack(pady=2)
        tk.Button(self.root, text="Choose Logo (optional)", command=self.choose_logo).pack(pady=2)

        tk.Button(self.root, text="Generate QR Code", command=self.gui_qr_generator, bg="green", fg="white").pack(pady=10)

    def choose_color(self, var):
        color_code = colorchooser.askcolor(title="Choose color")[1]
        if color_code:
            var.set(color_code)

    def choose_logo(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if path:
            self.logo_path.set(path)

    def gui_qr_generator(self):
        data = self.entry.get()
        if not data:
            messagebox.showerror("Input required!", "Please enter a text or URL.")
            return

        self._fill_color = self.fill_color.get()
        self._back_color = self.back_color.get()

        qr_img = super().generate_qr(data).convert("RGB")

        if self.logo_path.get():
            try:
                logo = Image.open(self.logo_path.get())
                qr_w, qr_h = qr_img.size

                logo_size = int(qr_w / 4)
                logo = logo.resize((logo_size, logo_size))
                pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)

                qr_img.paste(logo, pos, mask=logo if logo.mode=='RGBA' else None)
            except Exception as e:
                messagebox.showerror("Logo error!", f"Failed to add logo: {e}")

        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])

        if filename:
            super().save_img(filename, qr_img)
            messagebox.showinfo("Success!", f"QR Code saved successfully as {filename}")

    def run_gui(self):
        self.root.mainloop()