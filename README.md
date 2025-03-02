本项目创建于2025年2月是本人的毕业设计项目！！
数据库er图：
    ![image](https://github.com/user-attachments/assets/2d845a0c-187d-4baf-8592-c86303eef186)
数据字典：    
    ![image](https://github.com/user-attachments/assets/5332446d-e7d6-470b-875d-4f75260e7543)
使用了gis数据库，需要下载GDAL并在setting中配置环境，
    配置完后修改setting中的数据库选项，
    if os.name == 'nt':
        import platform
        GDAL_DIR = r"C:\Program Files\GDAL"
        assert os.path.isdir(GDAL_DIR), "Directory does not exist: " + GDAL_DIR
        os.environ['OSGEO4W_ROOT'] = GDAL_DIR
        os.environ['GDAL_DATA'] = os.path.join(GDAL_DIR, "gdal-data")
        os.environ['PROJ_LIB'] = os.path.join(GDAL_DIR, "projlib")
        os.environ['PATH'] = GDAL_DIR + ";" + os.environ['PATH']
        # 根据实际的版本号修改 .dll 文件名
        GDAL_LIBRARY_PATH = os.path.join(GDAL_DIR, "gdal.dll")
    用于配置GDAL数据库环境连接
        DATABASES = 
        {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.mysql',
                'NAME': 'docking',
                'USER': 'root',
                'PASSWORD': 'Szc#030609',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
    用于配置数据库连接
    配置完成后执行
        python manage.py makemigrations
        python manage.py migrate
    完成数据库迁移