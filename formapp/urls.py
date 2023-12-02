from django.urls import path
from formapp import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings




# from .views import master_records_form,master_records_dashboard,action_plan_dashboard,login_view,register_view,home,asset_form,provision_dashboard,reintegration_register_dashboard,staff_movement_form,accident_register_dashboard,provision_form,reintegration_form,visitor_register_form,performance_appraisal_form,resident_form,social_entertainment_form,case_history_form,actionplan_register_form,awarness_register_form,bp_pulsenote,counselling_register_form,medicine_form,night_survey_form,skill_training_form,smc_register_form,staff_attendence_form,stock_form,employment_link_form,rehabitation_form,death_register_form,accident_register_form,medical_camp_form,food_menu_form,salary_register_form

urlpatterns = [
    path('', views.loginuser, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signupuser, name='signup'),
    path('home/',views.home,name='home'),
    path('master_records/', views.master_records_form, name='master_records'),
    path('master_records_dashboard/', views.master_records_dashboard, name='master_records_dashboard'),
    path('provision/',views.provision_form,name='provision'),
    path('provision_dashboard/',views.provision_dashboard,name='provision_dashboard'),
    path('reintegration_form/',views.reintegration_form,name='reintegration_form'),
    path('reintegration_register_dashboard/',views.reintegration_register_dashboard,name='reintegration_register_dashboard'),
    path('visitor_register_form/',views.visitor_register_form,name='visitor_register_form'),
    path('visitor_registration_dashboard/', views.visitor_registration_dashboard, name='visitor_registration_dashboard'),
    path('performance_appraisal_form/',views.performance_appraisal_form,name='performance_appraisal_form'),
    path('performance_appraisal_dashboard/', views.performance_appraisal_dashboard, name='performance_appraisal_dashboard'),
    path('resident_form/',views.resident_form,name='resident_form'),
    path('resident_attendance_form_dashboard/', views.resident_attendance_form_dashboard, name='resident_attendance_form_dashboard'),
    path('social_entertainment/',views.social_entertainment_form,name='social_entertainment'),
    path('social_entertainment_form_dashboard/', views.social_entertainment_form_dashboard,name='social_entertainment_form_dashboard'),
    path('case_history/',views.case_history_form,name='case_history'),
    path('case_history_record_dashboard/', views.case_history_record_dashboard,name='case_history_record_dashboard'),
    path('actionplan_register_form/',views.actionplan_register_form,name='actionplan_register_form'),
    path('action_plan_dashboard/',views.action_plan_dashboard,name='action_plan_dashboard'),
    path('food_menu/',views.food_menu_form,name='food_menu'),
    path('food_menu_dashboard/', views.food_menu_dashboard, name='food_menu_dashboard'),
    path('salary_register/',views.salary_register_form,name='salary_register'),
    path('salary_register_dashboard/', views.salary_register_dashboard, name='salary_register_dashboard'),
    path('staff_movement/', views.staff_movement_form, name='staff_movement'),
    path('staff_movement_note_dashboard/', views.staff_movement_note_dashboard, name='staff_movement_note_dashboard'),
    path('awarnes_register/',views.awarnes_register_form,name='awarnes_register'),
    path('awarnes_register_dashboard/', views.awarnes_register_dashboard, name='awarnes_register_dashboard'),
    path('asset_form/',views.asset_form,name='asset_form'),
    path('asset_register_dashboard/', views.asset_register_dashboard, name='asset_register_dashboard'),
    path('bp_pulsenote/',views.bp_pulsenote,name='bp_pulsenote'),
    path('bp_form_dashboard/', views.bp_form_dashboard, name='bp_form_dashboard'),
    path('counselling_register/',views.counselling_register_form,name='counselling_register'),
    path('counselling_register_dashboard/', views.counselling_register_dashboard, name='counselling_register_dashboard'),
    path('medical_camp/',views.medical_camp_form,name='medical_camp'),
    path('medical_register_dashboard/', views.medical_register_dashboard, name='medical_register_dashboard'),
    path('medicine/',views.medicine_form,name='medicine'),
    path('medicine_register_dashboard/', views.medicine_register_dashboard, name='medicine_register_dashboard'),
    path('night_survey/',views.night_survey_form,name='night_survey'),
    path('night_survey_dashboard/', views.night_survey_dashboard, name='night_survey_dashboard'),
    path('skill_training/',views.skill_training_form,name='skill_training'),
    path('skill_training_dashboard/', views.skill_training_dashboard, name='skill_training_dashboard'),
    path('smc_register/',views.smc_register_form,name='smc_register'),
    path('smc_register_dashboard/', views.smc_register_dashboard, name='smc_register_dashboard'),
    path('staff_attendance_form/',views.staff_attendance_form,name='staff_attendance_form'),
    path('staff_attendance_register_dashboard/', views.staff_attendance_register_dashboard, name='staff_attendance_register_dashboard'),
    path('inspection_register/', views.inspection_register, name='inspection_register'),
    path('inspection_register_dashboard/', views.inspection_register_dashboard, name='inspection_register_dashboard'),
    path('stock_form/',views.stock_form,name='stock_form'),
    path('stock_register_dashboard/',views.stock_register_dashboard,name='stock_register_dashboard'),
    path('employment_link_form/',views.employment_link_form,name='employment_link_form'),
    path('employment_linkage_form_dashboard/', views.employment_linkage_form_dashboard, name='employment_linkage_form_dashboard'),
    path('rehabitation/',views.rehabitation_form,name='rehabitation'),
    path('rehabitation_dashboard/', views.rehabitation_dashboard, name='rehabitation_dashboard'),
    path('death_register/',views.death_register_form, name='death_register'),
    path('death_register_dashboard/', views.death_register_dashboard, name='death_register_dashboard'),
    path('accident_register_form/',views.accident_register_form,name='accident_register_form'),
    path('accident_register_dashboard/',views.accident_register_dashboard,name='accident_register_dashboard'),
    path('personal_info_form/',views.personal_info_form,name='personal_info_form'),
    path('personal_info_dashboard/',views.personal_info_dashboard,name='personal_info_dashboard'),
    path('food_menu_form/',views.food_menu_form,name='food_menu_form'),
    path('food_menu_dashboard/', views.food_menu_dashboard, name='food_menu_dashboard'),
    # <a href="{% url 'staff_attendance_register_dashboard' %}">Staff Attendance Dashboard</a>



    


]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










