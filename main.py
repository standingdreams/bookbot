def read_file(file):
  with open("books/frankenstein.txt") as f:
    return f.read()

def get_word_count(file):
  words = file_contents.split()
  return len(words)

def sort_on(dict):
    return dict["count"]

def char_count_fn(file):
  lower_case = file.lower()
  char_count = {}
  for char in lower_case:
    if char not in char_count:
      char_count[char] = 1
    else:
      char_count[char] += 1
  return char_count

def is_letter(char):
  return char.isalpha()

def char_aggregate(file):
  file_contents = read_file(file)
  char_count = char_count_fn(file_contents)
  list_of_dicts = []
  for char in char_count:
    dict = {"char": char, "count": char_count[char]}
    list_of_dicts.append(dict)
  list_of_dicts.sort(reverse=True, key=sort_on)

  for dict in list_of_dicts:
    if is_letter(dict["char"]):
      print(f"The '{dict["char"]}' was found {dict["count"]} times")


with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  # word_count = get_word_count(file_contents)
  char_aggregate(file_contents)
