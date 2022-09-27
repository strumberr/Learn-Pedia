from types import NoneType
from flask import Flask
from flask import Flask, render_template, request, redirect, flash
from db import create_db
from db import insert_db, insert_db_ip
import sqlite3
import random
from emailmail import emailsend
con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()
import os
from datetime import datetime
from annoyingcodesnippets import db_string_replace, db_string_replace_comma

app = Flask('main')

app.secret_key = "secret_key"

@app.route('/', methods=["GET", "POST"])
def main():

    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)


    iplist = []

    for row in cur.execute('SELECT ip FROM allowedipaddresses'):
        rowstring = str(row)
        rowreplace6 = db_string_replace_comma(rowstring)
        iplist.append(rowreplace6)



    if request.method == "POST":
        
        password = request.form.get("ctext")


        if password == "learnlife2022":

            ip_addr2 = request.remote_addr

            insert_db_ip(ip_addr2)

            return render_template("home.html")
        else:
           return render_template("index.html")
    
    elif ip_addr in iplist:
        return render_template("home.html")

    return render_template("index.html")


@app.route('/home', methods=["GET", "POST"])
def home():

    try:
        if request.method == 'POST':

            titleremove = request.form.get("confirmremove")

            coderemove = request.form.get("coderemove")

            titleremovespace = titleremove.replace(" ", "")

            if "likebutton" in request.form.keys():
                print("button clicked!")

            if coderemove == "code":


                cur.execute(f"DELETE FROM pagetable WHERE joinedtitle LIKE '%{titleremovespace}%'")
                con.commit()

                posturl = f"/post/{titleremovespace}"
                print(posturl)

                cur.execute(f"DELETE FROM comments WHERE posturl LIKE '%{posturl}%'")
                con.commit()
            else:

                titlecode = titleremovespace + str(coderemove)



                cur.execute(f"DELETE FROM pagetable WHERE joinedtitle LIKE '%{titlecode}%'")
                con.commit()

                posturl = f"/post/{titleremovespace}"
                print(posturl)

                cur.execute(f"DELETE FROM comments WHERE posturl LIKE '%{posturl}%'")
                con.commit()
        else:
            pass
    except:
        pass
    
    list1 = []

    for row in cur.execute('SELECT title FROM pagetable'):
        rowstring = str(row)
        rowreplace6 = db_string_replace_comma(rowstring)
        list1.append(rowreplace6)


    list2 = []

    for row in cur.execute('SELECT briefdesc FROM pagetable'):
        briefdescrowstring = str(row)
        rowreplace6 = db_string_replace_comma(briefdescrowstring)
        list2.append(rowreplace6)



    list3 = []

    for row in cur.execute('SELECT url FROM pagetable'):
        urlrowstring = str(row)
        rowreplace6 = db_string_replace_comma(urlrowstring)
        list3.append(rowreplace6)

    



    return render_template("home.html", list1=list1, list2=list2, list3=list3, zip=zip, reversed=reversed)


@app.route('/college', methods=["GET", "POST"])
def college():
    



    return render_template("college.html")


