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
                self.id = input("Enter the ID of the user you want to get: ")
                self.get_user()
            elif process == '3':
                self.email = input("email: ")
                self.name = input("name: ")
                self.gender = input("gender: ")
                self.status = input("status: ")
                self.create_user()
            elif process == '4':
                self.id = input("Enter the ID of the user you want to update: ")
                self.email = input("email: ")
                self.name = input("name: ")
                self.gender = input("gender: ")
                self.status = input("status: ")
                self.update_user()
            elif process == '5':
                self.id = input("Enter the ID of the user you want to delete: ")
                self.delete_user()
            elif process == 'E' or process == 'Ç' or process == '6' or process == 'e' or process == 'ç':
                print('Your exit is done.')
                break
            else:
                print('You made the wrong choice. Please try again.')

    def get_users(self):
        result = requests.get('https://gorest.co.in/public/v2/users')
        print("status code", result.status_code)
        result = json.loads(result.text)

        for i in result:
            print(i)

    def get_user(self):
        result = requests.get(f"https://gorest.co.in/public/v2/users/{self.id}")
        print("status code", result.status_code)
        if result.status_code != 200:
            print("User not found")
        else:
            print(result.text)

    def create_user(self):
        url = "https://gorest.co.in/public/v2/users"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}

        body = {
            "email": f"{self.email}",
            "name": f"{self.name}",
            "gender": f"{self.gender}",
            "status": f"{self.status}"
        }
        result = requests.post(url, headers=headers, data=body)
        print("status code", result.status_code)
        print(result.json())
        if result.status_code == 201:
            print("User created")
        else:
            print("Has already been taken")

    def update_user(self):
        url = f"https://gorest.co.in/public/v2/users/{self.id}"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}

        body = {
            "email": f"{self.email}",
            "name": f"{self.name}",
            "gender": f"{self.gender}",
            "status": f"{self.status}"
        }
        result = requests.patch(url, headers=headers, data=body)
        print("status code", result.status_code)
        print(result.json())
        if result.status_code != 200:
            print("User not found")
        else:
            print("User Updated")

    def delete_user(self):
        url =f"https://gorest.co.in/public/v2/users/{self.id}"
        headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}

        result = requests.delete(url, headers=headers)
        print("status code", result.status_code)
        if result.status_code == 204:
            print("User Deleted")
        else:
            print("User not found")

app = GoRestClient()
app.init_app()