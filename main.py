from tkinter import ttk, Tk, Label, Button, LEFT, Frame, SUNKEN, Radiobutton, Entry, Listbox, END, E, NE, StringVar, IntVar, Menu, W, N, messagebox
from tkinter import *
import random


def open_file(filename):
    global numberList
    file = filename
    with open(file, "r") as fp:
        for n in range(0, 26):
            numberList[n].set(fp.readline())

    save(filename)


def confirm(filename):
    global hold_check
    check = Tk()
    hold_check = check

    check.title("Save Conformation")
    check.geometry("130x50")

    text = Label(check, text="Would you like to save")
    text.grid(row=0, column=0, columnspan=2)

    yes_option = Button(check, text="Yes", command=lambda: save(filename))
    yes_option.grid(row=1, column=0)

    no_option = Button(check, text="No", command=lambda: check.destroy())
    no_option.grid(row=1, column=1)


def save(filename):
    global numberList, typeList, total_all, text_all, elements_all, hold_check

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


def show_info():
    harvesting = """                                                Plants and Herbs
        Plants are used for creating alchemical potions and mixtures,
        and they are divided in four levels of rarity.

        * Common plants: which have one essence
        * Uncommon plants, which have two different essences
        * Rare plants, which have two essences of the same type
        * Very Rare plants, which have two essences of the same
           type and one extra essence

        To gather plants, herbs and other similar resources the
        character must make an Intelligence (Nature) check (DC 15).
        If the character success the check, the DM rolls a d20 to
        determine the number of resources gathered.

        d20                 Number of plants gathered

        1-10                1
        11-15              1d4
        16-18              1d4+1
        19                    1d4+2
        20                    Roll twice"""

    info = Tk()
    info.title("Info")
    info.geometry("370x350")

    text_info1 = Label(info, text=harvesting, justify=LEFT)
    text_info1.grid(row=0, column=0)


def show_area(choice):
    if choice == 0:
        plants = """                                             
                                        Arctic

                1d20                Name                        Rarity 
                1-5                   Blue herb                  Common
                6-10                 Drojos ivy                 Common
                11-15               Ucre bramble           Common
                16-18               White poppy            Uncommon
                19                     Kreet paste               Rare
                20                     Angel flower            Very Rare"""

    elif choice == 1:
        plants = """                                            
                                        Caves

                1d20              Name                                Rarity
                1-5                 Twilight wormwood       Common
                6-10               Blue herb                         Common
                11-15             Mandrake root                Common
                16-18             Abyss flower                    Uncommon
                19                   Kasuni juice                     Rare
                20                   Blackleaf Rose                 Very Rare
"""

    elif choice == 2:
        plants = """
                                        Desert
                                        
                1d20              Name                              Rarity
                1-5                 Drojos ivy                       Common
                6-10               Ellond scrub                   Common
                11-15             Ucre bramble                 Common
                16-18             Dried Ephedra                Uncommon
                19                   Olina petals                    Rare
                20                   Ebrium fungus               Very Rare
"""

    elif choice == 3:
        plants = """
                                        Forests

                1d20              Name                                      Rarity
                1-5                 Twilight wormwood             Common
                6-10               Drojos ivy                               Common
                11-15             Ellond scrub                           Common
                16-18             Blood herb                             Uncommon
                19                   Thunderleaf                           Rare
                20                   Wisp stems                            Very Rare
"""

    elif choice == 4:
        plants = """                                
                                    Lakes, rivers and ocean

                1d20              Name                                    Rarity
                1-5                 Twilight wormwood           Common
                6-10               Blue herb                              Common
                11-15             Mandrake root                     Common
                16-18             Aniseed sap                          Uncommon
                19                   Kreet paste                           Rare
                20                   Chromatic mud                   Very Rare
        """

    elif choice == 5:
        plants = """
                                        Mountains

                1d20            Name                                Rarity
                1-5               Drojos ivy                         Common
                6-10             Ellond scrub                     Common
                11-15           Mandrake root                 Common
                16-18           Ash chives                        Uncommon
                19                 Kasuni juice                      Rare
                20                 Dragontongue petals      Very Rare
        """

    elif choice == 6:
        plants = """
                                                  Plains

                1d20           Name                                   Rarity
                1-5              Ellond scrub                        Common
                6-10            Mandrake root                    Common
                11-15          Ucre bramble                      Common
                16-18          Aniseed sap                         Uncommon
                19                Lunar nectar                        Rare
                20                Dragontongue petals         Very Rare
        """

    else:
        plants = """
                                                Swamps

                1d20              Name                                  Rarity
                1-5                Twilight wormwood          Common
                6-10              Blue herb                             Common
                11-15            Ucre bramble                      Common
                16-18            Frenn moss                         Uncommon
                19                  Ecire laurel                          Rare
                20                  Spineflower berries            Very Rare

        """

    area = Tk()
    area.title("Area")
    area.geometry("350x180")

    text_info1 = Label(area, text=plants, justify=LEFT)
    text_info1.grid(row=0, column=0)


