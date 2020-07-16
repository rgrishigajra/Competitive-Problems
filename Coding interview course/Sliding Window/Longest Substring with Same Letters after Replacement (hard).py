# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
def length_of_longest_substring(str, k):
  characters={}
  window_start,max_length,max_length,curr_length,max_char_freq=0,0,0,0
  for char in range(len(str)):
    if str[char] in characters:
      characters[str[char]]+=1
    else:
      characters[str[char]]=1
    curr_length+=1
    max_char_freq=max(characters[str[char]], max_char_freq)
    if curr_length-max_char_freq>k:
      curr_length -= characters[str[window_start]]
      del characters[str[window_start]]
      while True:
        window_start +=1
        if str[window_start] != str[window_start -1]:
          break
    max_length=max(curr_length,max_length)
  return max_length

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()