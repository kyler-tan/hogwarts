import requests


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_from(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']["H"] == "header demo"