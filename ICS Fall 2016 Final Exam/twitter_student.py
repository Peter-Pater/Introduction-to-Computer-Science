

class Twitter:
    def __init__(self):
        self.all_users = []
        self.all_tweets = {}

    def get_users(self):
        return self.all_users

    def get_num_users(self):
        return len(self.all_users)

    def get_tweets(self, following):
        # TODO: Implement this function
        # After you implement the method, remember to delete pass
        tweets = {}
        for i in following:
            tweets[i] = self.all_tweets[i]
            tweets[i].reverse()
        return tweets

    def add_user(self,new):
        self.all_users.append(new)
        self.all_tweets[new] = []

    def add_tweet(self, user, tweet):
        # TODO: Implement this function
        # After you implement the method, remember to delete pass
        self.all_tweets[user].append(tweet)

class User:
    def __init__(self, twitter):
        self.twitter = twitter
        self.my_id = twitter.get_num_users()
        twitter.add_user(self.my_id)
        self.following = []

    def post_tweet(self, tweet):
        # TODO: Implement this function
        # After you implement the method, remember to delete pass
        self.twitter.add_tweet(self.my_id, tweet)

    def get_news_feed(self):
        # TODO: Implement this function
        # After you implement the method, remember to delete pass
        result = []
        tweets = self.twitter.get_tweets(self.following)
        for user in tweets:
            for msg in tweets[user]:
                result.append((user, msg))
        return result

    def follow(self, other):
        self.following.append(other)

    def unfollow(self, other):
        if other in self.following:
            self.following.remove(other)

def main():
    my_twitter = Twitter()

    user0 = User(my_twitter)
    user0.post_tweet("Hello world!")
    user0.post_tweet("Good morning!")
    user0.post_tweet("Good afternoon!")

    user1 = User(my_twitter)
    user1.post_tweet("Apple")
    user1.post_tweet("Orange")
    user1.post_tweet("Strawberry")

    user2 = User(my_twitter)
    user2.post_tweet("New York")
    user2.post_tweet("Shanghai")
    user2.post_tweet("London")
    for i in range(9):
        user2.post_tweet(str(i))

    user0.follow(1)
    user0.follow(2)
    user1.follow(0)

    result0 = user0.get_news_feed()
    result1 = user1.get_news_feed()
    result2 = user2.get_news_feed()

    print("\nThe news feed for user 0 is as following:")
    for inner in result0:
        print("User",inner[0],"posted:",inner[1])

    print("\nThe news feed for user 1 is as following:")
    for inner in result1:
        print("User",inner[0],"posted:",inner[1])

    print("\nThe news feed for user 2 is as following:")
    for inner in result2:
        print("User",inner[0],"posted:",inner[1])


main()

