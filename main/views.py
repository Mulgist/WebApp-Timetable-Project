from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
import simplejson
import datetime
from .models import Semester, Class, ClassTime, Calendar
from .forms import CreateSemester


def classtime(request):
    if request.user.is_authenticated:
        return render(request, "main/index.html")
    else:
        return HttpResponseRedirect(
            reverse('signin')
        )


def classtime_ajax(request):
    if request.is_ajax():
        date = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        current_weekday = date.weekday()
        monday = date - datetime.timedelta(days=(current_weekday - 1))
        sunday = date + datetime.timedelta(days=(7 - current_weekday))
        monday_str = monday.isoformat()
        sunday_str = sunday.isoformat()
        # 쿼리 시작
        semester_rows = Semester.objects.filter(user_id_id=request.user.user_id)
        semester_id = 0
        for semester_row in semester_rows:
            if (semester_row.start_day < date) and (semester_row.end_day > date):
                semester_id = semester_row.semester_id
                current_semester = semester_row
                break
            else:
                continue
        if semester_id == 0:
            return HttpResponse("No Data")

        lecture_rows = Class.objects.filter(semester_id_id=current_semester.semester_id)
        # classtime_rows = ClassTime.objects.filter()
        return HttpResponse("length is " )


    return HttpResponse("Invalid Request")


def semester(request):
    semesters = Semester.objects.all()
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date');
    return render(request, 'main/semester.html', {'semesters': semesters})


def create_semester(request):
    createform = CreateSemester()
    if request.method == 'POST':
        createform = CreateSemester(request.POST)
        if createform.is_valid():
            create = createform.save(commit=False)
            # create.start_day = datetime.datetime.strptime(request.POST["start_day"], "%Y-%m-%d").date()
            # create.end_day = datetime.datetime.strptime(request.POST["end_day"], "%Y-%m-%d").date()
            # return HttpResponse(create.start_day)
            create.user_id_id = request.user.user_id
            create.save()
            return HttpResponseRedirect(
                reverse('semester')
            )
    return render(request, "main/create_semester.html", {
        "createform": createform
    })


def lecture(request):
    return render(request, 'main/lecture.html')


def calendar(request):
    return render(request, 'main/calendar.html')
