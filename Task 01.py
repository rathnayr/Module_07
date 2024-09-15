seasons = ("Winter", "Spring", "Summer", "Autumn")
def Get_Seasons(Month):
    if Month in [12,1,2]:
        return seasons[0]
    elif Month in [3,4,5,]:
        return seasons[1]
    elif Month in [6,7,8]:
        return seasons[2]
    elif Month in [9,10,11]:
        return seasons[3]
    else:
        return
Month = int(input("Enter a number of a month:"))

season = Get_Seasons(Month)

if season:
    print(f"The corresponding season is: {season}.")
else:
    print("Input is incorrect. Enter number between 1 and 12.")