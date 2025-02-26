names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
name_age_dict = print(dict(zip(names, ages)))

text = "python"
indexed_text = print(list(enumerate(text, start=1)))

numbers = ["10", "20", "30", "40"]
int_numbers = print(list(map(int, numbers)))

words = ["apple", "banana", "cherry", "dog", "elephant"]
filtered_words = print(list(filter(lambda w: w.startswith("d"), words)))

numbers = [1, -2, 3, -4, 5, -6]
positive_squared = print(list(map(lambda x: x**2, filter(lambda x: x > 0, numbers))))

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
filtered_students = print(list(enumerate(filter(lambda s: s[1] > 80, zip(students, scores)), start=1)))


