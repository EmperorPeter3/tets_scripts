import unittest
from mock import Mock, call
# Preparing to Mock: Listing 1 - Listing 7
#---------------------------------------------LISTING 1---------------------------------------------
# The first constructor argument is the name argument, which gives a mock object a unique name.
# I create a mock object (mockFoo) with the name Foo. Notice the name appears next to the mock's 
# unique ID when I print the mock object.
#---------------------------------------------------------------------------------------------------
# create the mock object
#mockFoo = Mock(name = "Foo")
 
#print mockFoo
# returns: <Mock name='Foo' id='494864'>
#print repr(mockFoo)
# returns: <Mock name='Foo' id='494864'>
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 2---------------------------------------------
# The next constructor argument is the spec argument. Its sets the mock object's attributes - which 
# may be a property or a method. The attributes can be a list of strings or can come from another 
# Python class. 
# I have a list object (fooSpec) with three items: the property attribute _fooValue, and the method 
# attributes callFoo and doFoo. When I pass fooSpec to the class constructor, mockFoo gains three 
# attributes, which I can access with the dot operator. But if I access an undeclared attribute, 
# mockFoo raises an AttributeError and names the "faulty" attribute.
#---------------------------------------------------------------------------------------------------
# prepare the spec list
#fooSpec = ["_fooValue", "callFoo", "doFoo"]
 
# create the mock object
#mockFoo = Mock(spec = fooSpec)
 
# accessing the mocked attributes
#print mockFoo
# <Mock id='427280'>
#print mockFoo._fooValue
# returns <Mock name='mock._fooValue' id='2788112'>
#print mockFoo.callFoo()
# returns: <Mock name='mock.callFoo()' id='2815376'>
 
#mockFoo.callFoo()
# nothing happens, which is fine
 
# accessing the missing attributes
#print mockFoo._fooBar
# raises: AttributeError: Mock object has no attribute '_fooBar'
#mockFoo.callFoobar()
# raises: AttributeError: Mock object has no attribute 'callFoobar'
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 3---------------------------------------------
# Shows another use of the spec argument. This time, I have class Foo with the same three attributes. 
# I pass the class name to the constructor, which then produces a mock object with the same 
# attributes as Foo. Again, accessing an undeclared attribute raises an AttributeError. Also, 
# in both examples, the method attributes are non-functional. Calling a mocked method does nothing, 
# even if said method has functional code
#---------------------------------------------------------------------------------------------------
# The class interfaces
#class Foo(object):
#    # instance properties
#    _fooValue = 123
#     
#    def callFoo(self):
#        print "Foo:callFoo_"
#     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue    
 
# create the mock object
#mockFoo = Mock(spec = Foo)
 
# accessing the mocked attributes
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
#print mockFoo._fooValue
# returns <Mock name='mock._fooValue' id='2788112'>
#print mockFoo.callFoo()
# returns: <Mock name='mock.callFoo()' id='2815376'>
 
#mockFoo.callFoo()
# nothing happens, which is fine
 
# accessing the missing attributes
#print mockFoo._fooBar
# raises: AttributeError: Mock object has no attribute '_fooBar'
#mockFoo.callFoobar()
# raises: AttributeError: Mock object has no attribute 'callFoobar'
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 4---------------------------------------------
# The next constructor argument is return_value. This one sets a mock object's response when it gets 
# a direct call. 
# I use this argument for simulating a factory call.  I have return_value set to 456. When I call 
# mockFoo, I get 456 for a result.
#---------------------------------------------------------------------------------------------------
# create the mock object
#mockFoo = Mock(return_value = 456)
 
#print mockFoo
# <Mock id='2787568'>
 
#mockObj = mockFoo()
#print mockObj
# returns: 456
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 5---------------------------------------------
# I pass an instance of class Foo (fooObj) for return_value. Now, when I call mockFoo, I get fooObj 
# instead (shown here as mockObj). And unlike in Listings 2 and 3, the methods in mockObj are 
# functional.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
#     
#    def callFoo(self):
#        print "Foo:callFoo_"
#     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# creating the mock object
#fooObj = Foo()
#print fooObj
# returns: <__main__.Foo object at 0x68550>
 
