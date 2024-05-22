import pandas as pd
import qrcode

# Sample product data
products = [
    {"name": "EMEE", "price": 100, "mfg_date": "10/10/2023", "exp_date": "10/10/2026", "inventory": "a1"},
    # Add more products as needed
]

# Function to generate QR code
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Generate QR codes for each product URL
for index, product in enumerate(products):
    base_url = "http://172.20.10.2:5000/product"
    url = f"{base_url}?name={product['name']}"
    filename = f"qrcode_{index + 1}.png"
    generate_qr_code(url, filename)

print("QR codes generated successfully.")
