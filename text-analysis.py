text = input("Enter a block of text: ")
words = text.split()
word_count = len(words)
frequency ={}
for word in words:
    clean_word =word.lower().strip(".,!?;:\"'")
    if clean_word in frequency:
        frequency[clean_word] += 1
    else:
        frequency[clean_word] = 1
      
most_common = ""
highest_count =0
for word, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_common = word

total_letters = 0
for word in words:
    total_letters += len(word)
average_length = total_letters / word_count

print("\nText Analysis")
print("Total words:",word_count)
print("Most common word:",most_common, "(appears", highest_count, "times)")
print("Average word length:",round(average_length, 2))
