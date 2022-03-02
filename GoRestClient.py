import requests
import json



class GoRestClient:

    def init_app(self):
        msg = '*****\n1-Get All Users\n2-Get User\n3-Create User\n4-Update User\n5-Delete User\n6-Exit(E/Ç)'
        while True:
            print(msg)
            process = input('Selection: ')
            if process == '1':
                self.get_users()
            elif process == '2':
                self.get_user()
            elif process == '3':
                self.create_user()
            elif process == '4':
                self.update_user()
            elif process == '5':
                self.delete_user()
            elif process == 'E' or process == 'Ç' or process == '6' or process == 'e' or process == 'ç':
                print('Your exit is done.')
                break
            else:
                print('You made the wrong choice. Please try again.')

    def get_users(self):
        result = requests.get("https://gorest.co.in/public/v2/users")
        print("status code", result.status_code)
        result = json.loads(result.text)

        for i in result:
            print(i)

    def get_user(self):
        id = input("Enter the ID of the user you want to get: ")
        result = requests.get(f"https://gorest.co.in/public/v2/users/{id}")
        print("status code", result.status_code)
        if result.status_code != 200:
            print("User not found")
        else:
            print(result.text)


    def create_user(self):
        url = "https://gorest.co.in/public/v2/users"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}
        body = {
            "email": "cugce_murat@hotmail.com",
            "name": "Tugce Murat",
            "gender": "Female",
            "status": "active"
        }
        result = requests.post(url, headers=headers, data=body)
        print("status code", result.status_code)
        print(result.json())
        if result.status_code == 201:
            print("User created")
        else:
            print("Has already been taken")


    def update_user(self):
        id = input("Enter the ID of the user you want to update: ")
        url = f"https://gorest.co.in/public/v2/users/{id}"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}
        body = {
            "email": "bugra_murat@hotmail.com",
            "name": "Bugra avcı",
            "gender": "male",
            "status": "active"
        }
        result = requests.patch(url, headers=headers, data=body)
        print("status code", result.status_code)
        print(result.json())
        if result.status_code != 200:
            print("User not found")
        else:
            print("User Updated")



    def delete_user(self):
        id = input("Enter the ID of the user you want to delete: ")
        url =f"https://gorest.co.in/public/v2/users/{id}"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}

        result = requests.delete(url, headers=headers)
        print("status code", result.status_code)
        if result.status_code == 204:
            print("User Deleted")
        else:
            print("User not found")

app = GoRestClient()
app.init_app()