import paramiko

def connect():
    command = "python3 Directions/Forward.py"

    host = "192.168.81.8.211"
    port = 22
    username = "pi"
    password = "BeepBoop"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    #_stdin, _stdout,_stderr = client.exec_command("python3 Directions/Forward.py")
    #print(stdout.read().decode())
    client.close()

def forward():
    print("Fowrward")
def left():
    print("left")
def right():
    print("right")
def reverse():
    print("reverse")