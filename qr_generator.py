import qrcode

class QRGenerator:
    def __init__(self, data, fill="black", back="white"):
        self._fill_color = fill
        self._back_color = back

    def input_data(self):
        data = input("Enter the text or URL to encode in QR code: ")