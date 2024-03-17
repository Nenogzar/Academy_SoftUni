# from turtle import *
# tracer(0)
# r = 45
# for i in range(36):
#     rt(60)
#     fd(1 * r)
#     rt(60)
#     fd(1 * r)
#     rt(270)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * r, y * r)
#         dot(3, 'blue')
# goto(0, 0)
# update()
# exitonclick()

########################################
#
# from turtle import *
# tracer(0)
# r = 8
# for i in range(10):
#     for j in range(3):
#         fd(10 * r)
#         rt(90)
#         fd(10 * r)
#         rt(270)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-100, 5):
#         goto(x * r, y * r)
#         dot(3, 'blue')
# goto(0, 0)
# update()
# exitonclick()

########################################

# from turtle import *
# tracer(0)
# r = 15
# for i in range(100):
#     fd(10 * r)
#     rt(36)
# up()
# for x in range(-20, 40):
#     for y in range(-50, 20):
#         goto(x * r, y * r)
#         dot(3, 'blue')
# goto(0, 0)
# update()
# exitonclick()


########################################

from turtle import *
tracer(0)
r = 45
for i in range(10):
    goto(xcor() + 5 * r, ycor() + 7 * r)
    goto(xcor() + 4 * r, ycor() - 3 * r)
    goto(xcor() - 9 * r, ycor() - 4 * r)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(3, 'blue')
goto(0, 0)
update()
exitonclick()