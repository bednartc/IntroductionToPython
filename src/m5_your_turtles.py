"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Travis Bednarek.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
Window = rg.TurtleWindow()
bob = rg.SimpleTurtle('turtle')
bob.Pen = rg.Pen('red', 10)
bob.speed = 20
todd = rg.SimpleTurtle('turtle')
todd.Pen = rg.Pen('blue', 10)
todd.speed = 5
size = 200

for k in range(10):
    bob.draw_circle(size)
    bob.pen_up()
    bob.forward(10)
    bob.right(45)
    bob.forward(10)
    bob.left(45)
    bob.pen_down()
    size = size-10

    todd.draw_circle(size)
    todd.pen_up()
    todd.backward(10)
    todd.left(45)
    todd.forward(10)
    todd.right(45)
    todd.pen_down()

Window.close_on_mouse_click()
