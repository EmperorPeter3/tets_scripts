require 'git'
require 'net/ftp'
require 'logger'

puts 'Process started by user: ' + `whoami`
puts `git version`

class Main
	def check_git_files (path)
		check_files = ['.gitignore','.gitmodule']
		check_files.each do |file|
			if File.exist?(path+file)
				puts 'You have a git-file inside: ' + file
			end 
		end
	end

	def clone_repo(repo_dir, repo_url)
		if (File.exist?(repo_dir+'.git'))
			puts 'Error: You have a git-repository at ' + repo_dir+'.git'
			check_git_files(repo_dir)
		else
			if (File.exist?(repo_dir))
				puts "You have a folder of the same name with following files:"
				print Dir.entries(repo_dir)
				dir_for_copy = repo_dir.slice(0,repo_dir.size-1)+'-reserved'
				puts
				puts "All files in this folder are now copying to " + dir_for_copy
				FileUtils.cp_r repo_dir, dir_for_copy
				FileUtils.remove_dir(repo_dir, force=true)
			end
			Dir.mkdir(repo_dir)
			puts 'Cloning repo from ' + repo_url + ' into ' + repo_dir
			g = Git.clone(repo_url, $repo_name, :PATH => repo_dir)
			#puts g.status
			check_git_files(repo_dir)
		end
	end

	def make_symlink(sl_name,src)
		#unix 
		#puts 'Creating symlink source to ' + src
		#FileUtils.ln_s 'symlink', src
		#win
		puts 'Creating symlink source to C:\\Users\\RVjP46\\Git_repositories\\'
		puts `cmd.exe /c mklink /D symlink C:\\Users\\RVjP46\\Git_repositories\\`
	end

	def run_make_gcc (src_dir)
		#src_dir = "/home/rvjp46/Ruby_scripts/c_compile_src"
		Dir.chdir(src_dir)
		puts `make`
		Dir.chdir($pwd)
	end

	def run_make_jvm (src_dir)
		#src_dir = "/home/rvjp46/Ruby_scripts/jvm_compile_src"
		Dir.chdir(src_dir)
		puts `javac HelloWorld.java`
		Dir.chdir($pwd)
	end

	def run_make_ant (src_dir)
		#src_dir = "/home/rvjp46/Ruby_scripts/ant_compile_src"
		Dir.chdir(src_dir)
		puts `ant compile`
		Dir.chdir($pwd)
	end

	def run_make_msbuild(src_dir,filename)
		system('C:/Users/RVjP46/AppData/Local/Programs/Common/Microsoft/Visual C++ for Python/9.0/vcvarsall.bat')
		Dir.chdir(src_dir)
		exec "cl /EHsc #{filename}"
		Dir.chdir($pwd)
	end

	def run_make_nmake(src_dir)
		system('C:/Users/RVjP46/AppData/Local/Programs/Common/Microsoft/Visual C++ for Python/9.0/vcvarsall.bat')
		Dir.chdir(src_dir)
		puts `nmake`
		Dir.chdir($pwd)
	end

	def upload_to_ftp (ftp_server,ftp_login,ftp_pass,filename)
		puts 'Uploading to ftp: ' + ftp_server
		txt_file_obj = File.new(filename)
		Net::FTP.open(ftp_server, ftp_login, ftp_pass) do |ftp|
			puts ftp
			ftp.putbinaryfile(txt_file_obj)
		end
	end
end


#--------------------------------LOGGING--------------------------------
file = File.open('ruby.log', File::WRONLY | File::APPEND | File::CREAT)
# To create new (and to remove old) logfile, add File::CREAT like:
# file = File.open('foo.log', File::WRONLY | File::APPEND | File::CREAT)
logger = Logger.new(file)
#sev level
logger.level = Logger::INFO
# DEBUG < INFO < WARN < ERROR < FATAL < UNKNOWN

#format
logger.formatter = proc do |severity, datetime, progname, msg|
  "#{datetime}: #{msg}\n"
end

#Message in a block.
#logger.fatal { "Argument 'foo' not given." }
#Message as a string.
#logger.error "Argument #{@foo} mismatch."
#With progname.
#logger.info('initialize') { "Initializing..." }
#With severity.
#logger.add(Logger::FATAL) { 'Fatal error!' }
#logger.close
#-----------------------------------------------------------------------

#-------------------------MAIN SCRIPT EXAMPLES--------------------------
repo_url = 'https://github.com/EmperorPeter3/atc_console.git'
$repo_name = 'atc_console'
#win
$pwd = Dir.pwd
repo_dir = $pwd + "/" + $repo_name + "/"
#repo_dir = 'C:/Users/RVjP46/Git_repositories/'
#unix repo_dir = '/home/rvjp46/git_repositories/'

example = Main.new()
#example.clone_repo(repo_dir, repo_url)
#example.make_symlink("symlink", $pwd)
#Building (UNIX only)
#example.run_make_gcc("/home/rvjp46/Ruby_scripts/c_compile_src")
#example.run_make_jvm("/home/rvjp46/Ruby_scripts/jvm_compile_src")
#example.run_make_ant("/home/rvjp46/Ruby_scripts/ant_compile_src")
#Building (WIN only)
#example.run_make_msbuild("E:/Scripts/Ruby_scripts/msbuild_compile_src/",'basic.cpp')
#example.run_make_nmake("E:/Scripts/Ruby_scripts/msbuild_compile_src/")
#FTP uploading
#example.upload_to_ftp("127.0.0.1","ftp","ftp","Readme_ruby.txt")
