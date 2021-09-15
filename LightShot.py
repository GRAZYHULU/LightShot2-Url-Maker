


def main():

    idString = "op"
    range_min = 7000
    range_max = 8000

    fileName = f"id {idString} {range_min} - {range_max}.txt"
    with open(fileName, "w") as f:
        for i in range(range_min, range_max + 1):
            url = "https://prnt.sc/{0}{1:04}".format(idString, i)
            print(url)
            f.write(url + "\n")


if __name__ == "__main__":
    main()