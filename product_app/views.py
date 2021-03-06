
from .utils import get_or_create
from flask import request, render_template, flash, redirect
from flask.blueprints import Blueprint
from .models import Color, ProductColorSize, db, Product, Size, ProductSize
from .forms import ProductForm
main = Blueprint('main', __name__)


@main.route('/')
def test():
    return redirect("products")


@main.route('/products', methods=['POST', 'GET'])
def handle_products():
    form = ProductForm()

    if request.method == 'POST':
        data = request.form
        new_product = Product(name=data['name'])

        product_size = ProductSize(price=data['price'])
        product_size.size = Size(name=data['size'])
        new_product.sizes.append(product_size)
        SKU = ProductColorSize()
        SKU.color = Color(name=data['color'])
        product_size.colors.append(SKU)

        db.session.add(new_product)
        db.session.add(product_size)
        db.session.add(SKU)
        db.session.commit()
        flash(f'Product {new_product.name} Created Successfully ')

        return redirect('/products')

    elif request.method == 'GET':
        form.color.choices = [
            (color.id, color.name) for color in Color.query.all()]

        form.size.choices = [(size.id, size.name) for size in Size.query.all()]
        products = Product.query.all()

        return render_template('product.html', products=products, form=form)


@main.route('/products/<product_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'GET':
        response = {
            "name": product.name,
            "color": product.color,
            "size": product.size,
            "price": product.price
        }
        return {"message": "success", "product": response}

    elif request.method == 'PUT':
        data = request.get_json()
        product.name = data['name']
        product.color = data['color']
        product.size = data['size']
        db.session.add(product)
        db.session.commit()
        return {"message": f"product {product.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        flash(f"Product {product.name} successfully deleted.")
        return redirect('products')


# @main.rou
