from flask import Flask, render_template, request, redirect, url_for, jsonify, flash

app = Flask(__name__)


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake menus

menu = {'name': 'entrada', 'description': 'para antes da comida', 'id': '1'}

menus = [{'name': 'entrada','description' : 'para antes da comida', 'id': '1'},
        {'name': 'bebidas', 'description' : 'para beber', 'id': '2'},
        {'name': 'prato principal', 'description' : 'para se deliciar', 'id': '3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'},
        {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},
        {'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},
        {'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},
        {'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id': '6'}


@app.route('/restaurants/JSON')
def restaurantJSON():
    # get restaurants on db
    #falta o serialize
    return jsonify(restaurants)

@app.route('/restaurants/<int:restaurant_id>/menus/JSON')
def restaurantMenuJSON(restaurant_id):
    # get menus form restaurant on db
    # falta o serialize
    return jsonify(menus)

# ADD JSON ENDPOINT HERE
@app.route('/restaurants/<int:restaurant_id>/menus/<int:menu_id>/items/JSON')
def menuItemJSON(restaurant_id, menu_id):
    # get items from menu on db
    # falta o serialize
    return jsonify(items)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    #pegar restaurantes do bd
    return render_template('restaurant/restaurants.html', restaurants = restaurants)
    
@app.route('/restaurants/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        flash('New Restaurant Created')
        return redirect(url_for('showRestaurants'))
    return render_template('restaurant/createRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit/',  methods=['GET', 'POST'])
def editRestaurant(restaurant_id, methods=['GET', 'POST']):
    #pegar restaurant do bd
    if request.method == 'POST':
        flash('Restaurant Edited')
        return redirect(url_for('showRestaurants'))

    # return render_template('restaurant/editRestaurant.html', restaurant= restauranteToEdit)
    return render_template('restaurant/editRestaurant.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/delete/',  methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    #pegar restaruante do bd
    if request.method == 'POST':
        flash('Restaurant deleted')
        return redirect(url_for('showRestaurants'))

    #return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)
    return render_template('restaurant/deleteRestaurant.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/menus')
def showMenus(restaurant_id):
    #pegar os menus do restaurante do bd
    return render_template('menu/menus.html', restaurant_id=restaurant_id, menus=menus)
    # return render_template('menu/menus.html/', menus=menus)

@app.route('/restaurants/<int:restaurant_id>/menu/new',  methods=['GET', 'POST'])
def createMenu(restaurant_id):
    #pegar o restaurante do bd
    if request.method == 'POST':
        flash('New Menu Created')
        return redirect(url_for('showMenus', restaurant_id=restaurant_id))
    return render_template('menu/createMenu.html/', restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/',  methods=['GET', 'POST'])
def editMenu(restaurant_id, menu_id):
    # pegar o menu do restaurante do bd menuToEdit
    if request.method == 'POST':
        flash('Menu Edited')
        return redirect(url_for('showMenus', restaurant_id=restaurant_id))

    #return render_template('menu.html', restaurant_id=restaurant_id, menu=menuToEdit)
    return render_template('menu/editMenu.html/', restaurant_id=restaurant_id, menu=menu)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/',  methods=['GET', 'POST'])
def deleteMenu(restaurant_id, menu_id):
    # pegar o menu do restaurante do bd
    if request.method == 'POST':
        flash('Menu Deleted')
        return redirect(url_for('showMenus', restaurant_id=restaurant_id))

    #return render_template('menu/deleteMenu.html', menu=menuToDelete)
    return render_template('menu/deleteMenu.html/', restaurant_id=restaurant_id, menu=menu)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/items/')
def showMenu(restaurant_id, menu_id):
    #pegar os items do menu do bd

    return render_template('item/items.html', restaurant_id=restaurant_id, menu_id=menu_id, items = items)
    # return render_template('item/items.html/')

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/item/new',  methods=['GET', 'POST'])
def createItem(restaurant_id,menu_id):
    if request.method == 'POST':
        flash('New Item Created')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id, menu_id=menu_id))
    return render_template('item/createItem.html/', restaurant_id=restaurant_id, menu_id=menu_id)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/item/<int:item_id>/edit/',  methods=['GET', 'POST'])
def editItem(restaurant_id,menu_id, item_id):
    #pegar o item do menu do bd
    if request.method == 'POST':
        flash('Item edited')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id, menu_id=menu_id))

    # return render_template('item/editItem.html/', restaurant_id=restaurant_id, menu_id=menu_id, item=itemToEdit)
    return render_template('item/editItem.html/' , restaurant_id=restaurant_id, menu_id=menu_id, item=item)

@app.route('/restaurants/<int:restaurant_id>/menu<int:menu_id>/item/<int:item_id>/delete/',  methods=['GET', 'POST'])
def deleteItem(restaurant_id, menu_id, item_id):
    #pegar o item do menu do bd
    if request.method == 'POST':
        flash('Item deleted')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id, menu_id=menu_id))

    #return render_template('item/deleteItem.html/', restaurant_id=restaurant_id, menu_id=menu_id, item=itemToDelete)
    return render_template('item/deleteItem.html/', restaurant_id=restaurant_id, menu_id=menu_id, item=item)


if __name__ == '__main__':
    app.secret_key = 'super_secre_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)