import qrcode
import os

def create_qr(data, filename):

    os.makedirs("reports", exist_ok=True)

    img = qrcode.make(data)

    path = f"reports/{filename}.png"

    img.save(path)

    return path