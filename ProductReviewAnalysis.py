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
            if keyword.capitalize() in review:
                review = review.replace(keyword.capitalize(), keyword.upper())
            review = review.replace(keyword, keyword.upper())
        uppercase_review.append(review)
    return uppercase_review

# call function and pass through reviews list and feedback list
uppercase_review = uppercase_feedback(reviews, feedback)

#displays updated reviews with the capitallized keywords
for review in uppercase_review:
    print(review)