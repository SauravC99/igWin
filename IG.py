#########################
#   Saurav Chhapawala   #
#          2018         #
#########################

from InstagramAPI import InstagramAPI
import time

username = input("Enter your Username: ")
password = input("Enter your Password: ")
api = InstagramAPI(username, password)


def main():
    api.login()

    USERID = getUserID()

    following_list = getFollowingList(USERID)
    follower_list = getFollowerList(USERID)

    print(follower_list)
    print(following_list)

    print("Num of followers is", len(follower_list))
    print("Num of following is", len(following_list))


    api.logout()


'''
Gets the user's profile ID
'''
def getUserID():
    api.getProfileData()
    result = api.LastJson
    userID = result["user"]["pk"]
    return userID


'''
Gets the user's followers
Returns them in a set
'''
def getFollowerList(userID):
    followers = []
    max_id = True
    while max_id:
        # first iteration hack
        if(max_id == True):
            max_id = ''
        a = api.getUserFollowers(getUserID(), maxid = max_id)
        followers.extend(api.LastJson.get("users", []))
        max_id = api.LastJson.get("next_max_id", "")
        time.sleep(1)

    followers_list = followers

    user_list = map(lambda x: x["username"], followers_list)
    followers_set = set(user_list)
    return list(followers_set)


'''
Gets a set of people the user is following
'''
def getFollowingList(userID):
    following = []
    max_id = True
    while max_id:
        # first iteration hack
        if(max_id == True):
            max_id = ''
        a = api.getUserFollowings(getUserID(), maxid = max_id)
        following.extend(api.LastJson.get("users", []))
        max_id = api.LastJson.get("next_max_id", "")
        time.sleep(1)

    following_list = following

    user_list = map(lambda x: x["username"], following_list)
    following_set = set(user_list)
    return list(following_set)


main()