#mockFoo = Mock(return_value = fooObj)
#print mockFoo
# returns: <Mock id='2788144'>
 
# creating an "instance"
#mockObj = mockFoo()
#print mockObj
# returns: <__main__.Foo object at 0x68550>
 
# working with the mocked instance
#print mockObj._fooValue
# returns: 123
#mockObj.callFoo()
# returns: Foo:callFoo_
#mockObj.doFoo("narf")
# returns: Foo:doFoo:input =  narf
# <Mock id='428560'>
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 6---------------------------------------------
# Counter to return_value is the side_effect argument. This one assigns the mock with an alternative 
# result, one that overrides return_value. In short, a simulated factory call returns the 
# side_effect value, not the return_value. 
# I create an instance of class Foo (fooObj) and pass it as a return_value argument. The result is 
# similar to Listing 5; mockFoo returns fooObj when called. But then I repeat the same steps, 
# passing StandardError for the side_effect argument. Now, calling mockFoo raises StandardError, 
# instead of returning fooObj.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
#    # instance properties
#    _fooValue = 123
#     
#    def callFoo(self):
#        print "Foo:callFoo_"
#     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# creating the mock object (without a side effect)
#fooObj = Foo()
 
#mockFoo = Mock(return_value = fooObj)
#print mockFoo
# returns: <Mock id='2788144'>
 
# creating an "instance"
#mockObj = mockFoo()
#print mockObj
# returns: <__main__.Foo object at 0x2a88f0>
 
# creating a mock object (with a side effect)
 
#mockFoo = Mock(return_value = fooObj, side_effect = StandardError)
#mockObj = mockFoo()
# raises: StandardError
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 7---------------------------------------------
# I pass a list object (fooList) to the class constructor. Then, each time I call mockFoo, it 
# returns a list item in succession. Once mockFoo reaches the end of the list, another call will 
# raise a StopIteration error. You could pass other iterable objects (set, tuple) to the side_effect
# argument. What you cannot pass is a primitive (integer, string, and so on) because these are not 
# iterable. To make a primitive iterable, add it to a single-item list.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
#    # instance properties
#    _fooValue = 123
#     
#    def callFoo(self):
#        print "Foo:callFoo_"
#     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# creating the mock object (with a side effect)
#fooObj = Foo()
 
#fooList = [665, 666, 667]
#mockFoo = Mock(return_value = fooObj, side_effect = fooList)
 
#fooTest = mockFoo()
#print fooTest
# returns 665
 
#fooTest = mockFoo()
#print fooTest
# returns 666
 
#fooTest = mockFoo()
#print fooTest
# returns 667
 
#fooTest = mockFoo()
#print fooTest
# raises: StopIteration
#---------------------------------------------------------------------------------------------------

# Asserting with a Mock: Listing 8 - Listing 13
# Asserts methods from the Mock help track the method calls made to the mock by the test subject. 
# They can work in conjunction with the asserts from the unittest module. They can be attached to 
# the mock or to one of its method attributes. All but one take the same two optional arguments: a 
# variable sequence, and a key/value sequence.

#---------------------------------------------LISTING 8---------------------------------------------
# assert_called_with() checks if a mocked method gets the right arguments. It fires when at least 
# one argument has the wrong value or type, when there is a wrong number of arguments, when the 
# arguments are in the wrong order, or when the mocked method is not expecting any arguments at all.
# I prepared a mock object with class Foo as its spec. I call the mocked method doFoo(), passing a 
# string for input. With assert_called_with(), I check if the method gets the right input. The 
# assert in line 20 passes because doFoo() got "narf" for input. But the next assert fails because 
# doFoo() got "zort", which is wrong.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.doFoo("narf")
#mockFoo.doFoo.assert_called_with("narf")
# assertion passes
 
