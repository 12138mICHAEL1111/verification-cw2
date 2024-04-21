# Create a new text file and write text into it
with open("example.txt", "w") as file:
    file.write("This is an example text. Write this to the file.")

# Read and print the contents of the file
with open("example.txt", "r") as file:
    print(file.read())

# ************* Module s_1
# results/raw/s_1.py:2:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
# results/raw/s_1.py:6:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
# -------------------------------------------------------------------
# Your code has been rated at 5.00/10 (previous run: 10.00/10, -5.00)