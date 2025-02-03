import qrcode
import random
import string
import matplotlib.pyplot as plt

def generate_random_string(length=10):
    """Generate a random alphanumeric string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_qr_code():
    """Generate and display a QR code with random content."""
    data = generate_random_string()
    qr = qrcode.make(data)
    
    plt.imshow(qr, cmap='gray')
    plt.axis('off')
    plt.title(f"QR Code: {data}")
    plt.show()

if __name__ == "__main__":
    generate_qr_code()