#mockFoo.doFoo("zort")
#mockFoo.doFoo.assert_called_with("narf")
# AssertionError: Expected call: doFoo('narf')
# Actual call: doFoo('zort')
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 9---------------------------------------------
# I call the mocked method callFoo(), first without input, and then with the string "zort". The 
# first assert passes, because callFoo() is not supposed to get any input. And the second assert 
# fails for obvious reasons.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.callFoo()
#mockFoo.callFoo.assert_called_with()
# assertion passes
 
#mockFoo.callFoo("zort")
#mockFoo.callFoo.assert_called_with()
# AssertionError: Expected call: callFoo()
# Actual call: callFoo('zort')
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 10--------------------------------------------
# assert_called_once_with() also checks if the test subject called a mocked method correctly. But 
# this method will fire when the same method call happens more than once, whereas 
# assert_called_with() will ignore multiple calls. 
# I make two calls to the mocked method callFoo(). On the first call, the assert passes. But on the 
# second call, the assert fires, sending its error message to stdout.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.callFoo()
#mockFoo.callFoo.assert_called_once_with()
# assertion passes
 
#mockFoo.callFoo()
#mockFoo.callFoo.assert_called_once_with()
# AssertionError: Expected to be called once. Called 2 times.
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 11--------------------------------------------
# assert_any_call() checks if the test subject called a mocked method at any point of the test 
# routine. This is regardless of how many other calls were made between the mocked method and the 
# assert. Compare this with the previous two asserts, both of which check only the most recent call.
# The first assert_any_call() passes even though two doFoo() calls separate the assert and callFoo(). 
# The second assert also passes even though a callFoo() separates it from the doFoo() in question. 
# On the other hand, the third assert fires, because none of the doFoo() calls used the string "egad" 
# for input.
#---------------------------------------------------------------------------------------------------
# The mock specification
#class Foo(object):
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.callFoo()
#mockFoo.doFoo("narf")
#mockFoo.doFoo("zort")
 
#mockFoo.callFoo.assert_any_call()
# assert passes
 
#mockFoo.callFoo()
#mockFoo.doFoo("troz")
 
#mockFoo.doFoo.assert_any_call("zort")
# assert passes
 
#mockFoo.doFoo.assert_any_call("egad")
# raises: AssertionError: doFoo('egad') call not found
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 12--------------------------------------------
# assert_has_calls() looks at a sequence of method calls, checks if they are in the right order and 
# with the right arguments. It takes two arguments: a list of expected method calls and an optional 
# argument any_order. It fires when the test subject calls the wrong method, calls one method out 
# of order, or gives a method the wrong input.
# I make three method calls, providing input to two. Then, I prepare a list of expected calls 
# (fooCalls) and pass this list to assert_has_calls(). Since the list matches the method calls, the 
# assert passes.
#---------------------------------------------------------------------------------------------------
# The mock specification
#class Foo(object):
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.callFoo()
#mockFoo.doFoo("narf")
#mockFoo.doFoo("zort")
 
#fooCalls = [call.callFoo(), call.doFoo("narf"), call.doFoo("zort")]
#mockFoo.assert_has_calls(fooCalls)
# assert passes
 
#fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
#mockFoo.assert_has_calls(fooCalls)
# AssertionError: Calls not found.
# Expected: [call.callFoo(), call.doFoo('zort'), call.doFoo('narf')]
# Actual: [call.callFoo(), call.doFoo('narf'), call.doFoo('zort')]
 
#fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
#mockFoo.assert_has_calls(fooCalls, any_order = True)
# assert passes
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 13--------------------------------------------
# Listing 13 demonstrates another use. To the list fooCalls, I added a nonexistent method dooFoo(). 
# Then I passed fooCalls to assert_has_calls(). The assert fires, informing me that the expected 
# call sequence did not match what actually happened. If I pass a True to the any_order argument, 
# the assert names dooFoo() as the offending method call.
#---------------------------------------------------------------------------------------------------
# The mock specification
#class Foo(object):
#    _fooValue = 123
     
