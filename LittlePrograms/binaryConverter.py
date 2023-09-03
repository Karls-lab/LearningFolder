"""Simple Program created by Karl that converts an integer to it's binary representation
    The limit is up to the interger 511, 9 bits of information"""

while True: 
    try: 
        num = int(input("Please input a number: "))
    except TypeError:
        print('Please input an integer')
    print(f"The integer {num} -> ", end='')

    """Starting at 256, if the number is equal to or larger than the binary counter, 
       add a 1, and subtract the binary counter from the number. Divide the binary 
       counter by 2 and continue on this fashion until the binary counter is >= 1."""
    binary_counter = 256 #
    binary_number = ""
    while binary_counter >= 1:
        if num % binary_counter < num:
            binary_number += "1"
            num -= binary_counter
        else:
            binary_number += "0"
        binary_counter /= 2
    print(f"{binary_number}")

