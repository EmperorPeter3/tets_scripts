require 'net/ftp'
require 'minitest'
require 'minitest/spec'
require 'minitest/autorun'

class FTP
	def initialize(host = nil, user = nil, passwd = nil, acct = nil)
	      super()
	      @binary = true
	      @passive = false
	      @debug_mode = false
	      @resume = false
	      @sock = NullSocket.new
	      @logged_in = false
	      if host
	        connect(host)
	        if user
	          login(user, passwd, acct)
	        end
	      end
	    end

	def FTP.open(host, user = nil, passwd = nil, acct = nil)
      if block_given?
        ftp = new(host, user, passwd, acct)
        begin
          yield ftp
        ensure
          ftp.close
        end
      else
        new(host, user, passwd, acct)
      end
    end

end



def test_purging_mail
  txt_file_obj = File.new("Readme_ruby.txt")
   
  mock = MiniTest::Mock.new
   
  # mock expects:
  #            method      return  arguments
  #-------------------------------------------------------------
  mock.expect(:authenticate,  nil, ['LOGIN', 'user', 'password'])
  mock.expect(:select,        nil, ['INBOX'])
  mock.expect(:search,        ids, [["BEFORE #{formatted_date}"]])
  mock.expect(:store,         nil, [ids, "+FLAGS", [:Deleted]])
   
  mp = MailPurge.new(mock)
  mp.purge(date)
   
  puts mock.verify
end

test_purging_mail