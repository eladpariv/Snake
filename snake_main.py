
import game_parameters
from game_display import GameDisplay

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    direction = "Up"
    len_of_snake = 3
    num_of_need_more_apples_on_board = 3
    num_of_need_more_bombs_on_board = 1
    lst_of_apples_on_board = []
    coordinates_of_snake = [[10,10],[10,9],[10,8]]
    score = 0

    time_until_explosion = 0
    radios_explosion = 0
    place_x_of_bomb = 0
    place_y_of_bomb = 0
    radios_explosion_every_step = 0
    no_need_to_continue = False
    snake_is_out = False
    some_num = 0
    need_to_grow = 0
    is_first_round = 0

    try:
        while True:
            gd.show_score(score)
            if is_first_round==0:
                for index in coordinates_of_snake:
                    gd.draw_cell(index[0], index[1], "black")





            if num_of_need_more_apples_on_board>0 and len(lst_of_apples_on_board)<3:
                lst_of_apples_on_board = apple_appending_to_board(lst_of_apples_on_board,coordinates_of_snake,num_of_need_more_apples_on_board)
                num_of_need_more_apples_on_board = 0


            for apple in lst_of_apples_on_board:
                gd.draw_cell(apple[0], apple[1], "green")

            if num_of_need_more_bombs_on_board==1:
                # bomb_data = game_parameters.get_random_bomb_data()
                bomb_data = bomb_appending_to_board(coordinates_of_snake)
                time_until_explosion = bomb_data[3]
                radios_explosion = bomb_data[2]
                place_x_of_bomb = bomb_data[0]
                place_y_of_bomb = bomb_data[1]
                radios_explosion_every_step = 0
                num_of_need_more_bombs_on_board=0


            if time_until_explosion>0:
                for dot in coordinates_of_snake:
                    if dot[0]==place_x_of_bomb and dot[1]==place_y_of_bomb:
                        coordinates_of_snake.remove(dot)
                        gd.draw_cell(place_x_of_bomb, place_y_of_bomb, "Red")
                        for dot4 in coordinates_of_snake:
                            gd.draw_cell(dot4[0], dot4[1], "black")##############

                        gd.end_round()
                        return None
                gd.draw_cell(place_x_of_bomb,place_y_of_bomb,"Red")
                time_until_explosion-=1
            elif time_until_explosion==0:
                if radios_explosion>=radios_explosion_every_step:
                    lst_of_orange_cells = []

                    lst_of_orange_cells.append([place_x_of_bomb,place_y_of_bomb])


                    for step in range(1,radios_explosion_every_step+1):
                        lst_of_orange_cells.append([place_x_of_bomb+step, place_y_of_bomb])
                        lst_of_orange_cells.append([place_x_of_bomb, place_y_of_bomb+step])
                        lst_of_orange_cells.append([place_x_of_bomb-step, place_y_of_bomb])
                        lst_of_orange_cells.append([place_x_of_bomb, place_y_of_bomb-step])
                        lst_of_orange_cells.append([place_x_of_bomb-step, place_y_of_bomb-step])
                        lst_of_orange_cells.append([place_x_of_bomb+step, place_y_of_bomb+step])
                        lst_of_orange_cells.append([place_x_of_bomb+step, place_y_of_bomb-step])
                        lst_of_orange_cells.append([place_x_of_bomb-step, place_y_of_bomb+step])
                    lst_of_cells_to_print = []
                    for dot in lst_of_orange_cells:
                        if abs(place_x_of_bomb - dot[0]) + abs(place_y_of_bomb - dot[1]) == radios_explosion_every_step:
                            lst_of_cells_to_print.append(dot)

                    dot_to_print_in_board = False
                    for dot in lst_of_cells_to_print:
                        if dot[0]>=0 and dot[0]<=game_parameters.WIDTH-1 and dot[1]>=0 and dot[1]<=game_parameters.HEIGHT-1:
                            dot_to_print_in_board = True

                        else:
                            dot_to_print_in_board=False
                            num_of_need_more_bombs_on_board = 1
                            break

                    if dot_to_print_in_board==True:
                        for dot1 in lst_of_cells_to_print:
                            for dot_of_snake in coordinates_of_snake:#if the bomb touch the snake
                                if dot1[0]==dot_of_snake[0] and dot1[1]==dot_of_snake[1]:
                                    gd.draw_cell(dot1[0], dot1[1], "Orange")
                                    coordinates_of_snake.remove(dot_of_snake)
                                    for dot in coordinates_of_snake:
                                        gd.draw_cell(dot[0],dot[1],"black")
                                    for dot3 in lst_of_cells_to_print:
                                        gd.draw_cell(dot3[0],dot3[1],"orange")

                                    gd.end_round()
                                    return None


                            gd.draw_cell(dot1[0], dot1[1], "Orange")

                            for apple in lst_of_apples_on_board:
                                if dot1[0]==apple[0] and dot1[1]==apple[1]:
                                    lst_of_apples_on_board.remove(apple)
                                    num_of_need_more_apples_on_board+=1


                    radios_explosion_every_step+=1
                else:
                    num_of_need_more_bombs_on_board=1



            if is_first_round == 1:
                key_clicked = gd.get_key_clicked()

                if (key_clicked == 'Left') and (x > 0):
                    if direction!="Right":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0,[coordinates_of_snake[0][0]-1,coordinates_of_snake[0][1]])
                        direction="Left"
                    elif direction == "Right":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0] + 1, coordinates_of_snake[0][1]])
                        direction = "Right"


                elif (key_clicked == 'Right') and (x < game_parameters.WIDTH-1):
                    if direction != "Left":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0] + 1, coordinates_of_snake[0][1]])
                        direction = "Right"
                    elif direction == "Left":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0] - 1, coordinates_of_snake[0][1]])
                        direction = "Left"


                elif (key_clicked == 'Up') and (y < game_parameters.HEIGHT-1):
                    if direction !="Down":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1]+1])
                        direction = "Up"
                    elif direction == "Down":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1] - 1])
                        direction = "Down"



                elif (key_clicked == 'Down') and (y > 0):
                    if direction !="Up":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1] - 1])
                        direction = "Down"

                    elif direction=="Up":
                        if need_to_grow == 0:
                            coordinates_of_snake.pop()
                        else:
                            need_to_grow -= 1
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1] + 1])
                        direction = "Up"


                else:
                    if need_to_grow==0:
                        coordinates_of_snake.pop()
                    else:
                        need_to_grow-=1

                    if direction=="Left":
                        # coordinates_of_snake.pop()
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0] - 1, coordinates_of_snake[0][1]])
                    elif direction =="Right":
                        # coordinates_of_snake.pop()
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0] + 1, coordinates_of_snake[0][1]])
                    elif direction== "Up":
                        # coordinates_of_snake.pop()
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1] + 1])
                    elif direction == "Down":
                        # coordinates_of_snake.pop()
                        coordinates_of_snake.insert(0, [coordinates_of_snake[0][0], coordinates_of_snake[0][1] - 1])


                for index_of_place,index in enumerate(coordinates_of_snake):
                    if index[0]>game_parameters.WIDTH or index[1]>game_parameters.HEIGHT or index[0]<-1 or index[1]<-1:
                        coordinates_of_snake.remove(index)

                    else:
                        for dot_is_apple in lst_of_apples_on_board:
                            if dot_is_apple[0]==index[0] and dot_is_apple[1]==index[1]:
                                len_of_snake+=3
                                need_to_grow+=3
                                score+=dot_is_apple[2]
                                apple_data = game_parameters.get_random_apple_data()
                                lst_of_apples_on_board.append(apple_data)
                                lst_of_apples_on_board.remove(dot_is_apple)


                        for index_of_dot,dot in enumerate(coordinates_of_snake):
                            if index[0]==dot[0] and index[1]==dot[1] and index_of_dot!=index_of_place:
                                coordinates_of_snake.remove(dot)
                                gd.end_round()
                                return None

                    gd.draw_cell(index[0], index[1], "black")

            is_first_round=1
            gd.end_round()



    except:
        return None

