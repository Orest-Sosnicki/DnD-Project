from tkinter import *

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