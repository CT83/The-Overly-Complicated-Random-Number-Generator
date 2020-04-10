from flask import request
from flask_restful import Resource

from app.api.tasks.utils import background_task
from shared.factories import rq


class TasksRes(Resource):

    def post(self):
        seed = request.get_json()['seed']
        job = background_task.queue(seed)
        return {"message": "Job added to queue",
                "job_id": job.id, }

    def get(self):
        job_key = request.args['job_key']
        job = rq.get_queue().fetch_job(job_key)
        print(job.result)
        return {"msg": {"is_started": job.is_started,
                        "is_queued": job.is_queued,
                        "is_finished": job.is_finished,
                        },
                "result": job.result}


class HelloWorldRes(Resource):

    def get(self):
        return "Hello World"
