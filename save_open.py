from tkinter import *

def open_file(filename, numberList, typeList, total_all, elements_all):
    file = filename
    with open(file, "r") as fp:
        for n in range(0, 26):
            numberList[n].set(fp.readline())
    
    save(filename, numberList, typeList, total_all, elements_all, hold_check = "")

def confirm(filename, numberList, typeList, total_all, elements_all):
    check = Tk()
    hold_check = check

    check.title("Save Conformation")
    check.geometry("130x50")

    text = Label(check, text="Would you like to save")
    text.grid(row=0, column=0, columnspan=2)

    yes_option = Button(check, text="Yes", command=lambda: save(filename, numberList, typeList, total_all, elements_all, hold_check))
    yes_option.grid(row=1, column=0)

    no_option = Button(check, text="No", command=lambda: check.destroy())
    no_option.grid(row=1, column=1)


def save(filename, numberList, typeList, total_all, elements_all, hold_check):

    try:
        typeList[0][
            "text"] = f"Earth-{numberList[0].get()} Negative-{numberList[0].get()}"
        typeList[1][
            "text"] = f"Air-{numberList[1].get()} Positive-{numberList[1].get() * 2}"
        typeList[2][
            "text"] = f"Water-{numberList[2].get()} Earth-{numberList[2].get()}"
        typeList[3][
            "text"] = f"Air-{numberList[3].get()} Fire-{numberList[3].get()}"
        typeList[4][
            "text"] = f"Fire-{numberList[4].get()} Negative-{numberList[4].get() * 2}"
        typeList[5][
            "text"] = f"Water-{numberList[5].get()} Negative-{numberList[5].get()}"
        typeList[6]["text"] = f"Water-{numberList[6].get()}"
        typeList[7][
            "text"] = f"Water-{numberList[7].get() * 2} Air-{numberList[7].get()}"
        typeList[8][
            "text"] = f"Fire-{numberList[8].get() * 2} Air-{numberList[8].get()}"
        typeList[9][
            "text"] = f"Fire-{numberList[9].get()} Earth-{numberList[9].get()}"
        typeList[10]["text"] = f"Earth-{numberList[10].get()}"
        typeList[11][
            "text"] = f"Earth-{numberList[11].get() * 2} Negative-{numberList[11].get()}"
        typeList[12]["text"] = f"Positive-{numberList[12].get() * 2}"
        typeList[13]["text"] = f"Fire-{numberList[13].get()}"
        typeList[14][
            "text"] = f"Air-{numberList[14].get()} Negative-{numberList[14].get()}"
        typeList[15]["text"] = f"Earth-{numberList[15].get() * 2}"
        typeList[16]["text"] = f"Water-{numberList[16].get() * 2}"
        typeList[17]["text"] = f"Negative-{numberList[17].get() * 2}"
        typeList[18]["text"] = f"Air-{numberList[18].get()}"
        typeList[19]["text"] = f"Fire-{numberList[19].get() * 2}"
        typeList[20][
            "text"] = f"Water-{numberList[20].get()} Earth-{numberList[20].get() * 2}"
        typeList[21]["text"] = f"Air-{numberList[21].get() * 2}"
        typeList[22]["text"] = f"Negative-{numberList[22].get()}"
        typeList[23]["text"] = f"Positive-{numberList[23].get()}"
        typeList[24][
            "text"] = f"Air-{numberList[24].get()} Positive-{numberList[24].get()}"
        typeList[25][
            "text"] = f"Earth-{numberList[25].get()} Positive-{numberList[25].get() * 2}"

        file = open(filename, "w")
        for n in range(0, 26):
            file.write(f"{numberList[n].get()}\n")
        file.close()

        total_all[0] = numberList[2].get() + numberList[5].get() + numberList[6].get() + (numberList[7].get() * 2) + \
                       (numberList[16].get() * 2) + numberList[20].get()
        total_all[3] = numberList[1].get() + numberList[3].get() + numberList[7].get() + numberList[8].get() + \
                       numberList[14].get() + numberList[18].get() + (numberList[21].get() * 2) + numberList[24].get()
        total_all[2] = numberList[3].get() + numberList[4].get() + (numberList[8].get() * 2) + numberList[9].get() + \
                       numberList[13].get() + (numberList[19].get() * 2)
        total_all[1] = numberList[0].get() + numberList[2].get() + numberList[9].get() + numberList[10].get() + \
                       (numberList[11].get() * 2) + (numberList[15].get() * 2) + (numberList[20].get() * 2) + \
                       numberList[25].get()
        total_all[4] = (numberList[1].get() * 2) + (numberList[12].get() * 2) + numberList[23].get() + \
                       numberList[24].get() + (numberList[25].get() * 2)
        total_all[5] = numberList[0].get() + (numberList[4].get() * 2) + numberList[5].get() + numberList[11].get() + \
                       numberList[14].get() + (numberList[17].get() * 2) + numberList[22].get()

        elements_all[0]["text"] = f"Water: {total_all[0]}"
        elements_all[1]["text"] = f"Earth: {total_all[1]}"
        elements_all[2]["text"] = f"Fire: {total_all[2]}"
        elements_all[3]["text"] = f"Air: {total_all[3]}"
        elements_all[4]["text"] = f"Positive: {total_all[4]}"
        elements_all[5]["text"] = f"Negative: {total_all[5]}"

        if hold_check != "":
            hold_check.destroy()

        hold_check = ""

    except TclError as error:
        messagebox.showinfo("Invalid Entry",
                            "You need to enter a number in each box")