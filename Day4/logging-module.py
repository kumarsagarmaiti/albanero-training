# Logging is done for the following purposes:
# Information gathering
# Troubleshooting
# Generating statistics
# Auditing
# Profiling

# Logging is not limited to identifying errors in software development. It is also used in detecting security incidents, monitoring policy violations, providing information in case of problems, finding application bottlenecks, or generating usage data.
# Events that should be logged include input validation failures, authentication and authorization failures, application errors, configuration changes, and application start-ups and shut-downs.

# The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
# The logging module provides you with a default logger that allows you to get started without needing to do much configuration. The corresponding methods for each level can be called as shown in the following example:

import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# The output of the above program would look like this:
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message
# The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger. (Loggers are discussed in detail in later sections.) This format, which shows the level, name, and message separated by a colon (:), is the default output format that can be configured to include things like timestamp, line number, and other details.

# Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels if you want. You can also define your own severity levels by changing configurations, but it is generally not recommended as it can cause confusion with logs of some third-party libraries that you might be using.

# You can use the basicConfig(**kwargs) method to configure the logging:
# Some of the commonly used parameters for basicConfig() are the following:

# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.
# By using the level parameter, you can set what level of log messages you want to record. This can be done by passing one of the constants available in the class, and this would enable all logging calls at or above that level to be logged. Here’s an example:


logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

# DEBUG:root:This will get logged
# All events at or above DEBUG level will now get logged.

import logging 

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# One main advantage of logging to a file is that your application does not need to account for the possibility of encountering network-related errors while streaming logs to an external destination. If it runs into any issues with streaming logs over the network, you won’t lose access to those logs, since they’ll be stored locally on each server. Logging to a file also allows you to create a more customized logging setup, where you can route different types of logs to separate files, and tail and centralize those files with a log monitoring service.

# It should be noted that calling basicConfig() to configure the root logger works only if the root logger has not been configured before. Basically, this function can only be called once.

# debug(), info(), warning(), error(), and critical() also call basicConfig() without arguments automatically if it has not been called before. This means that after the first time one of the above functions is called, you can no longer configure the root logger because they would have called the basicConfig() function internally.

# Formatting the Output:
# While you can pass any variable that can be represented as a string from your program as a message to your logs, there are some basic elements that are already a part of the LogRecord and can be easily added to the output format. If you want to log the process ID along with the level and message, you can do something like this:

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
# 18472-WARNING-This is a Warning
# format can take a string with LogRecord attributes in any arrangement you like. The entire list of available attributes can be found here.

# Here’s another example where you can add the date and time info:

# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')
# 2018-07-11 20:12:06,288 - Admin logged in
# %(asctime)s adds the time of creation of the LogRecord. The format can be changed using the datefmt attribute, which uses the same formatting language as the formatting functions in the datetime module, such as time.strftime():


# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')
# 12-Jul-18 20:53:19 - Admin logged out


# The logging module also allows you to capture the full stack traces in an application. Exception information can be captured if the exc_info parameter is passed as True, and the logging functions are called like this:

import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    
# If exc_info is not set to True, the output of the above program would not tell us anything about the exception, which, in a real-world scenario, might not be as simple as a ZeroDivisionError. Imagine trying to debug an error in a complicated codebase with a log that shows only this:

# ERROR:root:Exception occurred

# If you’re logging from an exception handler, use the logging.exception() method, which logs a message with level ERROR and adds exception information to the message. To put it more simply, calling logging.exception() is like calling logging.error(exc_info=True). 

# The most commonly used classes defined in the logging module are the following:

# Logger: This is the class whose objects will be used in the application code directly to call the functions.

# LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

# Handler: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.

# Formatter: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

# Configure multiple loggers and capture the logger name
# To follow the best practice of creating a new logger for each module in your application, use the logging library’s built-in getLogger() method to dynamically set the logger name to match the name of your module:

logger = logging.getLogger(__name__)
# This getLogger() method sets the logger name to __name__, which corresponds to the fully qualified name of the module from which this method is called. This allows you to see exactly which module in your application generated each log message, so you can interpret your logs more clearly.

# For example, if your application includes a lowermodule.py module that gets called from another module, uppermodule.py, the getLogger() method will set the logger name to match the associated module. Once you modify your log format to include the logger name (%(name)s), you’ll see this information in every log message. You can define the logger within each module like this:

# lowermodule.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

def word_count(myfile):
    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            logger.info("this file has %d words", final_word_count)
            return final_word_count
    except OSError as e:
        logger.error("error reading the file")
# [...]

# uppermodule.py

# import lowermodule 

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
# logger = logging.getLogger(__name__)

# def record_word_count(myfile):
#     logger.info("starting the function")
#     try:
#         word_count = lowermodule.word_count(myfile)
#         with open('wordcountarchive.csv', 'a') as file:
#             row = str(myfile) + ',' + str(word_count)
#             file.write(row + '\n')
#     except:
#         logger.warning("could not write file %s to destination", myfile)
#     finally:
#         logger.debug("the function is done for the file %s", myfile)
# If we run uppermodule.py on an accessible file (myfile.txt) followed by an inaccessible file (nonexistentfile.txt), the logging module will generate the following output:

# 2019-03-27 21:16:41,200 __main__ INFO:starting the function
# 2019-03-27 21:16:41,200 lowermodule INFO:this file has 44 words
# 2019-03-27 21:16:41,201 __main__ DEBUG:the function is done for the file myfile.txt
# 2019-03-27 21:16:41,201 __main__ INFO:starting the function
# 2019-03-27 21:16:41,202 lowermodule ERROR:[Errno 2] No such file or directory: 'nonexistentfile.txt'
# 2019-03-27 21:16:41,202 __main__ DEBUG:the function is done for the file nonexistentfile.txt
# The logger name is included right after the timestamp, so you can see exactly which module generated each message. If you do not define the logger with getLogger(), each logger name will show up as root, making it difficult to discern which messages were logged by the uppermodule as opposed to the lowermodule. Messages that were logged from uppermodule.py list the __main__ module as the logger name, because uppermodule.py was executed as the top-level script.

# Although we are now automatically capturing the logger name as part of the log format, both of these loggers are configured with the same basicConfig() line. In the next section, we’ll show you how to streamline your logging configuration by using fileConfig() to apply logging configuration across multiple loggers.