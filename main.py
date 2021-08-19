from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard
from random import randint
game_over = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
scoreBoard.show_score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

while not game_over:
    screen.update()
    sleep(0.1)
    snake.movement()
    if snake.head.distance(food) < 15:
        food.goto(randint(-260, 260), randint(-260, 260))
        scoreBoard.add_score()
        scoreBoard.show_score()
        snake.add_segment(snake.snake[-1].position())

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreBoard.game_over()
        game_over = True

    for i in range(1, len(snake.snake)):
        if snake.head.distance(snake.snake[i]) < 10:
            scoreBoard.game_over()
            game_over = True

screen.exitonclick()
