import twitter

consumer_key = '***********************************'
consumer_secret = '*******************************************'
access_token = '****************************************'
access_secret = '*****************************************'



api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_secret)


print(api.VerifyCredentials())


follwers = api.GetFollowers()
friends = api.GetFriends()

status_var = 'HELLO MY FIRST PYTHON TWITTER'
post_update = api.PostUpdates(status=status_var)

length_status = twitter.twitter_utils.calc_expected_status_length(status=status_var)

new_messsage = api.PostDirectMessage(screen_name='pythoncodeine', text='Hi there')
print(new_messsage)

api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id=787079994451202048) #status_id = 787079994451202048
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()