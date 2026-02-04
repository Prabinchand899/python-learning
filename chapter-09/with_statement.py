
# Open the file in read mode using 'with', which automatically closes the file



with open("file.txt", "r") as f:
    # Read the contents of the file
    text = f.read()
    # Print the contents
print(text)