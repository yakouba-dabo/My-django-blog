from django.views import generic
from .models import Post
from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
      model = Post
      template_name = 'post_detail.html'


#this is for the searching functionnality 

def index(request):
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q =Q(Q(title__icontains=q))
            posts=Post.objects.filter(multiple_q)
        else:
            posts=Post.objects.all()
        context= {
            'posts':posts
        }
        return render(request,'index.html',context)


def contact(request):
        if request.method== 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')

            form_data={
                  'name':name,
                  'email':email,
                  'phone':phone,
                  'message':message,
            }
            message=''' 
            From:\n\t\t{}\n
            Message:\n\t\t{}\n
            Email:\n\t\t{}\n
            Phone:\n\t\t{}\n
            '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['phone'])
            send_mail('You got a mail', message , '' , ['daboyakouba22@gmail.com']) #this will be your email address
        return render(request,'contact.html', {})