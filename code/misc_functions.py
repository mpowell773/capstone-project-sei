
#python module that allows you to read csv files
from csv import reader

def import_csv_layout(path):
    terrain_map = []
    #open the path and give variable name level_map
    with open(path) as level_map:
        #read through map and add commas throughout // creates object
        layout = reader(level_map, delimiter = ',')
        #loop through the object and append the lists into our own list
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
