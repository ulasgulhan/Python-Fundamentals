from random import choice, randint

bots = ['ahmet', 'mehmet', 'ayşe']
users_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123',
        'safe': 1200
    },
    '2': {
            'user_name': 'savage',
            'password': '123',
            'safe': 2200
        },
}

minimum_bet = 100


def assing_default_bot(bot_list: list) -> str:
    return choice(bot_list)


def roll_dice() -> int:
    return randint(2, 12)


def bet_is_valid(currnet_bet: int, safe: int) -> bool:
    if minimum_bet <= currnet_bet <= safe:
        return True
    else:
        return False


def gain_daily_chips() -> int:
    return randint(1000, 2000)


def login(user_name: str, password: str) -> dict:
    test = False
    user_id = ''
    for id in users_dict:
        if users_dict[str(id)]['user_name'] == user_name and users_dict[str(id)]['password'] == password:
            test = True
            user_id = str(id)
            break

    if test:
        return users_dict[user_id]
    else:
        return {}


def main():
    auth_user = login(
        input('User Name: '),
        input('Password: ')
    )

    if auth_user != {}:
        daily_chips = gain_daily_chips()
        auth_user.update({'safe': auth_user['safe'] + daily_chips})

        print(f"Welcome {auth_user['user_name']}, you gain {daily_chips} and so your safe is {auth_user['safe']}")

        while True:
            if auth_user['safe'] >= minimum_bet:
                bet = int(input('Please make a bet: '))
                if bet_is_valid(bet, auth_user['safe']):
                    player_2 = assing_default_bot(bots)

                    player_1_roll = roll_dice()
                    player_2_roll = roll_dice()

                    if player_1_roll > player_2_roll:
                        print(f'Your dicle is {player_1_roll}\n{player_2} dicle is {player_2_roll}')
                        auth_user.update({'safe': auth_user['safe'] + (bet * 2)})
                        print(f"Congratulations {auth_user['user_name']}, your current safe is {auth_user['safe']}")
                    elif player_2_roll > player_1_roll:
                        print(f'Your dicle is {player_1_roll}\n{player_2} dicle is {player_2_roll}')
                        auth_user.update({'safe': auth_user['safe'] - bet})
                        print(f"{auth_user['user_name']} aren't victor..! Your current safe is {auth_user['safe']}")
                    else:
                        print(f'Your dicle is {player_1_roll}\n{player_2} dicle is {player_2_roll}')
                        print('Player tie..!')

                else:
                    print('Please gibe a valid bet...')
            else:
                print('Your safe is under the minimum bet!\nDo you want to buy chios?')
                break
    else:
        print('Invalid information')


main()