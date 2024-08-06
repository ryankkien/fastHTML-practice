from fasthtml.common import *

def render(todo):
    tid = f'todo-{todo.id}'
    toggle = A('Toggle', hx_get=f'/toggle/{todo.id}', target_id=tid)
    delete = A('Del', hx_delete=f'/{todo.id}', hx_swap = 'outerHTML' ,target_id=tid)
    return Li(toggle, delete,
              todo.title + (' done' if todo.done else ''),
              id=tid)
    
app,rt,todos,Todo = fast_app('todosdb', live=True, render=render,
                             id=int, title=str, done=bool, pk='id')

@rt('/')
def get():
    return Titled('Todos',
                  Ul(*todos()),
                  )
    
@rt('/toggle/{tid}')
def get(tid:int):
    todo = todos[tid]
    todo.done = not todo.done
    todos.update(todo)
    return todo

@rt('/{tid}')
def delete(tid:int):
    todos.delete(tid)
    # return None #done automatically
    
serve()