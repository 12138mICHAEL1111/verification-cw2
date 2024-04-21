# Create a new text file and write text into it
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, this is a text file created by Python.")

# Reading the text from the file and printing the result
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 6.00/10, +4.00)