from flask import Flask, render_template

app = Flask(__name__)

RESTAURANT_INFO = {
    'name': 'Bella Napoli Bakery & Café',
    'tagline': 'Authentic Italian Pastries & Fresh Café',
    'instagram': '@bellanapolibakery',
    'closed_day': 'CLOSED EASTER SUNDAY',
    'latham': {
        'name': 'Latham Café & Bakery',
        'address': '672 New Loudon Road, Latham, NY 12110',
        'phone': '518-783-0196',
        'hours_mon_sat': 'Mon – Sat: 6am-7pm',
        'hours_sunday': 'Sunday: 6am-6pm'
    },
    'troy': {
        'name': 'Troy Bakery',
        'address': '721 River Street, Troy, NY 12180',
        'phone': '518-274-8277',
        'hours': 'Mon – Sun: 6am-?pm'
    },
    'about': '''Welcome to Bella Napoli Bakery & Café, where authentic Italian baking traditions meet 
    the warmth of a neighborhood café. Our family has been crafting traditional Italian pastries, 
    specialty cakes, and fresh baked goods for generations. Every morning, our ovens are filled 
    with freshly baked Italian cookies, biscotti, artisan breads, and decadent pastries. 
    Stop by for a fresh espresso, a slice of our famous Italian cream cake, or pick up a 
    beautiful custom cake for your special occasion.'''
}

NAV_LINKS = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'Café Menu', 'url': 'menu'},
    {'name': 'Bakery', 'url': 'bakery'},
    {'name': 'About Us', 'url': 'about'},
    {'name': 'Contact Us', 'url': 'contact'},
]

CAFE_MENU = {
    'breakfast': [
        {'name': 'Cornetti & Pastries', 'description': 'Fresh Italian croissants and pastries baked daily', 'price': None},
        {'name': 'Breakfast Sandwiches', 'description': 'Fresh eggs, cheese, and your choice of meat on artisan bread', 'price': None},
        {'name': 'Overnight Oats', 'description': 'Creamy oats with fresh fruit and honey', 'price': None},
        {'name': 'Avocado Toast', 'description': 'Smashed avocado on toasted Italian bread with cherry tomatoes', 'price': None},
    ],
    'lunch': [
        {'name': 'Panini Selection', 'description': 'Pressed Italian sandwiches with prosciutto, mozzarella, pesto', 'price': None},
        {'name': 'Caesar Salad', 'description': 'Romaine, parmesan, croutons, and house-made dressing', 'price': None},
        {'name': 'Minestrone Soup', 'description': 'Traditional Italian vegetable soup with pasta', 'price': None},
        {'name': 'Caprese Sandwich', 'description': 'Fresh mozzarella, tomato, basil, and balsamic', 'price': None},
    ],
    'beverages': [
        {'name': 'Espresso', 'description': 'Rich Italian espresso', 'price': None},
        {'name': 'Cappuccino', 'description': 'Espresso with steamed milk foam', 'price': None},
        {'name': 'Latte', 'description': 'Espresso with creamy steamed milk', 'price': None},
        {'name': 'Italian Sodas', 'description': 'Sparkling water with Italian syrups', 'price': None},
    ]
}

BAKERY_ITEMS = {
    'pastries': [
        {'name': 'Italian Pastry Specialties', 'description': 'Cannoli, sfogliatelle, and traditional Neapolitan pastries'},
        {'name': 'Italian Cookies & Biscotti', 'description': 'Assorted traditional Italian cookies, perfect for any occasion'},
        {'name': 'Danishes & More', 'description': 'Fruit danishes, cheese danishes, and sweet breakfast pastries'},
    ],
    'cakes': [
        {'name': 'Specialty Cakes', 'description': 'Custom decorated cakes for birthdays, weddings, and celebrations'},
        {'name': 'Tiramisu', 'description': 'Classic Italian dessert with espresso-soaked ladyfingers and mascarpone'},
        {'name': 'Cheesecake', 'description': 'Creamy New York style with your choice of toppings'},
    ],
    'breads': [
        {'name': 'Artisan Breads', 'description': 'Fresh baked daily - ciabatta, focaccia, and Italian loaves'},
        {'name': 'Bread Rolls', 'description': 'Perfect for sandwiches or table bread'},
    ]
}

ALLERGY_NOTICE = '''FOOD ALLERGY NOTICE: Please be advised that our products may contain these ingredients: 
wheat, milk, eggs, peanuts, tree nuts, sesame seeds, and soybeans. We are NOT a nut free facility.'''


@app.route('/')
def home():
    return render_template('index.html', info=RESTAURANT_INFO, nav=NAV_LINKS, allergy=ALLERGY_NOTICE)


@app.route('/menu')
def menu():
    return render_template('menu.html', info=RESTAURANT_INFO, nav=NAV_LINKS, 
                          cafe_menu=CAFE_MENU, allergy=ALLERGY_NOTICE)


@app.route('/bakery')
def bakery():
    return render_template('bakery.html', info=RESTAURANT_INFO, nav=NAV_LINKS,
                          bakery=BAKERY_ITEMS, allergy=ALLERGY_NOTICE)


@app.route('/about')
def about():
    return render_template('about.html', info=RESTAURANT_INFO, nav=NAV_LINKS, allergy=ALLERGY_NOTICE)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=RESTAURANT_INFO, nav=NAV_LINKS, allergy=ALLERGY_NOTICE)


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
