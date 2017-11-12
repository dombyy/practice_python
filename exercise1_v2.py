# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

def get_name():
    return input("Hogy hívnak?")


def get_age():
    return int(input("Mennyi idős vagy?"))


def centenarium(a):
    assert a > 0, "Kevesebb mint 0, butaság"
    if a > 100:
        return "elmult"
    else:
        return 2017 + 100 - a


def main():
    nev = get_name()
    kor = get_age()
    megoldas = centenarium(kor)

    if megoldas == "elmult":
        print("Te már elmultál 100, gratu")
    else:
        print(str(megoldas) + " évben leszel 100")


if __name__ == "__main__":
    main()
