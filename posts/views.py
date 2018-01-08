from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect,render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def post_list(request):
    query_set = Post.objects.all()
    context = {'object_list': query_set}
    return render(request, template_name='post_list.html', context=context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, pk=id)
    context = {'instance': instance}
    return render(request,context=context, template_name='detail.html')

def post_update(request, id=None):
    instance = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'instance': instance, 'form': form}
    return render(request,context=context, template_name='post_form.html')


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Successfully</a> created &", extra_tags='html_safe')
        messages.success(request, "Successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form':form}
    return render(request, template_name='post_form.html', context=context)

def post_delete(request, id):
    instance = get_object_or_404(Post, pk=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('posts:post_list')