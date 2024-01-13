from collections import defaultdict

def readInputFile():
    filename = 'p054_poker.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()
        data_list = [[line.strip().split(" ")[0:5], line.strip().split(" ")[5:10]] for line in lines]
    return data_list

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return True
    else:
        return False

def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else:
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False

def high_card_value(hand):
    values = sorted([i[0] for i in hand])[::-1]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1

    poker_dict = dict(value_counts)
    value = list(poker_dict.keys())[list(poker_dict.values()).index(1)]
    L = []
    for i in values:
        L.append(card_order_dict[i])
    return max(L)

def pair_value(hand):
    values = sorted([i[0] for i in hand])[::-1]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1

    poker_dict = dict(value_counts)
    value = list(poker_dict.keys())[list(poker_dict.values()).index(2)]
    high_card = list(poker_dict.keys())[list(poker_dict.values()).index(1)]

    #print(card_order_dict[value], high_card)
    return [card_order_dict[value], card_order_dict[high_card]]

def two_pair_value(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1

    poker_dict = dict(value_counts)
    #value = list(poker_dict.keys())[list(poker_dict.values()).index(2)]
    two_pair_values = [i for i, j in poker_dict.items() if j == 2]
    print(two_pair_values)
    return [card_order_dict[two_pair_values[0]], card_order_dict[two_pair_values[1]]]

def check_hand(hand):
    if check_straight_flush(hand):
        return 10
    if check_four_of_a_kind(hand):
        return 9
    if check_straight_flush(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pairs(hand):
        return 3
    if check_one_pairs(hand):
        return 2
    return 1

def main():
    S = 0
    N = 0
    hands = readInputFile()
    
    for i in range(len(hands)):
        hand1 = check_hand(hands[i][0])
        hand2 = check_hand(hands[i][1])
        if hand1 > hand2:
            S += 1
        elif hand1 == hand2:
            if hand1 == 1:
                if high_card_value(hands[i][0]) > high_card_value(hands[i][1]):
                    S += 1
                else:
                    N += 1
            elif hand1 == 2:
                pair_values1 = pair_value(hands[i][0])
                pair_values2 = pair_value(hands[i][1])
                if pair_values1[0] > pair_values2[0]:
                    S += 1
                elif pair_values1[0] == pair_values2[0] and pair_values1[1] > pair_values2[1]:
                    S += 1
                else:
                    N += 1
            else:
                print("TIE yolo")
        else:
            N += 1

    return S, N

print(main())