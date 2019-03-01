from app import app, db
from app.models import Measurement, Test

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Measurement': Measurement, 'Test': Test}