#    def callFoo(self):
#        pass
     
#    def doFoo(self, argValue):
#        pass
 
# create the mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#mockFoo.callFoo()
#mockFoo.doFoo("narf")
#mockFoo.doFoo("zort")
 
#fooCalls = [call.callFoo(), call.dooFoo("narf"), call.doFoo("zort")]
 
#mockFoo.assert_has_calls(fooCalls)
# AssertionError: Calls not found.
# Expected: [call.callFoo(), call.dooFoo('narf'), call.doFoo('zort')]
# Actual: [call.callFoo(), call.doFoo('narf'), call.doFoo('zort')]
 
#fooCalls = [call.callFoo(), call.dooFoo("narf"), call.doFoo("zort")]
#mockFoo.assert_has_calls(fooCalls, any_order = True)
# AssertionError: (call.dooFoo('narf'),) not all found in call list
#---------------------------------------------------------------------------------------------------

# Managing a Mock: Listing 14 - Listing 16
# This methods from the Mock class allow you to control and manage your mock object. You can change 
# how the mock behaves, alter some of its attributes, or restore the mock to its pre-test state. 
# You can even change the response values for each mocked method or for the mock itself.

#---------------------------------------------LISTING 14--------------------------------------------
# attach_mock() lets you add a second mock object to your mock. This method takes two arguments: the 
# second mock object (aMock) and an attribute name (aName).
# I create two mock objects, mockFoo and mockBar, each one with a different spec. To mockFoo, I add 
# mockBar using attach_mock() and the name "fooBar". Once that is done, I can access the second mock 
# and its attributes via the property fooBar. And I can still access the attributes for the first 
# mock, mockFoo.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
#class Bar(object):
    # instance properties
#    _barValue = 456
     
#    def callBar(self):
#        pass
     
#    def doBar(self, argValue):
#        pass
 
# create the first mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
# create the second mock object
#mockBar = Mock(spec = Bar)
#print mockBar
# returns: <Mock spec='Bar' id='2784400'>
 
# attach the second mock to the first
#mockFoo.attach_mock(mockBar, 'fooBar')
 
# access the first mock's attributes
#print mockFoo
# returns: <Mock spec='Foo' id='495312'>
#print mockFoo._fooValue
# returns: <Mock name='mock._fooValue' id='428976'>
#print mockFoo.callFoo()
# returns: <Mock name='mock.callFoo()' id='448144'>
 
# access the second mock and its attributes
#print mockFoo.fooBar
# returns: <Mock name='mock.fooBar' spec='Bar' id='2788592'>
#print mockFoo.fooBar._barValue
# returns: <Mock name='mock.fooBar._barValue' id='2788016'>
#print mockFoo.fooBar.callBar()
# returns: <Mock name='mock.fooBar.callBar()' id='2819344'>
#print mockFoo.fooBar.doBar("narf")
# returns: <Mock name='mock.fooBar.doBar()' id='4544528'>
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 15--------------------------------------------
# configure_mock() lets you make wholesale changes to the mock object. Its sole argument is a 
# sequence of key/value pairs, each key being the attribute you want changed. If the mock does not 
# have the specified attribute, configure_mock() will add the attribute to the mock.
# I have a mock object (mockFoo) with class Foo for a spec and 555 for a return_value. Then with 
# configure_mock(), I changed the return_value property to 999. When I call mockFoo directly, I get 
# 999 for a result, instead of the original 555.
# Next, I prepare a dictionary object (fooSpec) into which I set the return values for two mocked 
# methods and the side effect for doFoo(). I pass fooSpec into configure_mock(), taking care to 
# prefix fooSpec with '**'. Invoking callFoo() now returns "narf" as a result; and invoking doFoo(), 
# regardless of input, raises a StandardError signal. If I alter fooSpec, setting the side-effect 
# value for doFoo() to None, I get a result of "zort" when invoking doFoo().
#---------------------------------------------------------------------------------------------------
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
#mockFoo = Mock(spec = Foo, return_value = 555)
#print mockFoo()
# returns: 555
 
