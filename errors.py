from pyhtml import *

def e405():
    return str(html(
        head(
            title("uh oh!"),
            link(href="static/styles/error.css",rel="stylesheet")
        ),
        body(
            div(_class="text-container")(
                div(_class="uhoh")(h2("405:"),h1("Uh oh!")),
                p("You seem to have stumbled here by ",em("mistake"),"..."),
                p("Click",a("here")," to go back home!")
            )
        )
    ))

def e404():
        return str(html(
        head(
            title("uh oh!"),
            link(href="static/styles/error.css",rel="stylesheet")
        ),
        body(
            div(_class="text-container")(
                div(_class="uhoh")(h2("404:"),h1("Not Found.")),
                p("How did I get here? You seem to be in a ",em("strange")," place..."),
                p("Click",a("here")," to go back home!")
            )
        )
    ))

def e400():
        return str(html(
        head(
            title("uh oh!"),
            link(href="static/styles/error.css",rel="stylesheet")
        ),
        body(
            div(_class="text-container")(
                div(_class="uhoh")(h2("400:"),h1("Not Found.")),
                p("Erm... we couldn't do that for you. Maybe ",em("try again")," in a second?"),
                p("Click",a("here")," to go back home!")
            )
        )
    ))