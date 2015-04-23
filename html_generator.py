def generate_lessonbox_html(lessonsubheading, nano_des):
    html_box1 = """
<div class="lessonbox">
    <h3 class="lessonsubheading">
        """ + lessonsubheading
    html_box2 = """
     </h3>      
     <div class="nano_des">
     """ + nano_des
    html_box3 = """
     </div>
</div>"""
#Code for Adding all 3 HTML Box
    mainhtmlbox = html_box1 + html_box2 + html_box3
    return mainhtmlbox

#Now for the lessonbox DIV   
def get_lessonsubheading(lessonbox):
    begin_location = lessonbox.find('lessonsubheading:')
    end_location = lessonbox.find('des:')
    heading =  lessonbox[begin_location+7 : end_location-1]
    return heading

#Now for the nano_dis DIV   - dis mean description
def get_nano_des(lessonbox):
    begin_location = lessonbox.find('des:')
    lessonsubheading =  lessonbox[begin_location+13 :]
    return lessonsubheading

#Now for the THE OVERALL 
def get_lessonboxBN(text, lessonbox_number):
    counter = 0
    while counter <  lessonbox_number:
        counter = counter + 1
        next_begin_lessonbox = text.find('lessonsubheading:')
        next_end_lessonbox = text.find('lessonsubheading:', next_begin_lessonbox + 1)
        lessonbox = text[next_begin_lessonbox:next_end_lessonbox]
        text =text[next_end_lessonbox:]
    return lessonbox
    

TEST_TEXT = """lessonsubheading: What is HTML
nano_des: HTML Stand for Hyper Transfer Markup Text and it is Use to Link Multiples Documents Togethers.
World Wide Web Consortium Website for HTML Documentation W3C for Guideline on it.
HTML Use Markup Tags to Descibe the Web Page Content.
lessonsubheading: Computers are Really Stupid and Humans are Smart
nano_des: Computers Don't Know to How to Correct a Simple Tag Error Where Humans Can Correct it.
Computers Need Instructions to Know What to Do and What Not to Do.
lessonsubheading: Which are the Best Text Editors
nano_des: The Best Text Editor for Industrail Standard is Dreamweaver But The Learning Cruve is Very and It Over Kill the Process for HTML and CSS Coding.
For Quick Coding the Editor is Notepad++ But If You Want to Open 2 Tabs of Code in the Same Editor than Sublime Test is the Winner."""


def generate_all_html(text):
    now_lessonbox_number = 1
    lessonbox = get_lessonboxBN(text, now_lessonbox_number)
    all_html = ""
    while lessonbox != "":
        lessonsubheading = get_lessonsubheading(lessonbox)
        nano_des = get_nano_des(lessonbox)

        lessonbox_html = generate_lessonbox_html(lessonsubheading, nano_des)
        all_html = all_html + lessonbox_html

        now_lessonbox_number = now_lessonbox_number + 1
        lessonbox = get_lessonboxBN(text, now_lessonbox_number)

    return all_html

print generate_all_html(TEST_TEXT)
    
    
    
