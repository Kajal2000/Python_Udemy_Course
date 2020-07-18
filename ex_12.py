def get_hand_value(*args):
    pass
    a = sum(args)
    if a <= 21:
        return a
# While testing the execution of your program, I will use the hands below:
# hand_1 = get_hand_value(4,4,4,4)
# hand_2 = get_hand_value(11,10)
# hand_3 = get_hand_value(11,5,6,4,11,4)
# hand_4 = get_hand_value(11,5,6,10)
# hand_5 = get_hand_value(10,5,7)
# hand_6 = get_hand_value(5,6,5,10)
# hand_7 = get_hand_value(10,11)
# hand_8 = get_hand_value(11,11,11,11,10,10)
hand_9 = get_hand_value(5,6,5,5)
print(get_hand_value(hand_9))