from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
import pyperclip

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


global text
text = ""
global new_text
new_text = ""

@app.route('/convert', methods=['POST'])
def convert():
    global text
    global new_text

    text = request.form['text']
    text = text.replace('\r', "")

    text_file = open("static/TextToHtml.txt", "w")
    text_file.write(text)
    text_file.close()

    contents = open("static/TextToHtml.txt", "r")

    with open("html.txt", "w") as e:
        for lines in contents.readlines():
            lines = lines.replace("\r", "")
            if lines != "\n":
                lines = lines.replace("\n", "")
                e.write(f"<p>{lines}</p>\n")
            if lines == "\n":
                e.write("<br>\n")
    contents.close()

    with open('html.txt', 'r') as file:
        new_text = file.read()

    return render_template("index.html", new_text=new_text, text=text)

@app.route('/copy')
def copy():
    global text
    global new_text
    pyperclip.copy(new_text)
    return render_template("index.html", text=text, new_text=new_text)


if __name__ == "__main__":
    app.run(debug=True)
