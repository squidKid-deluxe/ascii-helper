"""
Module to assist with the creation of python ascii art
"""


def goto(x_pos, y_pos):
    """
    Move the cursor to a given position
    """
    x_pos = int(x_pos)
    y_pos = int(y_pos)
    print(f"\033[{y_pos};{x_pos}H", end="")


def set_color(red, green, blue):
    """
    Set the foreground color of the text
    """
    red = int(red)
    green = int(green)
    blue = int(blue)
    print(f"\033[38;2;{red};{green};{blue}m", end="")


def set_bgcolor(red, green, blue):
    """
    Set the background color of the text
    """
    red = int(red)
    green = int(green)
    blue = int(blue)
    print(f"\033[48;2;{red};{green};{blue}m", end="")


def clear_effects():
    """
    Clear all effects having to do with text appearance
    """
    print("\033[0m", end="")


def clear():
    """
    Clear the terminal screen
    """
    print("\033c", end="")


def bold():
    """
    Make any text that follows bold
    """
    print("\033[1m", end="")


def faint():
    """
    Make any text that follows faint
    """
    print("\033[2m", end="")


def blink():
    """
    Make any text that follows blink
    """
    print("\033[5m", end="")


def strike():
    """
    Make any text that follows have a strikethrough
    """
    print("\033[9m", end="")


def move_up(chars):
    """
    Move the cursor up
    """
    print(f"\033[{chars}A", end="")


def clear_line():
    """
    Clear the current line of the terminal
    """
    print("\033[2K", end="")


def title(text):
    """
    Set the title of the terminal
    """
    print("\x1b]2;" + text + "\x07", end="")


def rgb():
    """
    Run all tests for text color
    """
    from time import sleep

    for red in range(255):
        set_color(red, 0, 0)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    print()

    for green in range(255):
        set_color(0, green, 0)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    print()

    for blue in range(255):
        set_color(0, 0, blue)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    print()

    for red in range(255):
        set_bgcolor(red, 0, 0)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    print()

    for green in range(255):
        set_bgcolor(0, green, 0)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    print()

    for blue in range(255):
        set_bgcolor(0, 0, blue)
        move_up(1)
        print("Hello World")
        sleep(0.005)

    clear_effects()


def unit_tests():
    """
    Run all unit tests for the module
    """
    from time import sleep

    clear()
    title("Unit test of: ascii.py")
    blink()
    print("Hello World")
    clear_effects()
    bold()
    print("Hello World")
    clear_effects()
    faint()
    print("Hello World")
    clear_effects()
    strike()
    print("Hello World")
    clear_effects()
    print("Hello World")
    sleep(1)

    rgb()

    goto(60, 5)
    print("Hello World")
    goto(1, 15)
    sleep(1)

    print("#")
    move_up(2)
    sleep(1)
    print("#")
    sleep(1)

    goto(1, 17)
    print("Hello World")
    sleep(1)
    move_up(1)
    clear_line()
    sleep(1)
    goto(1, 24)


if __name__ == "__main__":
    unit_tests()
