from django.urls import path
from .views import dashboard,provision_form,reintegration_form,visitor_register_form,performance_appraisal_form,resident_form,social_entertainment_form,case_history_form,actionplan_register_form,awarness_register_form,bp_pulsenote_form,counselling_register_form,medical_camp_form,medicine_form,night_survey_form,skill_training_form,smc_register_form,staff_attendence_form,stock_form,employment_link_form,rehabitation_form,death_register_form,accident_register_form

urlpatterns = [
    path('',provision_form,name='provision_form'),
    path('reintegration/',reintegration_form,name='reintegration_form'),
    path('visitor_register/',visitor_register_form,name='visitor_register_form'),
    path('performance_appraisal/',performance_appraisal_form,name='performance_appraisal_form'),
    path('resident/',resident_form,name='resident_form'),
    path('social_entertainment/',social_entertainment_form,name='social_entertainment_form'),
    path('case_history/',case_history_form,name='case_history_form'),
    path('actionplan_register/',actionplan_register_form,name='actionplan_register_form'),
    path('awarness_register/',awarness_register_form,name='awarness_register_form'),
    path('bp_pulsenote/',bp_pulsenote_form,name='bp_plusenote_form'),
    path('counselling_register/',counselling_register_form,name='counselling_register_form'),
    path('medical_camp/',medical_camp_form,name='medical_camp_form'),
    path('medicine/',medicine_form,name='medicine_form'),
    path('night_survey/',night_survey_form,name='night_survey_form'),
    path('skill_training/',skill_training_form,name='skill_training_form'),
    path('smc_register/',smc_register_form,name='smc_register_form'),
    path('staff_attendence/',staff_attendence_form,name='staff_attendence_form'),
    path('stock/',stock_form,name='stock_form'),
    path('employment_link/',employment_link_form,name='employment_link_form'),
    path('rehabitation/',rehabitation_form,name='rehabitation_form'),
    path('death_register/',death_register_form, name='death_register_form'),
    path('accident_register/',accident_register_form,name='accident_register_form'),
    path('dashboard/',dashboard,name='dashboard'),

]
















