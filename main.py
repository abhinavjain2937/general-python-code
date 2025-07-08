# import colorgram

# #extract six colour from image
# colours = colorgram.extract('painting.jpg',50)


# #colourgram.extract returns color objects which let you access
# #RGB ,HSL and what proportion of images was that colour

# rgb_colour = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r,g,b)
#     rgb_colour.append(new_colour)

# print(rgb_colour)
## we extracrted the colour so we dont need to run thids code again
# ##____________________________________________________

import turtle as t
import random

t.colormode(255)
aj = t.Turtle()
aj.speed(0)
aj.penup()
colour_list = [(246, 240, 233), (249, 234, 241), (233, 247, 237), (227, 236, 245), (239, 233, 75), (209, 161, 103), (226, 70, 133), (217, 155, 10), (176, 78, 24), (204, 136, 186), (115, 168, 236), (224, 235, 2), (79, 177, 36), (72, 98, 224), (238, 164, 193), (69, 34, 26), (51, 120, 42), (241, 53, 32), (151, 66, 140), (132, 197, 131), (188, 20, 9), (52, 101, 150), (207, 6, 52), (149, 217, 173), (155, 184, 242), (24, 95, 22), (240, 172, 162), (138, 214, 234), (84, 72, 38), (65, 42, 151), (253, 6, 17), (253, 6, 4), (79, 7, 8), (18, 101, 108), (8, 75, 8), (17, 57, 253), (96, 139, 155)]

aj.setheading(225)
aj.forward(388)
aj.setheading(0)
num_of_dots = 100
for dot_count in range(1,num_of_dots +1):
    aj.dot(20, random.choice(colour_list))
    aj.forward(50)
    
    if dot_count % 10 == 0 :
        aj.setheading(90)
        aj.forward(50)
        aj.setheading(180)
        aj.forward(500)
        aj.setheading(0)


screen = t.Screen()
screen.exitonclick()





