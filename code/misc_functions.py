
import pygame
#python module that allows you to read csv files
from csv import reader
#walk lets you walk through os's file system
from os import walk

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

def import_folder(path):
   #declaring empty list to store values
    surface_list = []
   
    #path holds data in third element of list, other two elements not useful to us
    for _, __, img_files in walk(path):
        #looping through each image
        for image in img_files:
            #concaternating path to img_file and then adding each file as a surface
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            #add each surface to list at end of list
            surface_list.append(image_surface)

        return surface_list

