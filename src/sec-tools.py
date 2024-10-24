import socket


def getUrls():
        # Open the file in read mode
    with open('urls.txt', 'r') as file:
        # Read all lines and store them in a list
        lines = file.readlines()

    # Remove any newline characters at the end of each line
    return [line.strip() for line in lines]

ports = (80,443,20,25565,8080,8443)
urls = getUrls()



for url in urls:
    print(f"testing ports for url {url}:")
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)
        status = client.connect_ex((url,port))
        if status == 0:
            print(f"port {port} is open!")
