from flask import request
from flask_restful import Resource

from app.api.tasks.utils import background_task
from shared.factories import rq


class TasksRes(Resource):

    def post(self):
        job = background_task.queue()
        return {"message": "Job added to queue",
                "job_key": job.id, }

    def get(self):
        job_key = request.args['job_key']
        job = rq.get_queue().fetch_job(job_key)
        print(job.result)
        return {"msg": {"is_started": job.is_started,
                        "is_queued": job.is_queued,
                        "is_finished": job.is_finished,
                        "result": job.result}}
