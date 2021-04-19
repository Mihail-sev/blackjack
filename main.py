############### Blackjack Project #####################
from random import randint

#Валет, дама и король - 10, туз - 11
cards = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#функция выбора случайной карты из колоды. Колода не уменьшается.
def  take_cards():
  """ Выбирает карту из колоды"""
  return cards[randint (0, len(cards)-1)]

# функция игры
def play_jack_black(bank, bet):
  cards_of_player = []
  sum_player_cards = 0
  cards_of_comp = []
  sum_comp_cards = 0

  # Первоначальная раздача по две карты
  for i in range (2):
    cards_of_player += [take_cards()]
    cards_of_comp += [take_cards()]
    sum_player_cards += cards_of_player[i]
    sum_comp_cards += cards_of_comp[i]
  print(f"Ваши карты: {cards_of_player}. Ваша сумма = {sum_player_cards}\n Первая карты компьютера [{cards_of_comp[0]}]")  

  add_card = True
  in_game = True
  add_card_comp = True
  in_game_comp = True

  #Добор карт игроком
  while add_card and in_game:
    take_card = input("""
    Хотите взять еще одну карту?\n
    Если да - напишите 'y', если нет - 'n'
    """).lower()
    #отсечка неверного ввода
    if take_card != "y" and take_card != "n":
      print (" Вы сделали недопустимый выбор. Повторите.")
    # добавление карты и оценка
    elif take_card == "y":
      cards_of_player += [take_cards()]
      sum_player_cards += cards_of_player[len(cards_of_player)-1]
      print(f"Ваши карты: {cards_of_player}. Ваша сумма = {sum_player_cards}")
      if sum_player_cards > 21:
        in_game = False
        in_game_comp = False
        print ("У Вас перебор. Вы проиграли.")
        bank = bank - bet
        return  bank 
    # конец добора игроком
    else:
      add_card = False
      print(f"Итак, ваши карты: {cards_of_player}. Ваша финальная сумма = {sum_player_cards}. Очередь  дилера.")
  # Добор карт компьютером
  while add_card_comp and in_game_comp:
    if sum_player_cards > sum_comp_cards:
      cards_of_comp += [take_cards()]
      sum_comp_cards += cards_of_comp[len(cards_of_comp)-1]
      if sum_comp_cards > 21:
        in_game_comp = False
        print (f"Карты дилера: {cards_of_comp}. Сумма дилера= {sum_comp_cards}. У дилера перебор.\n  Вы выиграли!.")
        bank = bank + bet
        return  bank 
  #Конец добора компьютером
    else:
      add_card_comp = False
      print(f"Итак, карты дилера: {cards_of_comp}. Сумма дилера= {sum_comp_cards}")
      if sum_player_cards < sum_comp_cards:
        print(f"Так как у Вас всего {sum_player_cards}, то вы проиграли")
        bank = bank - bet
        return  bank 
      else:
        print ("У нас ничья")
        bank = bank
        return  bank 

print (f"Добро пожаловать в BlackJack! Не проиграйте все ':)'")
player_bank = float (input ("Какую сумму хотите внести в банк? Введите число\n"))
begin_bank = player_bank
print (f"У Вас на счету ${player_bank}. Начинаем!")
play_again = "y"
while play_again == "y":
  player_bet = float(input(f"Сколько Вы хотите поставить на раздаче ? Введите число\n"))
  # отсечка ставки больще банка
  while player_bet> player_bank:
    player_bet = float(input("Э нет, так нельзя? Введите число меньше Вашего счета\n"))
  # раздача и обновление банка игрока
  player_bank = play_jack_black(player_bank, player_bet)
  #продолжение игры
  if player_bank == 0:
      play_again = "n"
  else:
    play_again = input (f"У Вас на счету ${player_bank}. Хотите продолжить? Если да - напишите 'y', если нет - 'n'\n").lower()
      #отсечка неверного ввода продолжения
    while play_again != "y" and play_again != "n":
      play_again = input (" Вы сделали недопустимый выбор. Повторите.Если да - напишите 'y', если нет - 'n'\n").lower()
  
if player_bank == 0:
  print (f"Вы проиграли все {begin_bank}. Как разживетесь деньгами, будем рады снова Вас видеть в нашем казино")
elif begin_bank > player_bank:
  print (f"К выплате ${player_bank}. Вы проиграли {begin_bank- player_bank}. Будем рады снова Вас видеть в нашем казино")
elif begin_bank < player_bank:
  print (f"К выплате ${player_bank}. Вы выиграли {player_bank - begin_bank}. Здесь за углом есть другое хорошее казино")
else:
  print(f"К выплате ${player_bank}. Вы впустую потратили свое и главное наше время")