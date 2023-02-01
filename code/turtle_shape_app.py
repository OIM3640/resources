import turtle

import turtle_shape


def draw_stuff():
    """
    draws a square and a circle
    """
    leo = turtle.Turtle()

    # draw a square at the default origin position
    turtle_shape.square(leo, 100)

    # move pen to a new position (200px to eastward, 100px northward)
    turtle_shape.move(leo, 200, 100)

    # draw a circle at the new position
    turtle_shape.circle(leo, 50)

    turtle.mainloop()


if __name__ == "__main__":
    draw_stuff()