@app.route('/page_create_sucksess', methods=["GET", "POST"])
def pagecreatesuccess():

    if request.method == 'POST':
        title = request.form.get("title")
        briefdesc = request.form.get("briefdesc")
        wholetext = request.form.get("wholetext")
        keywords = request.form.get("keywords")
        sliderhard = request.form.get("hardslider")
        sliderenjoy = request.form.get("enjoyslider")
        hours = request.form.get("hours")
        links = request.form.get("links")
        authorname = request.form.get("authorinputname")
        authorcontact = request.form.get("authorinputcontact")

        sliderhardint = int(sliderhard)
        if sliderhardint <= 2:
            sliderhard = sliderhard + "/10" + " - Very Easy"
        elif sliderhardint <= 4:
            sliderhard = sliderhard + "/10" + " - Easy"
        elif sliderhardint <= 6:
            sliderhard = sliderhard + "/10" + " - Normal"
        elif sliderhardint <= 8:
            sliderhard = sliderhard + "/10" + " - Relatively Hard"
        elif sliderhardint <= 10:
            sliderhard = sliderhard + "/10" + " - Very Hard"

        
        sliderenjoyint = int(sliderenjoy)
        if sliderenjoyint <= 2:
            sliderenjoy = sliderenjoy + "/10" + " - Didn't Enjoy It At All"
        elif sliderenjoyint <= 4:
            sliderenjoy = sliderenjoy + "/10" + " - Not Enjoyable"
        elif sliderenjoyint <= 6:
            sliderenjoy = sliderenjoy + "/10" + " - Don't Mind It"
        elif sliderenjoyint <= 8:
            sliderenjoy = sliderenjoy + "/10" + " - Relatively Fun"
        elif sliderenjoyint <= 10:
            sliderenjoy = sliderenjoy + "/10" + " - A Lot Of Fun"




        



        titleremovespace2 = title.replace(" ", "")

        keywordsspace = keywords.replace("\n", "<br>")

        wholetextspace = wholetext.replace("\n", "<br>")

        linksspace = links.replace("\n", "<br>")



        url2 = title.replace(" ", "")
        url = "/post/" + url2

        wholeurl = "https://learnlifepedia.herokuapp.com" + url

        listurls = []

        for row in cur.execute('SELECT url FROM pagetable'):
            urlrowstring = str(row)
            urlrowreplace = urlrowstring.replace("'", "")
            urlrowreplace2 = urlrowreplace.replace("[", "")
            urlrowreplace3 = urlrowreplace2.replace("]", "")
            urlrowreplace4 = urlrowreplace3.replace("(", "")
            urlrowreplace5 = urlrowreplace4.replace(")", "")
            urlrowreplace6 = urlrowreplace5.replace(",", "")
            listurls.append(urlrowreplace6)

        listauthorcodes = []

        for row in cur.execute('SELECT authorcode FROM pagetable'):
            listauthorcodes.append(urlrowreplace6)

        


        my_file = open("badwords.txt", "r")
        data = my_file.read()
        data_into_list = data.split("\n")
        print(data_into_list)
        my_file.close()

        list_wholetext = []

        for el in wholetext.split(" "):
            list_wholetext.append(el)
        print(list_wholetext)

        list_bad_words = []


        for x in list_wholetext:
    
            for y in data_into_list:

                if x == y:
                    print(f"BAD WORD {x}")
                    list_bad_words.append(x)
        
        print(list_bad_words)
    

        if not list_bad_words:
            if url not in listurls:
                authorcode = random.randint(10000000, 999999999)
                admincode = "code"

                titleremovespace = title.replace(" ", "")
                titlecode = titleremovespace + str(authorcode)

                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                time_now = f"{dt_string} GMT+2"

                emailsend(authorname, authorcontact, authorcode, title, wholeurl)
                insert_db(title, briefdesc, wholetextspace, keywordsspace, url, titlecode, sliderhard, sliderenjoy, hours, linksspace, authorname, authorcontact, authorcode, admincode, comments="", creationdate=time_now, edited=0)
                
                return render_template("pagecreatesuccess.html", email=authorcontact)

            else:
                pass
        else:
            flash(f"Using bad words? You used '{x}' in your text. We do not tolerate bad words.")




        

    return render_template("pagecreatesuccess.html")




@app.route('/pagecreatefail', methods=["GET", "POST"])
def pagecreatefail():

    return render_template("pagecreatefail.html")

@app.route('/testing', methods=["GET", "POST"])
def testing():

    return render_template("testing.html")




