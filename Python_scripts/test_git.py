import os, shutil, stat, sys, getpass, git, subprocess, ctypes
from git import Repo

print "Proccess: {pid}\nRunned by user: {uname}\nOS:{OSname}".format(
    pid=os.getpid(), uname=getpass.getuser(), OSname=os.name
    )

repo_url = "https://github.com/EmperorPeter3/atc_console.git"
repo_name = "atc_console"
cwd = os.getcwd()
repo_dir = os.path.join(cwd,""+repo_name)
git_check_dir = os.path.join(cwd,""+repo_name+"\.git")


#print os.path.abspath(REPO_DIR)
#print os.path.expanduser(REPO_DIR)
#print os.path.normcase(REPO_DIR)
#print os.path.splitunc(REPO_DIR)

def check_git_files(path):
    check_files = {".gitignore",".gitmodule"}
    for file in check_files:
        if os.path.exists(os.path.join(path,file)):
            print "You have a git-file inside: " + file

def clone_repo (repo_dir, repo_url):
    if os.path.isdir(git_check_dir):
        print "Error: You have a git-repository at {src}".format(src=repo_dir)
        check_git_files(repo_dir)
    else:
        if os.path.isdir(repo_dir):
            print "You have a folder of the same name with following files: \n{indir}".format(
                indir=os.listdir(repo_dir)
                )
            res_dir=os.path.join(cwd, ""+repo_name+"-reserved")
            print "All files in this folder are now copying to {dst}".format(
                dst=res_dir
                )
            shutil.copytree(repo_dir,res_dir) 
            shutil.rmtree(repo_dir)
        
        os.mkdir(repo_dir)
        #it's for permissions to folder
        #os.chmod(repo_dir, stat.S_IRWXU)
        #os.chmod(repo_dir, stat.S_IRWXG)
        #os.chmod(repo_dir, stat.S_IRWXO)
        print "Cloning repo from {grurl} into {pwd}".format(grurl=repo_url, pwd=cwd)
        Repo.clone_from(repo_url, repo_dir)
        check_git_files(repo_dir)

def make_symlink (sl_name, src):
    if os.path.isdir(cwd+"\\"+sl_name):
        print "Removing same name file"
        subprocess.call(["rmdir",os.getcwd()+"\\"+sl_name])

    print "Creating symlink source to " + src
    #unix
    #os.symlink(src, sl_name)
    #win
    subprocess.call(["cmd.exe", "/c",  "mklink /D ", sl_name, src])

def run_make_gcc (src_dir):
    #src_dir = "/home/rvjp46/Python_scripts/c_compile_src"
    try:
        os.chdir(src_dir)
        os.system("make")
    finally:
        os.chdir(cwd)

def run_make_jvm (src_dir):
    #src_dir = "/home/rvjp46/Python_scripts/jvm_compile_src"
    try:
        os.chdir(src_dir)
        os.system("javac HelloWorld.java")
    finally:
        os.chdir(cwd)

def run_make_ant (src_dir):
    #src_dir = "/home/rvjp46/Python_scripts/ant_compile_src"
    try:
        os.chdir(src_dir)
        os.system("ant compile")
    finally:
        os.chdir(cwd)

#clone_repo(repo_dir,repo_url)
#make_symlink("symlink","C:\\Python27\\Scripts\")
#run_make_gcc("/home/rvjp46/Python_scripts/c_compile_src")
#run_make_ant("/home/rvjp46/Python_scripts/ant_compile_src")
#run_make_jvm("/home/rvjp46/Python_scripts/jvm_compile_src")