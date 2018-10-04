#########################
#   Saurav Chhapawala   #
#          2018         #
#########################

from InstagramAPI import InstagramAPI

username = input("Enter your Username: ")
password = input("Enter your Password: ")
api = InstagramAPI(username, password)


def main():
    api.login()

    following_list = getFollowingList(getUserID())
    follower_list = getFollowerList(getUserID())

    print(following_list)
    print(follower_list)

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
 Returns them in an array
'''
def getFollowerList(userID):
    api.getUserFollowers(userID)
    follower = api.LastJson["users"]
    follower_list = []
    for i in follower:
        follower_list.append(i["username"])

    return(follower_list)


'''
Gets a list of people the user is following
'''
def getFollowingList(userID):
    api.getUserFollowings(userID)
    following = api.LastJson["users"]
    following_list = []
    for i in following:
        following_list.append(i["username"])

    return(following_list)


main()