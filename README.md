ISSUES TO ADDRESS:
    * Files upon creation are ending up in root and not being moved to media directory
    * Templates are kind of a mess
    * Views are kind of a mess
    * Model looking alright, but `upload_to` does not appear to be working
    * add a unicode/str method to models
    * still need to transcode webm renditions for streaming

decision: save all file(paths?) in db and let django treat them as if the user uploaded them,
since in a way, they did.