def add_interface():
    global total, radio_value, areas_list, area_box, found, output_list

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

    found_enter = Entry(add, textvariable=found, width=2, justify="left")
    found_enter.grid(row=1, column=1)

    area_box = ttk.Combobox(add, values=areas_list, width=10, state="readonly")
    area_box.grid(row=1, column=2, padx=5)
    area_box.set(areas_list[3])

    found_button = Button(add,
                          text="Quick Add",
                          command=lambda: quick_add(found_enter.get()))
    found_button.grid(row=2, column=0)

    total_label = Label(add, text="")
    total_label.grid(row=2, column=1, columnspan=2)

    total = total_label

    # List Box --------------------------------------------------------------------------------------------------------
    output_list = Listbox(add, width=30, height=6)
    output_list.grid(row=3, column=0, columnspan=3)


def radio_button(enter):
    global radio_value
    radio_value = enter


def quick_add(option):
    global radio_value, area_box, areas_list, output_list
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


def bomb_display():
    global herb_listbox, ingredients_listbox, effect, repeat, additional_effect, display_calculated, display_total, \
        effect_list, additional_effect_list, numbers

    craft = Tk()

    craft.title("Bomb Crafting")
    craft.geometry("470x400")

    # effect ------------------------------------------------------------------------------------------------------
    effect_label = Label(craft, text="Effects")
    effect_label.grid(row=0, column=2, sticky=E)

    effect = ttk.Combobox(craft,
                          values=effect_list,
                          width=20,
                          state="readonly")
    effect.grid(row=0, column=3)

    repeat = ttk.Combobox(craft, values=numbers, width=2, state="readonly")
    repeat.grid(row=0, column=4)

    # additional effects ------------------------------------------------------------------------------------------
    additional_effect_label = Label(craft, text="Additional Effects")
    additional_effect_label.grid(row=1, column=2, sticky=NE)

    additional_effect = ttk.Combobox(craft,
                                     values=additional_effect_list,
                                     width=20,
                                     state="readonly")
    additional_effect.grid(row=1, column=3, sticky=NE)

    # Calculate ---------------------------------------------------------------------------------------------------
    calculate = Button(craft, text="Calculate", command=calculate_total)
    calculate.grid(row=3, column=3)

    # herb list ---------------------------------------------------------------------------------------------------
    collected_label = Label(craft, text="Collected Herbs")
    collected_label.grid(row=1, column=0)

    herb_listbox = Listbox(craft, width=30, height=10)
    herb_listbox.grid(row=2, column=0, columnspan=2, rowspan=7)
    herb_listbox.bind("<Double-Button-1>", add_ingredient)

    # ingredients want to us --------------------------------------------------------------------------------------
    ingredients_label = Label(craft, text="Ingredients")
    ingredients_label.grid(row=9, column=0)

    ingredients_listbox = Listbox(craft, width=30, height=10)
    ingredients_listbox.grid(row=10, column=0, columnspan=2, rowspan=7)
    ingredients_listbox.bind("<Double-Button-1>", remove_ingredient)

    # effect total-------------------------------------------------------------------------------------------------

    ingredient_water = Label(craft, text=f"Element Costs:")
    ingredient_water.grid(row=2, column=2, sticky=E)

    effect_water = Label(craft, text=f"Water: 0")
    effect_water.grid(row=3, column=2, sticky=E)

    effect_earth = Label(craft, text=f"Earth: 0")
    effect_earth.grid(row=4, column=2, sticky=E)

    effect_fire = Label(craft, text=f"Fire: 0")
    effect_fire.grid(row=5, column=2, sticky=E)

    effect_air = Label(craft, text=f"Air: 0")
    effect_air.grid(row=6, column=2, sticky=E)

    effect_positive = Label(craft, text=f"Positive: 0")
    effect_positive.grid(row=7, column=2, sticky=E)

    effect_negative = Label(craft, text=f"Negative: 0")
    effect_negative.grid(row=8, column=2, sticky=E)

    display_calculated = [
        effect_water, effect_earth, effect_fire, effect_air, effect_positive,
        effect_negative
    ]

    # Ingredients total -------------------------------------------------------------------------------------------

    ingredient_water = Label(craft, text=f"Ingredients Totals:")
    ingredient_water.grid(row=10, column=2, sticky=E)

    ingredient_water = Label(craft, text=f"Water: 0")
    ingredient_water.grid(row=11, column=2, sticky=E)

    ingredient_earth = Label(craft, text=f"Earth: 0")
    ingredient_earth.grid(row=12, column=2, sticky=E)

    ingredient_fire = Label(craft, text=f"Fire: 0")
    ingredient_fire.grid(row=13, column=2, sticky=E)

    ingredient_air = Label(craft, text=f"Air: 0")
    ingredient_air.grid(row=14, column=2, sticky=E)

    ingredient_positive = Label(craft, text=f"Positive: 0")
    ingredient_positive.grid(row=15, column=2, sticky=E)

    ingredient_negative = Label(craft, text=f"Negative: 0")
    ingredient_negative.grid(row=16, column=2, sticky=E)

    display_total = [
        ingredient_water, ingredient_earth, ingredient_fire, ingredient_air,
        ingredient_positive, ingredient_negative
    ]

    set_list()
    update_list()


