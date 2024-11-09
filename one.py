# 1. Even or Odd

def even_or_odd(number=3):
    if (number % 2) == 0:
        print("even")
        result = "Even"
    else:
        print("Odd")
        result = "Odd"
    return result

result = even_or_odd()
print(result)

# 2. Int to Str

def number_to_string(num):
    print(str(num))
    return str(num)

# 3. Vowel Count

def get_count(sentence): 
    vowels = ["a", "e", "i", "o", "u"] 
    count = sum(1 for char in sentence if char in vowels) 
    
    return count