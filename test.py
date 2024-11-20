import requests
import json

BASE = "http://127.0.0.1:5000"

#TEST: ListUsers
print("ListUsers")
response_list = requests.get(f"{BASE}/users")
print("Status Code:", response_list.status_code)
print(json.dumps(response_list.json(), indent=2))


#TEST: RegisterUser (required and optional params provided)
print("\nRegisterUser (required and optional params provided)")
response = requests.post(f"{BASE}/user", json={
    "name": "Elizabeth",
    "age": 20
})

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

valid_id_elizabeth = response.json()["id"] # capture valid id for other tests

# Adding a couple other users
response = requests.post(f"{BASE}/user", json={
    "name": "Jane",
    "age": 22
})
print(json.dumps(response.json(), indent=2))

valid_id_jane = response.json()["id"] # capture valid id for other tests

response = requests.post(f"{BASE}/user", json={
    "name": "Mary",
    "age": 18
})
print(json.dumps(response.json(), indent=2))

valid_id_mary = response.json()["id"] # capture valid id for other tests

#TEST: RegisterUser (required params not provided)
print("\nRegisterUser(required params not provided)")
response = requests.post(f"{BASE}/user", json={
    "age" : 22
})

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: RegisterUser (only required params provided)
print("\nRegisterUser (only required params provided)")
response = requests.post(f"{BASE}/user", json={
    "name": "Lydia"
})

valid_id_lydia = response.json()["id"]

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: GetUser with (valid id)
print("\nGetUser (with valid id)")
response = requests.get(f"{BASE}/user/{valid_id_mary}")

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: GetUser with (bad id)
print("\nGetUser (with bad id)")
bad_id = "123456"
response = requests.get(f"{BASE}/user/{bad_id}")

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: RemoveUser with (valid id)
print("\nRemoveUser (with valid id)")
response = requests.delete(f"{BASE}/user/{valid_id_mary}")

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: RemoveUser (with bad id)
print("\nRemoveUser (with bad id)")
response = requests.delete(f"{BASE}/user/{bad_id}")

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: ListUsers
print("\nListUsers")
response_list = requests.get(f"{BASE}/users")
print(response_list.status_code)
print(json.dumps(response_list.json(), indent=2))

# print(valid_id_elizabeth)

#TEST: AddWorkout (required params provided)
print("\nAddWorkout (required params provided)")
response = requests.put(f"{BASE}/workouts/{valid_id_elizabeth}", json = {
    "date" : "18 Nov 2024",
    "time" : "23 mins",
    "distance" : "5 km"
})

print(response.status_code)
print(json.dumps(response.json(), indent=2))

response = requests.put(f"{BASE}/workouts/{valid_id_elizabeth}", json = {
    "date" : "10 Dec 2024",
    "time" : "120 mins",
    "distance" : "20 km"
})

print(response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: AddWorkout (required params not provided)
print("\nAddWorkout (required params not provided)")
response = requests.put(f"{BASE}/workouts/{valid_id_elizabeth}", json = {
    "date" : "9 Jan 2025",
})

print(response.status_code)
print(json.dumps(response.json(), indent=2))

#TEST: ListWorkouts
print("\nListWorkouts")
response = requests.get(f"{BASE}/workouts/{valid_id_elizabeth}")

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

print("ListUsers")
response_list = requests.get(f"{BASE}/users")
print("Status Code:", response_list.status_code)
print(json.dumps(response_list.json(), indent=2))

#TEST: FollowFriend (required params provided)
print("\nFollowFriend (required params provided)")
response = requests.put(f"{BASE}/follow-list/{valid_id_elizabeth}", json = {
    "follow_id" : valid_id_lydia,
})

response = requests.put(f"{BASE}/follow-list/{valid_id_elizabeth}", json = {
    "follow_id" : valid_id_jane,
})

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))

#TODO: required params not provided
#TEST: FollowFriend (required params provided)
print("\nFollowFriend (required params not provided)")
response = requests.put(f"{BASE}/follow-list/{valid_id_elizabeth}", json = {
})

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))


print("\nShowFriendWorkouts (with valid follow_id)")
response = requests.put(f"{BASE}/follow-list/{valid_id_jane}", json = {
    "follow_id" : valid_id_elizabeth,
})

response_list = requests.get(f"{BASE}/follow-list/{valid_id_jane}/{valid_id_elizabeth}")
print("Status Code:",response_list.status_code)
print(json.dumps(response_list.json(), indent=2))

# user to follow not in user_store
print("\nShowFriendWorkouts (with invalid follow_id)")
response_list = requests.get(f"{BASE}/follow-list/{valid_id_jane}/{valid_id_mary}")
print("Status Code:",response_list.status_code)
print(json.dumps(response_list.json(), indent=2))

# not following user to follow
print("\nShowFriendWorkouts (with invalid follow_id)")
response_list = requests.get(f"{BASE}/follow-list/{valid_id_jane}/{valid_id_lydia}")
print("Status Code:",response_list.status_code)
print(json.dumps(response_list.json(), indent=2))

# problem: .get vs ["key"]
# set are not serializable