import random

from models.sample_data_model import SampleDataModel
from shared.factories import db, rq


@rq.job
def background_task(seed):
    random.seed(seed)
    v = SampleDataModel(random_data=str(random.randint(1, 1000)))
    db.session.add(v)
    db.session.commit()
    return v.random_data
