from django import template
register = template.Library()

def index(element, liste):

  return liste.index(element)

def word_list(elements):

  tab=elements.split('\r\n')
  term=' '.join(tab)
  liste=term.split(' ')
  return liste

register.filter(word_list)
register.filter(index)
