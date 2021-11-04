import random
from random_word import list_of_rand_words

word = random.choice(list_of_rand_words)
word_list = []
unique_letter = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())
        # if item in unique_letter:
        #     unique_letter.remove(item)

#print(word_list)
print(" ".join(word_list))
word_length = len(unique_letter) - 2
count_number = 1
already_tried = []
new_word = " ".join(word_list)

while count_number <= word_length:
    user_letter = input("Alege o litera ").lower()

    if user_letter == '':
        print('Introdu o litera')
        continue
    if user_letter in new_word:
        print("Litera este deja adaugata")
    elif user_letter in already_tried:
        print(f'Litera a fost deja incercata, literle deja incercate sunt: {" ".join(already_tried)}')
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(word_list)
            new_word = " ".join(word_list)
            print(new_word)
            already_tried.append(user_letter)
        else:
            count_number += 1
        if '_' not in "".join(word_list):
            print("Won")
            break
        elif count_number > word_length:
            print(f"Ai pierdut! Cuvantul era {word}")
        already_tried.append(user_letter)

