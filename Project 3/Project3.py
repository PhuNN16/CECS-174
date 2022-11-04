#displaying stock list
def Stock_list(num_n, num_d, num_q, num_o, num_f):
  print()
  print(f'Stock contains:\n{num_n:^6} nickels\n{num_d:^6} dimes\n{num_q:^6} quarters\n{num_o:^6} ones\n{num_f:^6} fives')
  print()

#displaying menu
def display_menu():
  print()
  print('Menu for deposit:')
  print("  'n' - deposit a nickel")
  print("  'd' - deposit a dime")
  print("  'q' - deposit a quarter")
  print("  'o' - deposit a one dollar bill")
  print("  'f' - deposit a five dollar bill")
  print("  'c' - cancel the purchase")
  print()

#computing how much one dollar is in the total cents
def get_ones_from_total_cents(tot_cents):
  return int(tot_cents // 100)

#computing the left over cents
def get_leftover_cents_from_total_cents(tot_cents):
  return int(tot_cents % 100)

#Finding the amount of change in cents to give back to user
def get_change_in_cents(given_money, money_owed):
  if given_money > money_owed:
    change_in_cents = given_money - money_owed
  elif given_money == money_owed:
    change_in_cents = 0
  else:
    change_in_cents = given_money
  return change_in_cents

#find least amount of coins needed to be given
def convert_to_min_coin(total_cent_change, quarters_available, dimes_available, nickels_available):
  given_quarters = 0
  given_dimes = 0
  given_nickels = 0
  leftover_ones = 0
  leftover_cents = 0
  while total_cent_change >= 25 and quarters_available > 0:
    total_cent_change -= 25
    given_quarters += 1
    quarters_available -= 1 #this is to know when we run out of coins
  while total_cent_change >= 10 and dimes_available > 0:
    total_cent_change -= 10
    given_dimes += 1
    dimes_available -= 1
  while total_cent_change >= 5 and nickels_available > 0:
    total_cent_change -= 5
    given_nickels += 1
    nickels_available -= 1
  if quarters_available == 0 and dimes_available == 0 and nickels_available == 0:
    leftover_ones = int(total_cent_change // 100)
    leftover_cents = int(total_cent_change % 100)
  return given_quarters, given_dimes, given_nickels, leftover_ones, leftover_cents

#displaying all the coins given back to user
def display_coins(dq_change, dd_change, dn_change):
  print() #space between statements
  print('Please take the change below.') 
  if dq_change != 0:
    print(f'   {dq_change} quarters')
  if dd_change != 0:
    print(f'   {dd_change} dimes')
  if dn_change != 0:
    print(f'   {dn_change} nickels') 
  if dq_change == 0 and dd_change == 0 and dn_change == 0:
    print('  No change due.')


#message for when we run out of change
def empty_machine_msg(leftover_one, leftover_cent):
  print('Machine out of change.')
  print('See store manager for remaining refund.')
  print('Amount due: ', end='')
  if leftover_one != 0:
    print(f'{leftover_one} dollars ', end='')
  print(f'{leftover_cent} cents')

#display the total amount of money left in the machine after user quit program
def display_total(num_n, num_d, num_q, num_o, num_f):
  total_cents_stock = (5*num_n) + (10*num_d) + (25*num_q) + (100*num_o) + (500*num_f)
  dollars_total = get_ones_from_total_cents(total_cents_stock)
  cents_total = get_leftover_cents_from_total_cents(total_cents_stock)
  print() # create emppty space
  print(f'Total: {dollars_total} dollars and {cents_total} cents')
  
#main program
n_stock = 25
d_stock = 25
q_stock = 25
o_stock = 0
f_stock = 0
print('Welcome to the vending machine change maker program\nChange maker initialized.', end='')
Stock_list(n_stock, d_stock, q_stock, o_stock, f_stock)
p_price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
while p_price != 'q' and p_price != 'Q':
  round_pprice = float(p_price) * 100 #multiply by 100 to reduce float point usage
  if (round_pprice % 5 != 0) or (round_pprice < 0): #checking conditions for price
    print('Illegal price: Must be non-negative multiple of 5 cents.')
    print()
    p_price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
  else:
    display_menu()
    deposit_amount = 0
    total_cents_owed = round_pprice #variable made to keep track of payment due
    while total_cents_owed > 0: #also used as a countdown for while loop
      print(f'Payment due: {get_ones_from_total_cents(total_cents_owed)} dollar(s) and {get_leftover_cents_from_total_cents(total_cents_owed)} cents')
      deposit = input('Indicate your deposit: ')
      if (deposit == 'n') or (deposit == 'N'):
        total_cents_owed = total_cents_owed - 5
        deposit_amount += 5 #keep track to find change
        n_stock += 1
      elif (deposit == 'd') or (deposit == 'D'):
        total_cents_owed = total_cents_owed - 10
        deposit_amount += 10
        d_stock += 1
      elif (deposit == 'q') or (deposit == 'Q'):
        total_cents_owed = total_cents_owed - 25
        deposit_amount += 25
        q_stock += 1
      elif (deposit == 'o') or (deposit == 'O'):
        total_cents_owed = total_cents_owed - 100
        deposit_amount += 100
        o_stock += 1
      elif (deposit == 'f') or (deposit == 'F'):
        total_cents_owed = total_cents_owed - 500
        deposit_amount += 500
        f_stock += 1
      elif (deposit == 'c') or (deposit == 'C'):
        break
      else:
        print(f'Illegal selection: {deposit}') #for cases of bad inputs
        
    #calculating change to give
    change = get_change_in_cents(deposit_amount, round_pprice)
    min_coin_change = convert_to_min_coin(change, q_stock, d_stock, n_stock)
    quarter_change = min_coin_change[0] #used tuples to store multiple values in 1 function
    dimes_change = min_coin_change[1]
    nickels_change = min_coin_change[2]
    display_coins(quarter_change, dimes_change, nickels_change)
    
    #Update stock
    q_stock -= min_coin_change[0]
    d_stock -= min_coin_change[1]
    n_stock -= min_coin_change[2]
    if (q_stock == 0) and (d_stock == 0) and (n_stock == 0):
      one_due = min_coin_change[3]
      cent_due = min_coin_change [4]
      empty_machine_msg(one_due, cent_due)
    
      #Re-display stock and ask for new user input for the next loop iteration
    Stock_list(n_stock, d_stock, q_stock, o_stock, f_stock)
    p_price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')

display_total(n_stock, d_stock, q_stock, o_stock, f_stock)