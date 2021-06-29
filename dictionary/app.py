from flask import Flask
from flask.templating import render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "hello world - go to <a href='/dictionary'>dictionary</a>"


@app.route('/dictionary')
def dictionaryhome():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return render_template('dictionaryhome1.html', alpha=alpha)

@app.route('/dictionary/<string:given_word>')
def dictionary(given_word):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    f = open('words.txt')
    word_list = f.read().splitlines()
    count = 0
    for word in word_list:
        match = 0
        for i in range(0, len(given_word)):
            if len(given_word) <= len(word):
                if given_word[i].upper() == word[i]:
                    match += 1   
        if match == (len(given_word)):
            count += 1

    for letter in alpha:
        new_word = given_word + letter
        count2 = 0
        for word in word_list:
            match2 = 0
            for i in range(0, len(new_word)):
                if len(new_word) <= len(word):
                    if new_word[i].upper() == word[i]:
                        match2 += 1   
            if match2 == (len(new_word)):
                count2 += 1
        if count2 == 0:
            alpha.remove(letter)



    # for letter in alpha:
    #     for word in word_list:
    #         new_word = given_word + letter
    #         if len(new_word) <= len(word):
    #             if new_word[-1].upper() == word[len(new_word)-1]:
    #                 second_count += 1
    #     if second_count == 0:
    #         alpha.remove(letter)
    

    return render_template('dictionarylist1.html', given_word=given_word, count=count, alpha=alpha)
