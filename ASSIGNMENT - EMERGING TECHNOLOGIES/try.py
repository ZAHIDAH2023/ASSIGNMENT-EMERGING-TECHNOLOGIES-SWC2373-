import requests
import json

acc_token = input("Please Enter Your Access Token:")
print("\n\tMAIN MENU OPTION")
print("-" * 35)
print("| 0 - Test connection              |")
print("| 1 - Display User Information     |")
print("| 2 - Display 5 Rooms              |")
print("| 3 - Create a room                |")
print("| 4 - Send message to a room       |")
print("-" * 35)

option = input("\nPlease enter your Option : ")

headers = {
    'Authorization':'Bearer {}'. format(acc_token),
    'Content-Type': 'application/json'
}
url = 'https://webexapis.com/v1/people/me'
res = requests.get(url, headers=headers)


if option == "0":
    if res.status_code == 200:
        print("\nConnection to Web Server is Succesfull")
    else:
        print("\nConnection to Web Server is Failed")

elif option == "1":
        
        userinfo = res.json()
        print("\n\t\t\tUSER DETAILS")
        print("-" * 64)
        print(f"| User Displayed Name: {userinfo['displayName']}      |")   
        print(f"| User Nickname: {userinfo['nickName']}              |")
        print(f"| User Emails: {' , '.join(userinfo['emails'])}               |")
        print("-" * 64)

elif option == "2":
    url = 'https://webexapis.com/v1/rooms'
    params = {'max':'5'}
    res = requests.get(url, headers=headers, params=params)
    

    roomInfo = res.json()
    if res.status_code == 200:
            if 'items' in roomInfo:
                print("\n\t\t\t\t\t\tROOM DETAILS")
                print("*" * 111)
                for item in roomInfo['items']:
                    print(f"\n| Room ID: {item['id']}")
                    print(f"| Room Title: {item['title']}")
                    print(f"| Date Created: {item['created']}")
                    print(f"| Last Activity: {''.join(item['lastActivity'])}")
                    print("*" * 111)
        

elif option == "3":
    create_room = input("Enter Room Name: ")
    params = {'title': create_room}
    url = 'https://webexapis.com/v1/rooms'
    res = requests.post(url, headers=headers, json=params)

    if res.status_code == 200:
        print("\nRoom has been Created:")
        print(f"{create_room} Successfully Created\n")
    else:
        print("Room has Failed to Create:")
        print(f"{create_room} Unccessfully Create due to {res.status_code}")

elif option == "4":
    url='https://webexapis.com/v1/rooms'
    params={'max':'5'}
    res=requests.get(url,headers=headers, params=params)
    roomInfo = res.json()

    if res.status_code == 200:
            print("\n\t\tROOMS")
            print("-" * 40)
            for i,item in enumerate ( roomInfo['items']):
                print(f" ({i + 1}) {item['title']}")

                print("-" * 40)
            chooseRoom=int(input("\nChoose a room to send a message:"))-1

            if 0 <= chooseRoom <len( roomInfo['items']): 
                roomIDselected = roomInfo['items'] [chooseRoom]['id']
                roomNameSelected = roomInfo['items'] [chooseRoom]['title']
                messageToRoom = input("enter the message you want to send:")
                params = {'roomId':roomIDselected,'markdown':messageToRoom}
                url ='https://webexapis.com/v1/messages'
                res = requests.post(url, headers=headers,json=params)

                if res.status_code == 200:
                    print(f"\nmessagge :{messageToRoom} Succesfully SENT:{roomNameSelected}" )
                else:
                    print(f"\nERROR to send :{res.status_code}") 

else:
    print("\nPlease Enter 0 - 4 ONLY ")  
    userInput=input("\nPress any button to proceed")



         

