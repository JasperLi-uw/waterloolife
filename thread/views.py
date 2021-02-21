from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Thread, ThreadType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.models import User


def get_thread_list_common_data(request, threads_all_list):
	paginator = Paginator(threads_all_list, settings.THREADS_NUMBER_PER_PAGE)
	page_num = request.GET.get('page', 1) 
	page_of_threads = paginator.get_page(page_num)
	currentr_page_num = page_of_threads.number
	page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
				 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
	if page_range[0] - 1 >= 2:
		page_range.insert(0, '...')
	if paginator.num_pages - page_range[-1] >= 2:
		page_range.append('...')
	if page_range[0] != 1:
		page_range.insert(0, 1)
	if page_range[-1] != paginator.num_pages:
		page_range.append(paginator.num_pages)

	context = {}
	context['threads'] = page_of_threads.object_list
	context['page_of_threads'] = page_of_threads
	context['page_range'] = page_range
	context['thread_types'] = ThreadType.objects.annotate(thread_count=Count('thread'))
	return context

# Create your views here.
def get_newest_threads(request):
	threads_all_list = Thread.objects.all()
	context = get_thread_list_common_data(request, threads_all_list)
	return render(request, 'thread_list.html', context)

def threads_with_type(request, thread_type_pk):
	thread_type = get_object_or_404(ThreadType, pk=thread_type_pk)
	threads_all_list = Thread.objects.filter(thread_type=thread_type)

	context = get_thread_list_common_data(request, threads_all_list)
	context['thread_type'] = thread_type

	return render(request, 'threads_with_type.html', context)

def thread_detail(request, thread_pk):
	thread = get_object_or_404(Thread, pk=thread_pk)

	context = {}
	context['previous_thread'] = Thread.objects.filter(created_time__gt=thread.created_time).last()
	context['next_thread'] = Thread.objects.filter(created_time__lt=thread.created_time).first()
	context['thread'] = thread
	context['thread_types'] = ThreadType.objects.annotate(thread_count=Count('thread'))
	response = render(request, 'thread_detail.html', context)
	return response
