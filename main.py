from flask import Flask, render_template, flash, request, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/caesarcipher/", methods=["POST", "GET"])
def caesarcipher():
    try:
        if request.method == "POST":
            txt = request.form['unEncryptedTxt'].lower()
            shift = int(request.form['shift'])
            txtOut = ""
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
            for i in txt:
                if i != " ":
                    position = alphabet.index(i)
                    position = (position + shift) % 26
                    letter = alphabet[position]
                    txtOut += (letter)

            output1=txtOut

            txt = request.form['encryptedTxt'].lower()
            txtOut = ""
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
            for i in txt:
                if i != " ":
                    position = alphabet.index(i)
                    position = (position - shift) % 26
                    letter = alphabet[position]
                    txtOut += (letter)

            output2 = txtOut

        return render_template('caesarcipher.html', output1=output1, output2=output2)
    except:
        return render_template('caesarcipher.html')

@app.route("/caesarcipher2/", methods=["POST", "GET"])
def caesarcipher2():
    try:
        if request.method == "POST":

            if request.form['options']=="encrypt":
                txt = request.form['txt'].lower()
                shift = int(request.form['shift'])
                txtOut = ""

                alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                            "t", "u", "v", "w", "x", "y", "z"]
                for i in txt:
                    if i != " ":
                        position = alphabet.index(i)
                        position = (position + shift) % 26
                        letter = alphabet[position]
                        txtOut += (letter)

                output = txtOut
            elif request.form['options'] == "decrypt":

                txt = request.form['txt'].lower()
                shift = int(request.form['shift'])
                txtOut = ""
                alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                            "t", "u", "v", "w", "x", "y", "z"]
                for i in txt:
                    if i != " ":
                        position = alphabet.index(i)
                        position = (position - shift) % 26
                        letter = alphabet[position]
                        txtOut += (letter)

                output = txtOut

        return render_template('caesarcipher2.html', output=output)
    except:
        return render_template('caesarcipher2.html')

@app.route("/caesarcipherkeyed/", methods=["POST", "GET"])
def caesarcipherkeyed():
    try:
        if request.method == "POST":
            if request.form['options']=="encrypt":
                txt = request.form['txt'].lower()
                keyword = request.form['key'].lower()
                shift = int(request.form['shift'])
                txtOut = ""

                alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                            "t", "u", "v", "w", "x", "y", "z"]
                keyword = ''.join(sorted(set(keyword), key=keyword.index))

                for elmt in alphabet:
                    for i in keyword:
                        if elmt == i:
                            alphabet.remove(i)

                for elmt in alphabet:
                    for i in keyword:
                        if elmt == i:
                            alphabet.remove(i)

                for elmt in keyword[::-1]:
                    alphabet.insert(0, elmt)

                txtOut = ""

                for i in txt:
                    if i != " ":
                        position = alphabet.index(i)
                        position = (position + shift) % 26
                        letter = alphabet[position]
                        txtOut += (letter)


                output = txtOut
            elif request.form['options'] == "decrypt":
                txt = request.form['txt'].lower()
                keyword = request.form['key'].lower()
                shift = int(request.form['shift'])
                txtOut = ""

                alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s",
                            "t", "u", "v", "w", "x", "y", "z"]
                keyword = ''.join(sorted(set(keyword), key=keyword.index))

                for elmt in alphabet:
                    for i in keyword:
                        if elmt == i:
                            alphabet.remove(i)

                for elmt in alphabet:
                    for i in keyword:
                        if elmt == i:
                            alphabet.remove(i)

                for elmt in keyword[::-1]:
                    alphabet.insert(0, elmt)

                txtOut = ""

                for i in txt:
                    if i != " ":
                        position = alphabet.index(i)
                        position = (position - shift) % 26
                        letter = alphabet[position]
                        txtOut += (letter)

                output = txtOut

        return render_template('caesarcipherkeyed.html', output=output)
    except:
        return render_template('caesarcipherkeyed.html')

if __name__ == "__main__":
    app.run()


