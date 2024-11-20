from flask_restful import Resource, reqparse
from uuid import uuid4 as generateId

user_store = {}
workouts = {}

register_user_parser = (reqparse.RequestParser(bundle_errors=True)
                        .add_argument("name", type = str, required = True)
                        .add_argument("age", type = int, required = False))
class RegisterUser(Resource):
    def post(self):
        name, age = register_user_parser.parse_args().values()
        uuid = str(generateId())
        if name is None:
            return {"message":"Name is a required value"}, 400
        user_store[uuid] = {
            "id" : uuid,
            "name" : name,
            "age" : age
        }
        return user_store[uuid], 200
    
class GetUser(Resource):
    def get(self, user_id):
        user = user_store.get(user_id)
        if user is None:
            return {"message" : "user not found in our user store"}, 404
        return user_store[user_id], 200

class RemoveUser(Resource):
    def delete(self, user_id):
        if user_id in user_store:
            del user_store[user_id]
            return {}, 200
        return {"message" : "user not found in our store"}, 404


class ListUsers(Resource):
    def get(self):
        return {"users" :[*user_store.values()]}, 200

add_workout_parser = (reqparse.RequestParser(bundle_errors=True)
    .add_argument("date", type=str, required=True)
    .add_argument("distance", type=str, required=True)
    .add_argument("time", type=str, required=True))
class AddWorkout(Resource):
    def put(self, user_id):
        date, distance, time = add_workout_parser.parse_args().values()
        if user_id not in workouts:
            workouts[user_id] = []
        workout = {
            "date" : date,
            "distance" : distance,
            "time" : time
        }
        workouts[user_id].append(workout)
        return workout, 200

class ListWorkouts(Resource):
    def get(self, user_id):
        return {"workouts" : workouts.get(user_id)}, 200


#Extra Credit Stuff
following = {}

follow_friend_parser = (reqparse.RequestParser()
    .add_argument("follow_id", type=str, required=True))
class FollowFriend(Resource):
    
    def put(self, user_id):
        args = follow_friend_parser.parse_args()
        follow_id = args["follow_id"]
        user = user_store.get(user_id)
        if user is None:
            return {"message": "user not found in our user_store"}, 404
        if follow_id is None:
            return {"message": "user to follow not found in our user_store"}, 404
        if user_id not in following:
            following[user_id] = set()

        following[user_id].add(follow_id)

        return {"following" : list(following.get(user_id))}, 200
    
class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        user = user_store.get(user_id)
        follow_id = user_store.get(follow_id)
        if user is None:
            return {"message": "user not found in our user_store"}, 404
        if follow_id is None:
            return {"message": "user to follow not found in our user_store"}, 404
        follow_id = follow_id.get("id")
        if follow_id not in following.get(user_id):
            return {"message": "you do not follow this user, so you can't see their following list"}, 403
        return ListWorkouts.get(self, follow_id)
    