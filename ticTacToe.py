
data={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}


def draw_pattern():
    print(data[1], '|', data[2], '|', data[3])
    print('----------')
    print(data[4], '|', data[5], '|', data[6])
    print('----------')
    print(data[7], '|', data[8], '|', data[9])
    print('----------')


def computer():
    if (data[1] == data[2] == 'X' or data[6] == data[9] == 'X' or data[5] == data[7] == 'X') and (data[3] == ' '):
        data[3] = 'O'
    elif (data[2] == data[3] == 'X' or data[4] == data[7] == 'X' or data[5] == data[9] == 'X') and (data[1] == ' '):
        data[1] = 'O'
    elif (data[1] == data[3] == 'X' or data[5] == data[8] == 'X') and (data[2] == ' '):
        data[2] = 'O'
    elif (data[1] == data[7] == 'X' or data[5] == data[6] == 'X') and (data[4] == ' '):
        data[4] = 'O'
    elif (data[2] == data[8] == 'X' or data[4] == data[6] == 'X' or data[1] == data[9] == 'X' or data[3] == data[7] == 'X') and (data[5] == ' '):
        data[5] = 'O'
    elif (data[4] == data[5] == 'X' or data[3] == data[9] == 'X') and (data[6] == ' '):
        data[6] = 'O'
    elif (data[8] == data[9] == 'X' or data[1] == data[4] == 'X' or data[3] == data[5] == 'X') and (data[7] == ' '):
        data[7] = 'O'
    elif (data[2] == data[5] == 'X' or data[7] == data[9] == 'X') and (data[8] == ' '):
        data[8] = 'O'
    elif (data[7] == data[8] == 'X' or data[6] == data[3] == 'X' or data[1] == data[5] == 'X') and (data[9] == ' '):
        data[9] = 'O'
    elif data[5]=='X':
        for i in [1,3,7,9]:
            if data[i]==' ':
                data[i]='O'
                break
    elif data[1]=='X' or data[3]=='X' or  data[7]=='X' or  data[9]=='X':
        data[5]='O'
    else:
        for i in data:
            if data[i] == ' ':
                data[i] = 'O'
                break


def user_restriction(choice):
    if data[choice] == 'O':
        return False
    else:
        return True


def winner():
    for i in ['X','O']:
        if data[1] == data[2] == data[3] == i:
            return i
        elif data[1] == data[4] == data[7] == i:
            return i
        elif data[2] == data[5] == data[8] == i:
            return i
        elif data[3] == data[6] == data[9] == i:
            return i
        elif data[4] == data[5] == data[6] == i:
            return i
        elif data[7] == data[8] == data[9] == i:
            return i
        elif data[1] == data[5] == data[9] == i:
            return i
        elif data[3] == data[5] == data[7] == i:
            return i


def game():
    playing = True
    count = 0
    while playing:
        user_choice = int(input('enter the position : '))
        user_restriction(user_choice)
        if user_restriction(user_choice):

            data[user_choice] = 'X'
            if count > 0:
                computer()
            else:
                for i in data:
                    if data[i] == ' ':
                        data[i] = 'O'
                        break

            draw_pattern()
        else:
            print('already filled: ')
        n = []
        for i in range(1,10):
            n.append(data[i])
        # print(n)
        if n.count(' ')==0:
            print('draw')
            playing=False

        count += 1
        if count==9:

            playing=False
        win = winner()

        if win:
            if win=='X':
                print('you won')
            else:
                print('computer won')
            playing = False


game()
