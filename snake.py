from Tkinter import *
import time
import random


class Snake:

    def __init__(player):
        player.body = [[200, x] for x in range(200, 250, 10)]
        player.color = ('#00a9ae', '#051403')
        player.move = 'up'
        player.score = 0
        player.speed = 0.1
        player.b = True
        player.tar = create_target()

    def stop(self, event):
        if player.b:
            player.b = False
            return
        player.b = True
        game()

    def move_up(player, event):
        if player.move != 'down': player.move = 'up'

    def move_down(player, event):
        if player.move != 'up': player.move = 'down'

    def move_left(player, event):
        if player.move != 'right': player.move = 'left'

    def move_right(player, event):
        if player.move != 'left': player.move = 'right'

    def draw(player):
        a, b = 0, 1
        for x, y in player.body:
            canv.create_oval(y, x, y + 10, x + 10, tag = 'rect', fill = player.color[a], outline = player.color[a])
            a, b = b, a

    def step(player):
        head = player.body[len(player.body) - 1][:]
        if player.move == 'up':
            head[0] -= 10
            if head[0] == -10: head[0] = 490
        elif player.move == 'down':
            head[0] += 10
            if head[0] == 500: head[0] = 0
        elif player.move == 'left':
            head[1] -= 10
            if head[1] == -10: head[1] = 490
        elif player.move == 'right':
            head[1] += 10
            if head[1] == 500: head[1] = 0

        player.body.append(head)
        del player.body[0]

        for x in player.body[:-1]:
            if x == head:
                player.b = False
                canv.create_text(250, 200, text='GAME OVER', font='Arial 30', fill='#000')
           

        if head == player.tar:
            player.score += 1
            player.body.append(player.tar)
            player.tar = create_target()
            if player.speed > 0.02: player.speed -= 0.002
            canv.delete('score')
            canv.create_text(60, 16, text='score: ' + str(player.score), tag='score', font='Arial 12', fill='#000')
        

def game():
    while snake.b:
        canv.delete('rect')
        snake.step()
        snake.draw()
        canv.update()
        time.sleep(snake.speed)


def create_target():
    canv.delete('target')
    x = (random.randint(1, 49) * 10)
    y = (random.randint(1, 49) * 10)
    canv.create_oval(x, y, x + 10, y + 10, tag='target', fill='#9966cc')
    return [y, x]

root = Tk()
root.title('Snake')


canv = Canvas(root, width=500, height=500, bg='#DDD')
canv.pack()





snake = Snake()

root.bind('<w>', snake.move_up)
root.bind('<s>', snake.move_down)
root.bind('<a>', snake.move_left)
root.bind('<d>', snake.move_right)

game()

root.mainloop()
