import random, os, sys;from colorama import Fore
class Start:
    def Generatename():
        formattedfirst = []
        formattedlast = []
        with open('first-names.txt', 'r') as f:
            first = f.readlines()
        for s in first:
            formattedfirst.append(s.split('\n')[0])
        with open('last-names.txt', 'r') as f:
            last = f.readlines()
        for s in last:
            formattedlast.append(s.split('\n')[0])
        generatedname = random.choice(formattedfirst) + " " + random.choice(formattedlast)
        return generatedname
    def Start():
        formattedcountries = []
        with open('countries.txt', 'r') as f:
            first = f.readlines()
        for s in first:
            formattedcountries.append(s.split('\n')[0])
        yesno = ['yes', 'no']
        yesnomaybe = ['yes', 'no', 'maybe']
        os.system("cls" if os.name == 'nt' else "clear")
        name = Start.Generatename()
        em = ['gmail', 'yahoo', 'hotmail']
        email = name.replace(" ", ".") + f"{random.randrange(10, 100)}" + f"@{random.choice(em)}.com"
        print("Name: "+name)
        print("")
        print("CC:")
        print(f"├ number: {random.randrange(4, 6)}{random.randrange(100, 1000)} {random.randrange(1000, 10000)} {random.randrange(1000, 10000)} {random.randrange(1000, 10000)}")
        print(f"├ exp: {random.randrange(1, 13)}/{random.randrange(23, 30)}")
        print(f"└ cvc: {random.randrange(100, 1000)}")
        print("")
        print("Personal info:")
        print(f"├ DOB: {random.randrange(1, 31)}/{random.randrange(1, 13)}/{random.randrange(1990, 2006)} (DD/MM/YYYY)")
        print(f"├ POB: {random.choice(formattedcountries)}")
        print(f"├ Email address: {email}")
        print(f"└ Pet name: {Start.Generatename()}")
        print("")
        print("Addictions:")
        print(f"├ Smoking: {random.choice(yesno)}")
        print(f"├ Drinking: {random.choice(yesno)}")
        print(f"├ Drugs: {random.choice(yesno)}")
        print(f"├ Gambling: {random.choice(yesno)}")
        print(f"├ Video games: {random.choice(yesnomaybe)}")
        print(f"└ Movies: {random.choice(yesnomaybe)}")

def main():
    os.system("title Identity generator by Theta | 🥩Join the schnitzel gang discord.gg/tzeP4BKpth")
    Start.Start()
    #print("\n🥩 Join the Schnitzel Gang: https://discord.gg/tzeP4BKpth")
    print(f"\nPress {Fore.CYAN}ENTER{Fore.WHITE} to generate a new identity;")
    if input(f"Type {Fore.RED}'exit'{Fore.WHITE} to exit the program.") == "exit":sys.exit()
    main()
main()