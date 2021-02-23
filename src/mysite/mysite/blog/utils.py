import logging

from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def login_user_is_writer(login_user: User, writer: User) -> bool:
    if not login_user.is_authenticated:
        return False
    
    logger.debug(f'Login User ID: {login_user.id}')
    logger.debug(f'Writer ID: {writer.id}')
    
    if not login_user.id == writer.id:
        return False
    return True