def calculate_total():
    global effect, additional_effect, repeat, display_calculated, effect_list, effect_list, \
        additional_effect_list, numbers

    element_totals = [0, 0, 0, 0, 0, 0]

    multiply = int(repeat.get())

    if effect.get() == effect_list[0]:
        element_totals[2] += 1 * multiply
        element_totals[1] += 1 * multiply

    elif effect.get() == effect_list[1]:
        element_totals[0] += 2 * multiply

    elif effect.get() == effect_list[2]:
        element_totals[3] += 2 * multiply

    elif effect.get() == effect_list[3]:
        element_totals[3] += 1 * multiply
        element_totals[2] += 1 * multiply

    elif effect.get() == effect_list[4]:
        element_totals[3] += 2 * multiply

    elif effect.get() == effect_list[5]:
        element_totals[5] += 2 * multiply

    elif effect.get() == effect_list[6]:
        element_totals[2] += 2 * multiply

    elif effect.get() == effect_list[7]:
        element_totals[4] += 2 * multiply

    elif effect.get() == effect_list[8]:
        element_totals[3] += 1 * multiply
        element_totals[4] += 1 * multiply

    # additional effect adding ----------------------------------------------------------------------------------------
    if additional_effect.get() == additional_effect_list[0]:
        element_totals[0] += 1
        element_totals[1] += 1

    elif additional_effect.get() == additional_effect_list[1]:
        element_totals[0] += 1
        element_totals[4] += 1

    elif additional_effect.get() == additional_effect_list[2]:
        element_totals[2] += 1
        element_totals[4] += 1

    elif additional_effect.get() == additional_effect_list[3]:
        element_totals[2] += 1
        element_totals[3] += 1

    elif additional_effect.get() == additional_effect_list[4]:
        element_totals[3] += 1
        element_totals[5] += 1

    display_calculated[0]["text"] = f"Water: {element_totals[0]}"
    display_calculated[1]["text"] = f"Earth: {element_totals[1]}"
    display_calculated[2]["text"] = f"Fire: {element_totals[2]}"
    display_calculated[3]["text"] = f"Air: {element_totals[3]}"
    display_calculated[4]["text"] = f"Positive: {element_totals[4]}"
    display_calculated[5]["text"] = f"Negative: {element_totals[5]}"


def set_list():
    global numberList, amount_list, position_list, element_totals

    amount_list = []
    position_list = []
    count = 0
    element_totals = [0, 0, 0, 0, 0, 0]

    for n in numberList:
        if n.get() != 0:
            amount_list.append(int(n.get()))
            position_list.append(count)
        count += 1


def update_list():
    global herb_listbox, amount_list, position_list, herb_list, element_label
    herb_listbox.delete(0, END)
    count = 0

    for n in position_list:
        into = f"{herb_list[n]['text']} {element_label[n]} {amount_list[count]}"
        herb_listbox.insert(END, into)
        count += 1


