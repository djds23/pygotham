import os
import shutil

from element_gen import TwitterElement
from django.conf import settings

def make_element(username):
    slideshow = TwitterElement(username)
    slideshow.create_slideshow()
    slideshow.clean_up()
    shutil.move(slideshow.slideshow_filename, '/static/transcoder/videos/')
    return final_path