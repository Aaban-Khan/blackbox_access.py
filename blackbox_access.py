import time
import sys
import random
from colorama import Style, Fore


def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def levelOne():
    global score, history
    typewriter(
        f"{Fore.MAGENTA}\n🔐 Level 1: Crack the 3-digit Vault Code{Style.RESET_ALL}"
    )
    secret_code = random.randint(100, 999)
    attempts = 0
    start_time = time.time()

    while True:
        try:
            guess = int(input(f"{Fore.CYAN}Enter the 3-digit code: {Style.RESET_ALL}"))

            if 100 <= guess <= 999:
                attempts += 1
                enlapsed = round(time.time() - start_time, 2)

                if guess == secret_code:
                    typewriter(
                        f"{Fore.GREEN}✅ Access Granted! Code cracked in {enlapsed} Seconds!! 🫨{Style.RESET_ALL}"
                    )
                    score += 1
                    history.append((attempts, secret_code, "Level-1"))
                    break
                else:
                    if guess < secret_code:
                        print(f"{Fore.YELLOW}- Too Low{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}- Too High{Style.RESET_ALL}")

                    hint = ""
                    for i in range(3):
                        if str(guess)[i] == str(secret_code)[i]:
                            hint += Fore.GREEN + str(guess)[i] + " " + Style.RESET_ALL
                        else:
                            hint += Fore.RED + "_ " + Style.RESET_ALL
                    print(
                        f"\n🔍 {Fore.LIGHTMAGENTA_EX}HINT: {hint.strip()}{Style.RESET_ALL}"
                    )

            else:
                print(
                    f"{Fore.RED}❗ Please guess a valid number (100-999) 🙏{Style.RESET_ALL}"
                )

            print(f"{Fore.RED}🕒 Attempts left: {8 - attempts}{Style.RESET_ALL}")

            if attempts > 7:
                print(
                    f"{Fore.RED}🔒 Too many failed attempts. Vault is locked!{Style.RESET_ALL}"
                )
                time.sleep(1.5)
                typewriter(
                    f"{Fore.RED}💀 SECURITY BREACH DETECTED! System shutting down...{Style.RESET_ALL}"
                )
                break

        except ValueError:
            print(f"{Fore.RED}❌ Incorrect Code. Try again{Style.RESET_ALL}")


def levelTwo():
    global score, history
    typewriter(f"{Fore.CYAN}🔓 Level 2: Crack the Secret Password {Style.RESET_ALL}")

    words = ["apple", "hacker", "vault", "python", "secure"]
    secret_word = random.choice(words)
    print(f"Password contains {len(secret_word)} letters: {"_ " * len(secret_word)}")
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Guess the password: ").lower().strip()
        try:
            if guess.isalpha():
                attempts += 1
                enlapsed = round(time.time() - start_time, 2)
                if guess == secret_word:
                    typewriter(
                        f"{Fore.GREEN}✅ Access Granted! Code cracked in {enlapsed} Seconds!! 🫨{Style.RESET_ALL}"
                    )
                    score += 1
                    history.append((attempts, secret_word, "Level-2"))
                    break
                else:
                    hint = ""
                    for i in range(len(secret_word)):
                        if i < len(guess) and guess[i] == secret_word[i]:
                            hint += Fore.GREEN + guess[i] + Style.RESET_ALL + " "
                        else:
                            hint += Fore.LIGHTMAGENTA_EX + "_ " + Style.RESET_ALL
                    print(f"\n🔍HINT: {hint.strip()}")

                if attempts > 7:
                    print("🔒 Too many failed attempts. Vault is locked!")
                    time.sleep(0.3)
                    typewriter(
                        f"\n{Fore.RED}💀 SECURITY BREACH DETECTED! System shutting down...{Style.RESET_ALL}"
                    )
                    break
                print(f"{Fore.RED}-{8 - attempts} Attempts left {Style.RESET_ALL}")
            else:
                print("❗Please guess a valid Alphabetic input 🙏")
        except ValueError:
            print(f"❌ Incorrect Code. Try again")


