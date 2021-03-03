# Grid Parameters
Xmin = 250
Xmax = 950
Ymin = 70
Ymax = 550

# Field Count
fields = 9
lanes = 5

# Field Size
fieldX = (Xmax - Xmin) / fields
fieldY = (Ymax - Ymin) / lanes


# Array of Plants
board = [[0]*fields for i in range(lanes)]