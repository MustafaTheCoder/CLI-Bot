from .commands import Help
from .commands import changePrefix

while True:
    with open("data/prefix.txt", "r") as f:
        PREFIX = f.read()

    CMD_INPUT = str(input(f"{PREFIX} "))
    if CMD_INPUT == "help".lower():
        print(Help())
    elif CMD_INPUT == "changepre".lower():
          

    else:
        break
        