from player import Player


player = Player(1,2)
player.print()
# p = {}
# p["x"] = 2
# p["y"] = 3
# boxes = []
# boxes.append({"x":7, "y":4})
# boxes.append({"x":9, "y":3})
# boxes.append({"x":2, "y":5})
#
# gates = []
# gates.append({"x" : 5, "y" :7})
# gates.append({"x" : 4, "y" :5})
# gates.append({"x" : 1, "y" :5})
#
#
# screen_width = 12
# screen_height = 12
#
#
# def in_map(x, y, screen_width, screen_height):
#     if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
#         return False
#     return True
#
# def move(x, y, dx, dy):
#     return [x + dx, y + dy]
#
# def match(objects, x, y):
#     for object in objects:
#         if object["x"] ==x and object ["y"]== y:
#             return True
#     return False
#
# def find_object(objects, x, y):
#     for object in objects:
#         if object["x"] == x and object["y"] == y:
#             return object
#     return None
#
# def check_win(boxes, gates):
#     for i in range(len(boxes)):
#         if (boxes[i]["x"] != gates[i]["x"]) or (boxes[i]["y"] != gates[i]["y"]):
#             return False
#     return True
#
# def print_map(p, boxes, gates, screen_width, screen_height):
#     for y in range(screen_height):
#         for x in range(screen_width):
#             if x == p["x"] and y == p["y"]:
#                 print("P ", end="")
#             elif match(boxes, x, y):
#                 print("B ", end="")
#             elif match(gates, x, y):
#                 print("G " , end ="")
#             else:
#                 print("- ", end="")
#         print()
# while True:
#     print_map(p, boxes, gates, screen_width, screen_height)
#
#     choice = input("What do you want? U - D - L - R: ").upper()
#
#     dx = 0
#     dy = 0
#
#     if choice == "W":
#         dy = -1
#     elif choice == "S":
#         dy = 1
#     elif choice == "A":
#         dx = -1
#     elif choice == "D":
#         dx = 1
#
#     [next_px, next_py] = move(p["x"], p["y"], dx, dy)
#
#     if not in_map(next_px, next_py, screen_width, screen_height):
#         print("Go away!!!")
#     else:
#         found_box = find_object(boxes, next_px, next_py)
#         if found_box is not None:
#
#             next_box_x, next_box_y = move(found_box["x"], found_box["y"], dx, dy)
#             if in_map(next_box_x, next_box_y, screen_width, screen_height) and find_object(boxes, next_box_x, next_box_y) is None:
#                 found_box["x"], found_box["y"] = next_box_x, next_box_y
#             p["x"], p["y"] = next_px, next_py
#         else:
#             p["x"], p["y"] = next_px, next_py
#     # else:
#     #
#     #     if next_px == bx and next_py == by:
#     #         [next_bx, next_by] = move(bx, by,dx, dy)
#     #         if in_map(next_bx, next_by, screen_width, screen_height):
#     #             bx, by = next_bx, next_by
#     #             p["x"], p["y"] = next_px, next_py
#     #
#     #     else:
#     #         p["x"], p["y"] = next_px, next_py
#     # if check_win(gx, gy, bx, by):
#     #     print("you win!")
#
#     if check_win(boxes, gates):
#         print ("You win!")