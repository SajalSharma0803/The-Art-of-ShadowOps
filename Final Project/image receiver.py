import socket

def receive_image(server_address, server_port, output_image_path):
    """
    Receives an image from a client and saves it to the specified file.

    :param server_address: Address to bind the server.
    :param server_port: Port number on the server.
    :param output_image_path: Path where the received image will be saved.
    """
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((server_address, server_port))

        # Listen for incoming connections (can queue up to 5 connections)
        s.listen(5)
        print("Server listening on {}:{}".format(server_address, server_port))

        # Accept a connection
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)

            # First, receive the length of the image data
            data_length = int.from_bytes(conn.recv(8), byteorder='big')

            # Then, receive the image data
            image_data = b""
            while len(image_data) < data_length:
                packet = conn.recv(4096)
                if not packet:
                    break
                image_data += packet

            # Write the image data to a file
            with open(output_image_path, 'wb') as output_image:
                output_image.write(image_data)

        print("Image received and saved as", output_image_path)

# Example usage
if __name__ == "__main__":
    server_address = 'localhost'
    server_port = 5000
    output_image_path = 'received_image.jpg'  # Replace with the desired output path

    receive_image(server_address, server_port, output_image_path)
