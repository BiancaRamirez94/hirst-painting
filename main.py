# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('paint.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(208, 165, 125), (140, 49, 106), (164, 169, 38), (244, 80, 57), (228, 116, 164), (3, 143, 56),
 (216, 235, 231), (241, 65, 140), (2, 143, 184), (162, 55, 52), (51, 202, 226), (254, 230, 0),
 (21, 165, 127), (211, 234, 238), (28, 195, 218), (120, 183, 147), (231, 167, 192), (142, 213, 225),
 (242, 171, 155), (158, 212, 183), (103, 45, 97), (191, 191, 193), (12, 110, 37)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
  tim.dot(20, random.choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
   tim.setheading(90)
   tim.forward(50)
   tim.setheading(180)
   tim.forward(500)
   tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()