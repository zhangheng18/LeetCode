import heapq


class User:
    def __init__(self, user_id):
        self.followed = set()
        self.id = user_id
        self.tweet_head = None

        self.followed.add(user_id)

    def follow(self, user_id):
        self.followed.add(user_id)

    def unfollow(self, user_id):
        # 不能取关自己
        if user_id != self.id and user_id in self.followed:
            self.followed.remove(user_id)

    def post(self, tweet_id, time):
        tweet = Tweet(tweet_id, time)
        tweet.next = self.tweet_head
        self.tweet_head = tweet


class Tweet:
    __slots__ = ('id', 'time', 'next')

    def __init__(self, tweet_id, time):
        self.id = tweet_id
        self.time = time
        self.next = None

    def __lt__(self, other):
        # heapq 最小堆，弹出的总是最小的， 这里按时间戳（最新）比较
        return self.time > other.time


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.user_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 新建用户
        if userId not in self.user_map:
            self.user_map[userId] = User(userId)
        # 发表推文
        self.user_map[userId].post(tweetId, self.timestamp)

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_map:
            return []
        user = self.user_map[userId]

        result = []
        pq = []
        followed_list = list(user.followed)
        # 取出所有关注者的最新推文
        for followed in followed_list:
            if tweet := self.user_map[followed].tweet_head:
                heapq.heappush(pq, tweet)

        # 获取最新的10条
        while pq:
            if len(result) == 10:
                break
            tweet = heapq.heappop(pq)
            result.append(tweet.id)
            # 放入下一条
            if tweet.next:
                heapq.heappush(pq, tweet.next)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # 关注
        if followerId not in self.user_map:
            self.user_map[followerId] = User(followerId)
        if followeeId not in self.user_map:
            self.user_map[followeeId] = User(followeeId)

        self.user_map[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 取关
        if followerId in self.user_map:
            self.user_map[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
