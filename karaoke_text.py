import time
from colorama import Fore, Style, init

init(autoreset=True)

lyrics = [
    (5.0,  "She was more", Fore.CYAN),
    (6.5,  "like a beauty queen", Fore.CYAN),
    (8.5,  "from a movie scene", Fore.CYAN),

    (10.0, "I said don't mind", Fore.MAGENTA),
    (12.0, "but what do you mean", Fore.MAGENTA),
    (14.0, "I am the one", Fore.MAGENTA),

    (17.0, "Who will dance", Fore.YELLOW),
    (19.0, "on the floor", Fore.YELLOW),
    (21.0, "in the round", Fore.YELLOW),

    (23.0, "She said", Fore.GREEN),
    (24.5, "I am the one", Fore.GREEN),

    (27.0, "Who will dance", Fore.RED),
    (28.5, "on the floor", Fore.RED),
    (30.0, "in the round", Fore.RED),
]

def print_karaoke(text, speed=0.05, color=Fore.CYAN):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(speed)
    print(Style.RESET_ALL)


start_time = time.time()
for timestamp, line, color in lyrics:
    while time.time() - start_time < timestamp:
        time.sleep(0.01)
    print_karaoke(line, speed=0.06, color=color)
