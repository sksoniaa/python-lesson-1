

person = {
  'name': 'Elizabeth',
  'age': 31,
  'is_hungry': True
}

print(person.items(), '<----- person.items()')
for key, val in person.items():
  print(f'This {val} is kept in {key}')

# for key in person:
#   print(f'{key} == {person[key]}')


# print(person)
# print(type(person))


# print(person['name'])

# print ('changing name .....')

# person['name'] = 'Liz'

# print('the name is changed to')
# print(person['name'])

# person['age'] = 19
# person['name'] = 'Sofiia'

# print(person)
# print(person['name'])
# print(person['age'])


# print(person.get('favorite_quote','fave'))
# print(person)
# print('===============================================')
# print('========After adding a quote ============')
# person['favourite_quote'] = 'rsthgysgfdhshg'
# print(person, '  < person')

# print(person)


# where_my_things_are = {
#   'bedroom': 'clothes',
#   'livingroom': 'speaker',
#   'kitchen': 'food',
#   'bathroom': 'lipstick'
# }

# for location, thing in where_my_things_are.items():
#   print(f'This {thing} is kept in {location}')


  ######################### LISTS ############################


# colors = ['red', 'yellow', 'green']

# colors.extend(['pink', 'purple'])
# print(colors)

# print(dir(colors))

# print(enumerate(colors))
# for idx, color in enumerate(colors):
#   print(idx, color)

# print(colors)
# print(type(colors))
# print(len(colors))

# print([] == [])


# scores = [
#   {
#     'name': 'name of the player',
#     'points': 25  # points the player scored
#   }
# ]

# scores.append(
#   {'name': 'She', 'points': 30}
# )

# for player in scores:
#   print(f"{player.get('name')} scored {player.get('points')} points")


#   nums = [1,2,3,4,5,6,7,8,9]

#   squares = [x * x for x in nums]

#   print(squares)

#   even_squares = [n * n for n in nums if(n * n) % 2 == 0]
#   print(even_squares , ' <---- even sqaures')



# airports = ('ohare', 'cdmx', 'mdw', 'atl')
# print(airports)
# print(type(airports))
# airports[0] = 'whatever' # error, as we can't change tuples ('...','...','...')
# print(airports)

colors = ('red', 'green', 'blue')
print(colors[:2])

sliced_colors = colors[:2]
print(colors)
# r, g, b = colors
# print(r, g, b)
# r = 'dark red'
# print(r)
# print(colors)

fruit = {
  'apples': 'red',
  'bananas': 'yellow',
  'oranges': 'orange'
}

color_of_bananas = fruit['bananas']
print(color_of_bananas)

# immutable - Can’t change
# mutable - Can Change