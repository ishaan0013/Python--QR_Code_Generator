import qrcode

final_qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

final_qr.add_data("https://www.linkedin.com/in/ishaan-bhardwaj-i0013/")

final_qr.make(fit=True)

img = final_qr.make_image(fill_color="white", back_color="black")

img.save("LinkedIn_profile.png")
