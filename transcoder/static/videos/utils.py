from element_gen import TwitterElement

def make_element(username):
    try:
        return TwitterElement(username)
    except ValueError:
        return None
