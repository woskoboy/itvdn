""" Найти гласные, которые присутствуют в каждом 
введенном через запятую слове  """

chars = {'a', 'e', 'y', 'i', 'u', 'o'}
# words = input('Enter a string: ').split(', ')
words = 'bseuti, fueri, myuia, rieuo'.split(', ')

for word in words:
    """ обновляем мн-во оставляя только те буквы,
    кот-е есть(пересекаются с буквами) в текущем слове """
    chars.intersection_update(word.lower())

print('\n'.join(chars))
