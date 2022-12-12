
def heading_two(text):
    '''
    return heading two text of html
    :param text: Any kind of string
    :return: html tag
    '''
    html = f'<2>{text}</h2>'
    return html

# data = heading_two('This is headline two ')
# print(data)
# data = heading_two('This is Another headline two ')
# print(data)


# print(len.__doc__)

# print(heading_two.__doc__)


def html_tag(text, html_tag):
    '''
    Return HTML Tag of any text
    :param text: Any kind of string
    :param html_tag: what kind of html tag you want to generate
    :return: HTML Tag of any text
    '''

    html = f'<{html_tag}>{text}</{html_tag}>'
    return html

# print(html_tag.__doc__)
print(html_tag('This is Paragraph','p'))
print(html_tag('This is Paragraph','h6'))
print(html_tag('This is Paragraph','strong'))
