# def create_first_round():
#     round = []
#     y = 0
#     level = 1
#     while level is not 4:
#         if level // 2:
#             list_of_x = list(range(60, 600, 120))
#             for x in list_of_x:
#                 new_block_pos = (x, y)
#                 round.append(new_block_pos)
#             y += 20
#             level += 1
#         else:
#             list_of_x = list(range(0, 600, 120))
#             for x in list_of_x:
#                 new_block_pos = (x, y)
#                 round.append(new_block_pos)
#             y += 20
#             level += 1
#     return round
#
# def create_second_round():
#     round = []
#     y = 0
#     level = 1
#     while level is not 6:
#         if level // 2:
#             list_of_x = list(range(60, 600, 120))
#             for x in list_of_x:
#                 new_block_pos = (x, y)
#                 round.append(new_block_pos)
#             y += 20
#             level += 1
#         else:
#             list_of_x = list(range(0, 600, 120))
#             for x in list_of_x:
#                 new_block_pos = (x, y)
#                 round.append(new_block_pos)
#             y += 20
#             level += 1
#     return round
#
#
# def create_third_round():
#     round = []
#     y = 0
#     level = 1
#     while level is not 6:
#         list_of_x = list(range(0, 600, 60))
#         for x in list_of_x:
#             new_block_pos = (x, y)
#             round.append(new_block_pos)
#         y += 20
#         level += 1
#     return round
#
# print(create_first_round())
# print()
# print(create_second_round())
# print()
# print(create_third_round())

if 5 % 2 == 0:
    print(True)
else:
    print(False)