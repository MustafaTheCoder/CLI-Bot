def Help():    
        print("""
        Games:
        [1] Economy
        [2] Number Guess""")

def changePrefix():
        x = str(input("New Prefix: "))
        with open("data/prefix.txt", "w") as f:
                f.write(x)

        with open("data/prefix.txt", "r") as f:
                prefix = f.read(x)

        print(f"Prefix Resetted: {prefix}")        


if __name__ == "__main__":
    Help()
    changePrefix()


