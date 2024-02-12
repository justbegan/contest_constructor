from fastapi.routing import APIRouter
from fastapi import UploadFile, File
import shutil
from typing import List
import calendar
import time
import os


router = APIRouter(
    prefix='/files',
    tags=['Файлы']
)


@router.post("/upload-doc")
def upload_file(file: UploadFile = File(...)):
    """
    Загрузить один документ
    """
    print(file)
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    if check_file(file):
        file.filename = f"{time_stamp}_{file.filename.lower()}"
    else:
        file.filename = f"{file.filename.lower()}"
    path = f'media/{file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        'file': file,
        'filename': path,
        'type': file.content_type
    }


@router.post("/upload-docs")
def upload_files(files: List[UploadFile] = File(...)):
    """
    Загрузить многофайлов
    """
    res = []
    for file in files:

        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)

        if check_file(file):
            file.filename = f"{time_stamp}_{file.filename.lower()}"
        else:
            file.filename = f"{file.filename.lower()}"

        path = f'media/{file.filename}'
        with open(path, 'wb+') as buffer:
            shutil.copyfileobj(file.file, buffer)
        res.append(file)
    return res


def check_file(file):
    original_path = f'media/{file.filename}'
    if os.path.exists(original_path):
        return True
    else:
        return False
