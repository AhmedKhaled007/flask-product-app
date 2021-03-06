from .extensions import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    sizes = db.relationship('ProductSize', back_populates='product')


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    products_size = db.relationship("ProductColorSize", back_populates="color")


class Size(db.Model):
    __tablename__ = 'size'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    products = db.relationship("ProductSize", back_populates="size")


class ProductSize(db.Model):
    __tablename__ = 'product_size'
    id = db.Column(db.Integer, primary_key=True)
    size_id = db.Column(db.ForeignKey('size.id'))
    product_id = db.Column(db.ForeignKey('product.id'))
    price = db.Column(db.Numeric(9, 2))

    product = db.relationship("Product", back_populates="sizes")
    size = db.relationship("Size", back_populates='products')

    colors = db.relationship("ProductColorSize", back_populates="product_size")

    __table_args__ = (db.UniqueConstraint('size_id', 'product_id'),)


class ProductColorSize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_size_id = db.Column(db.ForeignKey('product_size.id'))
    color_id = db.Column(db.ForeignKey('color.id'))

    color = db.relationship("Color", back_populates='products_size')
    product_size = db.relationship("ProductSize", back_populates='colors')

    __table_args__ = (db.UniqueConstraint('color_id', 'product_size_id'),)
