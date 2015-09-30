@Grapes([
	@Grab(group='ch.qos.logback', module='logback-classic', version='1.1.3'),
	@Grab('org.slf4j:slf4j-api:1.6.1')])

import org.slf4j.*
import groovy.util.logging.Slf4j
import ch.qos.logback.core.*
import ch.qos.logback.classic.encoder.*
import java.nio.file.Paths;

// Use annotation to inject log field into the class.
@Slf4j
class Family {
    static {
        new FileAppender().with {
            name = 'file appender'
            cwd = Paths.get("").toAbsolutePath().toString();
            file = cwd + "/" + "logfile.log"
            context = LoggerFactory.getILoggerFactory()
            encoder = new PatternLayoutEncoder().with {
                context = LoggerFactory.getILoggerFactory()
                pattern = "%date{HH:mm:ss.SSS} [%thread] %-5level %logger{35} - %msg%n"
                start()
                it
            }
            start()
            log.addAppender(it)
        }
    }

    def father() {
        log.debug 'car engine is hot'
        log.error 'my car is stuck'
    }

    def mother() {
        log.debug 'dont have a water in the kitchen'
        log.error 'Cant make a cake'
    }
}

def helloWorld = new Family()
helloWorld.father()
helloWorld.mother()