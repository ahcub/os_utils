import hashlib
from distutils.filelist import findall
from os.path import relpath, join, basename
from zipfile import ZipFile


def get_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file_:
        batch_size = 4096
        chunk = file_.read(batch_size)
        while chunk:
            md5_hash.update(chunk)
            chunk = file_.read(batch_size)

        return hashlib.md5(file_.read()).hexdigest()


def zip_dir(path, zip_file_path=None, zip_root=None):
    zip_file_path = zip_file_path or '{}.zip'.format(path)
    zip_root = zip_root or basename(path)
    with ZipFile(zip_file_path, 'w') as zip_file:
        for file in findall(path):
            zip_file.write(file, join(zip_root, relpath(file, path)))

