# file = open("decorators.py", "r")
# try:
    # file.write("#Hi from context managers")
# finally:
    # file.close()

# with open("decorators.py","a") as file:
#     file.write("#Hi from context managers")


class File:
    def __init__(self, filename,method):
        super().__init__()
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file 

    def __exit__(self, type, value, traceback):
        self.file.close()
        print("Exit")

with File("decorators.py", "a") as f:
    print("Middle")
    f.write("#hello from context managers")
    raise FileExistsError()