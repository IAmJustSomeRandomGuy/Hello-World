brown = 300
blue = 300
brown_blue = 300


def year():
    global brown, blue, brown_blue

    brown1 = brown / 3
    blue1 = blue / 3
    brown_blue1 = brown_blue / 3

    blue = blue1 + ((blue1 + brown_blue1) / 2) + (brown_blue1 / 4)
    brown = brown1 + ((blue1 + brown_blue1) / 2) + (brown_blue1 / 4)
    brown_blue = (brown1 + blue1) + (brown_blue1 / 2) + ((brown1 + brown_blue1) / 2) + ((blue1 + brown_blue1) / 2)
    print(blue)
    print(brown)
    print(brown_blue)
    print(brown + blue + brown_blue)


year()
year()
