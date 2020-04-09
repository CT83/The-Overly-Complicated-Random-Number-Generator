from shared.factories import db


class SampleDataModel(db.Model):
    __tablename__ = 'sample_data_model'
    id = db.Column(db.Integer, primary_key=True)
    random_data = db.Column(db.String(120))
