from tkinter import ttk, Tk, Label, Button, LEFT, Entry, Listbox, END, E, NE, StringVar, IntVar, Menu, W, N, messagebox
from tkinter import *
import text_block
import save_open
import add_herb
import bomb

def parts_display():
  
  parts_list = Tk()
  parts_list.title("Monster Parts List")
  parts_list.geometry("400x400")

  # Add parts ----------------------------------------------------------------------------------------------
  add_labal = Label(parts_list, justify=LEFT, text="Part Name", height=2)
  add_labal.grid(row=0, column=0)

  add_part = Entry(parts_list, justify=LEFT, width=25)
  add_part.grid(row=0, column=1)

  add_part_button = Button(parts_list, justify=LEFT, text="Add")
  add_part_button.grid(row=0, column=2)

  # Parts list -----------------------------------------------------------------------------------------------

  parts_label = Label(parts_list, text="List of Parts")
  parts_label.grid(row=3, column=0)

  parts_listbox = Listbox(parts_list, width=30, height=10)
  parts_listbox.grid(row=4, column=0, rowspan=2, columnspan=7)
  parts_listbox.bind("<Double-Button-1>", add_ingredient)


def bomb_display(additional_effect_list, numbers, herb_listbox, ingredients_listbox, numberList):
        
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
    herb_listbox.bind("<Double-Button-1>", lambda i : add_ingredient(i, herb_listbox, ingredients_listbox, amount_list, position_list, display_total))

    # ingredients want to us --------------------------------------------------------------------------------------
    ingredients_label = Label(craft, text="Ingredients")
    ingredients_label.grid(row=9, column=0)

    ingredients_listbox = Listbox(craft, width=30, height=10)
    ingredients_listbox.grid(row=10, column=0, columnspan=2, rowspan=7)
    ingredients_listbox.bind("<Double-Button-1>", lambda i : remove_ingredient(i, herb_listbox, ingredients_listbox, amount_list, position_list, display_total))

    ingredients_listbox.delete(0, END)
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
    # Set List ---------------------------------------------------------------------------------------
    amount_list = []
    position_list = []
    count = 0
    element_totals = [0, 0, 0, 0, 0, 0]
    
    for n in numberList:
        if n.get() != 0:
            amount_list.append(int(n.get()))
            position_list.append(count)
        count += 1

    update_list(herb_listbox, amount_list, position_list)

def calculate_total():
    global effect, additional_effect, repeat, display_calculated, effect_list, effect_list,additional_effect_list, numbers

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


def update_list(herb_listbox, amount_list, position_list):
    
    herb_listbox.delete(0, END)
    count = 0

    for n in position_list:
        into = f"{herb_list[n]['text']} {element_label[n]} {amount_list[count]}"
        herb_listbox.insert(END, into)
        count += 1


def add_ingredient(event, herb_listbox, ingredients_listbox, amount_list, position_list, display_total):

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

            update_list(herb_listbox, amount_list, position_list)

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
        print("adding to fast")


def remove_ingredient(event, herb_listbox, ingredients_listbox, amount_list, position_list, display_total):
  
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

        update_list(herb_listbox, amount_list, position_list)

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
        print("clicking to fast")


window = Tk()

window.title("Arcane Creations: Version 2.1")
window.geometry("400x700")


areas_list = [
    "Arctic", "Caves", "Desert", "Forests", "Water", "Mountains", "Plains",
    "Swamps"
]

radio_value = IntVar()

herb_listbox = ""
ingredients_listbox = ""

element_totals = [0, 0, 0, 0, 0, 0]
amount_list = []
position_list = []

use_ingredient = []

effect = StringVar()
additional_effect = ""
repeat = 0
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

numberList = [IntVar(), IntVar(), IntVar(), IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
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
file_menu.add_command(label="Open", command=lambda: save_open.open_file("DnD_Bombs", numberList, typeList, total_all, elements_all))
file_menu.add_command(label="Save", command=lambda: save_open.confirm("DnD_Bombs", numberList, typeList, total_all, elements_all))
file_menu.add_command(label="", state="disabled")
file_menu.add_command(label="Open Backup",
                      command=lambda: save_open.open_file("DnD_Bombs_backup", numberList, typeList, total_all, elements_all))
file_menu.add_command(label="Save Backup",
                      command=lambda: save_open.confirm("DnD_Bombs_backup", numberList, typeList, total_all, elements_all))
file_menu.add_command(label="", state="disabled")
file_menu.add_command(label="Exit", command=window.quit)

# herb menu --------------------------------------------------------------------------------------------------
herb_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Herb", menu=herb_menu)
herb_menu.add_command(label="Info", command=text_block.show_info)

# herb area(submenu) ---------------------------------------------------
area_menu = Menu(herb_menu, tearoff=False)
herb_menu.add_cascade(label="Area", menu=area_menu)
area_menu.add_command(label="Arctic", command=lambda: text_block.show_area(0))
area_menu.add_command(label="Caves", command=lambda: text_block.show_area(1))
area_menu.add_command(label="Desert", command=lambda: text_block.show_area(2))
area_menu.add_command(label="Forests", command=lambda: text_block.show_area(3))
area_menu.add_command(label="Water", command=lambda: text_block.show_area(4))
area_menu.add_command(label="Mountains",
                      command=lambda: text_block.show_area(5))
area_menu.add_command(label="Plains", command=lambda: text_block.show_area(6))
area_menu.add_command(label="Swamps", command=lambda: text_block.show_area(7))

herb_menu.add_command(label="Add Herb", command=lambda: add_herb.add_interface(radio_value, areas_list))

# bombs menu ---------------------------------------------------------------------------------------------------
bomb_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Bomb", menu=bomb_menu)
bomb_menu.add_command(label="Craft", command=lambda: bomb_display(additional_effect_list,numbers, herb_listbox, ingredients_listbox, numberList))

# Parts menu ---------------------------------------------------------------------------------------------------
parts_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Parts", menu=parts_menu)
parts_menu.add_command(label="Monster Parts", command=parts_display)

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
