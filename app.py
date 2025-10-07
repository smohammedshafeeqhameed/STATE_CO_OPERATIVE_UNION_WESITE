
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='src')

# Mock data for news articles
news_articles = [
    {
        'id': 1,
        'title': 'HDC&BM 2025-2026 FINAL LIST PUBLISHED',
        'image': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60',
        'summary': 'The final list for the HDC&BM course for the academic year 2025-2026 has been published. Check the notifications section for more details.',
        'date': '2024-07-28'
    },
    {
        'id': 2,
        'title': 'Training to Co-operative employees',
        'image': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60',
        'summary': 'A new training program for co-operative employees will commence next month. The program aims to enhance skills in management and IT.',
        'date': '2024-07-27'
    },
    {
        'id': 3,
        'title': 'Training conducted via training centers in all districts',
        'image': 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60',
        'summary': 'The state-wide training program has been successfully conducted in all district training centers. Over 5000 employees participated.',
        'date': '2024-07-26'
    }
]

@app.route('/')
def root():
  return render_template('index.html')

@app.route('/home')
def home():
  return render_template('home.html')
  
@app.route('/profile')
def profile():
  return render_template('profile.html')

@app.route('/news')
def news():
  return render_template('news.html', articles=news_articles)

@app.route('/api/news')
def api_news():
  return jsonify(news_articles)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
