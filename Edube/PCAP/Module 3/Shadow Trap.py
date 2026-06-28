class Settings:
    theme = "Light"  # Class Variable

user1 = Settings()
user2 = Settings()

# User 1 customizes their theme
user1.theme = "Dark"

# A global update changes the default theme for everyone
Settings.theme = "Blue"
