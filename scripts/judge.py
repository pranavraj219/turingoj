import os, sys
import subprocess
import shlex
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turingoj.settings")

import django
django.setup()

from django.shortcuts import get_object_or_404
from submissions.models import SubmissionCache, MainSubmission, lang_extensions
from problems.models import Problem

DEFAULT_UID = 1000      # Set these both according to needs
DEFAULT_GID = 1000
ROOT_UID = 0
ROOT_GID = 0

TIME_QUANTUM = 0.2      # Update for more granular control over Execution Time

CHROOTPATH = '/var/jail/ubuntu'
JUDGEDIR = CHROOTPATH + '/judgedir'

# global vars
cpl_solution_path = os.path.dirname(os.path.realpath(__file__))+'/ven/curr_solution'

def backToHostRoot():
    os.fchdir(HOST_ROOT)
    os.chroot(".")


def cleanFiles(problem_directory):
    print(problem_directory)
    subprocess.call(['rm','-rf', JUDGEDIR + '/*'])           # BE VERY CAUTIOUS!! REMOVING TEMPORARY FILES
    subprocess.call(['cp', '-r', problem_directory + '/input', JUDGEDIR + '/'])
    subprocess.call(['cp', '-r', problem_directory + '/output', JUDGEDIR + '/'])
    subprocess.call(['cp', cpl_solution_path, JUDGEDIR + '/'])
    subprocess.call(['rm', cpl_solution_path])

def runCpp(csubmission):
    retStatus = 0                                   # 0 for accepted, 1 WA, 2 NZEC, 3 TLE
    verdict = "Accepted"
    corr_problem = csubmission.problem_submitted
    problem_directory = os.path.dirname(corr_problem.test_file.path)
    tot_files = subprocess.Popen(['ls','-1',problem_directory+'/input'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)             #Find total number of test cases
    tot_files.wait()
    stdout = tot_files.communicate()[0]
    total = stdout.decode('utf-8').count('\n')
    os.setgid(ROOT_GID)
    os.setuid(ROOT_UID)    #root
    cleanFiles(problem_directory)
    os.chroot(CHROOTPATH)
    executablePath = '/judgedir/curr_solution'
    for i in range(0, total):
        print("Running Test Case " + str(i))
        currID = ""
        if i <= 9:
            currID = '0' + str(i)
        else:
            currID = str(i)
        curr_input_file = open('/judgedir/input/input'+currID+'.txt')
        currProc = subprocess.Popen([executablePath], stdin=curr_input_file, stdout=subprocess.PIPE)
        currTime = 0
        TL = corr_problem.time_limit
        while currTime < TL:
            time.sleep(TIME_QUANTUM)
            currTime += TIME_QUANTUM
            if currProc.poll() is not None:
                break
        if currProc.poll() is None:
            p.kill()
            retStatus = 3
            verdict = "TLE on test case {}".format(str(i))
            return retStatus, currTime, verdict

        if currProc.returncode != 0 :
            retStatus = 2
            verdict = "NZEC on test case {}".format(str(i))
            return retStatus, currTime, verdict

        test_output = currProc.communicate()[0].decode('ascii')
        outputFile = open('/judgedir/output/output' + currID + '.txt')
        reqd_output = outputFile.read()
        if test_output != reqd_output:
            retStatus = 1
            verdict = "WA on test case {}".format(str(i+1))
            return retStatus, currTime, verdict
        return retStatus, currTime, verdict

def evaluate(csubmission):
    src_file = open(csubmission.solution.path, 'r')
    solution_path = os.path.dirname(os.path.realpath(__file__))+'/ven'
    new_src_file_path = solution_path + '/curr_solution.'+lang_extensions[csubmission.language]
    solution_file = open(new_src_file_path, 'w')
    solution_file.write(src_file.read())
    src_file.close()
    solution_file.close()
    cpl_src = subprocess.Popen(['g++', '-w', '-std=c++14', new_src_file_path,
    '-o', solution_path + '/curr_solution'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cpl_src.wait()
    stdout, stderr = cpl_src.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    verdict = ""
    executionTime = 0
    memory = 0
    retStatus = 0
    if stderr != "":
         verdict = "Compilation Error"
    else :
        retStatus, executionTime, verdict = runCpp(csubmission)
    print('Status - {}\nETime - {}\nVerdict - {}'.format(retStatus, executionTime, verdict))
    submission_main = get_object_or_404(MainSubmission, id=csubmission.sidno)
    submission_main.verdict = verdict
    submission_main.execution_time = executionTime
    submission_main.save()
    csubmission.judged = 'yes'
    csubmission.save()
while True:
    HOST_ROOT = os.open("/", os.O_RDONLY)
    if len(sys.argv) > 1:
        cache_submissions = SubmissionCache.objects.filter(sidno__range=(int(sys.argv[1]), int(sys.argv[2])))
    else:
        cache_submissions = SubmissionCache.objects.filter(judged__iexact='no')
    for csubmission in cache_submissions:
        print('Judging cache submission - {}\nMain - {}'.format(csubmission.id, csubmission.sidno))
        evaluate(csubmission)
    os.close(HOST_ROOT)
    if len(sys.argv) > 1:
        sys.exit(0)
    time.sleep(2.0)
