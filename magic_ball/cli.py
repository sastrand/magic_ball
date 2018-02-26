from magic_ball import DEFAULT_NAME

def get_name():
    n = input("Please enter your name.\n")
    if n: 
        return n
    else:
        return DEFAULT_NAME

def get_option():
    m = "What would you like to do?\n"\
        "\tA: converse with computer\n"\
        "\tB: quit this program\n"
    while True:
        s = input(m)[0]
        if s in ["A", "B", "a", "b"]:
            break
        print("Please choose A or B.") 
    return s

if __name__ == "__main__":
    get_option()
