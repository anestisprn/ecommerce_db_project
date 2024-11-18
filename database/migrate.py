from models import Base, create_engine


engine = create_engine('sqlite:///ecommerce.db')
Base.metadata.create_all(engine)