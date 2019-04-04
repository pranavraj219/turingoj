from django.db import models
from coders.models import UserProfile
from problems.models import Problem
from private_storage.fields import PrivateFileField
from django.utils import timezone

lang_choices = (
('text', 'Plain Text'),
('c_cpp', 'C++'),
('java', 'Java'),
)
lang_extensions = {
'text' : 'txt',
'c_cpp' : 'cpp',
'java' : 'java',
}
lang_dictionary = {
'text' : 'Plain Text',
'c_cpp' : 'C++',
'java' : 'Java',
}

def user_directory_path(instance, filename):
    if(isinstance(instance, SubmissionCache)):
        # print(instance.user_handle)
        return 'submissions/cache/sub_{}.{}'.format(instance.id, lang_extensions[instance.language])
    else:
        return 'submissions/main/sub_{}.{}'.format(instance.id, lang_extensions[instance.language])


class SubmissionCache(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    user_handle = models.ForeignKey(UserProfile, related_name = 'user_c_submission', on_delete=models.DO_NOTHING)
    problem_submitted = models.ForeignKey(Problem, related_name = 'problem_c_submission', on_delete=models.DO_NOTHING)
    language = models.CharField(blank=True,default='c_cpp', max_length=100, choices=lang_choices)
    actual_language = models.CharField(blank=True, max_length=100)
    solution = PrivateFileField(upload_to = user_directory_path)
    sidno = models.PositiveIntegerField(blank=True, null=True)
    judged = models.CharField(blank=True, default='no', max_length=5)
    def __str__(self):
        return 'p_{}_u_{}_s_{}'.format(self.problem_submitted.problem_name, self.user_handle.username, str(self.id))


class MainSubmission(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    # cache_submission_rel = models.OneToOneField(SubmissionCache,on_delete=models.DO_NOTHING, related_name='cache_to_main', null=True)
    user_handle = models.ForeignKey(UserProfile, related_name = 'user_m_submission', on_delete=models.DO_NOTHING)
    problem_submitted = models.ForeignKey(Problem, related_name = 'problem_m_submission', on_delete=models.DO_NOTHING)
    verdict = models.CharField(blank=True, default = '...',max_length=50)
    # execution_time = models.PositiveIntegerField(blank=True, null=True)
    execution_time = models.DecimalField(blank=True, null=True, default=0,max_digits=6, decimal_places=3)
    memory = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(blank=True,default='c_cpp', max_length=100, choices=lang_choices)
    actual_language = models.CharField(blank=True, max_length=100)
    solution = PrivateFileField(upload_to = user_directory_path)
    def __str__(self):
        return 'p_{}_u_{}_s_{}'.format(self.problem_submitted.problem_name, self.user_handle.username, str(self.id))
