import os, sys, time

class Terminal:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def delayPrint(text, delay=0.02):
        for x in text:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(delay)

    def progressBar(progress, total):
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        print(f"\r|{bar}| {percent:.2f} %", end="\r")

class Colors:
    BLUE = '\033[94m'
    BLUE2 = '\u001b[38;5;45m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    GREEN2 = '\u001b[38;5;82m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ORANGE = '\u001b[38;5;208m'
    PURPLE = '\u001b[38;5;135m'
    GRAY = '\u001b[38;5;8m'
    PINK = '\u001b[35m'
    ENDC = '\033[0m'

class ColorsRGB:
    WHITE = (255,255,255)
    LIGHTGRAY = (170,170,170)
    GRAY = (40,40,40)
    DARKGRAY = (10,10,10)