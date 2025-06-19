# tests.py

# from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    """
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result of 'lorem.txt'")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result of 'pkg/morelorem.txt'")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result of '/tmp/temp.txt'")
    print(result)
    """
    result = run_python_file("calculator", "main.py")
    print("Result of 'main.py'")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result of 'tests.py'")
    print(result)

    result = run_python_file("calculator", "../main.py")
    # this should return an error
    print("Result of '../main.py'")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    # this should return an error
    print("Result of 'nonexistent.py'")
    print(result)

if __name__ == "__main__":
    test()