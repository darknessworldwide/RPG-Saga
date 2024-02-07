from structures.rpg_saga import RPGSaga

while True:
    try:
        num_players = int(input("Введите количество игроков (от 2 до 4): "))
        if 2 <= num_players <= 4:
            break
        else:
            print("Пожалуйста, введите число от 2 до 4.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

game = RPGSaga(num_players)
game.start_game()