
import requests
import json

acc_token = input("Please enter your access token")
print("\nMENU OPTION")
print("-" * 130 )
print("Test connection (0)")
print("Display User Information (1)")
print("Display 5 Rooms (2)")
print("Create a room (3)")
print("Send message to a room (4)")
print("-" * 130 )

option=input("\nplease choose option: ")
headers = {
    'Authorization' : 'Bearer {}'. format(acc_token),
    'Content-Type' : 'application/json'
}
url='https://webexapis.com/v1/people/me'
res = requests.get(url, headers=headers)

if option== "0":
    if res.status_code == 200:
        print("\nconnection to webex server successfull")
    else:
        print("\nconnection to webex server failed")

elif option == "1":
        
        userInfo = res.json()
        print("USER INFORMATION")
        print("*" * 130)
        print(f"User Displayed name: {userInfo['displayName']} ")
        print(f"User Nickname: {userInfo['nickName']}")
        print(f"User email: {', '.join(userInfo['emails'])}")
        print("*" * 130)

elif option == "2":
     url='https://webexapis.com/v1/rooms'
     params={'max':'5'}
     res=requests.get(url,headers=headers, params=params)
     roomInfo = res.json()
     
     if res.status_code == 200:

         if'items' in roomInfo:
                print("ROOM INFORMATION")
                print("*" * 120)
                for item in roomInfo['items']:
                        
                    print(f"Room Id: {item['id']} ")
                    print(f"Room name: {item['title']}")
                    print(f"room's date created: {item['created']}")
                    print(f"Last activity: {', '.join(item['lastActivity'])}")
                    print("*" * 120)

elif option == "3":
     url='https://webexapis.com/v1/rooms'
     roomName=input("give the room to want to create a name :")
     params={'title': roomName}

     res = requests.post(url, headers=headers, json=params)
     if res.status_code == 200:
          print(f" \nroom:{roomName} has been created")
     else:
          print(f"\nfailed to create a room due to {res.status_code}")

elif option == "4":

        url='https://webexapis.com/v1/rooms'
        params={'max':'5'}
        res=requests.get(url,headers=headers, params=params)
        roomInfo = res.json()

        if res.status_code == 200:
            print("\tROOMS")
            print("*" * 120)
            for i,item in enumerate ( roomInfo['items']):
                print(f" ({i + 1}) {item['title']}")

                print("*" * 120)
            roomChoice=int(input("\nplease choose a room you want to send a message:"))-1

            if 0 <= roomChoice <len( roomInfo['items']): 
                roomIDselected=roomInfo['items'] [roomChoice]['id']
                roomNameSelected=roomInfo['items'] [roomChoice]['title']
                messageToRoom=input("enter the message you want to send:")
                params={'roomId':roomIDselected,'markdown':messageToRoom}
                url='https://webexapis.com/v1/messages'
                res=requests.post(url, headers=headers,json=params)

                if res.status_code == 200:
                    print(f"\nmessagge :{messageToRoom} is sent successfully to room :{roomNameSelected}" )
                else:
                    print(f"\nfailed to send message due to error:{res.status_code}") 
        
else:
    print("\nplease choose the right option")  
userInput=input("\npress enter to enter to main menu.........")





