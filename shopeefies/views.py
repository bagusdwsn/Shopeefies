from django.shortcuts import render
from django.http import HttpResponseBadRequest
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import json
import requests
import math
import pickle
import emoji

# Create your views here.
def cleansing(review):
    if isinstance(review, str):
        review = review.strip(" ")
        review = re.sub('[^a-zA-Z]', ' ', review)
        review = re.sub(r'[?|$|.|!_:")(-+,]', '', review)
        review = re.sub(r'(\w)\1+', r'\1', review)
        review = re.sub(r'\d+', '', review)
        review = re.sub(r"\b[a-zA-Z]\b", "", review)
        review = re.sub('\s+', ' ', review)
        review = emoji.demojize(review)  # Convert emojis to text representation
    return review

def casefolding(review):
    if isinstance(review, str):
        review = review.lower()
    return review
def is_valid(url):
    r = re.search(r'i\.(\d+)\.(\d+)', url)
    pattern = r"https?://shopee\.co\.id/.+"
    return re.match(pattern, url) is not None and r is not None

def home(request):
    return render(request, 'index.html')

def predict(request):
    with open('predict_sentimentv2.pkl', 'rb') as file:
        knn_model, vectorizer = pickle.load(file)

    if request.method == 'POST':
        url = request.POST.get('url')
        if not is_valid(url):
            error_message = 'Tautan produk tidak valid! mohon coba lagi.'
            return render(request, 'index.html', {'error_message': error_message})
        r = re.search(r'i\.(\d+)\.(\d+)', url)
        
        shop_id, item_id = r.group(1), r.group(2)
        ratings_url = 'https://shopee.co.id/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0'

        offset = 0
        max_revs = 10
        new_texts = []
        
        while True:
            data = requests.get(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)).json()

            try:
                for rating in data['data']['ratings']:
                    comment = rating['comment']

                    # Skip empty strings and None values
                    if comment is not None and comment != '' and comment.lower() != 'nan':
                        new_texts.append(comment)
            except TypeError:
                break

            if len(data['data']['ratings']) < 20:
                break

            offset += 20

        cleaned_texts = []

        for text in new_texts:
            text = casefolding(text)
            text = cleansing(text)
            if text != '' and text.lower() != 'nan':
                cleaned_texts.append(text)

        new_X = vectorizer.transform(cleaned_texts)
        predictions = knn_model.predict(new_X)

        results = []
        positive_count = 0
        negative_count = 0

        for text, label in zip(cleaned_texts, predictions):
            if label == 'positif':
                positive_count += 1
            elif label == 'negatif':
                negative_count += 1
            results.append({'Text': text, 'Prediction': label})
        
        total_count = positive_count + negative_count
        positive_percentage = (positive_count / total_count) * 100
        negative_percentage = (negative_count / total_count) * 100

        decision = ""
        if positive_percentage >= 70:
            decision = "Beli Barangnya!"
        elif negative_percentage >= 70:
            decision = "Jangan Beli Barangnya!"
        else:
            decision = "Pertimbangkan lagi ya!"

        return render(request, 'results.html', {
            'results': results,
            'positive_count': positive_count,
            'negative_count': negative_count,
            'positive_percentage': positive_percentage,
            'negative_percentage': negative_percentage,
            'decision': decision
        })

