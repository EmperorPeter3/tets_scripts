@Grapes([
   @Grab(group='org.eclipse.jgit', module='org.eclipse.jgit', version='4.0.1.201506240215-r'),
   @Grab(group='org.apache.commons', module='commons-io', version='1.3.2'),
   @Grab(group='commons-net', module='commons-net', version='3.3'),
   @Grab('org.slf4j:slf4j-simple:1.7.12')])

import java.nio.file.Paths;
import java.nio.file.Files;
import org.apache.commons.io.FileUtils;
import org.eclipse.jgit.api.Git;
import org.apache.commons.net.ftp.FTPClient;
import groovy.mock.interceptor.MockFor;
import groovy.mock.interceptor.StubFor;

def run_shell_command (command)
{
	def sh_proc = command.execute();
	sh_proc.waitForOrKill(1000);
	sh_proc.inputStream.eachLine {println it};
	//println "Process exit code: ${sh_proc.exitValue()}";
	//print "Std Out: ${sh_proc.in.text}";
	//println "Std Err: ${sh_proc.err.text}";
}

def cwd = Paths.get("").toAbsolutePath().toString();
//print ("Current working directory is: " + cwd);

print("Process runned by user: ");
run_shell_command("whoami");
run_shell_command("git version");
run_shell_command("cmd.exe /c ver");

def make_symlink (sl_name, src)
{
	Files.createSymbolicLink(Paths.get(sl_name), Paths.get(src));
}

class Gitwork {
	def check_git_files (path)
	{
		['.gitignore','.gitmodule'].each{
			if (new File(path + "${it}").exists())
			{
				println("You have a git-file inside: ${it}");
			}
		}
	}

	def clone_repo (String repo_dir, String repo_url)
	{
		File f = new File(repo_dir);
		if(new File(repo_dir+".git").exists()) 
		{ 
			println("Error: You have a git-repository at " + f.getAbsolutePath());
			check_git_files (repo_dir);
		}
		else
		{
			if (f.exists())
			{
				println("You have a folder of the same name with following files: \n" + f.list());
				File reserve_dir = new File(repo_dir.substring(0,repo_dir.length()-1)+"-reserved/");
				println("All files in this folder are now copying to " + reserve_dir.getAbsolutePath() + "...");
				FileUtils.copyDirectory(f, reserve_dir);
				FileUtils.deleteDirectory(f);
			}
			println("Cloning repo from " + repo_url + " into " + repo_dir);
			Git result = Git.cloneRepository().setURI(repo_url).setDirectory(f).call();
			check_git_files (repo_dir);
			result.getRepository().close();
		}
	}
}


class Builder {
	def run_make_gcc ()
	{
		//src_dir = "/home/rvjp46/Ruby_scripts/c_compile_src"
		run_shell_command('make -C /home/rvjp46/Groovy_scripts/c_compile_src')
	}

	def run_make_jvm ()
	{	
		//src_dir = "/home/rvjp46/Groovy_scripts/jvm_compile_src"
		run_shell_command('javac /home/rvjp46/Groovy_scripts/jvm_compile_src/HelloWorld.java')
	}

	def run_make_ant ()
	{	
		//src_dir = "/home/rvjp46/Groovy_scripts/ant_compile_src"
		run_shell_command('ant compile -f /home/rvjp46/Groovy_scripts/ant_compile_src/build.xml')
	}
}

class Uploading{
	def upload_to_ftp (ftp_server, ftp_login, ftp_pass, filename)
	{
		FTPClient client = new FTPClient();
	    FileInputStream fis = null;
	    try {
	            client.connect(ftp_server);
	            client.login(ftp_login, ftp_pass);
	 			return
	            // Create an InputStream of the file to be uploaded
	            fis = new FileInputStream(filename);
	 
	            // Store file to server7
	            client.storeFile(filename, fis);
	            client.logout();

	        } catch (IOException e) {
	            return e.printStackTrace();
	        } finally {
	            try {
	                if (fis != null) {
	                    fis.close();
	                }
	                client.disconnect();
	            } catch (IOException e) {
	                e.printStackTrace();
	            }
	        }
	}
}

def repo_url = "https://github.com/github/testrepo.git";
def repo_name = "test_repo";

//local path to repository:
//UNIX repo_dir = "home/rvjp46/git_repositories/" + repo_name + "/";
//WIN (local disk perceives as main disk) repo_dir = "/Git_repositories/" + repo_name + "/";
//absolute path: to directory where is script runned
def repo_dir = cwd + "/" + repo_name + "/";


//Gitwork gw = new Gitwork();
//gw.clone_repo(repo_dir, repo_url);
//make_symlink ('symlink', repo_dir);
//Builder bld = new Builder();
//bld.run_make_gcc();
//bld.run_make_jvm();
//bld.run_make_ant();
//Uploading upl = new Uploading()
//upl.upload_to_ftp("127.0.0.1","ftp","ftp","Readme_groovy.txt")

