import text_recognition as tr
import re


def get_name_surname(text):
    if len(text) <= 2:
        return ""
    name_res = ""
    for c in text:
        if c.isalpha():
            name_res += c
    return name_res


def get_release(text):
    if len(text) <= 2:
        return ""
    release_result = ""
    for c in text:
        if c == ' ':
            continue
        elif c == '.':
            release_result += "-"
        else:
            release_result += c
    return release_result


def get_number(text):
    if len(text) <= 2:
        return ""
    number_result = ""
    for c in text:
        if c == ' ':
            continue
        else:
            number_result += c

    students_number_int = 0
    try:
        students_number_int = int(number_result)
        return students_number_int
    except ValueError:
        return number_result


def found_city(text):
    if len(text) <= 2:
        return ""
    number_found = False
    city_result = ""
    for c in text:
        if number_found:
            city_result += c
        else:
            if c.isdigit():
                city_result += c
                number_found = True
    return city_result


def process_text_from_image(img):
    processed_text = tr.processing(img)
    lines = processed_text.split('\n')
    print(lines)

    if len(lines) > 2:
        name = lines[0]
        surname = lines[1]
        address = ""
        release = ""
        students_number = ""
        pesel = 0
        city = ""
        for i in range(2, len(lines)):
            if re.match("^.*Wydan..", lines[i]):
                release = re.sub("^.*Wydan..", ' ', lines[i], 1)
                release = release[1:]
                if release[0] == ' ':
                    release = release[1:]

            if re.match("^.*um..", lines[i]):
                students_number = re.sub("^.*um..", ' ', lines[i], 1)
                students_number = students_number[1:]

            if re.match("^.*PESEL[ :]?", lines[i]):
                pesel = re.sub("^.*PESEL[ :]?", ' ', lines[i], 1)
                pesel = pesel[1:]

            if re.match("^.*dr...", lines[i]):
                address = re.sub("^.*dr...", ' ', lines[i], 1)
                address = address[1:]
                if address[0] == ' ':
                    address = address[1:]

            if re.match("^.*[0-9][0-9]-[0-9][0-9][0-9]", lines[i]):
                city = lines[i]

        result_array = [get_name_surname(name), get_name_surname(surname), get_release(release),
                        get_number(students_number), get_number(pesel), address, found_city(city)]

        print(result_array)


def main():
    process_text_from_image('images/skanerprzegryww/03.jpg')


if __name__ == '__main__':
    main()
