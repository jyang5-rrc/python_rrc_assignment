class openFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.file.close()

# Example usage:
with openFile("example.txt", "r") as file:
    if file:
        content = file.read()
        print("File contents:")
        print(content)