#mockFoo.configure_mock(return_value = 999)
#print mockFoo()
# returns: 999
 
#fooSpec = {'callFoo.return_value':"narf", 'doFoo.return_value':"zort", 'doFoo.side_effect':StandardError}
#mockFoo.configure_mock(**fooSpec)
 
#rint mockFoo.callFoo()
# returns: narf
#print mockFoo.doFoo("narf")
# raises: StandardError
 
#fooSpec = {'doFoo.side_effect':None}
#mockFoo.configure_mock(**fooSpec)
#print mockFoo.doFoo("narf")
# returns: zort
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 16--------------------------------------------
# mock_add_spec() lets you add new attributes to the mock object. Its function is similar to the 
# constructor argument spec, except mock_add_spec() works on an existing object, and it "erases" 
# those attributes set by the constructor. The method takes two arguments: the attribute spec 
# (aSpec) and a spec_set flag (aFlag). Again, the spec may be a list of strings or it may be a 
# class. The added attributes are read-only by default, but passing a True to the spec_set flag make 
# those same attributes writable.
# Listing 16 demonstrates mock_add_spec() in action. The mock object (mockFoo) starts with attributes 
# coming from class Foo. When I access two of the attributes (_fooValue and callFoo()), I get a 
# result confirming their presence. Then, I use mock_add_spec() to add class Bar to mockFoo. The mock 
# object now assumes the attributes declared in class Bar. If I access any Foo attribute, the mock 
# object raises an AttributeError to signal their absence.
#---------------------------------------------------------------------------------------------------
# The class interfaces
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
#class Bar(object):
    # instance properties
#    _barValue = 456
     
#    def callBar(self):
#        pass
     
#    def doBar(self, argValue):
#        pass
     
# create the mock object
#mockFoo = Mock(spec = Foo)
 
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
#print mockFoo._fooValue
# returns <Mock name='mock._fooValue' id='2788112'>
#print mockFoo.callFoo()
# returns: <Mock name='mock.callFoo()' id='2815376'>
 
# add a new spec attributes
#mockFoo.mock_add_spec(Bar)
 
#print mockFoo
# returns: <Mock spec='Bar' id='491088'>
#print mockFoo._barValue
# returns: <Mock name='mock._barValue' id='2815120'>
#print mockFoo.callBar()
# returns: <Mock name='mock.callBar()' id='4544368'>
 
#print mockFoo._fooValue
# raises: AttributeError: Mock object has no attribute '_fooValue'
#print mockFoo.callFoo()
# raises: AttributeError: Mock object has no attribute 'callFoo'

# resetMock() puts the mock object back to its pre-test state. It clears the mock's call statistics 
# and asserts. It does not clear the return_value and side_effect properties for both mock and its 
# method attributes. Do this to reuse the mock and avoid the overhead of creating another mock.
# Finally, you can assign a return value or side-effect to each method attribute. This you do through 
# the accessors return_value and side_effect. For example, to make the method callFoo() return a 
# value of "narf", use the return_value accessor as follows:
#mockFoo.callFoo.return_value = "narf"
# To give callFoo() the side-effect of TypeError, use the side_effect accessor as follows:
#mockFoo.callFoo.side_effect = TypeError
# To clear the side-effect, pass None to the accessor:
#ockFoo.callFoo.side_effect = None
# You can also use the same two accessors to change how the mock object responds to a factory call.
#---------------------------------------------------------------------------------------------------

# Statistics with a Mock: Listing 17 - Listing 20
# This methods consists of accessors that track any calls made to a mock object. The accessor called 
# returns a True when the mock gets a factory call, False otherwise.

