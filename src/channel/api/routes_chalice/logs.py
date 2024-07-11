from chalice import Chalice
from src.driver.runner import pipeline_runner

app = Chalice(app_name='logs')


@app.route('/')
def index():
    return pipeline_runner("healtcheck", {})