@app.route('/page_remove', methods=["GET", "POST"])
def pageremove():

    if request.method == 'POST':

        titleremove = request.form.get("confirmremove")

        coderemove = request.form.get("coderemove")

        titleremovespace = titleremove.replace(" ", "")

        titlecode = titleremovespace + str(coderemove)



        cur.execute(f"DELETE FROM pagetable WHERE joinedtitle LIKE '%{titlecode}%'")
        con.commit()

        posturl = f"/post/{titleremovespace}"
        print(posturl)

        cur.execute(f"DELETE FROM comments WHERE posturl LIKE '%{posturl}%'")
        con.commit()

        
    

    pagetitles = []

    for row in cur.execute('SELECT title FROM pagetable'):
        urlrowstring = str(row)
        urlrowreplace = urlrowstring.replace("'", "")
        urlrowreplace2 = urlrowreplace.replace("[", "")
        urlrowreplace3 = urlrowreplace2.replace("]", "")
        urlrowreplace4 = urlrowreplace3.replace("(", "")
        urlrowreplace5 = urlrowreplace4.replace(")", "")
        urlrowreplace6 = urlrowreplace5.replace(",", "")
        pagetitles.append(urlrowreplace6)
        




    return render_template("pageremove.html", pagetitles=pagetitles)





@app.route('/pagecreate', methods=["GET", "POST"])
def pagecreate():
    if request.method == 'POST':
        title = request.form.get("title")
        briefdesc = request.form.get("briefdesc")
        wholetext = request.form.get("wholetext")
        keywords = request.form.get("keywords")
        sliderhard = request.form.get("hardslider")
        sliderenjoy = request.form.get("enjoyslider")
        hours = request.form.get("hours")
        links = request.form.get("links")
        authorname = request.form.get("authorinputname")
        authorcontact = request.form.get("authorinputcontact")

        sliderhardint = int(sliderhard)
        if sliderhardint <= 2:
            sliderhard = sliderhard + "/10" + " - Very Easy"
        elif sliderhardint <= 4:
            sliderhard = sliderhard + "/10" + " - Easy"
        elif sliderhardint <= 6:
            sliderhard = sliderhard + "/10" + " - Normal"
        elif sliderhardint <= 8:
            sliderhard = sliderhard + "/10" + " - Relatively Hard"
        elif sliderhardint <= 10:
            sliderhard = sliderhard + "/10" + " - Very Hard"

        
        sliderenjoyint = int(sliderenjoy)
        if sliderenjoyint <= 2:
            sliderenjoy = sliderenjoy + "/10" + " - Didn't Enjoy It At All"
        elif sliderenjoyint <= 4:
            sliderenjoy = sliderenjoy + "/10" + " - Not Enjoyable"
        elif sliderenjoyint <= 6:
            sliderenjoy = sliderenjoy + "/10" + " - Don't Mind It"
        elif sliderenjoyint <= 8:
            sliderenjoy = sliderenjoy + "/10" + " - Relatively Fun"
        elif sliderenjoyint <= 10:
            sliderenjoy = sliderenjoy + "/10" + " - A Lot Of Fun"




        



        titleremovespace2 = title.replace(" ", "")

        keywordsspace = keywords.replace("\n", "<br>")

        wholetextspace = wholetext.replace("\n", "<br>")

        linksspace = links.replace("\n", "<br>")



        url2 = title.replace(" ", "")
        url = "/post/" + url2

        wholeurl = "https://learnlifepedia.herokuapp.com" + url

        listurls = []

        for row in cur.execute('SELECT url FROM pagetable'):
            urlrowstring = str(row)
            urlrowreplace = urlrowstring.replace("'", "")
            urlrowreplace2 = urlrowreplace.replace("[", "")
            urlrowreplace3 = urlrowreplace2.replace("]", "")
            urlrowreplace4 = urlrowreplace3.replace("(", "")
            urlrowreplace5 = urlrowreplace4.replace(")", "")
            urlrowreplace6 = urlrowreplace5.replace(",", "")
            listurls.append(urlrowreplace6)

        listauthorcodes = []

        for row in cur.execute('SELECT authorcode FROM pagetable'):
            listauthorcodes.append(urlrowreplace6)

        


        my_file = open("badwords.txt", "r")
        data = my_file.read()
        data_into_list = data.split("\n")
        print(data_into_list)
        my_file.close()

        list_wholetext = []

        for el in wholetext.split(" "):
            list_wholetext.append(el)
        print(list_wholetext)

        list_bad_words = []


        # traverse in the 1st list
        for x in list_wholetext:
    
            # traverse in the 2nd list
            for y in data_into_list:

                # if one common
                if x == y:
                    print(f"BAD WORD {x}")
                    list_bad_words.append(x)
    

        if not list_bad_words:
            if url not in listurls:
                authorcode = random.randint(10000000, 999999999)
                admincode = "code"

                titleremovespace = title.replace(" ", "")
                titlecode = titleremovespace + str(authorcode)

                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                time_now = f"{dt_string} GMT+2"

                emailsend(authorname, authorcontact, authorcode, title, wholeurl)
                insert_db(title, briefdesc, wholetextspace, keywordsspace, url, titlecode, sliderhard, sliderenjoy, hours, linksspace, authorname, authorcontact, authorcode, admincode, comments="", creationdate=time_now, edited=0)
                
                return render_template("pagecreatesuccess.html", email=authorcontact)

            else:
                pass
        else:
            flash(f"Using bad words? You used '{x}' in your text. We do not tolerate bad words.")

 


    return render_template("pagecreate.html", pagetitle="Create Your Own Page")