#---------------------------------------------LISTING 17--------------------------------------------
# I create mockFoo, the called accessor returns a False result. If I do a factory call, it returns a 
# True result. But what if I create a second mock object, then invoke a mocked method callFoo()? In 
# that case, the called accessor will only give a False result.
# The accessor call_count gives the number of times a mock object gets a factory call. 
# I create mockFoo, call_count gives the expected result of 0. When I make a factory call to mockFoo, 
# call_count increases by 1. When I invoke the mocked method callFoo(), call_count remains unchanged. 
# If I do a second factory call, call_count should increase by 1 more.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#       print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# create the first mock object
#mockFoo = Mock(spec = Foo)
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#print mockFoo.called
# returns: False
 
#mockFoo()
#print mockFoo.called
# returns: True
 
#mockFoo = Mock(spec = Foo)
#print mockFoo.called
# returns: False
 
#mockFoo.callFoo()
#print mockFoo.called
# returns: False

#print mockFoo.call_count
# returns: 0
 
#mockFoo()
#print mockFoo.call_count
# returns: 1
 
#mockFoo.callFoo()
#print mockFoo.call_count
# returns: 1
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 18--------------------------------------------
#The accessor call_args returns the arguments used in a factory call. Listing Nineteen demonstrates 
# its action. For a newly created mock object (mockFoo), the call_args accessor gives a result of 
# None. If I make a factory call, passing "zort" for input, call_args reports it as "call('zort')". 
# Note the call keyword in the result. For a second factory call, without input, call_args returns 
# "call()". A third factory call, with "troz" for input, gives the result "call('troz')" from 
# call_args. But when I invoke the mocked method callFoo(), the call_args accessor still returns 
# "call('troz')".
#The accessor call_args_list also reports the arguments used in a factory call. But while call_args 
# returns the most recent arguments, call_args_list returns a list, with the first item being the 
# earliest argument.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# create the first mock object
#mockFoo = Mock(spec = Foo, return_value = "narf")
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
#print mockFoo.call_args
# returns: None
 
#mockFoo("zort")
#print mockFoo.call_args
#print mockFoo.call_args_list
# returns: call('zort') \n [call('zort')]
 
#mockFoo()
#print mockFoo.call_args
#print mockFoo.call_args_list
# returns: call() \n [call('zort'), call()]
 
#mockFoo("troz")
#print mockFoo.call_args
#print mockFoo.call_args_list
# returns: call('troz') \n [call('zort'), call(), call('troz')]
 
#mockFoo.callFoo()
#print mockFoo.call_args
#print mockFoo.call_args_list
# returns: call('troz') \n [call('zort'), call(), call('troz')]
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 19--------------------------------------------
# method_calls in action. With a newly created mockFoo, method_calls returns an empty list. The same 
# also happens when I do a factory call. When I invoke the mocked method callFoo(), method_calls 
# returns a list object with one entry. When I invoke doFoo(), passing "narf" for input, 
# method_calls returns a list with two items. Notice how each method name appears in the order of 
# its invocation.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# create the first mock object
#mockFoo = Mock(spec = Foo, return_value = "poink")
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
#print mockFoo.method_calls
# returns []
 
#mockFoo()
#print mockFoo.method_calls
# returns []
 
#mockFoo.callFoo()
#print mockFoo.method_calls
# returns: [call.callFoo()]
 
#mockFoo.doFoo("narf")
#print mockFoo.method_calls
# returns: [call.callFoo(), call.doFoo('narf')]
 
#mockFoo()
#print mockFoo.method_calls
# returns: [call.callFoo(), call.doFoo('narf')]
#---------------------------------------------------------------------------------------------------

#---------------------------------------------LISTING 20--------------------------------------------
#The last accessor mock_calls reports all calls made by the test subject to the mock object. The 
# result is again a list, but now showing both factory and method calls.
#---------------------------------------------------------------------------------------------------
# The mock object
#class Foo(object):
    # instance properties
#    _fooValue = 123
     
#    def callFoo(self):
#        print "Foo:callFoo_"
     
#    def doFoo(self, argValue):
#        print "Foo:doFoo:input = ", argValue
 
