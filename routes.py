from flask_restful import Api
from constants import *
from api import *

USER_ROUTE = "/user"
USER_ID_ROUTE = f"{USER_ROUTE}/<string:user_id>"
LIST_USERS_ROUTE = "/users"
WORKOUTS_USER_ID_ROUTE = "/workouts/<string:user_id>"
FOLLOW_LIST_USER_ID_ROUTE = "/follow-list/<string:user_id>"
SHOW_FRIEND_WORKOUTS_ROUTE = f"{FOLLOW_LIST_USER_ID_ROUTE}/<string:follow_id>"

ROUTES = {
    "RegisterUser" : USER_ROUTE,
    "GetUser" : USER_ID_ROUTE,
    "RemoveUser" : USER_ID_ROUTE,
    "ListUsers" : LIST_USERS_ROUTE,
    "AddWorkout": WORKOUTS_USER_ID_ROUTE,
    "ListWorkouts": WORKOUTS_USER_ID_ROUTE,
    "FollowFriend": FOLLOW_LIST_USER_ID_ROUTE,
    "ShowFriendWorkouts" : SHOW_FRIEND_WORKOUTS_ROUTE
}

METHODS= {
    "RegisterUser" : POST,
    "GetUser" : GET,
    "RemoveUser" : DELETE,
    "ListUsers" : GET,
    "AddWorkout": PUT,
    "ListWorkouts" : GET,
    "FollowFriend" : PUT,
    "ShowFriendWorkouts" : GET
}

#check this
RESOURCES = {
    "RegisterUser" : RegisterUser,
    "GetUser" : GetUser,
    "RemoveUser" : RemoveUser,
    "ListUsers" : ListUsers,
    "AddWorkout": AddWorkout,
    "ListWorkouts" : ListWorkouts,
    "FollowFriend": FollowFriend,
    "ShowFriendWorkouts" : ShowFriendWorkouts
}

def init_routes(api: Api) -> None:
    for [api_name, resource] in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])