import os, shutil, stat, sys, getpass, git, subprocess, ctypes, ftplib, logging, unittest
from mock import Mock, call, patch
from git import Repo

class Main(object):
    print "Proccess: {pid}\nRunned by user: {uname}\nOS:{OSname}".format(
        pid=os.getpid(), uname=getpass.getuser(), OSname=os.name
        )

    #print os.path.abspath(REPO_DIR)
    #print os.path.expanduser(REPO_DIR)
    #print os.path.normcase(REPO_DIR)
    #print os.path.splitunc(REPO_DIR)

    def check_git_files(self, path):
        check_files = {".gitignore",".gitmodule"}
        for file in check_files:
            if os.path.exists(os.path.join(path,file)):
                print "You have a git-file inside: " + file

    def clone_repo (self, repo_dir, repo_url):
        if os.path.isdir(git_check_dir):
            print "Error: You have a git-repository at {src}".format(src=repo_dir)
            self.check_git_files(repo_dir)
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
            self.check_git_files(repo_dir)

    def make_symlink (self,sl_name, src):
        if os.path.isdir(cwd+"\\"+sl_name):
            print "Removing same name file"
            subprocess.call(["rmdir",os.getcwd()+"\\"+sl_name])

        print "Creating symlink source to " + src
        #unix
        #os.symlink(src, sl_name)
        #win
        subprocess.call(["cmd.exe", "/c",  "mklink /D ", sl_name, src])

    _ftp_srvr = "127.0.0.1"
    _ftp_lgn = "ftp"
    _ftp_pswd = "ftp"
    _flnm = "Readme_python.txt"

    def get_session (self, ftp_server, ftp_login, ftp_pass):
        self._ftp_srvr = ftp_server
        self._ftp_lgn = ftp_login
        self._ftp_pswd = ftp_pass
        return ftplib.FTP(self._ftp_srvr, self._ftp_lgn, self._ftp_pswd)

    def upload_to_ftp (self, session, filename):
        print "Main: upload_to_ftp: start"
        #print "You are here: " + FTP.pwd()
        #FTP.cwd(path) - go to directory on ftp
        self._flnm = filename
        #session = ftplib.FTP(self._ftp_srvr, self._ftp_lgn, self._ftp_pswd)
        file = open(self._flnm, 'rb')
        session.storbinary('STOR '+ self._flnm, file)
        file.close()
        session.quit()

    def run_make_gcc (self,src_dir):
        #src_dir = "/home/rvjp46/Python_scripts/c_compile_src"
        try:
            os.chdir(src_dir)
            os.system("make")
        finally:
            os.chdir(cwd)

    def run_make_jvm (self,src_dir):
        #src_dir = "/home/rvjp46/Python_scripts/jvm_compile_src"
        try:
            os.chdir(src_dir)
            os.system("javac HelloWorld.java")
        finally:
            os.chdir(cwd)

    def run_make_ant (self,src_dir):
        #src_dir = "/home/rvjp46/Python_scripts/ant_compile_src"
        try:
            os.chdir(src_dir)
            os.system("ant compile")
        finally:
            os.chdir(cwd)

#--------------------------Main class examples--------------------------
repo_url = "https://github.com/EmperorPeter3/atc_console.git"
repo_name = "atc_console"
cwd = os.getcwd()
repo_dir = os.path.join(cwd,""+repo_name)
git_check_dir = os.path.join(cwd,""+repo_name+"\.git")

example = Main()
#example.clone_repo(repo_dir, repo_url)
#example.make_symlink("symlink","E:\\Scripts\\Python_scripts\\")
example.upload_to_ftp(example.get_session("127.0.0.1","ftp","ftp"),'Readme_python.txt')
#-----building (UNIX only)-----
#example.run_make_gcc("/home/rvjp46/Python_scripts/c_compile_src")
#example.run_make_ant("/home/rvjp46/Python_scripts/ant_compile_src")
#example.run_make_jvm("/home/rvjp46/Python_scripts/jvm_compile_src")
#-----------------------------------------------------------------------

#-----------------------Logger setup and examples-----------------------
logger = logging.getLogger('loggername')
hdlr = logging.FileHandler(cwd+"\\"+ "python.log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

#logger.error('We have a problem')
#logger.info('While this is just chatty')
#-----------------------------------------------------------------------


#--------------------------------TESTING--------------------------------
class MainTest(unittest.TestCase):
    # declare the test resource
    fooSource = None
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "MainTest:setUp_:begin"
         
        # identify the test routine
        testName = self.id().split(".")
        className = testName[1]
        testName = testName[2]
        print testName + " from class " + className
         
        # prepare and configure the test resource
        if (testName == "testA_newUpload"):
            self.fooSource = Mock(spec = ftplib, return_value = ftplib.FTP("127.0.0.1","ftp","ftp"))
            print "MainTest: setup_: testA_newUpload: started"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "MainTest: tearDown_: begin"
        print ""
     
    # test: new upload
    # objective: creating a new ftp upload
    #@patch('ftplib.FTP', autospec = True)
    def testA_newUpload(self):
        # creating a new instance
        testFtp = Main()
        print repr(testFtp)
         
        # test for a nil object
        self.assertIsNotNone(testFtp, "Order object is a nil.")
         
        # test for a valid args
        testSrvr = testFtp._ftp_srvr
        self.assertEqual(testSrvr, "127.0.0.1", "Invalid server name")

        testLgn = testFtp._ftp_lgn
        self.assertEqual(testLgn, "ftp", "Invalid login")

        testPswd = testFtp._ftp_pswd
        self.assertEqual(testPswd, "ftp", "Invalid password")

        testFlnm = testFtp._flnm
        self.assertEqual(testFlnm, "Readme_python.txt", "Wrong file name")


        #use mocking 'session' object
        #<ftplib.FTP instance at 0x023424sdf>
        #mock_ftp = mock_ftp_constructor.return_value
        #testSource = self.fooSource
        #testFtp.upload_to_ftp(testSource,testFlnm)

        # print the mocked calls
        #print self.fooSource.mock_calls


newTest = MainTest('testA_newUpload')
newTest.setUp()
newTest.testA_newUpload()
#---------------------------------------------------------------------------------------------------

