import random
from functools import reduce

def generate (german=True):

    if german:
        print("Passphrase wird generiert... ")
        with open("german.txt", "r") as f:
            words = f.readlines()
    else:
        print("Passphrase is being generated... ")
        with open("english.txt", "r") as f:
            words = f.readlines()
    words = list(map(lambda x: x.split(' ')[1][:-1], words))
    passphrase = reduce(lambda x, y: x+words[random.SystemRandom().randrange(7776)]+' ', range(6),'')[:-1]
    print("{}".format(passphrase))
    return passphrase

if __name__ == '__main__':
    language = input("German or English? (default: German): ")
    if language in ["", "German", "german", "g"]:
        generate()
    else:
        generate(False)
