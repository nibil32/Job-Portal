from django.urls import path
from jobseeker import views


urlpatterns = [
    path("reg/",views.Register.as_view(),name="reg"),
    path("seeker/",views.Student_home.as_view(),name="seekerindex"),
    path("create_profile/",views.Jobseeker_profile.as_view(),name="profile"),
    path('view/<int:pk>',views.Profileview.as_view(),name="view"),
    path('edit/<int:pk>',views.update_profile.as_view(),name="edit"),
    path('signout/',views.signout.as_view(),name="signout"),
    path('detail/<int:pk>',views.Jobdetailview.as_view(),name="job_detail"),
    path("applyjob/<int:pk>",views.Job_apply.as_view(),name="apply"),
    path("applied/",views.Applied_jobs.as_view(),name="applied"),
    path("delete_job/<int:pk>",views.Delete_job.as_view(),name="deljob")

]