def add_ingredient(event):
    global herb_listbox, amount_list, position_list, ingredients_listbox, herb_list, element_label, use_ingredient, \
        display_total, element_totals

    try:
        hold = herb_listbox.curselection()
        number = hold[0]

        if amount_list[number] != 0:
            amount_list[number] -= 1

            hold_position = position_list[number]
            into = f"{herb_list[hold_position]['text']} {element_label[hold_position]}"
            use_ingredient.append(into)

            ingredients_listbox.delete(0, END)
            for n in use_ingredient:
                ingredients_listbox.insert(END, n)

            update_list()

        element_totals[0] += water_value[hold_position]
        element_totals[1] += earth_value[hold_position]
        element_totals[2] += fire_value[hold_position]
        element_totals[3] += air_value[hold_position]
        element_totals[4] += positive_value[hold_position]
        element_totals[5] += negative_value[hold_position]

        display_total[0]["text"] = f"Water: {element_totals[0]}"
        display_total[1]["text"] = f"Earth: {element_totals[1]}"
        display_total[2]["text"] = f"Fire: {element_totals[2]}"
        display_total[3]["text"] = f"Air: {element_totals[3]}"
        display_total[4]["text"] = f"Positive: {element_totals[4]}"
        display_total[5]["text"] = f"Negative: {element_totals[5]}"

    except IndexError as error:
        messagebox.showinfo("Action Error",
                            "Trying to add to the list too fast")


def remove_ingredient(event):
    global use_ingredient, ingredients_listbox, position_list, amount_list, herb_list

    try:
        hold = ingredients_listbox.curselection()
        number = hold[0]
        hold_ingredient = use_ingredient[number].split(":")[0]
        hold_location = 0

        count = 0
        for n in position_list:
            if hold_ingredient == herb_list[n]["text"].split(":")[0]:
                amount_list[count] += 1
                hold_location = n
            count += 1
        use_ingredient.remove(use_ingredient[number])

        ingredients_listbox.delete(0, END)
        for n in use_ingredient:
            ingredients_listbox.insert(END, n)

        update_list()

        element_totals[0] -= water_value[hold_location]
        element_totals[1] -= earth_value[hold_location]
        element_totals[2] -= fire_value[hold_location]
        element_totals[3] -= air_value[hold_location]
        element_totals[4] -= positive_value[hold_location]
        element_totals[5] -= negative_value[hold_location]

        display_total[0]["text"] = f"Water: {element_totals[0]}"
        display_total[1]["text"] = f"Earth: {element_totals[1]}"
        display_total[2]["text"] = f"Fire: {element_totals[2]}"
        display_total[3]["text"] = f"Air: {element_totals[3]}"
        display_total[4]["text"] = f"Positive: {element_totals[4]}"
        display_total[5]["text"] = f"Negative: {element_totals[5]}"

    except IndexError as error:
        messagebox.showinfo("Action Error",
                            "Trying to remove from the list too fast")


hold_check = ""

window = Tk()

window.title("Arcane Creations: Version 2.1")
window.geometry("350x650")

total = ""

found = StringVar()
areas_list = [
    "Arctic", "Caves", "Desert", "Forests", "Water", "Mountains", "Plains",
    "Swamps"
]
area_box = StringVar()

radio_value = IntVar()
output_list = list()

herb_listbox = ""
ingredients_listbox = ""

element_totals = [0, 0, 0, 0, 0, 0]
amount_list = []
position_list = []

use_ingredient = []

effect = StringVar()
additional_effect = ""
repeat = ""
display_calculated = list()
display_total = list()

effect_list = [
    "Acid Damage(C) EF", "Cold Damage(D) WW", "Fire Damage(D) FF",
    "Force Damage(I) FA", "Lighting Damage(C) AA", "Necrotic Damage(C) NN",
    "Piercing Damage(D) EE", "Radiant Damage(D) PP", "Thunder Damage(D) AP",
    "None"
]
additional_effect_list = [
    "Sticky Gel WE", "Slippery oil WP", "Light Explosion FP", "Loud Sound FA",
    "Dense Fog AN", "None"
]
numbers = [1, 2, 3, 4, 5, 6, 7]

water_value = [
    0, 0, 1, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0,
    0
]
earth_value = [
    1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0,
    1
]
fire_value = [
    0, 0, 0, 1, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
    0
]
air_value = [
    0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1,
    0
]
positive_value = [
    0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
    2
]
negative_value = [
    1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0,
    0
]
element_label = [
    "EN", "APP", "WE", "AF", "FNN", "WN", "W", "WWA", "FFA", "FE", "E", "EEN",
    "PP", "F", "AN", "EE", "WW", "NN", "A", "FF", "WEE", "AA", "N", "P", "AP",
    "EPP"
]

