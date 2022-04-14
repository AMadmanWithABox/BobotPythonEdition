import paramiko

def connect():
    command = "python3 Directions/Forward.py"

    host = "192.168.8.211"
    port = 22
    username = "pi"
    password = "BeepBoop"

    global client
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    #print(stdout.read().decode())

def forward():
    print("Fowrward")
    try:
        client.exec_command("python3 Directions/Forward.py")
    except:
        client.close()
        connect()
def left():
    print("left")
    try:
        client.exec_command("python3 Directions/Left.py")
    except:
        client.close()
        connect()
def right():
    print("right")
    try:
        client.exec_command("python3 Directions/Right.py")
    except:
        client.close()
        connect()
def reverse():
    print("reverse")
    try:
        client.exec_command("python3 Directions/Reverse.py")
    except:
        client.close()
        connect()