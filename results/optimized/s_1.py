# Create a new text file and write text into it with specified encoding
with open("example.txt", "w", encoding='utf-8') as file:
    file.write("This is an example text. Write this to the file.")

# Read and print the contents of the file with specified encoding
with open("example.txt", "r", encoding='utf-8') as file:
    contents = file.read()

print(contents)

# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 5.00/10, +5.00)