# from flask import Flask,render_template


# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='c005c347b5fc41b79760188b38aa5812')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bengal',
#                                           #sources='bbc-news,the-verge',
#                                           #category='business',
#                                           language='en',
#                                           country='in')
        
# data = top_headlines['articles']

# # news = []

# # for i in data:
# #     news.append("Title=>>>"+i['title'])
# #     news.append("Published Date=>>>"+i['publishedAt'])
# #     news.append("Description =>>>"+i['description'])
    


# app = Flask(__name__)


# @app.route('/')
# def home():
    
#     name="AnandaNaidu"
#     return render_template('index.html',news=data)


# if __name__=="__main__":
#     app.run()


from flask import Flask,render_template



from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c005c347b5fc41b79760188b38aa5812')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')

app= Flask(__name__)
#url(home url ('/') declaration)
@app.route('/')
def home():
    name="gopianandanaidu"
    return render_template('index.html',name=name)

if __name__=="__main__":
    app.run()