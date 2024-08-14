#Task 1: Keyword Highlighter
#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
# keywords placed in list
feedback = ["good", "excellent", "bad", "poor", "average"]

# funciton  goes through list of reviews and replaces keywords with uppercase keyword
def uppercase_feedback(reviews, feedback):
    uppercase_review = []
    for review in reviews:
        for keyword in feedback:
            if keyword.capitalize() in review: #selects the capitalized keyword and makes it uppercase
                review = review.replace(keyword.capitalize(), keyword.upper())
            review = review.replace(keyword, keyword.upper())
        uppercase_review.append(review)
    return uppercase_review

# call function and pass through reviews list and feedback list
uppercase_review = uppercase_feedback(reviews, feedback)

#displays updated reviews with the capitallized keywords
for review in uppercase_review:
    print(review)

# Task 2 Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# function that counts positive and negative words used in review list
def finding_review_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    for review in reviews:
        for positive in positive_words: # loops through positive words list, checking both uppercase and capitalized words
            if positive.capitalize() or positive.upper() in review:
                positive_count += review.count(positive) 
        for negative in negative_words: # loops through negative list same way as the postive
            if negative.capitalize() or negative.upper() in review:
                negative_count += review.count(negative)
            negative_count += review.count(negative)
    return print(f"\nPositive word count: {positive_count} \nNegative word count: {negative_count}\n")

# calls tally function
finding_review_tally(reviews, positive_words, negative_words)

#Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
#Ensure that the summary does not cut off in the middle of a word.

def summarize_review(reviews):
    max_length =  30
    if len(review) <= max_length: #displays full review if under 30 characters
        return print(review)
    elif len(review) > max_length: 
        if review[max_length] != " ":
            space = review.find(" ", max_length) #finds where the word ends after 30 mark
            short_review = review[max_length:space] #characters between 30 mark and next space
            final_review = review[:max_length] + short_review + "..." #adds remaining words to the 30 mark and puts "..." at the end
            return print(final_review)
        
# loops through each review and calls the summary function
for review in reviews:
    summaries = summarize_review(reviews)


