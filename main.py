from accomBucket import accomDB
import PySimpleGUI as sg


def main():
    # $sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
    db = accomDB("./accomDB.db")
    db.load("./accomDB.db")
    if not db.get("Accomplishments"):
        db.set("Accomplishments", [])

    layout = [[sg.Text("Type in your Accomplishments!")], [sg.In(
        size=(60, 1), enable_events=True, key="-Input-")], [sg.Button("Save", enable_events=True, key="-Save-"), sg.Button("Exit", enable_events=True, key="-Exit-")]]

    # Create the window
    window = sg.Window("Bucket", layout)

    # Create an event loop
    while True:
        event, values = window.read()
    # End program if user closes window or
    # presses the EXIT button
    # Dumps DB to save even if window is closed
        if event == "-Exit-" or event == sg.WIN_CLOSED:
            db.dumpdb()
            break

    # Save accomplishment to DB
        elif event == "-Save-":
            accom = values["-Input-"]
            if len(accom) != 0:
                accomplishmentsList = db.get("Accomplishments")
                accomplishmentsList.append(accom)
                db.set("Accomplishments", accomplishmentsList)
                print(accomplishmentsList)

    window.close()


main()
