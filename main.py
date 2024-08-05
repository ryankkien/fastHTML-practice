from fasthtml.common import *

app,rt = fast_app(live=True)

@rt('/') #router
def get(): return Titled('Greeting',
                         Div(P('Alive!!'), hx_get="/change")
                         )#http req

serve()