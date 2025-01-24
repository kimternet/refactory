# utils.py
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def add_coordinates_to_image(img, coordinates, left_move, right_move, net_move):
   fig, ax = plt.subplots()
   ax.imshow(img)
   ax.axis('off')
   
   ax.text(coordinates[0][0], coordinates[0][1], f"{left_move}", color='black', fontsize=14, ha='center', va='center', fontfamily='serif')
   ax.text(coordinates[1][0], coordinates[1][1], f"0", color='black', fontsize=14, ha='center', va='center', fontfamily='serif')
   ax.text(coordinates[2][0], coordinates[2][1], f"+{net_move}", color='black', fontsize=14, ha='center', va='center', fontfamily='serif')
   
   return fig