numberList = [
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar(),
    IntVar()
]

elements1 = f"Earth-{numberList[0].get()} Negative-{numberList[0].get()}"
elements2 = f"Air-{numberList[1].get()} Positive-{numberList[1].get() * 2}"
elements3 = f"Water-{numberList[2].get()} Earth-{numberList[2].get()}"
elements4 = f"Air-{numberList[3].get()} Fire-{numberList[3].get()}"
elements5 = f"Fire-{numberList[4].get()} Negative-{numberList[4].get() * 2}"
elements6 = f"Water-{numberList[5].get()} Negative-{numberList[5].get()}"
elements7 = f"Water-{numberList[6].get()}"
elements8 = f"Water-{numberList[7].get() * 2} Air-{numberList[7].get()}"
elements9 = f"Fire-{numberList[8].get() * 2} Air-{numberList[8].get()}"
elements10 = f"Fire-{numberList[9].get()} Earth-{numberList[9].get()}"
elements11 = f"Earth-{numberList[10].get()}"
elements12 = f"Earth-{numberList[11].get() * 2} Negative-{numberList[11].get()}"
elements13 = f"Positive-{numberList[12].get() * 2}"
elements14 = f"Fire-{numberList[13].get()}"
elements15 = f"Air-{numberList[14].get()} Negative-{numberList[14].get()}"
elements16 = f"Earth-{numberList[15].get() * 2}"
elements17 = f"Water-{numberList[16].get() * 2}"
elements18 = f"Negative-{numberList[17].get() * 2}"
elements19 = f"Air-{numberList[18].get()}"
elements20 = f"Fire-{numberList[19].get() * 2}"
elements21 = f"Water-{numberList[20].get()} Earth-{numberList[20].get() * 2}"
elements22 = f"Air-{numberList[21].get() * 2}"
elements23 = f"Negative-{numberList[22].get()}"
elements24 = f"Positive-{numberList[23].get()}"
elements25 = f"Air-{numberList[24].get()} Positive-{numberList[24].get()}"
elements26 = f"Earth-{numberList[25].get()} Positive-{numberList[25].get() * 2}"

total_all = [
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar()
]

# menu bar -----------------------------------------------------------------------------------------------------
menu_bar = Menu(window)
window.config(menu=menu_bar)

# file menu ---------------------------------------------------------------------------------------------------
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: open_file("DnD_Bombs"))
file_menu.add_command(label="Save", command=lambda: confirm("DnD_Bombs"))
file_menu.add_command(label="", state="disabled")
file_menu.add_command(label="Open Backup",
                      command=lambda: open_file("DnD_Bombs_backup"))
file_menu.add_command(label="Save Backup",
                      command=lambda: confirm("DnD_Bombs_backup"))
file_menu.add_command(label="", state="disabled")
file_menu.add_command(label="Exit", command=window.quit)

# herb menu --------------------------------------------------------------------------------------------------
herb_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Herb", menu=herb_menu)
herb_menu.add_command(label="Info", command=show_info)

# herb area(submenu) ---------------------------------------------------
area_menu = Menu(herb_menu, tearoff=False)
herb_menu.add_cascade(label="Area", menu=area_menu)
area_menu.add_command(label="Arctic", command=lambda: show_area(0))
area_menu.add_command(label="Caves", command=lambda: show_area(1))
area_menu.add_command(label="Desert", command=lambda: show_area(2))
area_menu.add_command(label="Forests", command=lambda: show_area(3))
area_menu.add_command(label="Water", command=lambda: show_area(4))
area_menu.add_command(label="Mountains", command=lambda: show_area(5))
area_menu.add_command(label="Plains", command=lambda: show_area(6))
area_menu.add_command(label="Swamps", command=lambda: show_area(7))

herb_menu.add_command(label="Add Herb", command=add_interface)

# bombs menu ---------------------------------------------------------------------------------------------------
bomb_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Bomb", menu=bomb_menu)
bomb_menu.add_command(label="Craft", command=bomb_display)

# Abyss Flower -------------------------------------------------------------------------------------------------
herb1 = Label(window, text="Abyss flower:")
herb1.grid(row=0, column=0, ipadx=1, sticky=W)

