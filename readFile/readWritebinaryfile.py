def main():
    filename = "test.bin"

    data = b"hello"

    with open(filename, "wb") as file:
        file.write(data)
    with open(filename, "rb") as file:
        results = file.read(5) #5 bytes
        print(results)
main()