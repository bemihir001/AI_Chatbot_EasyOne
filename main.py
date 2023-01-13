user_input = input("Enter a string: ")

# split the input into a list of words
words = user_input.split()

# initialize an empty result string
result = ""

# loop through each word in the list
for word in words:
  # check if the length of the word is 1
  if len(word) == 1:
    # if the length is 1, add the word to the result string
    result += word
  else:
    # if the length is not 1, break out of the loop
    break

print(result)