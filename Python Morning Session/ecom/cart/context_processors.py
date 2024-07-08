from .cart import Cart

# create context processor so our cart can work on all pages of the site
def cart(request):
    # return default data from out cart
    return {'cart': Cart(request)}