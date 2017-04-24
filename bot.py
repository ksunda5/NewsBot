
# Script that houses main logic of bot
from messenger_parser import MessengerParser
from news_api_requests import suggested_articles
from messenger_api_requests import send_message
from helpers import response


def response_handler(request):
    # Grabs JSON request and makes it MessengerParser object for easy use
    received_message = MessengerParser(request)

    # Uses suggested_articles function in news_api_requests.py to get the articles
    translation #articles = suggested_articles()
    = translate_message(received_message.text, TARGET_LANGUAGE)

    # Uses send_message function in messenger_parser.py to send translated message back to user
    send_message(received_message.messenger_id, translation)

    # Ends FB's webhook request with a response with a 200 success code
    return response()

    from pymessenger.bot import Bot
    bot = Bot(<access_token>)
    elements = ['title', 'image', 'description', 'article_url']
    
    articles = request # array

    if len(articles) > 10:
        for i in range(10):
            article = articles[i]
            buttons = []
            button = URLButton('URL', a['article_url'])
            buttons.append()
            element = Element(title=a['title'], image_url=a['image'], subtitle=a['description'], item_url=a['article_url'], buttons=buttons)
            elements.append(element)
    else:
        for a in articles:
            buttons = []
            button = URLButton('URL', a['article_url'])
            buttons.append()
            element = Element(title=a['title'], image_url=a['image'], subtitle=a['description'], item_url=a['article_url'], buttons=buttons)
            elements.append(element)

    bot.send_generic_message(recipient_id, elements)

