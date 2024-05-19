Web APIs vs Native Library APIs
###############################

:date: 2024-05-02
:category: APIs
:author: Jeremiah Igrami
:tags: apis, api-documentation
:slug: web-vs-library-apis



There are many types of APIs. We often organize them into two broad categories: 
web APIs and native library APIs. 

Web APIs, also known as HTTP APIs or web services, are a class of APIs that 
communicate and exchange information over the internet using the HTTP protocol. 
Web APIs are typically used for connecting web applications and services. 
For example, a web developer can use the Twitter API to add some Twitter 
functionalities, like posting tweets and reading timelines, to his website.

With Web APIs, it doesn't matter what language you use because requests and 
responses are made through a common web protocol — HTTP. 
REST (representational state transfer ) and SOAP (simple object access protocol)
are the most common types of web API.

Native Library APIs, a.k.a. system-level APIs or library APIs, 
are toolkits (called code libraries) developers use to extend the 
capabilities of their apps or access some useful functions of the operating
system or software development framework they’re working with. 

Native Library APIs provide a way for applications to tap into the native 
capabilities of the system they’re running on. For example, a mobile app 
developer may use the Andriod API, a set of tools for building Android apps, 
to add text messaging and GPS functionalities to the app she’s building. 
These APIs are typically written in programming languages like C or C++ and are
specific to the platform they are designed for.


The difference between web APIs and native-library APIs?
=========================================================

Web APIs enable communication between web-based services using standard
internet protocols. Native-library APIs provide access to system-level 
functionality for applications built on a specific platform. 

While Web APIs deal with communication over the internet, 
Native-library APIs deal with the resources and capabilities of the 
device or computer on which an application is running. 

Native-library APIs are typically platform- and language-specific.  
For example, the Windows API ``(Win23 API)`` is a platform for building **native 
C/C++ Windows** applications (note the language and platform specs). 
It can’t be used for building, say, a macOS application. 
You’ll need the Cocoa framework for that. 

Web APIs, on the other hand, are language- and platform-agnostic: 
it doesn’t matter whether you’re writing in Python or Java or C --- from a Mac or 
Windows or Linux OS --- you can send a request to the 
Open Weather Map API and get a kind response.  
