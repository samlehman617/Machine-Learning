"""
Module to interact with GroupMe.

Scrapes data from GroupMe, parses it, and uses it to train a tensorflow chatbot
Chatbot then uses GroupMe APIs to interact with GroupMe
"""

base_url = "http://api.groupme.com/v3"
groups = []
bots = []


def main():
    """Main."""
    pass


class User:
    """Class representing a user."""

    name = ""
    id = ""
    picture = None

    def __init__(self):
        """Create a user object."""
        pass

    def get_groups(self, user):
        """Return the groups a user is in."""
        req = "GET /groups"


class Chatbot(User):
    """Class representing a single chatbot."""

    def reply(self, group):
        """Post a response in the specified group."""
        if self.name in groups:
            pass

    def train(self):
        """Train bot on entire dataset."""

ass

    def read(self):
        """Read a message."""
        pass


class Group:
    """Class representing a GroupMe group."""

    name = ""
    id = ""
    
    def __init__(self):
    
    def scrape(self):
        """Scrape the group for data."""
        pass

    def get_users(self):
        """Return all users in the group."""
        pass

    def get_chat(self, chatid):
        """Return the chat data."""
        pass


if __name__ == "__main__":
    main()
