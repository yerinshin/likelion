from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'wordcount/result.html', {'full':text, 'total' : len(words), 'dictionary' : word_dictionary.items()})
    