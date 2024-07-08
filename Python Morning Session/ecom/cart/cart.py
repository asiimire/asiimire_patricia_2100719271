from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # get the current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is available on all pages of the site
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in db model
        products = Product.objects.filter(id__in=product_ids)
        #  return those lookedup products
        return products
    
    def get_quants(self):
        # get ids from cart
        quantities = self.cart
        return quantities

