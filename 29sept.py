def my_decorator(func):
    def wrapper(self):
        print('I can return a value')
        return func(self)
    return wrapper

class Stars:
    @my_decorator
    def symbols(self):
        return '*)*)*)!'

if __name__ == '__main__':

    stars = Stars()
    print(stars.symbols())
























#surname = len('Lisovskaya')
#factorial = 1
#while surname > 1 :
#    factorial *= surname
#    surname -=1
#print(factorial)

#text = "apple"
#for i in range(len(text)):
#    print(text[i])

#temp = []
#for i in range(0, 10):
#    if i % 2:
#        continue
#    temp.append(i)
#print(sum(temp))


#x = 10
#for i in [1,2,3,4,5]:
#    if i % 2 == 0:
#        break
#    x -= i
#else:
#    x = 10
#print(x)


#zoo = [
#	['monkey', 'tiger', 'elephant'],
#	['frog', 'snake'],
#	['owl', 'pigeon'],
#	['hamster', 'mouse', 'hedgehog']
#]
#zoo_a = []
#for animals in zoo:
#  for a_words in animals:
#      if 'a' in a_words:
#         a_words.append(zoo_a)
#print(zoo_a)

#import json

#username = input("Your name?")
#with open('experiment.txt', 'w') as file_object:
#	file_object.write(username)

#with open('experiment.txt') as data:
#	data_to_print = data.read(),'r'
#	print(type(data_to_print))

