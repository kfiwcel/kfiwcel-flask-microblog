import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME ='506082526@qq.com'
    MAIL_PASSWORD = 'iaginkjummuvbjfb'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <506082526@qq.com>'
    FLASKY_ADMIN = 'kfiwcel@outlook.com'
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5



    CKEDITOR_HEIGHT = 300
    CKEDITOR_FILE_UPLOADER = 'main.upload'
    UPLOADED_PATH = os.path.join(basedir, 'uploads')


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app ( cls , app ) :
        Config.init_app ( app )

        # 把错误通过电子邮件发送给管理员
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr ( cls , 'MAIL_USERNAME' , None ) is not None :
            credentials = (cls.MAIL_USERNAME , cls.MAIL_PASSWORD)
            if getattr ( cls , 'MAIL_USE_TLS' , None ) :
                secure = ()
        mail_handler = SMTPHandler (
            mailhost=(cls.MAIL_SERVER , cls.MAIL_PORT) ,
            fromaddr=cls.FLASKY_MAIL_SENDER ,
            toaddrs=[ cls.FLASKY_ADMIN ] ,
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error' ,
            credentials=credentials ,
            secure=secure )
        mail_handler.setLevel ( logging.ERROR )
        app.logger.addHandler ( mail_handler )


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}