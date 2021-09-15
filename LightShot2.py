

def main():
    idString = "tu"
    numbers = '0123456789'
    alnum = 'abcdefghijklmnopqrstuvwxyz' + numbers
    fileName = f"id {idString} {alnum[0]} - {alnum[-1]}.txt"
    with open(fileName, "w") as f:
        for i in alnum:
            for j in alnum:
                for k in alnum:
                    for l in alnum:
                        url = f"https://prnt.sc/{idString}{i}{j}{k}{l}"
                        f.write(url + "\n")
                        print(url)



if __name__ == "__main__":
    main()