def go_left():
    global derection
    global current_x
    global current_y
    global result_list
    global number
    global x, y

    if current_x >= 0:
        if result_list[current_y][current_x] == -1:
                result_list[current_y][current_x] = number
                current_x -= 1
                number += 1
        else:
            current_x += 1
            current_y -= 1
            derection = 'up'
    else:
        current_x += 1
        current_y -= 1
        derection = 'up'


def go_right():
    global derection
    global current_x
    global current_y
    global result_list
    global number
    global x, y

    if current_x <= x - 1:
        if result_list[current_y][current_x] == -1:
                result_list[current_y][current_x] = number
                current_x += 1
                number += 1
        else:
            current_x -= 1
            current_y += 1
            derection = 'down'
    else:
        current_x -= 1
        current_y += 1
        derection = 'down'


def go_up():
    global derection
    global current_x
    global current_y
    global result_list
    global number
    global x, y

    if current_y >= 0:
        if result_list[current_y][current_x] == -1:
                result_list[current_y][current_x] = number
                current_y -= 1
                number += 1
        else:
            current_x += 1
            current_y += 1
            derection = 'right'
    else:
        current_x += 1
        current_y += 1
        derection = 'right'


def go_down():
    global derection
    global current_x
    global current_y
    global result_list
    global number
    global x, y

    if current_y <= y - 1:
        if result_list[current_y][current_x] == -1:
                result_list[current_y][current_x] = number
                current_y += 1
                number += 1
        else:
            current_x -= 1
            current_y -= 1
            derection = 'left'
    else:
        current_x -= 1
        current_y -= 1
        derection = 'left'

def make_spiral():
    global derection
    global current_x
    global current_y
    global result_list
    global number
    global x, y

    x, y = input("x,y:").split(",")
    x, y = int(x), int(y)
    derection = 'right'
    current_x = 0
    current_y = 0
    result_list = [[-1 for count in range(x)] for count in range(y)]
    number = 1

    while number <= x*y:
        if derection == 'right':
            go_right()
        elif derection == 'down':
            go_down()            
        elif derection == 'left':
            go_left()            
        else:
            go_up()            

    for part_list in result_list:
        print(part_list)

make_spiral()