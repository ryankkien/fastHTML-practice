from fasthtml.common import *

app,rt = fast_app(live=True)

@rt('/') #router
#http req
def get():
    nums = createList(10)
    return Titled('Greeting', nums,
                         Div(P('Alive!!')),
                         P(A('Link', href = '/change'))
                         )

def createList(n):
    return Ul(*[Li(o) for o in range(n)])

@rt('/change') #grabbed when link is clicked
def get():
        return Titled('Change',
                      Div(P('Changed!!')),
                    P(A('Home', href= '/'))
        )
serve()