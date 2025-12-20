import requests

headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json",
    "Job": "Matrix"
}

url = "https://reqres.in/api/users/2"

get_response = requests.get(url, headers=headers)
print("GET Status:", get_response.status_code)
print("GET Response:", get_response.json())

put_data = {
    "Updated At": "10.00 A.M"
}

put_response = requests.put(url + "/" + str(id), headers=headers, json=put_data)
print("\nPUT Status:", put_response.status_code)
print("PUT Response:", put_response.json())


