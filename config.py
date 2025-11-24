import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """A class to hold all configuration variables."""

    # Django
    DEBUG = str(os.getenv("DEBUG", ""))
    DJANGO_ALLOWED_HOSTS = str(os.getenv("DJANGO_ALLOWED_HOSTS", ""))
    SECRET_KEY = str(os.getenv("SECRET_KEY"))

    # Database module
    DB_USERNAME = str(os.getenv("DB_USERNAME", ""))
    DB_PASSWORD = str(os.getenv("DB_PASSWORD", ""))
    DB_HOST = str(os.getenv("DB_HOST", ""))
    DB_PORT = int(os.getenv("DB_PORT", ""))

    # Logger module
    LOG_CONFIG = str(os.getenv("LOG_CONFIG", ""))
    LOG_FILE = str(os.getenv("LOG_FILE", ""))

    # Mailer module
    MAIL_HOST = str(os.getenv("MAIL_HOST", ""))
    MAIL_PORT = int(os.getenv("MAIL_PORT", 1))
    MAIL_USER = str(os.getenv("MAIL_USER", ""))
    MAIL_PASSWORD = str(os.getenv("MAIL_PASSWORD", ""))
    MAIL_RECEIVER = str(os.getenv("MAIL_RECEIVER", ""))
