require 'git'

puts 'Process started by user: ' + `whoami`
puts `git version`

repo_url = 'https://github.com/EmperorPeter3/atc_console.git'
$repo_name = 'atc_console'
#win
$pwd = Dir.pwd
repo_dir = $pwd + "/" + $repo_name + "/"
#repo_dir = 'C:/Users/RVjP46/Git_repositories/'
#unix repo_dir = '/home/rvjp46/git_repositories/'

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

#clone_repo(repo_dir, repo_url)
#make_symlink("symlink", pwd)
#run_make_gcc ("/home/rvjp46/Ruby_scripts/c_compile_src")
#run_make_jvm ("/home/rvjp46/Ruby_scripts/jvm_compile_src")
#run_make_ant("/home/rvjp46/Ruby_scripts/ant_compile_src")