from django.shortcuts import render, HttpResponse
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.
def upload_file(request):
    context = None
    if request.method == 'POST':
        job_des = request.FILES['document']
        resume = request.FILES['resume']
        if job_des and resume:
            job_desc_txt = docx2txt.process(job_des)
            resume_txt = docx2txt.process(resume)
            overall_text = [resume_txt, job_desc_txt]
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(overall_text)
            match_percent = cosine_similarity(count_matrix)[0][1] * 100
            match_percent = round(match_percent,2)
            print(match_percent)
            return render(request, 'result.html',{'match_percent':match_percent})
        else:
            print('File do not recieved')
            return HttpResponse('<h3>File recieved</h3>')
    return render(request, 'index.html', {'context':context})

def how_to_use(request):
    return render(request,'how_to_use.html')

def made_by(request):
    return render(request, 'made_by.html')