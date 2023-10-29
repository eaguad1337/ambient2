from masonite.environment import env
from masonite.utils.location import base_path


DISKS = {
    "default": "local",
    "local": {"driver": "file", "path": base_path("storage/framework/filesystem")},
    "s3": {
        "driver": "s3",
        "client": env("S3_CLIENT"),
        "secret": env("S3_SECRET"),
        "bucket": env("S3_BUCKET"),
    },
}

STATICFILES = {
    # folder          # template alias
    "storage/static": "static/",
    "storage/compiled": "assets/",
    'storage/compiled': 'static/',
    'storage/uploads': 'static/',
    'resources/images': 'images/',
    'public/js': 'js/',
    'public/css': 'css/',
    'public': 'public/',
    'storage/public': '/',
}
