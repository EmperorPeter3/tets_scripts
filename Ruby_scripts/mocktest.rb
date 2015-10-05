require 'minitest'
require 'minitest/spec'
require 'minitest/autorun'
require 'date'
require 'git'

class MailPurge
  def initialize(imap)
    @imap = imap
  end
 
  def purge(date)
    # IMAP wants dates in the format: 8-Aug-2002
    formatted_date = date.strftime('%d-%b-%Y')
   
    @imap.authenticate('LOGIN', 'user', 'password')
    @imap.select('INBOX')
 
    message_ids = @imap.search(["BEFORE #{formatted_date}"])
    @imap.store(message_ids, "+FLAGS", [:Deleted])
  end
end

class GitClone
	def initialize()
		@git = Git
	end

	def cloneandstatus(repo_url, repo_name, repo_dir)
		g = @git.clone(repo_url, repo_name, :PATH => repo_dir)
		puts g.status
	end
end


def test_clone_repo
	repo_url = 'https://github.com/EmperorPeter3/atc_console.git'
	repo_name = 'atc_console'
	repo_dir = Dir.pwd + "/" + repo_name + "/"
   
  mock = MiniTest::Mock.new
   
  # mock expects:
  #            method      return  arguments
  #-------------------------------------------------------------
  mock.expect(:clone,         Git::Base, [repo_url, repo_name, repo_dir])
  #mock.expect(:status,        nil, [])
   
  gc = GitClone.new()
  gc.cloneandstatus(repo_url, repo_name, repo_dir)
   
  mock.verify
end

test_clone_repo