@app.route('/post/<variable>', methods=['GET', "POST"])
def daily_post(variable):
    if request.method == 'POST':

        codeinput = request.form.get("codeinput")
        wholetext = request.form.get("wholetext")

        commentusername = request.form.get("commentusername")
        commenttext = request.form.get("commenttext")

        print(f"codeinput - {commentusername}")
        print(f"codeinput - {commenttext}")

        if commentusername != None or "none" or "None" or "None," or "Null" or "NULL" or "none,":

            try:

                print("first")

                try:
                    cur.execute('''CREATE TABLE comments (posturl, authorcomment, commenttext)''')
                except:
                    pass
                
                try:
                    print("second")
                    last_row2 = cur.execute('select commenttext from comments').fetchall()[-1]
                    print("third")

                    urlrowstring = str(last_row2)
                    urlrowreplace = urlrowstring.replace("'", "")
                    urlrowreplace2 = urlrowreplace.replace("[", "")
                    urlrowreplace3 = urlrowreplace2.replace("]", "")
                    urlrowreplace4 = urlrowreplace3.replace("(", "")
                    urlrowreplace5 = urlrowreplace4.replace(")", "")
                    finalauthcomment = urlrowreplace5[:-1] + ""

                    print(f"Comment = {urlrowreplace5}")

                    print(f"Dis = {urlrowreplace5} to dis {commenttext}?")
                except:
                    posturl = f"first"
                    commentusername = f"first"
                    commenttext = f"first"

                if finalauthcomment != commenttext:

                    posturl = f"/post/{variable}"

                    cur.execute("INSERT INTO comments VALUES (?, ?, ?);", (posturl, commentusername, commenttext))

                    con.commit()

                    print(f"Successfully added comment user: {commentusername} and comment: {commenttext}")
                else:
                    pass

            except:
                pass

        


        try:

            titleremovespace = variable.replace(" ", "")

            titlecode = titleremovespace + str(codeinput)

            urlrow = cur.execute(f"SELECT * FROM pagetable WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()


            urlgood = urlrow[0][5]
            url2 = urlrow[0][4]

            print(f"urlrow = {urlrow}")

    

            if urlgood == titlecode:

                urlrowstring = str(variable)
                urlrowreplace = urlrowstring.replace("'", "")
                urlrowreplace2 = urlrowreplace.replace("[", "")
                urlrowreplace3 = urlrowreplace2.replace("]", "")
                urlrowreplace4 = urlrowreplace3.replace("(", "")
                urlrowreplace5 = urlrowreplace4.replace(")", "")
                urlrowreplace6 = urlrowreplace5.replace(",", "")
                urlrowreplace7 = str("/" + urlrowreplace6)

                urlrow = cur.execute(f"SELECT * FROM pagetable WHERE url LIKE '%{urlrowreplace7}%'").fetchall()

                wholetextspace = wholetext.replace("\n", "<br>")

                print(wholetextspace)

                urlrow = cur.execute(f"UPDATE pagetable SET wholetext = '{str(wholetextspace)}' WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()

                con.commit()


                print(titlecode)
                print(codeinput)

                return redirect(url2)
            else:
                print("wrong code")
                flash(f"Invalid Code! ({codeinput})")

        except:
            flash(f"Invalid Code! ({codeinput})")





    urlrowstring = str(variable)
    urlrowreplace = urlrowstring.replace("'", "")
    urlrowreplace2 = urlrowreplace.replace("[", "")
    urlrowreplace3 = urlrowreplace2.replace("]", "")
    urlrowreplace4 = urlrowreplace3.replace("(", "")
    urlrowreplace5 = urlrowreplace4.replace(")", "")
    urlrowreplace6 = urlrowreplace5.replace(",", "")
    urlrowreplace7 = str("/" + urlrowreplace6)



    urlrow = cur.execute(f"SELECT * FROM pagetable WHERE url LIKE '%{urlrowreplace7}%'").fetchall()





    listlinks = []

    for el in urlrow[0][9]:
        listlinks.append(el)

    pagetitle = urlrow[0][0]

    editurl = f"/post/{variable}/edit"

    posturl = f"/post/{variable}"

    keywordsbrremove = urlrow[0][3]
    keywordsbrremove2 = keywordsbrremove.replace("<br>", "| ")

    try:



        allcommenttext_list = []

        allcommenttext = cur.execute(f"SELECT commenttext FROM comments WHERE posturl LIKE '%{posturl}%'").fetchall()

        print(allcommenttext)

        for el in allcommenttext:

            urlrowstring = str(el)
            urlrowreplace = urlrowstring.replace("'", "")
            urlrowreplace2 = urlrowreplace.replace("[", "")
            urlrowreplace3 = urlrowreplace2.replace("]", "")
            urlrowreplace4 = urlrowreplace3.replace("(", "")
            urlrowreplace5 = urlrowreplace4.replace(")", "")
            finalauthcomment = urlrowreplace5[:-1] + ""
            allcommenttext_list.append(finalauthcomment)



        allauthorcomment_list = []

        allauthorcomment = cur.execute(f"SELECT authorcomment FROM comments WHERE posturl LIKE '%{posturl}%'").fetchall()

        print(allauthorcomment)

        for el in allauthorcomment:

            urlrowstring = str(el)
            urlrowreplace = urlrowstring.replace("'", "")
            urlrowreplace2 = urlrowreplace.replace("[", "")
            urlrowreplace3 = urlrowreplace2.replace("]", "")
            urlrowreplace4 = urlrowreplace3.replace("(", "")
            urlrowreplace5 = urlrowreplace4.replace(")", "")
            urlrowreplace6 = urlrowreplace5.replace(",", "")
            allauthorcomment_list.append(urlrowreplace6)

    
        
    except:
        pass

    creationdate = cur.execute(f"SELECT creationdate FROM pagetable WHERE url LIKE '%{posturl}%'").fetchall()
    creationdate2 = creationdate[0]

    edited = cur.execute(f"SELECT edited FROM pagetable WHERE url LIKE '%{posturl}%'").fetchall()

    edited2 = int(edited[0][0])

    print(edited2)

    if edited2 == 0:
        edited2 = "This post has not been edited"
        print(edited2)
    elif edited2 == 1:
        edited2 = "Note: This post has been edited"
        print(edited2)


    return render_template("2posttemplate.html", title = pagetitle, briefdesc = urlrow[0][0], wholetext = urlrow[0][2], keywords = urlrow[0][3], authorname = urlrow[0][10], authorcontact = urlrow[0][11], links = urlrow[0][9], hours = urlrow[0][8], sliderhard = urlrow[0][6], sliderenjoy = urlrow[0][7], url = urlrow[0][4], editurl = editurl, allcommenttext_list=allcommenttext_list, allauthorcomment_list=allauthorcomment_list, creationdate=creationdate2, edited=edited2, zip=zip, reversed=reversed)



@app.route('/post/<variable>/edit', methods=['GET', "POST"])
def edit_post(variable):
    if request.method == 'POST':

        codeinput = request.form.get("codeinput")
        wholetext = request.form.get("wholetext")
        kewordsupdate = request.form.get("kewordsupdate")

        try:

            titleremovespace = variable.replace(" ", "")

            titlecode = titleremovespace + str(codeinput)

            urlrow = cur.execute(f"SELECT * FROM pagetable WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()


            urlgood = urlrow[0][5]
            url2 = urlrow[0][4]

            print(f"urlrow = {urlrow}")

    

            if urlgood == titlecode:

                urlrowstring = str(variable)
                urlrowreplace = urlrowstring.replace("'", "")
                urlrowreplace2 = urlrowreplace.replace("[", "")
                urlrowreplace3 = urlrowreplace2.replace("]", "")
                urlrowreplace4 = urlrowreplace3.replace("(", "")
                urlrowreplace5 = urlrowreplace4.replace(")", "")
                urlrowreplace6 = urlrowreplace5.replace(",", "")
                urlrowreplace7 = str("/" + urlrowreplace6)

                urlrow = cur.execute(f"SELECT * FROM pagetable WHERE url LIKE '%{urlrowreplace7}%'").fetchall()

                wholetextspace = wholetext.replace("\n", "<br>")

                keywordsspace = kewordsupdate.replace("\n", "<br>")

                print(wholetextspace)

                urlrow = cur.execute(f"UPDATE pagetable SET wholetext = '{str(wholetextspace)}' WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()

                urlrow = cur.execute(f"UPDATE pagetable SET keywords = '{str(keywordsspace)}' WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()

                urlrow = cur.execute(f"UPDATE pagetable SET edited = '{str(1)}' WHERE joinedtitle LIKE '%{titlecode}%'").fetchall()

                con.commit()


                print(titlecode)
                print(codeinput)

                return redirect(url2)
            else:
                print("wrong code")
                flash(f"Invalid Code! ({codeinput})")

        except:
            flash(f"Invalid Code! ({codeinput})")


    urlrowstring = str(variable)
    urlrowreplace = urlrowstring.replace("'", "")
    urlrowreplace2 = urlrowreplace.replace("[", "")
    urlrowreplace3 = urlrowreplace2.replace("]", "")
    urlrowreplace4 = urlrowreplace3.replace("(", "")
    urlrowreplace5 = urlrowreplace4.replace(")", "")
    urlrowreplace6 = urlrowreplace5.replace(",", "")
    urlrowreplace7 = str("/" + urlrowreplace6)



    urlrow = cur.execute(f"SELECT * FROM pagetable WHERE url LIKE '%{urlrowreplace7}%'").fetchall()



    listlinks = []

    for el in urlrow[0][9]:
        listlinks.append(el)

    pagetitle = urlrow[0][0]

    wholetextnobr = urlrow[0][2]
    wholetextnobr2 = wholetextnobr.replace("<br>", "")


    keywordsnobr = urlrow[0][3]
    keywordsnobr2 = keywordsnobr.replace("<br>", "")
    

    editurl = f"/post/{variable}/edit"

    return render_template("edittemplate.html", title = pagetitle, briefdesc = urlrow[0][0], wholetext = wholetextnobr2, keywords = keywordsnobr2, authorname = urlrow[0][10], authorcontact = urlrow[0][11], links = urlrow[0][9], hours = urlrow[0][8], sliderhard = urlrow[0][6], sliderenjoy = urlrow[0][7], url = urlrow[0][4], editurl = editurl)





@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5560, debug=True, threaded=True)