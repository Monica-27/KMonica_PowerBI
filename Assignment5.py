# to create and write into file
with open("sample.txt", "w") as f:
    f.write("This is a sample file\n")

#to append
with open("sample.txt", "a") as f:
    f.write("Appending a line in sample file\n")

# read content from starting
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

#append and read together
with open("sample.txt", "a+") as f:
    f.write("This is a python file\n")
    f.seek(0) 
    print("\nReading content after appending and reading together:")
    print(f.read())