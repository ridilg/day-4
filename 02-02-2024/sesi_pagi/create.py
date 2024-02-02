# f = open("handling.txt", "x")

nama = input("Nama: ")
ruang = input("Ruang: ")
skema = input("skema: ")

teks = "Nama: {}\nRuang: {}\nskema: {}\n".format(nama,ruang,skema)

file_ini= open("handling.txt", "w")
file_ini.write(teks)
# file_ini.close()

file_ini= open("handling.txt", "a")
file_ini.write("\nHasil perhitungan desimal, oktal, biner, dan hexa dari huruf Ani adalah:\n")

# Define the characters
# characters = ['A', 'n', 'i']

# # Iterate over the characters
# for char in characters:
#     # Convert to decimal
#     decimal_value = ord(char)
#     print(f"Character '{char}' - Decimal: {decimal_value}, Binary: {bin(decimal_value)}, Octal: {oct(decimal_value)}, Hexadecimal: {hex(decimal_value)}")

# file_ini= open("handling.txt", "a+")
# file_ini.write((f"Character '{char}' - Decimal: {decimal_value}, Binary: {bin(decimal_value)}, Octal: {oct(decimal_value)}, Hexadecimal: {hex(decimal_value)}"))

####*****####

file_ini.close()

# Define the characters
characters = ['A', 'n', 'i']

# Open a text file in write mode
with open('handling.txt', 'a') as file:
    # Iterate over the characters
    for char in characters:
        # Convert to decimal
        decimal_value = ord(char)
        # Convert to binary
        binary_value = bin(decimal_value)
        # Convert to octal
        octal_value = oct(decimal_value)
        # Convert to hexadecimal
        hexadecimal_value = hex(decimal_value)
        
        # Write the conversions to the file
        file.write(f"Character '{char}' - Decimal: {decimal_value}, Binary: {binary_value}, Octal: {octal_value}, Hexadecimal: {hexadecimal_value}\n")
