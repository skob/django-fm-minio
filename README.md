# django-fm-minio

1. pre-create bucket, policy and keys
2. add fixtures_minio to installed apps and configure plugin

```
INSTALLED_APPS += ['fixtures_minio']

FM_MINIO_ACCESS_KEY = 'fixtures'  ###
FM_MINIO_BUCKET = 'fixtures'  ###
FM_MINIO_SECRET_KEY = 'fixtures'  ###
FM_MINIO_SECURE = False  ###
FM_MINIO_URL = 'localhost:9000'  ###
```