type1 = Label(window, text=elements1)
type1.grid(row=0, column=1, padx=0, pady=0, sticky=W)

entry1 = Entry(window, justify=LEFT, width=3, textvariable=numberList[0])
entry1.grid(row=0, column=2, padx=1, pady=0)

# Angel Flower -------------------------------------------------------------------------------------------------
herb2 = Label(window, text="Angel flower:")
herb2.grid(row=1, column=0, ipadx=1, sticky=W)

type2 = Label(window, text=elements2)
type2.grid(row=1, column=1, padx=0, pady=0, sticky=W)

entry2 = Entry(window, justify=LEFT, width=3, textvariable=numberList[1])
entry2.grid(row=1, column=2, padx=1, pady=0)

# Aniseed sap -------------------------------------------------------------------------------------------------
herb3 = Label(window, text="Aniseed sap:")
herb3.grid(row=2, column=0, ipadx=1, sticky=W)

type3 = Label(window, text=elements3)
type3.grid(row=2, column=1, padx=0, pady=0, sticky=W)

entry3 = Entry(window, justify=LEFT, width=3, textvariable=numberList[2])
entry3.grid(row=2, column=2, padx=1, pady=0)

# Ash Chives -------------------------------------------------------------------------------------------------
herb4 = Label(window, text="Ash Chives:")
herb4.grid(row=3, column=0, ipadx=1, sticky=W)

type4 = Label(window, text=elements4)
type4.grid(row=3, column=1, padx=0, pady=0, sticky=W)

entry4 = Entry(window, justify=LEFT, width=3, textvariable=numberList[3])
entry4.grid(row=3, column=2, padx=1, pady=0)

# Blackleaf Rose -------------------------------------------------------------------------------------------------
herb5 = Label(window, text="Blackleaf Rose:")
herb5.grid(row=4, column=0, ipadx=1, sticky=W)

type5 = Label(window, text=elements5)
type5.grid(row=4, column=1, padx=0, pady=0, sticky=W)

entry5 = Entry(window, justify=LEFT, width=3, textvariable=numberList[4])
entry5.grid(row=4, column=2, padx=1, pady=0)

# Blood Herb -------------------------------------------------------------------------------------------------
herb6 = Label(window, text="Blood Herb:")
herb6.grid(row=5, column=0, ipadx=1, sticky=W)

type6 = Label(window, text=elements6)
type6.grid(row=5, column=1, padx=0, pady=0, sticky=W)

entry6 = Entry(window, justify=LEFT, width=3, textvariable=numberList[5])
entry6.grid(row=5, column=2, padx=1, pady=0)

# Blue Herb -------------------------------------------------------------------------------------------------
herb7 = Label(window, text="Blue Herb:")
herb7.grid(row=6, column=0, ipadx=1, sticky=W)

type7 = Label(window, text=elements7)
type7.grid(row=6, column=1, padx=0, pady=0, sticky=W)

entry7 = Entry(window, justify=LEFT, width=3, textvariable=numberList[6])
entry7.grid(row=6, column=2, padx=1, pady=0)

# Chromatic Mud -------------------------------------------------------------------------------------------------
herb8 = Label(window, text="Chromatic Mud:")
herb8.grid(row=7, column=0, ipadx=1, sticky=W)

type8 = Label(window, text=elements8)
type8.grid(row=7, column=1, padx=0, pady=0, sticky=W)

entry8 = Entry(window, justify=LEFT, width=3, textvariable=numberList[7])
entry8.grid(row=7, column=2, padx=1, pady=0)

# Dragontongue Petals -------------------------------------------------------------------------------------------
herb9 = Label(window, text="Dragontongue Petals:")
herb9.grid(row=8, column=0, ipadx=1, sticky=W)

type9 = Label(window, text=elements9)
type9.grid(row=8, column=1, padx=0, pady=0, sticky=W)

entry9 = Entry(window, justify=LEFT, width=3, textvariable=numberList[8])
entry9.grid(row=8, column=2, padx=1, pady=0)

# Dried Ephedra -------------------------------------------------------------------------------------------------
herb10 = Label(window, text="Dried Ephedra:")
herb10.grid(row=9, column=0, ipadx=1, sticky=W)

type10 = Label(window, text=elements10)
type10.grid(row=9, column=1, padx=0, pady=0, sticky=W)

entry10 = Entry(window, justify=LEFT, width=3, textvariable=numberList[9])
entry10.grid(row=9, column=2, padx=1, pady=0)

