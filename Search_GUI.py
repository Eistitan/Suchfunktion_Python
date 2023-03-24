import PySimpleGUI as sg
import os



def file_copy(path: str):
    with open(path, "r",encoding='utf-8') as file:
        string = file.read()
    return string


def doc_search(text: str, such_string: str):
    such_liste = []
    count = 0
    split_text = text.split('.')
    for satz in split_text:
        satz_strip = satz.strip()
        if such_string in satz:
            count += 1
            such_liste.append(count.__str__() + ") " + satz_strip + ".")
        elif such_string in satz.lower():
            count += 1
            such_liste.append(count.__str__() + ") " + satz_strip + ".")
    return such_liste, count


# def path_finder(path):
#     split_text = path.split('/')
#     for satz in split_text:
#         if ".txt" in satz:
#             return satz

layout = [
    [sg.Text("Dokument: "), sg.Text(key="-FILE-"), sg.Input(key="-IN-", visible=False, enable_events=True),
     sg.FileBrowse(key="-BROWSE-", file_types=(("Text", "*.txt"),))],
    [sg.Input(key="-SUCH-"), sg.Button("Suchen")],
    [[sg.Listbox(values=[], size=(70, 5), key="-LISTBOX-")]],
    [sg.Exit()],
]

window = sg.Window("Suchfunktion", layout)  # TODO die Größe anpassen

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    such_wort=values["-SUCH-"]
    #print(such_wort)
    if event == "-IN-":
        filepath = values["-IN-"]
        filename = os.path.basename(filepath)
        window["-FILE-"].update(filename)
    elif event == "Suchen" and such_wort!="":
        filepath = values["-IN-"]
        dokument = file_copy(filepath)

        suchliste, counter = doc_search(dokument, such_wort)

        window["-LISTBOX-"].update(values=suchliste)


window.close()
