require_relative "test_git"
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase
 
  def test_ftp_uploading
    assert_equal('#<Net::FTP:0x30ccd20>', Main.new().upload_to_ftp("127.0.0.1","ftp","ftp","Readme_ruby.txt"))
  end
 
  #def test_typecheck
  #  assert_raise( RuntimeError ) { SimpleNumber.new('a') }
  #end

  #def test_failure
  #  assert_equal(3, SimpleNumber.new(2).add(2), "Adding doesn't work" )
  #end
 
end