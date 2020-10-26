# from tkinter import *
# def callback(r,c):
#     global player
#     if player == 'X' and states[r][c] == 0 and states2[r][c]==0:
#         b[r][c].configure(text='X', fg='blue', bg='white')
#         states[r][c] = 'X'
#         player = 'O'
#
#
#     if player == 'O' and states[r][c] == 0 and states2[r][c]==0 :
#         b[r][c].configure(text='O', fg='orange', bg='black')
#         states[r][c] ='O'
#         player = 'X'
#
#     check_for_winner()
#    # Stop_game_after_win()
#
#
# def check_for_winner():
#     global stop_game
#
#     for i in range(3):
#         if states[i][0] == states[i][1] == states[i][2] != 0:
#             b[i][0].configure(bg='grey')
#             b[i][1].configure(bg='grey')
#             b[i][2].configure(bg='grey')
#             stop_game = True
#
#
#         for i in range(3):
#             if states[0][i] == states[1][i] == states[2][i] != 0:
#                 b[0][i].configure(bg='grey')
#                 b[1][i].configure(bg='grey')
#                 b[2][i].configure(bg='grey')
#                 stop_game = True
#
#         if states[0][0] == states[1][1] == states[2][2] != 0:
#             b[0][0].configure(bg='grey')
#             b[1][1].configure(bg='grey')
#             b[2][2].configure(bg='grey')
#             stop_game = True
#
#         if states[2][0] == states[1][1] == states[0][2] != 0:
#             b[2][0].configure(bg='grey')
#             b[1][1].configure(bg='grey')
#             b[0][2].configure(bg='grey')
#             stop_game = True
#
#
#
#
# def Stop_game_after_win():
#     global end_game
#     for i in range(3):
#         if states2[i][0] == states2[i][1] == states2[i][2] == 0  :
#             b[i][0].configure(bg='red')
#             b[i][1].configure(bg='red')
#             b[i][2].configure(bg='red')
#             end_game= True
#
#
#         # for i in range(3):
#         #     if states2[0][i] == states2[1][i] == states2[2][i] == 0   :
#         #         b[0][i].configure(bg='red')
#         #         b[1][i].configure(bg='red')
#         #         b[2][i].configure(bg='red')
#         #
#         #
#         # if states2[0][0] == states2[1][1] == states2[2][2] == 0  :
#         #     b[0][0].configure(bg='red')
#         #     b[1][1].configure(bg='red')
#         #     b[2][2].configure(bg='red')
#         #
#         #
#         # if states2[2][0] == states2[1][1] == states2[0][2] == 0   :
#         #     b[2][0].configure(bg='red')
#         #     b[1][1].configure(bg='red')
#         #     b[0][2].configure(bg='red')
#
#
#
#
#
# root = Tk()
# root.title('TIC-TAC-TOE GAME')
#
# #The states is created to help check if the cell already has either  X or O so that the user cannot change it..
# states= [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
#
# states2= [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
#
# #Here we're creating 3 x 3 matrix for the board.....
# b = [[0,0,0],
#      [0,0,0],
#      [0,0,0]]
#
#
#
# for i in range(3):
#     for j in range(3):
#         b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',
#         command = lambda r=i,c=j: callback(r,c))
#         b[i][j].grid(row = i, column = j)
# player = 'X' #Starting player
# stop_game = False
# end_game=False
# mainloop()





from tkinter import *
def callback1(event):
    print('You pressed the enter key.')
def callback2(event):
    print('You pressed the up arrow.')
root = Tk()
root.bind('<Return>', callback1)
root.bind('<Up>', callback2)
mainloop()

