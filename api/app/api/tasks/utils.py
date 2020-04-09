from random import random

from models.sample_data_model import SampleDataModel
from shared.factories import db, rq


@rq.job
def background_task():
    v = SampleDataModel(random_data=str(random.randint()))
    db.session.add(v)
    db.session.commit()
    return SampleDataModel.query.count()
