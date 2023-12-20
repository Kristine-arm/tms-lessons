import requests

class PetStore:
    HOST = "https://petstore.swagger.io/v2"
    CREATE = "/user"   # POST
    READ = "/user/{}"  # GET
    UPDATE = "/user/{}"  # PUT
    DELETE = "/user/{}"  # DELETE

class TestPetStore:

    def test_create_user(self):
        url = f"{PetStore.HOST}{PetStore.CREATE}"
        data = {
            "id": 1,
            "username": "testuser",
            "firstName": "Tested",
            "lastName": "User",
            "email": "user@gmail.com",
            "password": "blabla123",
            "phone": "1234567890"
        }
        response = requests.post(url, json=data)
        assert response.status_code == 200, f"Failed during creation. {response.text}"

    def test_read_user(self):
        username = "testuser"
        url = f"{PetStore.HOST}{PetStore.READ.format(username)}"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed during reading {username}. {response.text}"
        assert response.json()['username'] == username, "Username mismatch"

    def test_update_user(self):
        username = "testuser"
        url = f"{PetStore.HOST}{PetStore.UPDATE.format(username)}"
        updated_data = {
            "id": 1,
            "username": "testuser",
            "firstName": "Updateduser",
            "lastName": "User",
            "email": "newuser@gmail.com",
            "password": "blablabla123",
            "phone": "0123456789"
        }
        response = requests.put(url, json=updated_data)
        assert response.status_code == 200, f"Failed during update {username}. {response.text}"

    def test_delete_user(self):
        username = "testuser"
        url = f"{PetStore.HOST}{PetStore.DELETE.format(username)}"
        response = requests.delete(url)
        assert response.status_code == 200, f"Failed during delete {username}. {response.text}"