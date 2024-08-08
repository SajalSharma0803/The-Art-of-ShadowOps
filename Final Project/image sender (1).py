import socket

def send_image(server_address, server_port, image_path):
    """
    Sends an image to the specified server.

    :param server_address: Address of the server to connect to.
    :param server_port: Port number on the server.
    :param image_path: Path to the image file to send.
    """
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((server_address, server_port))

        # Open the image file in binary mode
        with open(image_path, 'rb') as image_file:
            # Read the image data
            image_data = image_file.read()

            # Send the length of the image data first
            s.sendall(len(image_data).to_bytes(8, byteorder='big'))

            # Send the image data
            s.sendall(image_data)

    print("Image sent successfully.")

# Example usage
if __name__ == "__main__":
    server_address = 'localhost'  # Replace with the actual server IP if needed
    server_port = 5000
    image_path = 'lapt.jpg'  # Replace with the actual path to your image

    send_image(server_address, server_port, image_path)
