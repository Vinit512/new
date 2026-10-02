from hello import app

def home_test():
  client = app.test_client()
  response = client.get("/")

  assert response.status_code == 200
  assert response.data == "Hello, World"
