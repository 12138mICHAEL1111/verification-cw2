# Create a new text file and write text into it
with open('example.txt', 'w') as file:
    file.write("Hello, this is a text file created by Python.")

# Reading the text from the file and printing the result
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# ************* Module s_1
# results/raw/s_1.py:2:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
# results/raw/s_1.py:6:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
# -------------------------------------------------------------------
# Your code has been rated at 6.00/10 (previous run: 10.00/10, -4.00)