import requests
import json
import time
from termcolor import colored
import os
previous_balance = None

key = 'YOUR_API_KEY'
profile_id = 'YOUR_PROFILE_ID'
uuid = 'YOUR UUID'
previous_balance = None
url = f'https://api.hypixel.net/skyblock/profile?key={key}&profile={profile_id}'

while True:    
    try:
        #переменные
        r = requests.get(url).json()
        coin_purse = round(r['profile']['members'][uuid]['coin_purse'], 0)
        rounded_number = int(coin_purse)
        million_purse = float(str(coin_purse/1000000))

        #текущее кол-во монет доступных для продаж
        coins_for_sell = million_purse - 4 #   23000000 -> 23 -> 23-4 -> 19
        #выполняем цикл, если текущий баланс больше 1М
        if coin_purse >= 1000000:     
            print(f'Curret purse on account: {colored(rounded_number, "cyan")}')
            if coins_for_sell < 1: #если текущий баланс для продаж меньше 1, то мы запишем 1 в лот
                print(colored('Not enough coins for sell!', 'red'), f'({int(coins_for_sell)}M)')
                with open('data.txt', 'w') as f:
                    f.write('1')

            if previous_balance is None:
                previous_balance = coins_for_sell*1# if purse -4 -> *1 -> 4

            elif previous_balance != coins_for_sell*1:
                print(colored("Balance has changed!", 'yellow'), f'(~{int(coins_for_sell)}M)')

            elif previous_balance == coins_for_sell * 1:
                print(colored('Balance has not changed', 'red'), f'(~{int(coins_for_sell)}M)')


        else:
            print(colored('Balance < 1M!', 'red'), f'({coin_purse} coins)')

        #os.system('cls')
        if coins_for_sell >= 1:
            with open('data.txt', 'w') as f:
                f.write(str(int(coins_for_sell)))
        else:
            with open('data.txt', 'w') as f:
                f.write(str(1))
        previous_balance = coins_for_sell    
        print(colored(f'Coins for sell: ~{int(coins_for_sell)}M', 'blue'))
        time.sleep(10)
        os.system('cls')


        
    except Exception as e:
        for i in range(4):
            print(colored(e, 'red'))
        time.sleep(5)
        os.system('cls')

    os.system('cls')