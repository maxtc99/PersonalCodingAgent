from functions.write_file import write_file

def test():
    print(f"Writing to 'lorem.txt' file:\n{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}\n")
    print(f"Writing to 'pkg/morelorem.txt' file:\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}\n")
    print(f"Writing to '/tmp/temp.txt' file:\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}\n")

if __name__ == "__main__":
    test()