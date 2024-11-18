from sqlalchemy.orm import sessionmaker
from models import User, Product, Order, OrderItem, Review
from migrate import engine

Session = sessionmaker(bind=engine)
session = Session()

# Add sample users
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")
session.add_all([user1, user2])

# Add sample products
product1 = Product(name="Laptop", price=999.99)
product2 = Product(name="Smartphone", price=699.99)
session.add_all([product1, product2])

session.commit()
session.close()
