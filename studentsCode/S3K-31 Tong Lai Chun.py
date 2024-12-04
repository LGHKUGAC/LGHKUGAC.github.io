
bgcolor("black")
def draw_star(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()

def draw_logo():

    for i in range(20):
        penup()
        color(pick_random_color_())
        goto(-10 * i, 0)
        pendown()
        right(i * 60)
        draw_star(100 - i * 20, "grey")
        goto(-5 * i, 0)
        draw_star((100 - i * 20) + 20, pick_random_color_())

speed(0)
draw_logo()

