def file_copy(path: str):
    try:
        with open(path, "r",encoding='utf-8') as file:
            string = file.read()
        print("File gefunden")
        return string

    except FileNotFoundError:
        print("File nicht gefunden")
        return
    except:
        print("KEK")
        return

def doc_search(text: str, such_string: str):
    such_liste = []
    counter = 0
    split_text = text.split('.')
    for satz in split_text:
        if such_string in satz:
            counter += 1
            such_liste.append(satz)
        elif such_string in satz.lower():
            counter += 1
            such_liste.append(satz)
    return such_liste, counter

def ausgabe(such_liste, c):
    print(f"Es wurden {c} Sätze gefunden.\n")
    i = 0
    for item in such_liste:
        i += 1
        rows = item.split('\n')
        non_empty_rows = list(filter(lambda x: x != '', rows))
        item = '\n'.join(non_empty_rows)
        item_strip=item.strip()
        print(i, "  " + item_strip + ".")
    print("\n")
    # return


def main_prog():
    path = input("Path angeben: ").lower()
    full_text = file_copy(path)
    if full_text is None:  # break
        return

    while True:
        such_string = input("Suchen nach: ")
        if such_string == "break":
            return
        such_liste, counter = doc_search(full_text, such_string)

        ausgabe(such_liste, counter)


main_prog()
