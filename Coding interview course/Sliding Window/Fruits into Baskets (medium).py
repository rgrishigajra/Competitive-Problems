# Write a function to return the maximum number of fruits in both the baskets. Same as Longest substring with K chars but k=2
def fruits_into_baskets(fruits):
    start_ptr = 0
    baskets = {}
    max_number_of_fruits = 0
    current_number_of_fruits = 0
    for end_ptr in range(len(fruits)):
        if fruits[end_ptr] not in baskets:
            if len(baskets) >= 2:
                current_number_of_fruits -= baskets[fruits[start_ptr]]
                del baskets[fruits[start_ptr]]
                while True:
                    start_ptr += 1
                    if fruits[start_ptr-1] != fruits[start_ptr]:
                        break
                baskets[fruits[end_ptr]] = 1
                current_number_of_fruits += 1
                max_number_of_fruits = max(
                    max_number_of_fruits, current_number_of_fruits)
            else:
                baskets[fruits[end_ptr]] = 1
                current_number_of_fruits += 1
                max_number_of_fruits = max(
                    max_number_of_fruits, current_number_of_fruits)
        else:
            baskets[fruits[end_ptr]] += 1
            current_number_of_fruits += 1
            max_number_of_fruits = max(
                current_number_of_fruits, max_number_of_fruits)
    return max_number_of_fruits


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
