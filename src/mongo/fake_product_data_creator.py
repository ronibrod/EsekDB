import random

categories_data = [
  {
    'name': 'Coffee',
    'hebrewNeme': 'קפה',
    'basePrice': 10,
    'types': [
      {
        'name': 'Espresso',
        'hebrewNeme': 'אספרסו',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
      {
        'name': 'Cappuccino',
        'hebrewNeme': 'קפוצינו',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'milk',
            'quantity': 0.1,
          },
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
      {
        'name': 'Latte',
        'hebrewNeme': 'לאטה',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'milk',
            'quantity': 0.1,
          },
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
      {
        'name': 'Americano',
        'hebrewNeme': 'אמריקנו',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'milk',
            'quantity': 0.1,
          },
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
      {
        'name': 'Macchiato',
        'hebrewNeme': 'מקיאטו',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'milk',
            'quantity': 0.1,
          },
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
      {
        'name': 'Mocha',
        'hebrewNeme': 'מוקה',
        'preparationTime': 1,
        'ingredients': [
          {
            'name': 'milk',
            'quantity': 0.1,
          },
          {
            'name': 'coffeeBeans',
            'quantity': 0.01,
          },
        ],
        'uses': [
          {
            'equipment': 'coffeeMachine',
            'useTime': 0.5,
            'canUseInSameTime': 4,
          },
        ],
      },
    ],
  },
  {
    'name': 'Ice_Cream',
    'hebrewNeme': 'גלידה',
    'basePrice': 18,
    'types': [
      {
        'name': 'Vanilla',
        'hebrewNeme': 'וניל',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Chocolate',
        'hebrewNeme': 'שוקולד',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Strawberry',
        'hebrewNeme': 'תות',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Cookie_Dough',
        'hebrewNeme': 'בצק עוגיות',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Mint_Chocolate_Chip',
        'hebrewNeme': 'שוקולד ציפס ומנטה',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Cookies_and_Cream',
        'hebrewNeme': 'קצפת עוגיות',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Pistachio',
        'hebrewNeme': 'פיסטוק',
        'preparationTime': 2,
        'ingredients': [
          {
            'name': 'iceCream',
            'quantity': 0.12,
          },
        ],
        'uses': [],
      },
    ],
  },
  {
    'name': 'Cans',
    'hebrewNeme': 'פחיות',
    'basePrice': 7,
    'types': [
      {
        'name': 'Coca_Cola',
        'hebrewNeme': 'קוקה קולה',
        'preparationTime': 0,
        'ingredients': [
          {
            'name': 'can',
            'quantity': 1,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Coca_Cola_Zero',
        'hebrewNeme': 'קוקה קולה זירו',
        'preparationTime': 0,
        'ingredients': [
          {
            'name': 'can',
            'quantity': 1,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Fanta',
        'hebrewNeme': 'פנטה',
        'preparationTime': 0,
        'ingredients': [
          {
            'name': 'can',
            'quantity': 1,
          },
        ],
        'uses': [],
      },
      {
        'name': 'Sprite',
        'hebrewNeme': 'ספרייט',
        'preparationTime': 0,
        'ingredients': [
          {
            'name': 'can',
            'quantity': 1,
          },
        ],
        'uses': [],
      },
      {
        'name': '7UP',
        'hebrewNeme': '7 אפ',
        'preparationTime': 0,
        'ingredients': [
          {
            'name': 'can',
            'quantity': 1,
          },
        ],
        'uses': [],
      },
    ],
  },
  {
    'name': 'Beer',
    'hebrewNeme': 'בירה',
    'basePrice': 28,
    'types': [
      {
        'name': 'Heineken',
        'hebrewNeme': 'הייניקן',
        'preparationTime': 0.5,
        'ingredients': [
          {
            'name': 'heineken',
            'quantity': 0.1,
          },
        ],
        'uses': [
          {
            'equipment': 'beerTap',
            'useTime': 0.5,
            'canUseInSameTime': 1,
          },
        ],
      },
      {
        'name': 'Carlsberg',
        'hebrewNeme': 'קרלסברג',
        'preparationTime': 0.5,
        'ingredients': [
          {
            'name': 'carlsberg',
            'quantity': 0.1,
          },
        ],
        'uses': [
          {
            'equipment': 'beerTap',
            'useTime': 0.5,
            'canUseInSameTime': 1,
          },
        ],
      },
      {
        'name': 'Corona',
        'hebrewNeme': 'קורונה',
        'preparationTime': 0.5,
        'ingredients': [
          {
            'name': 'corona',
            'quantity': 0.083,
          },
        ],
        'uses': [
          {
            'equipment': 'beerTap',
            'useTime': 0.5,
            'canUseInSameTime': 1,
          },
        ],
      },
    ],
  },
]

def create_products_array():
  products_array = []

  for category in categories_data:    
    for product in category['types']:
      random_number_add_to_price = random.randint(0, round(category['basePrice'] * 0.3))
      random_number_sub_for_cost = random.randint(round(category['basePrice'] * 0.4), round(category['basePrice'] * 0.7))
      
      products_array.append({
        'product_id': category['name'] + '_' + product['name'],
        'category': category['name'],
        'categoryHebrewNeme': category['hebrewNeme'],
        'name': product['name'],
        'hebrewNeme': product['hebrewNeme'],
        'price': category['basePrice'] + random_number_add_to_price,
        'cost': category['basePrice'] - random_number_sub_for_cost,
        'tax': 'normal',
        'preparationTime': product['preparationTime'],
        'ingredients': product['ingredients'],
        'uses': product['uses'],
        'extraWorkers': 0,
        'extraStorage': 0,
      })

  return products_array
