"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ezrie McCurry.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """
    Calls the other functions in this module to test and/or demonstrate them.
    """
    drawing_speed = 10  # Bigger numbers mean faster drawing
    window = rg.TurtleWindow()
    window.tracer(drawing_speed)

    # -------------------------------------------------------------------------
    # When the _TODO_s ask you to test YOUR code,
    # comment-out the following two statements and replace them
    # by calls to   better_draw_circles   et al as needed.
    # -------------------------------------------------------------------------
    #draw_circles(rg.Point(100, 50))
    #draw_circles(rg.Point(-200, 0))
    #draw_circles(rg.Point(100,100))
    #draw_circles(rg.Point(-100, 100))
    #better_draw_circles(rg.Point(-50,-100),15)
    #better_draw_circles(rg.Point(50, -100), 5)
    #even_better_draw_circles(rg.Point(-50,-100), 42, 3, 'pink', 6)
    #even_better_draw_circles(rg.Point(50,-100), 3, 30, 'green', 1)
    even_better_draw_circles(rg.Point(0, -100), 3, 10, 'brown', 2)
    even_better_draw_circles(rg.Point(0, -50), 3, 10, 'brown', 2)
    even_better_draw_circles(rg.Point(0, 0), 3, 10, 'brown', 2)
    even_better_draw_circles(rg.Point(0, 50), 3, 10, 'brown', 2)
    even_better_draw_circles(rg.Point(0, 150), 3, 8, 'green', 2)
    even_better_draw_circles(rg.Point(-75, 125), 3, 10, 'green', 2)
    even_better_draw_circles(rg.Point(50, 175), 3, 15, 'green', 2)
    even_better_draw_circles(rg.Point(25, 100), 3, 13, 'green', 2)
    even_better_draw_circles(rg.Point(-25, 120), 3, 7, 'green', 2)
    even_better_draw_circles(rg.Point(-35, 165), 3, 10, 'green', 2)
    even_better_draw_circles(rg.Point(0, 200), 3, 16, 'green', 2)
    even_better_draw_circles(rg.Point(-50, 85), 3, 11, 'green', 2)

    window.update()
    window.close_on_mouse_click()


###############################################################################
# DONE: 2.
#   First, RUN this program.  You will see that it draws concentric circles
#   whose radii vary by 15.
#
#   Next, READ:
#     -- main.
#          Note that it  constructs a TurtleWindow and then calls the function
#             draw_circles
#          twice, sending   draw_circles  one Point the first time
#          and another Point the second time.
#     -- The function  draw_circles  is defined immediately below this _TODO_.
#            Be sure that you understand its code!  Ask questions as needed!
#
#   After you have done the above, change the above _TODO_ to DONE
#   and continue to the next _TODO_ below.
#
###############################################################################


def draw_circles(point):
    """
    Constructs a SimpleTurtle, then uses the SimpleTurtle to draw 10 circles
    such that:
      -- Each is centered at the given Point, and
      -- They have radii:  15  30  45  60  75  ..., respectively.
    """
    turtle = rg.SimpleTurtle()

    # -------------------------------------------------------------------------
    # Draw circles centered at the given Point, by telling the SimpleTurtle to:
    #  Step 1: Go to the given Point and point east (towards the right).
    #  Step 2: Go 15 pixels DOWN, with its Pen up.
    #          Then draw a radius R circle.
    #    Note: The circle will be centered at the given Point,
    #    because of the way that the SimpleTurtle  draw_circle  method works.
    #  Step 3: Repeat Step 2, but using 30 pixels instead of 15, in both places
    #  Step 4: Repeat Step 2, but using 45 pixels instead of 15
    #  Step 5: Repeat Step 2, but using 60 pixels instead of 15
    #    etc.
    # -------------------------------------------------------------------------

    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...


###############################################################################
# DONE: 3a.
#   The function
#       better_draw_circles
#   defined below this _TODO_ starts out exactly the same as the code for
#       draw_circles
#   that you read above.
#
#   Your job is to make
#       better_draw_circles
#   "better" than   draw_circles   by adding a PARAMETER for the amount
#   by which the radii of the concentric circles increase, as described below.
#
#   The new   better_draw_circles   function can do the same  thing as
#   the   draw_circles  function, but additionally allows for the radii to
#   vary by ANY desired amount.  Hence, the new version will be MORE POWERFUL.
#
#   So, modify the   better_draw_circles   function defined BELOW so that
#   it has a single ADDITIONAL PARAMETER that is the amount
#   by which the radii of the circles increase.
#
#   For example, if that new parameter is given the value 15,
#   then the circles should have radii:  15  30  45  60  75 ..., respectively,
#   just as in   draw_circles.  But if that new parameter is given the value 3,
#   then the circles should have radii:  3  6  9  12  15  18 ..., respectively.
#
# DONE: 3b.
#   In   main  at the place indicated, comment-out the two existing calls
#   to  draw_circles  and add at least two calls to the improved
#   better_draw_circles  function, to TEST that your modified code is correct
#   and does indeed allow for different amounts by which the radii can vary.
#
# #############################################################################


def better_draw_circles(point,incriment):
    """
    Starts out the same as the   draw_circles   function defined ABOVE.
    You Will make it an IMPROVED, MORE POWERFUL function per the above _TODO_.
    """
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)
    radius = 0

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(incriment)
        turtle.left(90)
        radius = radius + incriment
        turtle.pen_down()
        turtle.draw_circle(radius)  # Radius 15, 30, 45, 60, ...


###############################################################################
# TODO: 4a.
#   In the previous _TODO_, you made a MORE POWERFUL version
#   of   draw_circles   by introducing a new PARAMETER for the amount
#   by which the radii of the concentric circles increase.
#
#   In this _TODO_, you will implement a function called
#      even_better_draw_circles
#   that has FIVE parameters, for:
#     -- The center of the concentric circles (as it started with)
#     -- The amount by which the radii vary (as you did above)
#     -- The number of concentric circles drawn
#     -- The pen color of each of the concentric circles
#     -- The pen thickness of each of the concentric circles
#
#   Hence, this   even_better_draw_circles   function will be
#   even more POWERFUL than the previous functions,
#   in that it can draw LOTS of different kinds of circles.
#
#   Start by copy-and-pasting the code from   better_draw_circles  above
#   to the body of the   even_better_draw_circles   function defined below.
#   Then add parameters and modify the code to make them work!
#
# DONE: 4b.
#   In   main  at the place indicated, comment-out the existing calls
#   to  better_draw_circles  and add at least two calls to the improved
#   even_better_draw_circles  function, to TEST that your modified code is
#   correct and does indeed use its parameters per their descriptions above.
#
###############################################################################

def even_better_draw_circles(point, incriment, number_of_circles,color,thickness):

    turtle = rg.SimpleTurtle()  #create a turtle
    turtle.pen.color = color
    turtle.pen.thickness = thickness
    turtle.pen_up() #lift the pen up
    turtle.go_to(point) #moves the turtle to specified point
    turtle.set_heading(0)  # Point "east" (towards the right)
    radius = 0

    for k in range(1, number_of_circles):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(incriment)
        turtle.left(90)
        radius = radius + incriment
        turtle.pen_down()
        turtle.draw_circle(radius)  # Radius 15, 30, 45, 60, ...

###############################################################################
# DONE: 5.
#
# Finally, comment-out the existing calls to  even_better_draw_circles  and
# add code in   main  to draw various circles that form a BEAUTIFUL picture!
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
