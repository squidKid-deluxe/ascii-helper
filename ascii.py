"""
Module to assist with the creation of python ascii art
"""


def goto(x_pos, y_pos):
    """
    Move the cursor to a given position
    """
    x_pos = int(x_pos)
    y_pos = int(y_pos)
    print(f"\033[{x_pos};{y_pos}H")


def set_color(red, green, blue):
    """
    Set the foreground color of the text
    """
    red = int(red)
    green = int(green)
    blue = int(blue)
    print(f"\033[38;2;{red};{green};{blue}m")


def set_bgcolor(red, green, blue):
    """
    Set the background color of the text
    """
    red = int(red)
    green = int(green)
    blue = int(blue)
    print(f"\033[48;2;{red};{green};{blue}m")


def clear_effects():
    """
    Clear all effects having to do with text appearance
    """
    print("\033[0m")


def clear():
    """
    Clear the terminal screen
    """
    print("\033c")


def bold():
    """
    Make any text that follows bold
    """
    print("\033[1m")


def faint():
    """
    Make any text that follows faint
    """
    print("\033[2m")


def blink():
    """
    Make any text that follows blink
    """
    print("\033[5m")


def strike():
    """
    Make any text that follows have a strikethrough
    """
    print("\033[9m")


def move_up(chars):
    """
    Move the cursor up
    """
    print(f"\033[{chars}A")


def move_down(chars):
    """
    Move the cursor down
    """
    print(f"\033[{chars}B")


def move_left(chars):
    """
    Move the cursor left
    """
    print(f"\033[{chars}D")


def move_right(chars):
    """
    Move the cursor right
    """
    print(f"\033[{chars}C")


def clear_line():
    """
    Clear the current line of the terminal
    """
    print("\033[2K")


def title(text):
    """
    Set the title of the terminal
    """
    print("\x1b]2;" + text + "\x07")
