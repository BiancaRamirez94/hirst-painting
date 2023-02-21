# hirst-painting

This code creates a turtle graphics drawing of a dotted line using a pre-defined list of colors. The colors are initially generated using the colorgram library which extracts colors from an image file. In this code, it extracts colors from a file called "paint.jpg". The extracted colors are then added to the "color_list" variable which is used by the turtle to randomly select colors for the dots.

The turtle starts at a position and angle to draw a diagonal line, and then it proceeds to draw dots in a loop. Every time it draws 10 dots, it moves up, turns around and moves back to the start of the line to continue drawing dots. The turtle graphics screen is created using the turtle's Screen() method and can be closed by clicking on the screen.

Overall, this code generates an interesting graphic that resembles a dotted line with different colors.