def levelThree():
    global score, history
    typewriter(
        f"{Fore.YELLOW}🔓 Level 3: Numeric Lockdown Challenge {Style.RESET_ALL}\n"
    )

    attempts = 0
    secret_code = random.randint(100, 999)
    divisor = random.randint(2, 9)
    start_time = time.time()

    typewriter(f"🧩 Clue 1: It's a: {len(str(secret_code))}-digit number.")
    typewriter(f"🧩 Clue 2: It's ASCII value is: {[ord(i) for i in str(secret_code)]}")
    typewriter(f"🧩 Clue 3: Its Remainder by (1-9) is: {secret_code % divisor}")

    while True:
        try:
            guess = int(input("\nGuess the number: "))

            if 100 <= guess <= 999:
                attempts += 1
                enlapsed = round(time.time() - start_time, 2)
                if guess == secret_code:
                    typewriter(
                        f"{Fore.GREEN}✅ Access Granted! Code cracked in {enlapsed} Seconds!! 🫨{Style.RESET_ALL}"
                    )
                    score += 1
                    history.append((attempts, secret_code, "Level-3"))
                    break
                else:
                    if attempts >= 3:
                        hint = ""
                        for i in range(3):
                            if str(guess)[i] == str(secret_code)[i]:
                                hint += (
                                    Fore.GREEN + str(guess)[i] + Style.RESET_ALL + " "
                                )
                            else:
                                hint += Fore.RED + "_ " + Style.RESET_ALL
                        print(f"\n🔍Hint {hint.strip()}")
                print(f"{Fore.RED}🕒 Attempts left: {8 - attempts}{Style.RESET_ALL}")

            else:
                print(f"{Fore.RED}❗ Enter a valid 3-digit number! {Style.RESET_ALL}")

            if attempts > 7:
                print("🔒 Too many failed attempts. Vault is locked!")
                time.sleep(0.5)
                typewriter(
                    f"\n{Fore.RED}💀 SECURITY BREACH DETECTED! System shutting down...{Style.RESET_ALL}"
                )
                break

        except ValueError:
            print("❗Incorrect code, Try again!!")


typewriter("🧠 Welcome to Terminal Vault...\nInitializing security protocols...")
time.sleep(1)

username = input(f"\n{Fore.MAGENTA}Enter your Username: {Style.RESET_ALL}").capitalize()
score = 0
history = []
time.sleep(0.5)

while True:
    ask_level = input("\nChoose Difficulty Level(e/m/h): ").lower()
    if ask_level == "e":
        typewriter(
            f"{Fore.LIGHTCYAN_EX}📝 MISSION BRIEF: A digital vault has been locked with a 3-digit code. You’ve tapped into the security system. Crack the code using logic and hints. Each digit holds a secret — and a mistake can trigger the alarm!{Style.RESET_ALL}"
        )
        time.sleep(1)
        levelOne()
    elif ask_level == "m":
        typewriter(
            f"{Fore.LIGHTCYAN_EX}📝 MISSION BRIEF: A rogue AI has hidden a secret word in the system. Your job is to reveal it, letter by letter. Use position-based hints and guess wisely. You’ve only got a few chances before the system self-destructs!{Style.RESET_ALL}"
        )
        time.sleep(1)
        levelTwo()
    elif ask_level == "h":
        typewriter(
            f"{Fore.LIGHTCYAN_EX}📝 MISSION BRIEF: The final firewall stands tall — protected by a high-level numeric puzzle. Clues lie in ASCII codes, digits, and remainders. Crack the pattern or get caught. One wrong move and you're traced!{Style.RESET_ALL}"
        )
        time.sleep(1)
        levelThree()
    else:
        typewriter(f"{Fore.RED}Choose a Valid Level!! {Style.RESET_ALL}")

    continue_game = input("Do you want to Play Again?(y/n): ").lower()
    if continue_game == "n":
        print(f"\n📜 Game Summary for {username}:")
        for i, (a, code, lvl) in enumerate(history, 1):
            typewriter(f"{lvl}: Code {code} cracked in {a} attempts.")
        print(f"🏁 Final Score: {score}")
        break
