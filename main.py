from fasthtml.common import *

app,rt,todos,Todo = fast_app('todos.db', live=True, id =int, title=str, done=bool, pk = 'id') #sqLite

@rt('/') #router
#http req
def get():
    items = todos()
    return Titled('Todos',
                  Div(*items),
                  )

def createList(n):
    return Ul(*[Li(o) for o in range(n)])

@rt('/change') #grabbed when link is clicked
def get():
    return Div(P('Changed!!'))
serve()