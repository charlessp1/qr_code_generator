import qrcode

class QRGenerator:
    def __init__(self, fill="black", back="white"):
        self._fill_color = fill
        self._back_color = back

    def enter_data(self):
        data = input("Enter the text or URL to encode in QR code: ")

    def enter_filename(self):
        enter_filename = input("Enter filename: ")
        filename = f"{enter_filename}.png"

    def generate_qr(self, fill, back, data, filename):
        qr = qrcode.QRCode(
            version=1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
