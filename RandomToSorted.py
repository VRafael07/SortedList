from random import shuffle

bills = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
new_Bills = []
new_Coins = []
shuffle(bills)  # Scramble bills list
shuffle(coins)  # Scramble coins list

while bills and coins:  # Create a new sorted list of bills and coins from a scrambled one
    highest_bills = bills.index(max(bills))  # Get the index of the maximum value of each list
    highest_coins = coins.index(max(coins))
    new_Bills.append(bills.pop(highest_bills))  # Remove the highest value from each original list
    new_Coins.append(coins.pop(highest_coins))

answer = 'Y'
while answer == 'Y':
    money = float(input("Money: $"))
    if 0 <= money <= 1000000.00:
        print("BILLS:")
        for i in new_Bills:
            quantity = money // i
            print(f"{quantity:.0f} bill(s) of ${i:.2f}")
            money = round(money - quantity * i)
        print("=" * 20)
        print("COINS:")
        for i in new_Coins:
            quantity = money // i
            print(f"{quantity:.0f} coin(s) of ${i:.2f}")
            money -= quantity * i

        answer = str(input("Continue: [Y/n] ")).upper()
