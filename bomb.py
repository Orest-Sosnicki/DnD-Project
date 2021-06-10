from tkinter import *

def bomb_display():
    global herb_listbox, ingredients_listbox, effect, repeat, additional_effect, display_calculated, display_total, \
        effect_list, additional_effect_list, numbers

    craft = Tk()

    craft.title("Bomb Crafting")
    craft.geometry("600x450")

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
    repeat.set(1)

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