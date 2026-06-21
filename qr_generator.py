import qrcode

class QRGenerator:
    def __init__(self, fill="black", back="white"):
        self._fill_color = fill
        self._back_color = back

    def enter_data(self):
        data = input("Enter the text or URL to encode in QR code: ")
        return data

    def enter_filename(self):
        enter_filename = input("Enter filename: ")
        filename = f"{enter_filename}.png"
        return filename

    def generate_qr(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self._fill_color, back_color=self._back_color)
        return img

    def save_img(self, filename, img):
        img.save(filename)
        print(f"QR code successfully generated as {filename}")
