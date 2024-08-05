from fasthtml.common import *

app,rt = fast_app(live=True)

@rt('/') #router
#http req
def get():
    nums = Ul(*[Li(o) for o in range(10)])
    return Titled('Greeting',
                         Div(P('Alive!!')),
                         P(A('Link', href = '/change'))
                         )


@rt('/change') #grabbed when link is clicked
def get():
        return Titled('Change',
                      Div(P('Changed!!')),
                    P(A('Home', href= '/'))
        )
serve()