def apple_appending_to_board(lst_of_apples_on_board,coordinates_of_snake,num_of_need_more_apples_on_board):
    while True:
        apple_to_place = True
        apple_data = game_parameters.get_random_apple_data()
        for apple in lst_of_apples_on_board:
            if not apple[0] == apple_data[0] and apple[1] == apple_data[1]:
                apple_to_place = False
        for cord in coordinates_of_snake:
            if not cord[0]==apple_data[0] and cord[1]==apple_data[1]:
                apple_to_place = False

        if apple_to_place == True:
            lst_of_apples_on_board.append(apple_data)
            num_of_need_more_apples_on_board-=1
            if num_of_need_more_apples_on_board==0:
                return lst_of_apples_on_board


def bomb_appending_to_board(coordinates_of_snake):
    bomb_data = game_parameters.get_random_bomb_data()
    place_of_bomb_is_fine = True
    for dot in coordinates_of_snake:
        if dot[0]!=bomb_data[0] and dot[1]!=bomb_data[1]:
            place_of_bomb_is_fine = True
        else: place_of_bomb_is_fine = False
    if place_of_bomb_is_fine ==True:
        return bomb_data
    else: return bomb_appending_to_board(coordinates_of_snake)


if __name__ == "__main__":
    main_loop(GameDisplay())
