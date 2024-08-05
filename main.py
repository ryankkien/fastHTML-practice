from fasthtml.common import *

def render(todo):
    tid = todo.id
    toggle = A('Toggle', hx_get=f'/toggle{todo.id}')
    return Li(toggle, todo.title + ('w' if todo.done else ''))


app,rt,todos,Todo = fast_app('todosdb', live=True, render=render,
                             id=int, title=str, done=bool, pk='id')

@rt('/')
def get():
    return Titled('Todos',
                  Ul(*todos()),
                  )
    
@rt('/toggle/{tid}')
def get(tid):
    todo = todos[tid]
    todo.done = not todo.done
    return get()

serve() 