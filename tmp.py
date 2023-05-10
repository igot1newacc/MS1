import sys
import requests

# Set up your bot's token and the channel ID for where you want to send messages
TOKEN = "ODg2NDQ4ODQzNTUyNTg3Nzc3.GGVuUl.JFsTrs511agJBXfgCyLRAcespk0n8kFaatk4M0"
CHANNEL_ID = 1104762876574568488 # Replace with the actual ID of the channel you want to send messages to

# Override the default standard output to send messages to Discord
class DiscordOutput:
    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.header = {
            'authorization': self.token
        }

    def write(self, message):
        payload = {
            'content': message
        }
        requests.post(f"https://discord.com/api/v9/channels/{self.channel_id}/messages", data=payload, headers=self.header)

# Create an instance of DiscordOutput and redirect standard output to it
discord_output = DiscordOutput(TOKEN, CHANNEL_ID)
sys.stdout = discord_output

# Test the new output
print('Hello, world! from VS')

# Redirect standard output back to console
sys.stdout = sys.__stdout__