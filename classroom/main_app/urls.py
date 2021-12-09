from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.MainPage,name='main_page'),
    path('information/',views.Information,name='information'),
    path('contact/',views.Contact,name='contact'),

    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),

    path('password_reset/',views.PasswordReset,name='password_reset'),
    path('password_reset_email_sent/',views.PasswordResetEmailSent,name='password_reset_email_sent'),
    path('password_reset_form/<str:email>/<token>',views.PasswordResetForm,name='password_reset_form'),
    path('password_reset_done/<str:email>',views.PasswordResetDone,name='password_reset_done'),

    path('applications_form/',views.ApplicationsFormView,name='applications_form'),
    

    path('home/',views.HomeView,name='home'),

    path('my_grades/email=<str:email>',views.GradesView,name='my_grades'),
    path('my_grades/work/work_id=<str:work_id>',views.GradeData,name='grade'),

    path('recent_content/',views.RecentContent),

    path('user_profile/email=<str:email>/',views.UserProfileView,name='user_profile'),
    path('user_profile_update/email=<str:email>/',views.UserProfileUpdate,name='user_profile_update'),

    path('password_change/email=<str:email>/',views.PasswordsChange,name='password_change'),

   
    
    

    path('students/',views.StudentsView,name='students'),
    path('students/student/email=<str:email>',views.StudentData,name='student'),
    path('students/student_update/email=<str:email>',views.StudentUpdate,name='student_update'),
    path('students/student_delete/email=<str:email>',views.StudentDelete,name='student_delete'),

    path('teachers/',views.TeachersView,name='teachers'),
    path('teachers/teacher_create/',views.TeacherCreate,name='teacher_create'),    
    path('teachers/teacher/email=<str:email>/',views.TeacherData,name='teacher'),
    path('teachers/teacher_update/email=<str:email>/',views.TeacherUpdate,name='teacher_update'),
    path('teacher_delete/<str:email>/',views.TeacherDelete,name='delete_teacher'),

    path('admins/',views.AdminsView,name='admins'),
    path('admins/admin_create/',views.AdminCreate,name='admin_create'),
    path('admins/admin/email=<str:email>',views.AdminsData,name='admin'),
    path('admins/admin_update/email=<str:email>/',views.AdminUpdate,name='admin_update'),

    path('courses/',views.CoursesView,name='courses'),
    path('courses/course/name=<str:name>/year=<str:year>/',views.CourseData,name='course'),
    path('courses/course_update/name=<str:name>/year=<str:year>/',views.CourseUpdate,name='course_update'),
    path('courses/course_delete/name=<str:name>/year=<str:year>/',views.CourseDelete,name='course_delete'),
    path('courses/course_create/',views.CourseCreate,name='course_create'),

    path('courses/course=<str:course>/topic=<str:topic>/',views.TopicsView,name='topic'),
    path('courses/course=<str:course>/topic_create/',views.TopicCreate,name='topic_create'),
    path('courses/course=<str:course>/topic=<str:topic>/topic_update',views.TopicUpdate,name='topic_update'),
    path('courses/course=<str:course>/topic=<str:topic>/topic_delete',views.TopicDelete,name='topic_delete'),
    
    path('courses/course=<str:course>/topic=<str:topic>/assignment_add',views.AssignmentAddForm,name='assignment_add'),
    path('courses/course=<str:course>/topic=<str:topic>/assignment=<str:assignment>',views.Assignment,name='assignment'),
    path('courses/course=<str:course>/topic=<str:topic>/assignment=<str:assignment>/student_works/',views.StudentWorkList,name='student_works'),
    path('courses/course=<str:course>/topic=<str:topic>/assignment=<str:assignment>/student_work/work=<str:work_id>',views.StudentWork,name='student_work'),

    path('courses/course=<str:course>/topic=<str:topic>/content_add/',views.ContentAdd,name='content_add'),
    path('courses/topic=<str:topic>/content=<str:name>/content_delete/<str:id>',views.ContentDelete,name='content_delete'),

    path('years/',views.YearsViews,name='years'),
    path('years/year=<str:pk>/',views.YearData,name='year'),

    path('events/',views.EventsView,name='events'),
    path('events/event_create/',views.EventCreate,name='event_create'),
    path('events/event/title=<str:title>/date=<str:date>',views.EventData,name='event'),

    path('comment_add/event=<str:pk>/',views.CommentAdd,name='comment_add'),
    path('comment_delete/<str:pk>/',views.CommentDelete,name='comment_delete'),




]