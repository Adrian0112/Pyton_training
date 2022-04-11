
summ_all = 0

while True:
    name = input('Enter product name: ')
    quantity = int(input('Specify quantity: '))
    prize = float(input('Give the prices of product: '))
    # numbers after decimals

    prize_tag = prize * quantity
    summ_all += prize_tag  # the same as summ_all + prize_tag
    print(f'Produkt {name} kosztowal: {prize_tag}')  # show price on screen
    answer_loop = input('You want to end? [Y/N]')  # ending loop
    if answer_loop == 'Y' or answer_loop == 'y':  # ending loop
        break

print(f'Summary of your purchases is {summ_all}')