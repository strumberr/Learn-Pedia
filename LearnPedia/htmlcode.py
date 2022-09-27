postcode = """
<!DOCTYPE html>
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='stylescollege.css')}}" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <html>
    <body>



    <style>
    body {
        background: rgb(29, 29, 29);
    }

    .head1 {
    font-family: Arial;
    color: white;
    font-size: 60px; 
    margin: 20px;
    font-weight: 400;

    }

    .allpage {
        justify-content: space-evenly;
        vertical-align: middle;
        text-align: left;
    }

    .allpage2 {
        justify-content: space-evenly;
        vertical-align: middle;
        text-align: left;
    }

    .boxdesign {
        border-radius: 12pt;
        padding: 20px;
        margin: 20px;
        color: white;
        font-family: Arial;
        height: auto;
        width: auto;
        background-color: #3d3d3d;
        flex-wrap: wrap;
    }

    .boxtitle {
        font-size: 30px;
        font-weight: 400;
        flex-wrap: wrap;
    }

    .boxtext {
        font-size: 18px;
        font-weight: 200;
        flex-wrap: wrap;
    }

    .boxtext2 {
        font-size: 18px;
        font-weight: 200;
        flex-wrap: wrap;
        margin-top: 20px;
    }

    .editdeletebutton {
        align-items: center;
        margin-top: 20px;
        margin-right: 20px;
        
    }


    .editbutton {
        padding: 5px;
        border-radius: 12px;
        background-color: rgb(0, 122, 255);
        border-color: rgb(0, 122, 255);
        cursor: pointer;
        color: white;
        padding: 20px;
        height: auto;
        width: 120px;

    }

    .deletebutton {
        padding: 5px;
        border-radius: 12px;
        background-color: rgb(255, 59, 48);
        border-color: rgb(255, 59, 48);
        cursor: pointer;
        color: white;
        padding: 20px;
        height: auto;
        width: 120px;
    }

    .keywordboxdesign {
        border-radius: 12pt;
        padding: 20px;
        margin: 20px;
        color: white;
        font-family: Arial;
        height: auto;
        width: 400px;
        background-color: #3d3d3d;
        flex-wrap: wrap;
        justify-content: flex-start;
    }

    .sliderboxdesign {
        border-radius: 12pt;
        padding: 20px;
        margin: 20px;
        color: white;
        font-family: Arial;
        height: auto;
        width: 70%%;
        background-color: #3d3d3d;
        flex-wrap: wrap;
        justify-content: flex-start;
    }

    .keywordslider {
        display: flex;
        justify-content: flex-start;
        flex-direction: row;

    }


    .header {
        flex-direction: row;
        display: flex;
        justify-content: space-between;
    }

    .sliderdata {
        font-family: Arial;
        font-size: 30px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 40px;
        color: rgb(48, 209, 88);
    }

    .hoursstyle {
        font-size: 50px;
        font-weight: 550;
        color: rgb(255, 69, 59);
        text-align: center;
        margin-top: 30px;
    }



    .boxtext3 {
        font-size: 18px;
        font-weight: 200;
        flex-wrap: wrap;
        margin-top: 20px;
    }

    .authordata {
        font-family: Arial;
        font-size: 30px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 40px;
        color: rgb(0, 140, 255);
    }

    .likebutton {
        background-color: rgb(48, 209, 88);
        padding: 5px;
        border-radius: 12px;
        border-color: rgb(48, 209, 88);
        cursor: pointer;
        color: white;
        padding: 20px;
        height: auto;
        width: 120px;
    }

    .dislikebutton {
        background-color: rgb(255, 159, 10);
        padding: 5px;
        border-radius: 12px;
        border-color: rgb(255, 159, 10);
        cursor: pointer;
        color: white;
        padding: 20px;
        height: auto;
        width: 120px;
    }



    </style>

    <link rel="shortcut icon" href="{{ url_for('static', filename='learnpediafaviconp.png') }}">

    <title>Post - %s</title>

    <div class="header">
        <div class="head1">
            %s
        </div>
        <div class="editdeletebutton">

        <a href="/page_remove">
                <button class="likebutton">
                    <span class="material-symbols-outlined">
                    thumb_up
                    </span>
                </button>
        </a>

        <a href="/page_remove">
                <button class="dislikebutton">
                    <span class="material-symbols-outlined">
                    thumb_down
                    </span>
                </button>
        </a>

        <a href="/page_remove">
            <button class="deletebutton">
                <span class="material-symbols-outlined">
                delete
                </span>
            </button>
        </a>
        </div>
    </div>




    <div class="allpage">
        <div class="boxdesign">
                <div class="boxtext">
                    %s
                </div>
        </div>


        <div class="keywordslider">
            <div class="keywordboxdesign">
                <div class="boxtitle">
                    Keywords
                    <div class="boxtext2">
                        <div>
                            %s
                        </div>
                    </div>
                </div>
            </div>


            <div class="sliderboxdesign">
                <div class="boxtitle">
                    Author Details
                    <div class="boxtext2">
                        Author Name:
                        <div class="authordata">
                            %s
                        </div>
                        Author Contact
                        <div class="authordata">
                            %s
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <div class="allpage2">
        <div class="keywordslider">
            <div class="sliderboxdesign">
                <div class="boxtitle">
                    Links
                    <div class="boxtext3">
                        %s
                    </div>
                </div>
            </div>


            <div class="keywordboxdesign">
                <div class="boxtitle">
                    Time spent on this project
                    <div class="boxtext2">
                        <div class="hoursstyle">
                            %s Hours
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </div>

    <div class="keywordslider">


        <div class="keywordboxdesign">
                <div class="boxtitle">
                    Auto generated keywords
                    <div class="boxtext2">
                        <div>
                            Coming Soon...
                        </div>
                    </div>
                </div>
        </div>
            


        <div class="sliderboxdesign">
            <div class="boxtitle">
                Review
                <div class="boxtext2">
                    On a scale of how hard it was to make this, the person that wrote it found it
                    <div class="sliderdata">
                        %s
                    </div>
                    On a scale of how much the person enjoyed making this, they wrote they found it
                    <div class="sliderdata">
                        %s
                    </div>
                </div>
            </div>
        </div>








    </body>
    </html>
    """