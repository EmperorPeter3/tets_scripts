import groovy.mock.interceptor.MockFor;
import groovy.mock.interceptor.StubFor;
//---MAP COERCION---

class TranslationService {
    String convert(String key) {
        return "test"
    }
}

def service = [convert: { String key -> 'some text' }] as TranslationService
assert 'some text' == service.convert('key.text')

//---CLOSURE COERCION---

abstract class BaseService {
    abstract void doSomething()
}

BaseService bservice = { -> println 'doing something' }
bservice.doSomething()

//---MOCKFOR and STUBFOR---

class Person {
    String first, last, one, two, three
}

class Family {
    Person father, mother
    def nameOfMother() { "$mother.first $mother.last $mother.one" }
    def nameOfFather() { "$father.first $father.last $father.one" }
}

//---MOCKFOR---

def mock = new MockFor(Person)
mock.demand.getFirst{ 'dummy' }
mock.demand.getLast{ 'name' }
mock.demand.getOne{ 'blablabla' }
mock.use {
    def mary = new Person(first:'Mary', last:'Smith', one: 'Klacklac')
    def f = new Family(mother:mary)
    assert f.nameOfMother() == 'dummy name blablabla'
}
mock.expect.verify() 

//---STUBFOR--- LOOSED ORDER

def stub = new StubFor(Person)
stub.demand.with {
	getOne{ 'blablabla' }
	getLast{ 'name' }
	getFirst{ 'dummy' }
}
stub.use {
    def john = new Person(first:'John', last:'Smith', one:'Klockloc')
    def f = new Family(father:john)
    assert f.nameOfFather() == 'dummy name blablabla'
}
stub.expect.verify() 