from qr_generator import QRGenerator
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class GUIQR(QRGenerator):
    super().__init__()

    def generate_qr(self, data):
        data = entry.get()
        if not data:
            messagebox.showerror("Input required!", "Please enter a text or URL.")
            return