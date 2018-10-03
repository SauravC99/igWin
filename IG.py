#########################
#   Saurav Chhapawala   #
#          2018         #
#########################

from InstagramAPI import InstagramAPI

def main():

    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    api = InstagramAPI(username, password)
    InstagramAPI.login(api)

main()