# Drojos Ivy -------------------------------------------------------------------------------------------------
herb11 = Label(window, text="Drojos Ivy:")
herb11.grid(row=10, column=0, ipadx=1, sticky=W)

type11 = Label(window, text=elements11)
type11.grid(row=10, column=1, padx=0, pady=0, sticky=W)

entry11 = Entry(window, justify=LEFT, width=3, textvariable=numberList[10])
entry11.grid(row=10, column=2, padx=1, pady=0)

# Ebrium Fungus -------------------------------------------------------------------------------------------------
herb12 = Label(window, text="Ebrium Fungus:")
herb12.grid(row=11, column=0, ipadx=1, sticky=W)

type12 = Label(window, text=elements12)
type12.grid(row=11, column=1, padx=0, pady=0, sticky=W)

entry12 = Entry(window, justify=LEFT, width=3, textvariable=numberList[11])
entry12.grid(row=11, column=2, padx=1, pady=0)

# Ecire Laurel -------------------------------------------------------------------------------------------------
herb13 = Label(window, text="Ecire Laurel:")
herb13.grid(row=12, column=0, ipadx=1, sticky=W)

type13 = Label(window, text=elements13)
type13.grid(row=12, column=1, padx=0, pady=0, sticky=W)

entry13 = Entry(window, justify=LEFT, width=3, textvariable=numberList[12])
entry13.grid(row=12, column=2, padx=1, pady=0)

# Ellond Scrub -------------------------------------------------------------------------------------------------
herb14 = Label(window, text="Ellond Scrub:")
herb14.grid(row=13, column=0, ipadx=1, sticky=W)

type14 = Label(window, text=elements14)
type14.grid(row=13, column=1, padx=0, pady=0, sticky=W)

entry14 = Entry(window, justify=LEFT, width=3, textvariable=numberList[13])
entry14.grid(row=13, column=2, padx=1, pady=0)

# Frenn Moss -------------------------------------------------------------------------------------------------
herb15 = Label(window, text="Frenn Moss:")
herb15.grid(row=14, column=0, ipadx=1, sticky=W)

type15 = Label(window, text=elements15)
type15.grid(row=14, column=1, padx=0, pady=0, sticky=W)

entry15 = Entry(window, justify=LEFT, width=3, textvariable=numberList[14])
entry15.grid(row=14, column=2, padx=1, pady=0)

# Kasuni Juice -------------------------------------------------------------------------------------------------
herb16 = Label(window, text="Kasuni Juice:")
herb16.grid(row=15, column=0, ipadx=1, sticky=W)

type16 = Label(window, text=elements16)
type16.grid(row=15, column=1, padx=0, pady=0, sticky=W)

entry16 = Entry(window, justify=LEFT, width=3, textvariable=numberList[15])
entry16.grid(row=15, column=2, padx=1, pady=0)

# Kreet Paste -------------------------------------------------------------------------------------------------
herb17 = Label(window, text="Kreet Paste:")
herb17.grid(row=16, column=0, ipadx=1, sticky=W)

type17 = Label(window, text=elements17)
type17.grid(row=16, column=1, padx=0, pady=0, sticky=W)

entry17 = Entry(window, justify=LEFT, width=3, textvariable=numberList[16])
entry17.grid(row=16, column=2, padx=1, pady=0)

# Lunar Nectar -------------------------------------------------------------------------------------------------
herb18 = Label(window, text="Lunar Nectar:")
herb18.grid(row=17, column=0, ipadx=1, sticky=W)

type18 = Label(window, text=elements18)
type18.grid(row=17, column=1, padx=0, pady=0, sticky=W)

entry18 = Entry(window, justify=LEFT, width=3, textvariable=numberList[17])
entry18.grid(row=17, column=2, padx=1, pady=0)

# Mandrake Root -------------------------------------------------------------------------------------------------
herb19 = Label(window, text="Mandrake Root:")
herb19.grid(row=18, column=0, ipadx=1, sticky=W)

type19 = Label(window, text=elements19)
type19.grid(row=18, column=1, padx=0, pady=0, sticky=W)

entry19 = Entry(window, justify=LEFT, width=3, textvariable=numberList[18])
entry19.grid(row=18, column=2, padx=1, pady=0)

# Olina Petals -------------------------------------------------------------------------------------------------
herb20 = Label(window, text="Olina Petals:")
herb20.grid(row=19, column=0, ipadx=1, sticky=W)

