sentence = input("Enter a sentence: ")
cap_sentence = sentence.title()
split_sentence = cap_sentence.split(" ")

split_sentence[0] = split_sentence[0].lower()

join_sentence = "".join(split_sentence)


print(join_sentence)