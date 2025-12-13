from functions.get_file_content import get_file_content

def test():
    print(f"Contents of 'main.py' file:\n{get_file_content("calculator", "main.py")}\n")
    print(f"Contents of 'pkg/calculator.py' file:\n{get_file_content("calculator", "pkg/calculator.py")}\n")
    print(f"Contents of '/bin/cat' file:\n{get_file_content("calculator", "/bin/cat")}\n")
    print(f"Contents of 'pkg/does_not_exist.py' file:\n{get_file_content("calculator", "pkg/does_not_exist.py")}\n")

if __name__ == "__main__":
    test()

