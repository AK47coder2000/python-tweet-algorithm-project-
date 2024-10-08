# Define a function to clean tweet text

# function takes a tweet as input and converts 
# all characters to lowercase to ensure case-insensitive comparison
# and returns the cleaned tweet.
def clean_tweet(tweet):
    tweet = tweet.lower()                                               #converting all the tweets into lowercase tweet
    return tweet                                                        #after converting it to the lowercase return the tweet

#define list of positive and negative words

#the two lists "positive_words" and "negative_words" contain words 
#associated with positive and negative sentiments.

positive_words = [
    "love", "great", "fantastic", "amazing", "wonderful", "good", 
    "enjoyed", "best", "positive", "happy", "awesome", "beautiful", 
    "like","beautifully","welcoming","stunning","suited"
]
negative_words = [
    "hate", "horrible", "terrible", "bad", "boring", "worst", 
    "negative", "sad", "angry", "disgusting", "awful", "stinks", 
    "bored","poorly","stressful","couldn't","shrunk","ruined",
    "cheap","didn't","depressing","gloomy","loud","crowded"
]

# Define a function to determine sentiment

def determine_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)                                   #clean the tweet
    words = cleaned_tweet.split()                                        # to determine the sentiments split the cleaned tweet into individual words
    sentences = cleaned_tweet.split(".")
    for sentence in sentences:
        split_sentence = sentence.split()
    positive_count = sum(1 for word in words if word in positive_words)  #count positive words
    negative_count = sum(1 for word in words if word in negative_words)  #count negative words

#determine sentiment

    if positive_count > negative_count:                                  #if positive words are more then negative words 
        return "Positive"                                                #then return "positive"
    
    elif negative_count > positive_count:                                #if negative words are more then positive words
        return "Negative"                                                #then return "negative"
    
    else :                                                               # if counts are equal
        return "Neutral"                                                 # then return "netural"


# Define topics

#this list contains all given topics in assignment
topics = [
    "movie",
    "weather",
    "game",
    "clothes",
    "restaurant",
    "food",
    "party",
    "day",
    "dress",
    "house",
    "show",
    "dance",
    "holiday",
    "vacation",
    "outfit",
    "shoes",
    "shirt",
    "song",
    "concert"
]
#sample tweets
list_of_tweets = ["That movie was great",
        "The weather stinks today",
        "The basketball game was boring",
        "That movie was boring",
        "That movie was beautiful",
        "We went to the movies. I was bored out of my mind.",
        "We went to the movies. The movie was boring.",
        "We went to the movies. The movie was boring. We then went to eat at the best restaurant in the city and it was wonderful.",
        "Your dress is beautiful",
        "The movie was neutral",
        "I love this song",
        "Today we went to a concert. it was poorly organized",
        "My firends love my outfit",
        "Alex bought gucci shoes. i really like his shoes",
        "we really enjoyed the comedy show",
        "The vacation we went last time was horrible",
        "The food at the party was so good, i enjoyed it alot.",
        "The house we visited was beautifully decorated and felt very welcoming.",
        "The dance class was too advanced for me, i couldn't keep up with the steps.",
        "The Shirt shrunk in the wash and is now too small to wear.",
        "The holiday traffic was terrible, the whole holiday got ruined",
        "The dress she wore to the event was stunning and suited her perfectly",
        "The clothes i ordered online didn't fit well and the material felt cheap",
        "The weather has been gloomy and rainy all week, it's quite depressing",
        "The restaurant we went to last night was amazing, the food was delicious and the service was good",
        "The party was too loud and crowded, i could barely hear myself."
]

#now analyze tweet and print results
def analyze_and_print_results(tweets, topics):

    #loop through tweets
    for i, tweet in enumerate(tweets, start=1):                                                    #Enumerate through tweets starting with index 1

        sentiment = determine_sentiment(tweet)                                                     #determine the sentiment of the tweet

        cleaned_tweet = clean_tweet(tweet)                                                         #clean the tweet

        for topic in topics:                                                                       #check each topic is found in the cleaned tweet

            if topic in cleaned_tweet:                                                             #if the topic is found in the cleaned tweet

                print(f"Tweet #{i} expressed a {sentiment.lower()} opinion about a {topic}.")      #print the result


# run the analyisis and print the result

#this line calls the "analyze_and_print_results" function with the sample tweets and topics.
analyze_and_print_results(list_of_tweets,topics)