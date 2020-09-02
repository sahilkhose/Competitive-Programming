
def print_formatted(number):
    w = len(bin(number).replace("0b",""))
    for i in range(1, number+1):
        print(
        str(i).rjust(w, " "), 
        oct(i).replace("0o", "").rjust(w, " "), 
        hex(i).replace("0x", "").upper().rjust(w, " "), 
        bin(i).replace("0b", "").rjust(w, " ")
        )


if __name__ == '__main__':