# create the first mock object
#mockFoo = Mock(spec = Foo, return_value = "poink")
#print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
#print mockFoo.mock_calls
# returns []
 
#mockFoo()
#print mockFoo.mock_calls
# returns [call()]
 
#mockFoo.callFoo()
#print mockFoo.mock_calls
# returns: [call(), call.callFoo()]
 
#mockFoo.doFoo("narf")
#print mockFoo.mock_calls
# returns: [call(), call.callFoo(), call.doFoo('narf')]
 
#mockFoo()
#print mockFoo.mock_calls
# returns: [call(), call.callFoo(), call.doFoo('narf'), call()]
#---------------------------------------------------------------------------------------------------

# Testing with a Mock
# In the test setup are three classes. The Order class is the test subject. It models a single item 
# purchase order, which it fills from a data source. The Warehouse class is the test resource. 
# It contains a sequence of key/value pairs, the key being the item name, the value being the 
# available quantity. And the OrderTest class is the test case itself.

#---------------------------------------------LISTING 21--------------------------------------------
# Listing 21 describes the Order class. The class declares three properties: the item name 
# (_orderItem), the requested quantity (_orderAmount) and the filled quantity (_orderFilled). Its 
# constructor takes two arguments, which it uses to populate the properties _orderItem and 
# _orderAmount. Its __repr__() method returns a summary of the purchase order.
#---------------------------------------------------------------------------------------------------
class Order(object):
    # instance properties
    _orderItem = "None"
    _orderAmount = 0
    _orderFilled = -1
     
    # Constructor
    def __init__(self, argItem, argAmount):
        print "Order:__init__"
         
        # set the order item
        if (isinstance(argItem, str)):
            if (len(argItem) > 0):
                self._orderItem = argItem
         
        # set the order amount
        if (argAmount > 0):
            self._orderAmount = argAmount
         
    # Magic methods
    def __repr__(self):
       # assemble the dictionary
        locOrder = {'item':self._orderItem, 'amount':self._orderAmount}
        return repr(locOrder)
     
    # Instance methods
    # attempt to fill the order
    def fill(self, argSrc):
        print "Order:fill_"
         
        try:
            # does the warehouse has the item in stock?
            if (argSrc is not None):
                if (argSrc.hasInventory(self._orderItem)):
                    # get the item
                    locCount =    argSrc.getInventory(self._orderItem, self._orderAmount)
                 
                    # update the following property
                    self._orderFilled = locCount
                else:
                    print "Inventory item not available"
            else:
                print "Warehouse not available"
        except TypeError:
            print "Invalid warehouse"
     
    # check if the order has been filled
    def isFilled(self):
        print "Order:isFilled_"
        return (self._orderAmount == self._orderFilled)

class Warehouse(object):    
    # private properties
    _houseName = None
    _houseList = None
         
    # accessors
    def warehouseName(self):
        return (self._houseName)
     
    def inventory(self):
        return (self._houseList)
     
     
    # -- INVENTORY ACTIONS
    # set up the warehouse
    def setup(self, argName, argList):
        pass
     
    # check for an inventory item
    def hasInventory(self, argItem):
        pass
     
    # retrieve an inventory item
    def getInventory(self, argItem, argCount):
        pass
         
    # add an inventory item
    def addInventory(self, argItem, argCount):
        pass

