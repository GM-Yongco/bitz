import requests

link_01:str = "http://127.0.0.1:5000/update"
json_01 = {
        "message": "test"
}
response_01 = requests.post(
    link_01,
    json=json_01
)
print(response_01.json())

# =========================

link_02:str = "http://127.0.0.1:5000/status"
response_02 = requests.get(link_02)
print(response_02.json())
