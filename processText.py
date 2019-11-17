import text_recognition as tr
import re


def main():
    processedText = tr.processing('images/skanerprzegryww/02.jpg')
    lines = processedText.split('\n')
    print(lines)
    name = lines[0]
    surname = lines[1]
    address = ""
    release = ""
    studentsNumber = 0
    pesel = 0
    city = ""

    for i in range(2, len(lines)):
        if re.match("Wydana.", lines[i]):
            release = re.sub("Wydana", ' ', lines[i], 1)
            if release[0] == ' ':
                release = release[2:]
            else:
                release = release[1:]

        if re.match("Nr alb", lines[i]):
            studentsNumber = int(re.sub("Nr albumu: ", ' ', lines[i], 1))

        if re.match("PESEL.", lines[i]):
            pesel = re.sub("PESEL.", ' ', lines[i], 1)
            if pesel[1] == ":":
                pesel = pesel[2:]
            else:
                pesel = pesel[1:]

        if re.match("Adr", lines[i]):
            address = re.sub("Adres", ' ', lines[i], 1)
            address = address[1:]
            if address[0] == ':':
                address = address[1:]

        if re.match("[0-9]+-[0-9]+", lines[i]):
            city = lines[i]

    print(name)
    print(surname)
    print(release)
    print(int(studentsNumber))
    print(int(pesel))
    print(address)
    print(city)


if __name__ == '__main__':
    main()
