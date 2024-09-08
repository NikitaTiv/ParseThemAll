import uuid

from parse_them_all.settings import UNAUTHORIZED_USER_FOLDER


def get_directory_path(instance, filename):
    user = getattr(instance, 'user', None)
    upload_folder = user and user.username or UNAUTHORIZED_USER_FOLDER
    file_extension = filename.split('.')[-1]
    return f'{upload_folder}/{uuid.uuid4()}.{file_extension}'
