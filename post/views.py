from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
import time
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
from .forms import PostForm

class IndexView(View):
    form_class = PostForm
    initial = {}
    template_name = 'post/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        posts = Post.objects.all().order_by('-id')
        return render(request, self.template_name, {'form': form, 'posts': posts})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user_id = request.user.id
            frm.save()
            return HttpResponseRedirect(reverse('post:index'))

        return render(request, self.template_name, {'form': form})


def event_stream():
    
    initial_data = ""
    while True:
        data = json.dumps(list(Post.objects.order_by("-id").values("message", 
                "date_created", "user__username")),
                cls=DjangoJSONEncoder
            )

        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data) 
            initial_data = data
        time.sleep(1)

        

class PostStreamView(View):

    def get(self, request):
        response = StreamingHttpResponse(event_stream())
        response['Content-Type'] = 'text/event-stream'
        return response
