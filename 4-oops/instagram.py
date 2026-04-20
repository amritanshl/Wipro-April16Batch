class InstagramAccount:
    def __init__(self, username, bio, followers=0):
        self.username = username
        self.bio = bio
        self.followers = followers

    def __str__(self):
        return f"Instagram Account: {self.username}, Bio: {self.bio}, Followers: {self.followers}"
    
account1 = InstagramAccount("john_doe", "Travel enthusiast", 1500)
print(account1)
account2 = InstagramAccount("jane_smith", "Food lover", 2000)
print(account2)

amritaccount = InstagramAccount("amritansh_lal", "Tech and coding", 3000)
print(amritaccount)

del account1
try:
    print(account1)  # This will raise an error since account1 has been deleted 
except NameError:
    print("account1 has been deleted.")

#Advanced Inheritance
class BusinessAccount(InstagramAccount):
    def __init__(self, username, bio, followers=0, business_category="General", website=""):
        super().__init__(username, bio, followers)
        self.business_category = business_category
        self.website = website


    def __str__(self):
        return f"{super().__str__()}, Business Category: {self.business_category}, Website: {self.website}"
nike = BusinessAccount("nike", "Just Do It", 5000000, "Sportswear", "www.nike.com")
print(nike)
amritaccount = BusinessAccount("amritansh_lal", "Tech and coding", 3000, "Technology", "www.amritansh.com")
print(amritaccount)

class SecureAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute
        #_SecureAccount__password is the name mangled version of __password, which can be accessed from outside the class using this name.
    def login(self, attempted_password):
        if attempted_password == self.__password:
            return "Login successful!"
        else:
            return "Login failed. Incorrect password."
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return "Password changed successfully!"
        else:
            return "Password change failed. Incorrect old password."
secure_account = SecureAccount("john_doe", "securepassword123")
print(secure_account.login("wrongpassword"))  # Should fail
print(secure_account.login("securepassword123"))  # Should succeed

#_password is a convention to indicate that the attribute is intended to be protected, meaning it should not be accessed directly from outside the class, but it can still be accessed from subclasses.
#__password is a convention to indicate that the attribute is intended to be private, but it can still be accessed from outside the class.

class Post:
    def display(self):
        pass
class ImagePost(Post):
    def display(self):
        return "Displaying an image post."
class ReelPost(Post):
    def display(self):
        return "Displaying a video post."
class AdPost(Post):
    def display(self):
        return "Displaying an advertisement post."
image_post = ImagePost()
reel_post = ReelPost()
ad_post = AdPost()
print(image_post.display())
print(reel_post.display())
print(ad_post.display())

instagram_feed = [image_post, reel_post, ad_post]
for post in instagram_feed: 
    print(post.display())

class Instagram:
    def post_story(self, content):
        return f"Posting a story on Instagram: {content}"
class Whatsapp:
    def post_status(self, text):
        return f"Posting a status on WhatsApp: {text}"

def share_content(app_object, data):
    if isinstance(app_object, Instagram):
        return app_object.post_story(data)
    elif isinstance(app_object, Whatsapp):
        return app_object.post_status(data)
    else:
        return "Unsupported app."