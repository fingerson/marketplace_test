from urllib.request import urlopen

def test_render_homepage():
    homepage_html = urlopen("http://localhost:5000").read().decode("utf-8")
    print(homepage_html)
    assert "<title>Online Books for You</title>" in homepage_html
    assert homepage_html.count("<li>") == 3
'''if __name__ == "__main__":
    test_render_homepage()
'''
