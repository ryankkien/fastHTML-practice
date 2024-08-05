from fasthtml.common import *

app,rt,todos,Todo = fast_app('todosdb', live=True,
                             id=int, title=str, done=bool, pk='id')

def render(todo):
    return Li(todo.title)

@rt('/')
def get():
    todos.insert(Todo(title="Second todo", done = False))
    items = [Li(o) for o in todos()]
    return Titled('Todos',
                  Ul(*todos()),
                  )
serve()