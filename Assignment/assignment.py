def popular(l):
  # Create an empty dictionary to store the word counts
  word_counts = {}
  
  # Iterate through the list of words

  for word in l:
    # If the word is not in the dictionary, add it and set its count to 1

    if word not in word_counts:
      word_counts[word] = 1
    # If the word is already in the dictionary, increment its count by 1
    
    else:
      word_counts[word] += 1
  
  # Find the word with the highest count
  most_common_word = None
  highest_count = 0