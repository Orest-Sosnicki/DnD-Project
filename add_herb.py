from tkinter import *
import random

radio_value = 0


def radio_button(enter):
    global radio_value
    radio_value = enter

def add_interface(radio_value, areas_list, total):

    add = Tk()
    add.title("Add Herb")
    add.geometry("200x200")

    # frame ---------------------------------------------------------------------------------------------------------
    option_frame = Frame(add,
                         width=100,
                         height=50,
                         relief=SUNKEN,
                         borderwidth=1)
    option_frame.grid(row=0, column=0, columnspan=3)
    # option_frame.pack_propagate(0)

    full_radio = Radiobutton(option_frame,
                             text="Quick Find",
                             value=1,
                             variable=radio_value,
                             indicatoron=1,
                             command=lambda: radio_button(1))
    full_radio.pack(side="left")

    herb_radio = Radiobutton(option_frame,
                             text="Add Herb",
                             value=2,
                             variable=radio_value,
                             indicatoron=1,
                             command=lambda: radio_button(2))
    herb_radio.pack(side="right")

    full_radio.invoke()

    # below frame----------------------------------------------------------------------------------------------------
    instruction = Label(add, text="Enter Success: ", padx=5, pady=5)
    instruction.grid(row=1, column=0)

    found_enter = Entry(add, textvariable=StringVar(), width=2, justify="left")
    found_enter.grid(row=1, column=1)

    area_box = ttk.Combobox(add, values=areas_list, width=10, state="readonly")
    area_box.grid(row=1, column=2, padx=5)
    area_box.set(areas_list[3])

    # List Box --------------------------------------------------------------------------------------------------------
    output_list = Listbox(add, width=30, height=6)
    output_list.grid(row=3, column=0, columnspan=3)

    found_button = Button(add,
                          text="Quick Add",
                          command=lambda: quick_add(found_enter.get(),total, area_box, output_list))
    found_button.grid(row=2, column=0)

    total_label = Label(add, text="")
    total_label.grid(row=2, column=1, columnspan=2)

    total = total_label


def quick_add(option, total, area_box, output_list):
    try:
        value = int(option)
        total_gathered = value
        output_list.delete(0, END)

        plant_list = ["", "", "", "", "", ""]
        count_list = [0, 0, 0, 0, 0, 0]

        if radio_value == 1:
            total_gathered = 0
            while value != 0:
                found_herb = random.randint(1, 20)
                low_roll = random.randint(1, 4)

                if found_herb <= 10:
                    total_gathered += 1

                elif found_herb <= 15:
                    total_gathered += low_roll

                elif found_herb <= 18:
                    total_gathered += (low_roll + 1)

                elif found_herb == 19:
                    total_gathered += (low_roll + 2)

                else:
                    value += 2

                value -= 1

            total["text"] = f"Total gathered: {total_gathered}"

        else:
            total["text"] = f""

        while total_gathered != 0:
            roll = random.randint(1, 20)

            if area_box.get() == "Arctic":
                if roll <= 5:
                    plant_list[0] = "Blue herb "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Drojos ivy "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Ucre bramble "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "White poppy "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Kreet paste "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Angel flower "
                    count_list[5] += 1

            elif area_box.get() == "Caves":
                if roll <= 5:
                    plant_list[0] = "Twilight wormwood "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Blue herb "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Mandrake root "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Abyss flower "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Kasuni juice "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Blackleaf Rose "
                    count_list[5] += 1

            elif area_box.get() == "Desert":
                if roll <= 5:
                    plant_list[0] = "Drojos ivy "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Ellond scrub "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Ucre bramble "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Dried Ephedra "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Olina petals "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Ebrium fungus "
                    count_list[5] += 1

            elif area_box.get() == "Forests":
                if roll <= 5:
                    plant_list[0] = "Twilight Wormwood "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Drojos ivy "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Ellond scrub "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Blood herb "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Thunderleaf "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Wisp stems "
                    count_list[5] += 1

            elif area_box.get() == "Water":
                if roll <= 5:
                    plant_list[0] = "Twilight Wormwood "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Blue herb "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Mandrake root "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Aniseed sap "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Kreet paste "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Chromatic mud "
                    count_list[5] += 1

            elif area_box.get() == "Mountains":
                if roll <= 5:
                    plant_list[0] = "Drojos ivy "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Ellond scrub "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Mandrake root "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Ash chives "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Kasuni juice "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Dragontongue petals "
                    count_list[5] += 1

            elif area_box.get() == "Plains":
                if roll <= 5:
                    plant_list[0] = "Ellond scrub "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Mandrake root "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Ucre bramble "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Anissed sap "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Lunar nectar "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Dragontongue petals "
                    count_list[5] += 1

            elif area_box.get() == "Swamps":
                if roll <= 5:
                    plant_list[0] = "Twilight wormwood "
                    count_list[0] += 1
                elif roll <= 10:
                    plant_list[1] = "Blue herb "
                    count_list[1] += 1
                elif roll <= 15:
                    plant_list[2] = "Ucre bramble "
                    count_list[2] += 1
                elif roll <= 18:
                    plant_list[3] = "Frenn moss "
                    count_list[3] += 1
                elif roll == 19:
                    plant_list[4] = "Ecire laurel "
                    count_list[4] += 1
                else:
                    plant_list[5] = "Spineflower berries "
                    count_list[5] += 1
            total_gathered -= 1

        new_plant_list = list(filter(None, plant_list))
        new_count_list = list(filter(None, count_list))

        combined_list = list(zip(new_plant_list, new_count_list))
        for n in combined_list:
            show = f"{n[0]} {n[1]}"
            output_list.insert(END, show)
        
    except ValueError:
        messagebox.showinfo("Invalid Entry", "You need to enter a number")