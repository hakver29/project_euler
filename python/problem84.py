import numpy as np

ch_card = [7,22,36]
cc_card = [2,17,33]
g2j = [30]
jail = [10]
railways = [5,15,25,35]
utility = [12,28]

def draw_cc(current_pos, card):
    if card == 0:
        return 0
    elif card == 1:
        return 10
    else:
        return current_pos

def draw_ch(current_pos, card):
    if card == 0:
        return 0
    elif card == 1:
        return 10
    elif card == 2:
        return 11
    elif card == 3:
        return 24
    elif card == 4:
        return 39
    elif card == 5:
        return 5
    elif card in [6,7]:
        while max(railways) < current_pos:
            current_pos -= 40
        for i in railways:
            if i > current_pos:
                return i
    elif card == 8:
        while max(utility) < current_pos:
            current_pos -= 40
        for i in utility:
            if i > current_pos:
                return i
    elif card == 9:
        current_pos = (current_pos - 3) % 40
        return current_pos
    else:
        return current_pos

def draw_card(current_pos):
    card = np.random.randint(low=1, high=17)
    if card in [1,3]:
        return 0
    elif card in [2,4]:
        return 10
    elif card == 5:
        return 11
    elif card == 6:
        return 24
    elif card == 7:
        return 39
    elif card == 8:
        return 5
    elif card in [9,10]:
        while max(railways) < current_pos:
            current_pos -= 40

        for i in railways:
            if i > current_pos:
                return i
    elif card == 11:
        while max(utility) < current_pos:
            current_pos -= 40

        for i in utility:
            if i > current_pos:
                return i
    elif card == 12:
        current_pos = (current_pos - 3) % 40
        return (current_pos-3) % 40
    else:
        return current_pos


def main():
    current_pos = 0
    board_heatmap = [0] * 40
    ch_card = [7, 22, 36]
    cc_card = [2, 17, 33]
    ch_counter = 0
    cc_counter = 0
    doubles = 0

    n = 10000000
    for i in range(n):
        ch_counter = ch_counter % 16
        cc_counter = cc_counter % 16
        dices = np.random.randint(low=1, high=5, size=2)
        current_pos += dices.sum()
        current_pos = current_pos % 40

        if dices[0] == dices[1]:
            doubles += 1
        else:
            doubles = 0

        if doubles == 3:
            current_pos = 10
            doubles = 0
        elif current_pos == 30:
            current_pos = 10
        elif current_pos in cc_card:
            current_pos = draw_cc(current_pos, cc_counter)
            cc_counter += 1
        elif current_pos in ch_card:
            current_pos = draw_ch(current_pos, ch_counter)
            ch_counter += 1

        board_heatmap[current_pos] += 1

    for i in range(len(board_heatmap)):
        board_heatmap[i] /= n

    indices = sorted(range(len(board_heatmap)), key=lambda i: board_heatmap[i], reverse=True)[:3]

    answer = ''
    for i in indices:
        if i == 0:
            answer += '00'
        else:
            answer += str(i)
    return answer

print(main())