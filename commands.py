def Help():    
        print("""
        Games:
        [1] Economy
        [2] Number Guess""")

def changePrefix():
        x = str(input("New Prefix: "))
        with open("data/prefix.txt", "w") as f:
                prefix = f.write(x)
        print(f"Prefix Reseted: {prefix}")        


if __name__ == "__main__":
    Help()


