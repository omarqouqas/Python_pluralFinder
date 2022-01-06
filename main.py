from flask import Flask
from flask import request, render_template

app = Flask(__name__)


def plural_word(word):
    try:
        if word.endswith('y') and word[-2] in ['a', 'o', 'e', 'u', 'i']:
            return word + 's'
        elif word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith('ies'):
            return word
        elif word in ['deer', 'sheep', 'moose', 'bison', 'salmon', 'pike', 'trout', 'fish', 'swine']:
            return word
        elif word.endswith('on'):
            return word[:-2] + 'a'
        elif word[-2:] in 'ex':
            return word[:-2] + 'ices'
        elif word[-2:] in 'ix':
            return word[:-2] + 'ices'
        elif word in ['mouse', 'louse']:
            return word[:1] + 'i' + 'c' + word[4:]
        elif word[-2:] in ['is']:
            return word[:-2] + 'es'
        elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
            return word + 'es'
        elif word.endswith('o') and word[-2] in ['a', 'o', 'e', 'u', 'i']:
            return word + 's'
        elif word.endswith('o'):
            return word + 'es'
        elif word.endswith('fe'):
            return word[:-2] + 'ves'
        elif word in ['man', 'woman', 'policeman', 'ploicewoman']:
            return word[:-2] + 'en'
        elif word.endswith('z'):
            return word + 'es'
        elif word in ['tooth', 'foot', 'goose']:
            return word[0] + 'e' + 'e' + word[3:]
        elif word in ['child']:
            return 'children'
        elif word in ['ox']:
            return 'oxen'
        else:
            return word + 's'
    except ValueError:
        return "Invalid input, try again!"


@app.route("/", methods=['GET', 'POST'])
def index():

    word = None

    if request.method == 'POST':
        word = request.form['word']
        plural_of_this_word = plural_word(word)
        if plural_of_this_word:
            plural_word(word)
            word = {
                'word': word,
                'plural_of_this_word': plural_word(word)
            }

    return render_template('index.html', word=word, )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