class OrderTest(unittest.TestCase):
    # declare the test resource
    fooSource = None
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "OrderTest:setUp_:begin"
         
        # identify the test routine
        testName = self.id().split(".")
        idString = testName[1]
        testName = testName[2]
        print testName + " " + idString
         
        # prepare and configure the test resource
        if (testName == "testA_newOrder"):
            print "OrderTest:setup_:testA_newOrder:RESERVED"
        elif (testName == "testB_nilInventory"):
            self.fooSource = Mock(spec = Warehouse, return_value = None)
        elif (testName == "testC_orderCheck"):
            self.fooSource = Mock(spec = Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 0
        elif (testName == "testD_orderFilled"):
            self.fooSource = Mock(spec = Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 10
        elif (testName == "testE_orderIncomplete"):
            self.fooSource = Mock(spec = Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 5
        else:
            print "UNSUPPORTED TEST ROUTINE"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "OrderTest:tearDown_:begin"
        print ""
     
    # test: new order
    # objective: creating an order
    def testA_newOrder(self):
        # creating a new order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)
         
        # test for a nil object
        self.assertIsNotNone(testOrder, "Order object is a nil.")
         
        # test for a valid item name
        testName = testOrder._orderItem
        self.assertEqual(testName, "mushrooms", "Invalid item name")
         
        # test for a valid item amount
        testAmount = testOrder._orderAmount
        self.assertGreater(testAmount, 0, "Invalid item amount")
     
    # test: nil inventory
    # objective: how the order object handles a nil inventory
    def testB_nilInventory(self):
        """Test routine B"""
        # creating a new order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)
         
        # fill the order
        testSource = self.fooSource()
        testOrder.fill(testSource)
         
        # print the mocked calls
        print self.fooSource.mock_calls
         
        # check the call history
        testCalls = [call()]
        self.fooSource.assert_has_calls(testCalls)

    # test: checking the inventory
    # objective: does the order object check for inventory?
    def testC_orderCheck(self):
        """Test routine C"""
        # creating a test order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)
         
        # perform the test
        testOrder.fill(self.fooSource)
         
        # perform the checks
        self.assertFalse(testOrder.isFilled())
        self.assertEqual(testOrder._orderFilled, 0)
         
        self.fooSource.hasInventory.assert_called_once_with("mushrooms")
        print self.fooSource.mock_calls
         
        # creating another order
        testOrder = Order("cabbage", 10)
        print repr(testOrder)
         
        # reconfigure the test resource
        self.fooSource.hasInventory.return_value = False
        self.fooSource.reset_mock()
         
        # perform the test
        testOrder.fill(self.fooSource)
         
        # perform the checks
        self.assertFalse(testOrder.isFilled())
        self.assertEqual(testOrder._orderFilled, -1)
         
        self.fooSource.hasInventory.assert_called_once_with("cabbage")
        print self.fooSource.mock_calls

    # test: fulfilling an order
    # objective: how does the order object behave with a successful transaction
    def testD_orderFilled(self):
        """Test routine D"""
        # creating a test order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)
         
        # perform the test
        testOrder.fill(self.fooSource)
        print testOrder.isFilled()
         
        # perform the checks
        self.assertTrue(testOrder.isFilled())
        self.assertNotEqual(testOrder._orderFilled, -1)
         
        self.fooSource.hasInventory.assert_called_once_with("mushrooms")
        self.fooSource.getInventory.assert_called_with("mushrooms", 10)
         
        testCalls = [call.hasInventory("mushrooms"), call.getInventory("mushrooms", 10)]
        self.fooSource.assert_has_calls(testCalls)

     # test: fulfilling an order
    # objective: how does the order object behave with an incomplete transaction
    def testE_orderIncomplete(self):
        """Test routine E"""
        # creating a test order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)
         
        # perform the test
        testOrder.fill(self.fooSource)
        print testOrder.isFilled()
         
        # perform the checks
        self.assertFalse(testOrder.isFilled())
        self.assertNotEqual(testOrder._orderFilled, testOrder._orderAmount)
         
        self.fooSource.hasInventory.assert_called_once_with("mushrooms")
        self.fooSource.getInventory.assert_called_with("mushrooms", 10)
        print self.fooSource.mock_calls
         
        testCalls = [call.hasInventory("mushrooms"), call.getInventory("mushrooms", 10)]
        self.fooSource.assert_has_calls(testCalls)
#---------------------------------------------------------------------------------------------------

newOT = OrderTest('testE_orderIncomplete')
newOT.setUp()
newOT.testE_orderIncomplete()