import turtle

def draw_tree(length, angle = 30, level = 0, color = "black"):
    if level == 0:
        pass
    else:
        turtle.forward(length)
        turtle.right(angle)
        draw_tree(length*.75, angle, level - 1)
        turtle.left(2*angle)
        draw_tree(length*.75, angle, level - 1)
        turtle.right(angle)
        turtle.backward(length)
    



turtle.left(90)
# turtle.tracer(False)
turtle.speed(.1)
draw_tree(100, angle = 15, level = 7)

# 
#    
# 
# 
# def draw_sierpinski(length,depth):
#     if depth==0:
#         for i in range(0,3):
#             turtle.fd(length)
#             turtle.left(120)
#     else:
#         draw_sierpinski(length/2,depth-1)
#         turtle.fd(length/2)
#         draw_sierpinski(length/2,depth-1)
#         turtle.bk(length/2)
#         turtle.left(60)
#         turtle.fd(length/2)
#         turtle.right(60)
#         draw_sierpinski(length/2,depth-1)
#         turtle.left(60)
#         turtle.bk(length/2)
#         turtle.right(60)
# 
# turtle.tracer(False)
# draw_sierpinski(1000,7)