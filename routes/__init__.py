from routes.main.product import product
from routes.main.index import index
from config import app

app.register_blueprint(product)
app.register_blueprint(index)
