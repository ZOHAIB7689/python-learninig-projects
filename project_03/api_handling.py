import requests 

def fetch_username ():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        userdata = data["data"]

        username = userdata["name"]["first"]
        location = userdata["location"]["city"]
        age = userdata["dob"]["age"]
        return username ,location,age
    else :
        raise Exception("Failed to fetch data")


def main():
    try:
        username , location, age = fetch_username()
        print(f"Name: {username} from: {location} , age:{age}")
    except Exception as e:
        print(str(e))

if __name__  == "__main__":
    main()