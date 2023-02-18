@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage_header(self):
        time.sleep(5)
