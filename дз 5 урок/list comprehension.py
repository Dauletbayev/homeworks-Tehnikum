print('1)')
nums = [i for i in range(1, 100)]
even = [i for i in nums if i % 2 == 0]
print(even)

print('2)')
fruits = ["apple", "banana", "cherry", "orange", 'pineapple']
word_lengths = [len(l) * 2 for l in fruits]
print(word_lengths)

print('3)')
names = ['Pasha', 'Sasha', 'Pavel', 'Andrey', 'Dima', 'Denis']
sort = [y.upper() for y in names]
print(sort)

print('4)')
sortlow = [y[-1].upper() for y in names]
print(sortlow)

print('5)')
numbers = [a for a in range(0, 101)]
numsort = [a for a in nums if a % 2 == 0 and a % 5 == 0]
print(numsort)

print('6)')
number = [12, 13, 14, 30, 45, 67]
squared = [x ** 2 for x in number]
print(squared)

print('7)')
words = ['bake', 'smile', 'shake', 'want', 'stop', 'ask', 'attack', 'believe', 'close']
word = [q for q in words if q[-1] == 'e']
print(word)