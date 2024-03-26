color = ''
while color != 'quit':
  color = input('enter "green", "yellow", "red"').lower()
  print(f'The user entered {color}')
  
  if color == "green":
    print(f'{color} - go')
  elif color == "yellow":
    print(f'{color} - wait')
  elif color == 'red':
    print(f'{color} - stop')
  else:
    print('bogus')
