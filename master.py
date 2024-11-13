from flask import Flask, request, session, flash, redirect, send_file
from pyhtml import *
from auth import *
from func import *
from errors import *
from datamanager import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'noonewillexpectiputthewordcapybarainthesecretkey' 

# static -> landing
@app.route('/', methods=['GET', 'POST'])
def landing():
    landingPage = html(
        head(
            title("lecture summarizer"),
            link(href="static/styles/landing.css",rel="stylesheet")
        ),
        body(
            div(_class="navbar")(
                img(alt="logo",height="40",width="40",src="static/assets/transcriptionSqJpeg.jpg"),
                div(
                    a(href="https://github.com/rerealising/transcript-summarizer")("Source Code"),
                    a(href="https://github.com/rerealising/transcript-summarizer/blob/main/README.md#about-the-project")("How it Works"),
                    a(href="https://x.com/rerealising")("Contact Us")
                ),
                div(_class="auth-buttons")(
                    a(id="login",href="/login")("Log in"),
                    a(id="signup",href="/signup")("Sign up")
                )
            ),
            div(_class="container")(
                div(_class="content")(
                    div(_class="text")(
                        h1("study lazier,",br(),"not harder."),
                        p("Hate long lectures? We do too."),
                        p("Sit back & relax - let ",strong(style="font-weight:1000;")("us")," write your notes!"),
                        div(_class="buttons")(
                            a(id="demo",href="/signup")("Try It for Free"),
                            a(id="info",href="https://github.com/rerealising/transcript-summarizer#getting-started")("More Info")
                        )
                    ),
                    div(_class="image")(
                        img(alt="illustration of a classroom lecture",height="300",src="static/assets/lecture.svg")
                    )
                )
            ),
            div(_class="footer")(
                p(id="powered")("Powered by"),
                a(href="https://deepmind.google/technologies/gemini/")(img(src="static/assets/gemini_logo.png"))
            ),
            div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
        )
    )
    return str(landingPage)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect("/dashboard")
    loginPage = str(html(
        head(
            title("login"),
            link(href="static/styles/login.css",rel="stylesheet")
        ),
        body(
            div(_class="login-container")(
                h1("login"),
                form(method="POST",action="/login")(
                    input(type="text",id="username",placeholder="username",required="True",name="username"),
                    input(type="password",id="password",placeholder="password",required="True",name="password"),
                    button(type="submit")("log in")
                ),
                div(_class="no-acc")(
                    a(href="/signup")("don't have an account?")
                )
            ),
            div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
        )
    ))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        users = load_users()

        if username in users and users[username] == password:
            session['username'] = username
            return redirect("/dashboard")
        else:
            loginPage = str(html(
                head(
                    title("login"),
                    link(href="static/styles/login.css",rel="stylesheet")
                ),
                body(
                    div(_class="login-container")(
                        h1("login"),
                        form(method="POST",action="/login")(
                            p(style="color:red;")("incorrect username or password!"),
                            input(type="text",id="username",placeholder="username",required="True",name="username"),
                            input(type="password",id="password",placeholder="password",required="True",name="password"),
                            button(type="submit")("log in")
                        ),
                        div(_class="no-acc")(
                            a(href="/signup")("don't have an account?")
                        ),
                    ),
                    div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
                )
            ))

    return str(loginPage)

# signup page
# password validation rules: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])\S{8,16}$
# js is used for dynamic feedback on password
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect("/dashboard")
    signupPage = str(html(
        head(
            title("signup"),
            link(href="static/styles/signup.css",rel="stylesheet")
        ),
        body(
            div(_class="signup-container")(
                h1("signup"),
                form(
                    input(type="text",id="username",placeholder="username",required="True",name="username",pattern="[a-zA-Z0-9]{4,16}"),
                    input(type="password",id="password",placeholder="password",required="True",name="password",pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])\S{8,}$"),
                    div(id="message",style="visibility:hidden;height:0")(
                        b("password must contain at least:"),
                        p(id="lower",_class="invalid")("1 lowercase letter"),
                        p(id="upper",_class="invalid")("1 uppercase letter"),
                        p(id="number",_class="invalid")("1 number"),
                        p(id="special",_class="invalid")("1 special character"),
                        p(id="length",_class="invalid")("8 characters")
                    ),
                    button(type="submit")("sign up")
                ),
                script(src="static/scripts/signup.js"),
                div(_class="have-acc")(
                    a(href="/login")("already have an account?")
                )
            ),
            div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
        )
    ))
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        users = load_users()
        
        if username in users:
                signupPage = str(html(
                    head(
                        title("signup"),
                        link(href="static/styles/signup.css",rel="stylesheet")
                    ),
                    body(
                        div(_class="signup-container")(
                            h1("signup"),
                            form(
                                p(style="color:red;")("username already exists!"),
                                input(type="text",id="username",placeholder="username",required="True",name="username",pattern="[a-zA-Z0-9]{4,16}"),
                                input(type="password",id="password",placeholder="password",required="True",name="password",pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])\S{8,}$"),
                                div(id="message",style="visibility:hidden;height:0")(
                                    b("password must contain at least:"),
                                    p(id="lower",_class="invalid")("1 lowercase letter"),
                                    p(id="upper",_class="invalid")("1 uppercase letter"),
                                    p(id="number",_class="invalid")("1 number"),
                                    p(id="special",_class="invalid")("1 special character"),
                                    p(id="length",_class="invalid")("8 characters")
                                ),
                                button(type="submit")("sign up")
                            ),
                            script(src="static/scripts/signup.js"),
                            div(_class="have-acc")(
                                a(href="/login")("already have an account?")
                            )
                        ),
                        div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
                    )
                ))
        else:
            users[username] = password
            save_users(users)
            session['username'] = username
            return redirect("/dashboard")
    return str(signupPage)

