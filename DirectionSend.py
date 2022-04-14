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
    client.exec_command("python3 Directions/Forward.py")
def left():
    print("left")
    client.exec_command("python3 Directions/Left.py")
def right():
    print("right")
    client.exec_command("python3 Directions/Right.py")
def reverse():
    print("reverse")
    client.exec_command("python3 Directions/Reverse.py")