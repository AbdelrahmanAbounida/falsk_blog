
class Config:
    SECRET_KEY = "e09c4d4df3c64b9b4ec5ee6089e28142"
    MONGO_URI = "mongodb+srv://aboneda:aboneda@cluster0.psahi.mongodb.net/?retryWrites=true&w=majority" #os.environ.get('MONGO_URI')

    # file upload
    UPLOAD_FOLDER = 'static/backgrounds'
    BACKGROUND_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'zip'}

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    Testing = True

class ProductionConfig(Config):
    Production = True

config = {
    'development' : DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
