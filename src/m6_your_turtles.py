"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ashley Fowler.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(10)

samwell = rg.SimpleTurtle()
samwell.pen = rg.Pen('goldenrod',5)
samwell.speed=10

ben=rg.SimpleTurtle()
ben.pen=rg.Pen('wheat',5)
ben.speed=10

size=200


for k in range(14):
    samwell.draw_square(size)
    ben.draw_square(size)

    samwell.pen_up()
    ben.pen_up()
    samwell.right(35)
    ben.right(35)
    samwell.forward(12)
    ben.forward(9)
    samwell.left(50)
    ben.left(50)

    samwell.pen_down()
    ben.pen_down()
    size=size-15




window.close_on_mouse_click()

