NAMES = {"AliceBlue".lower(): "#f0f8ff", "AntiqueWhite".lower(): "#faebd7",
         "AntiqueWhite1".lower(): "#ffefdb", "AntiqueWhite2".lower(): "#eedfcc",
         "AntiqueWhite3".lower(): "#cdc0b0", "AntiqueWhite4".lower(): "#8b8378",
         "aquamarine1".lower(): "#7fffd4", "aquamarine2".lower(): "#76eec6",
         "aquamarine4".lower(): "#458b74", "azure1".lower(): "#f0ffff",
         "azure2".lower(): "#e0eeee", "azure3".lower(): "#c1cdcd", "azure4".lower(): "#838b8b",
         "beige".lower(): "#f5f5dc", "bisque1".lower(): "#ffe4c4"}

name = input("Enter a colour name: ").lower()
while name != "":
    try:
        print(NAMES[name])
    except KeyError:
        print("Invalid colour name!")
    name = input("Enter a colour name: ").lower()
