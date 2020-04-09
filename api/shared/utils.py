import os
import random
import shutil
import string
import uuid

from sqlalchemy.exc import SQLAlchemyError


def create_dir_if_not_exists(output_dir):
    try:
        os.makedirs(output_dir)
        return output_dir
    except OSError:
        if not os.path.isdir(output_dir):
            raise

        return output_dir


def delete_file_if_exists(file):
    try:
        os.remove(file)
    except Exception:
        pass


def delete_dir_if_exists(folder):
    try:
        shutil.rmtree(folder)
    except Exception:
        pass


def datetime_to_filename(dt):
    return dt.strftime("%d%m%Y_%H%M%S%f")


def generate_random_hash():
    return str(uuid.uuid4().hex)


def generate_random_image():
    """Generates random images, using a randomly generated numpy array - used in tests"""
    import numpy as np
    rgb = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)
    return rgb


def generate_random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def db_connection_successful(db):
    """Checks if DB Connection is successful"""
    from flask import current_app
    try:
        db.session.execute('SELECT 1')
        current_app.logger.info("DB Connection Successful!")
    except SQLAlchemyError as se:
        current_app.logger.error(str(se))
        return False
    return True