# logout method, not a page!
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect("/")

# dashboard
# js is used for dynamic display of different types of inputs + dynamic textbox size
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    dashboardPage = str(html(
        head(
            title("dashboard"),
            link(href="static/styles/dashboard.css",rel="stylesheet")
        ),
        body(
            div(_class="logo")(
                img(alt="logo of transcript summarizer",height="60px",length="60px",src="static/assets/transcriptionSqJpeg.jpg"),
                h1("lecture summarizer")
            ),
            form(action="/response")(
                div(_class="container")(
                    div(_class="dropdown")(
                        label(_for="options")("choose an option:"),br(),
                        select(id="options",name="service")(
                            option(value="")("---"),
                            option(value="option1")("transcript"),
                            option(value="option2")("YouTube link"),
                            option(value="option3",disabled=True)("echo360 - deprecated, transcripts are now downloadable")
                        )
                    ),
                    div(_class="textbox",id="textbox")(
                        label(_for="inputText")("enter link:"), br(),
                        input(id="inputText",placeholder="link here...",type="url",name="link"),
                        div(_class="submitbutton")(button("summarize"))
                    ),
                    div(_class="textbox",id="textAreaBox",style="display:none;")(
                        label(_for="inputTextArea")("enter transcript:"), br(),
                        textarea(id="inputTextArea",placeholder="paste transcript here...",name="transcript"),
                        div(_class="submitbutton")(button("summarize"))
                    )
                )
            ),
            a(href="/notes")(div(_class="viewnotes")(button("view past notes"))),
            a(href="/logout")(div(_class="logoutbutton")(button("log out"))),
            script(src="static/scripts/dashboard.js"),
            div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
        )
    ))
    if 'username' not in session:
        return redirect("/login")
    return dashboardPage

@app.route('/response', methods=['GET','POST'])
def response():
    if request.method == 'GET':
        return e405()
    if request.form.get("service") == "option1":
        transcript = request.form.get("transcript")
        result = summarize(transcript)
        session['result'] = result
        contentuuid = createDoc(result)
        return redirect(f"/view?doc={contentuuid}")
    if request.form.get("service") == "option2":
        YTLink = request.form.get("link")
        if YTValidate(YTLink) == True:
            transcript = getYTTranscript(YTLink)
            result = summarize(transcript)
            session['result'] = result
            contentuuid = createDoc(result)
            return redirect(f"/view?doc={contentuuid}")
        return e400()
    return e404() # error failsafe

# notes -> list of previous notes
@app.route('/notes', methods=['GET','POST'])
def notes():
    if 'username' not in session:
        return redirect("/login")
    user = session['username']
    doctree = docList(user)
    print(doctree)
    notesPageChild = ()
    for uuid in doctree:
        notesPageChild += li(_class="document-item")(
            img(alt="document icon",height="50px",width="50px",src="static/assets/transcriptionSqJpeg.jpg"),
            div(_class="document-info")(h2(f"{doctree[uuid]}")),
            div(_class="document-actions")(
                a(href=f"/view?doc={uuid}")(i(_class="fas fa-eye")),
                a(href=f"/download?doc={uuid}")(i(_class="fas fa-download")),
                a(href=f"/delete?doc={uuid}")(i(_class="fas fa-trash-alt"))
            )
        ),
    notesPage = str(html(
        head(
            title("notes"),
            link(rel="stylesheet",href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"),
            link(rel="stylesheet",href="static/styles/notes.css"),
            script(src="static/scripts/notes.js")
        ),
        body(
            div(_class="container")(
                h1("lecture summarizer"),
                div(_class="search-bar")(input(id="searchInput",onkeyup="filterDocuments()",placeholder="search by title...",type="text")),
                div(id="no-result")(p("no results :(")),
                ul(_class="document-list")(
                    notesPageChild
                )
            ),
            div(_class="back")(a(href="/dashboard")(button("back"))),
            div(_class="copyright")("© rere 2024 - GNU GPL v3.0")
        )
    ))
    return notesPage

# view past notes
@app.route('/view', methods=['GET','POST'])
def view():
    if 'username' not in session:
        return redirect("/login")
    docid = request.args.get('doc')
    doc = getDoc(docid)
    return str(head(title("viewing your notes..."),link(rel="stylesheet",href="static/styles/universalnotes.css"))) + doc + str(div(_class="back")(a(href="/notes")(button("✕"))))

@app.route('/delete', methods=['GET','POST'])
def delete():
    if 'username' not in session:
        return redirect("/login")
    docID = request.args.get('doc')
    if deleteDoc(docID):
        session['req'] = "delete"
        return redirect("/notes")
    return e400()

@app.route('/download', methods=['GET','POST'])
def download():
    if 'username' not in session:
        return redirect("/login")
    docID = request.args.get('doc')
    with open('data/_userdocs.json', 'r') as f:
        userData = json.load(f)
    if docID in userData[session['username']]:
        try:
            send_file(f"data/{docID}.html", as_attachment=True)
            session['req'] = "download"
            return send_file(f"data/{docID}.html", as_attachment=True)
        except:
            return e404()


@app.route('/debug', methods=['GET','POST'])
def debug():
    newDocLog("12sdafasdf3")
    return "Complete"

if __name__ == "__main__":
    app.run(port=50001,debug=True)