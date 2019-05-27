from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        response = client.get(url_for('users.login'))
        assert response.status_code == 200
