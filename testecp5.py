grocery_shopping = {'Item': ['Wine', 'Bacon', 'Soda', 'Biscuit', 'Chocolate'],
                    'Price': ['66.90', '23.90', '11.90', '3.32', '5.40'],
                    'Stock': [10, 20, 35, 80, 20],
                    'Brand': ['Vignarosa', 'Sadia', 'Coca Cola', 'Trakinas', 'Diamante Negro'],
}

cart = {'Name': '',
        'Addres': '',
        'Products': {}
       }

index = {grocery_shopping['Item'][i]: i for i in range(len(grocery_shopping['Item']))}

def force_option(msg, option_in_list, error_msg = 'Invalid'):
    options = '\n'.join(option_in_list)
    option = input(f'{msg}\n{options}\n->')
    while option not in option_in_list:
        print(error_msg)
        option = input(f'{msg}\n{options}\n->')
    return option

def number_check(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('Gotta choose a number')
            
def buy():
    value = 0
    while True:
        product = force_option('Which product would u like to buy? ', grocery_shopping['Item'] )
        product_index = index[product]
        for key in grocery_shopping.keys():
            print(f'{key} : {grocery_shopping[key][product_index]}')
        quantity = number_check(f'How many {product} would u like?\n->')
        if quantity > grocery_shopping['Stock'][product_index]:
            print(f'We only have {grocery_shopping['Stock'][product_index]} {product}')
            continue
        else:
            grocery_shopping['Stock'][product_index] -= quantity
            if product not in cart['Products']:
                cart['Products'][product] = quantity
            else:
                cart['Products'][product] += quantity
        price = float(grocery_shopping['Price'][product_index])
        value += price * quantity
        Continue = force_option(f'{name} would you like to buy any more products? ', ['yes', 'no'])
        if Continue == 'no':
            break
    return value

print('Welcome to our Grocery Shopping')
name = input('Hello customer, what is your name? ')
addres = input('What is your addres? ')
cart['Name'] = name
cart['Addres'] = addres

value = buy()

if value >= 200:
    discount = value * 0.10
    value -= discount
    print(f'{name}, thanks for shopping with us! You bought {cart['Products']} and the value was: ${value} with the 10% discount')
else:
    print(f'{name}, thanks for shopping with us! You bought {cart['Products']} and the value was: ${value}')
