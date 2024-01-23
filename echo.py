#echo.py


def echo(text: str, repititions: int = 3) -> str:
    num_chars = 0
    last_three_chars = ''

    # iterate from the end of the string
    for c in reversed(text):
        if c not in (' ', '.', '?', '!') and num_chars < repititions:
            last_three_chars += c
            num_chars += 1
    final_echo = ""
    for i in range(repititions):
        final_echo = final_echo + last_three_chars[i:]
        if i < 2:
            final_echo += '\n'
        else:
            final_echo += '\n.'
    return final_echo

    
    

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