type20 = Label(window, text=elements20)
type20.grid(row=19, column=1, padx=0, pady=0, sticky=W)

entry20 = Entry(window, justify=LEFT, width=3, textvariable=numberList[19])
entry20.grid(row=19, column=2, padx=1, pady=0)

# Spineflower Berries -------------------------------------------------------------------------------------------
herb21 = Label(window, text="Spineflower Berries:")
herb21.grid(row=20, column=0, ipadx=1, sticky=W)

type21 = Label(window, text=elements21)
type21.grid(row=20, column=1, padx=0, pady=0, sticky=W)

entry21 = Entry(window, justify=LEFT, width=3, textvariable=numberList[20])
entry21.grid(row=20, column=2, padx=1, pady=0)

# Thunderleaf -------------------------------------------------------------------------------------------------
herb22 = Label(window, text="Thunderleaf:")
herb22.grid(row=21, column=0, ipadx=1, sticky=W)

type22 = Label(window, text=elements22)
type22.grid(row=21, column=1, padx=0, pady=0, sticky=W)

entry22 = Entry(window, justify=LEFT, width=3, textvariable=numberList[21])
entry22.grid(row=21, column=2, padx=1, pady=0)

# Twilight Wormwood --------------------------------------------------------------------------------------------
herb23 = Label(window, text="Twilight Wormwood:")
herb23.grid(row=22, column=0, ipadx=1, sticky=W)

type23 = Label(window, text=elements23)
type23.grid(row=22, column=1, padx=0, pady=0, sticky=W)

entry23 = Entry(window, justify=LEFT, width=3, textvariable=numberList[22])
entry23.grid(row=22, column=2, padx=1, pady=0)

# Ucre Bramble -------------------------------------------------------------------------------------------------
herb24 = Label(window, text="Ucre Bramble:")
herb24.grid(row=23, column=0, ipadx=1, sticky=W)

type24 = Label(window, text=elements24)
type24.grid(row=23, column=1, padx=0, pady=0, sticky=W)

entry24 = Entry(window, justify=LEFT, width=3, textvariable=numberList[23])
entry24.grid(row=23, column=2, padx=1, pady=0)

# White Poppy -------------------------------------------------------------------------------------------------
herb25 = Label(window, text="White Poppy:")
herb25.grid(row=24, column=0, ipadx=1, sticky=W)

type25 = Label(window, text=elements25)
type25.grid(row=24, column=1, padx=0, pady=0, sticky=W)

entry25 = Entry(window, justify=LEFT, width=3, textvariable=numberList[24])
entry25.grid(row=24, column=2, padx=1, pady=0)

# Wisp Stems -------------------------------------------------------------------------------------------------
herb26 = Label(window, text="Wisp Stems:")
herb26.grid(row=25, column=0, ipadx=1, sticky=W)

type26 = Label(window, text=elements26)
type26.grid(row=25, column=1, padx=0, pady=0, sticky=W)

entry26 = Entry(window, justify=LEFT, width=3, textvariable=numberList[25])
entry26.grid(row=25, column=2, padx=1, pady=0)

typeList = [
    type1, type2, type3, type4, type5, type6, type7, type8, type9, type10,
    type11, type12, type13, type14, type15, type16, type17, type18, type19,
    type20, type21, type22, type23, type24, type25, type26
]

herb_list = [
    herb1, herb2, herb3, herb4, herb5, herb6, herb7, herb8, herb9, herb10,
    herb11, herb12, herb13, herb14, herb15, herb16, herb17, herb18, herb19,
    herb20, herb21, herb22, herb23, herb24, herb25, herb26
]
# Elements Total -----------------------------------------------------------------------------------------------
blank = Label(window, text=" ")
blank.grid(row=26, column=0, columnspan=3)

water = Label(window, text=f"Water: 0")
water.grid(row=27, column=0, sticky=N)

earth = Label(window, text=f"Earth: 0")
earth.grid(row=27, column=1, sticky=N)

fire = Label(window, text=f"Fire: 0")
fire.grid(row=27, column=2, sticky=N)

air = Label(window, text=f"Air: 0")
air.grid(row=28, column=0, sticky=N)

positive = Label(window, text=f"Positive: 0")
positive.grid(row=28, column=1, sticky=N)

negative = Label(window, text=f"Negative: 0")
negative.grid(row=28, column=2, sticky=N)

elements_all = [water, earth, fire, air, positive, negative]

window.mainloop()
