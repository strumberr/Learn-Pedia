def db_string_replace(last_row2):
    urlrowstring = str(last_row2)
    urlrowreplace = urlrowstring.replace("'", "")
    urlrowreplace2 = urlrowreplace.replace("[", "")
    urlrowreplace3 = urlrowreplace2.replace("]", "")
    urlrowreplace4 = urlrowreplace3.replace("(", "")
    urlrowreplace5 = urlrowreplace4.replace(")", "")
    return urlrowreplace5
    
def db_string_replace_comma(row):
    briefdescrowstring = str(row)
    briefdescrowreplace = briefdescrowstring.replace("'", "")
    briefdescrowreplace2 = briefdescrowreplace.replace("[", "")
    briefdescrowreplace3 = briefdescrowreplace2.replace("]", "")
    briefdescrowreplace4 = briefdescrowreplace3.replace("(", "")
    briefdescrowreplace5 = briefdescrowreplace4.replace(")", "")
    briefdescrowreplace6 = briefdescrowreplace5.replace(",", "")

    return briefdescrowreplace6