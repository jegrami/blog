
Eight types of APIs technical writers should know
###################################################

:date: 2023-12-20
:author: Jeremiah Igrami
:category: APIs
:tag: apis, technical-writing
:slug: eight-types-of-apis
:modified: 2024-05-18


API stands for application programming interface. They’re a way for apps to 
interact with each other and exchange information over the internet. APIs differ 
from user interfaces (UIs). The user interface allows communication between a 
system and its end users. For example, Twitter's UI allows you to login to 
your account, post tweets, and interact with the posts of others. Same thing with 
TikTok, Amazon, and other web apps. The UI is basically what you, the user,
see and interact with when you use an application like Instagram.


APIs, on the other hand, provide a way for a developer from one computer to make use 
of the resources and capabilities of another computer. For example, you're building
a ride-hailing application. Essential to this app is a feature that would let 
users select their current location and destination. Luckily, Google has something
called Google Maps, a free web-based mapping service with mappings of
more than 220 countries and territories. Just what my app needs. So, instead of 
coding a map from scratch, you decide to tap into the capabilities of
Google Maps by integrating it into your app through an API. Your app will now be 
able to do things that Google Maps does, like checking your current location or 
choosing a destination.  

The document that guides developers on how to make that software-to-software 
interaction is called an API specification. This document is often written by 
technical writers.

Below is an intro to eight types of APIs you might encounter in your work as 
a technical documentation writer. The goal is to give you an idea of the most
types of APIs technical writers deal with and how they differentiate from
each other.


Simple Object Access Protocol (SOAP)
====================================

SOAP APIs are web services that use the XML Information Set (XML Infoset) 
as their format for exchanging data. The XML Infoset is a file that specifies 
the set of information items, such as `Document Type Declaration` and `Attribute 
Information Items`, that should be included in a valid XML document. Salesforce,
PayPal, and eBay are examples of companies that offer  SOAP APIs.


Representational State Transfer (REST)
=======================================

REST is an API that lets you make requests for resources through URLs. 
With REST APis, you can perform CRUD (create, read, update, delete) operations on
web resources using the HTTP methods ``GET``, ``POST``, ``DELETE``, ``PUT``, 
``OPTIONS``, and ``PATCH``. This is the most common type of web API. And its 
responses are usually returned in JSON or XML format.

Graph APIs
===========

Graph APIs are a special type of APIs that represent data as nodes and edges,
similar to a graph. The data entities are the nodes and the relationship
between them are the edges. For instance, imagine you want to query data from a 
server storing information about books, authors, and reviews. With a REST API, 
to get details about a specific book, its author, and its reviews, you might 
need to make three separate HTTP requests --- each for the particular book, author,
and reviews for that book. But with a Graph API, you can make a single request 
that fetches the book details, its author, and its reviews in one go. The technology 
was designed at Facebook in 2010 and is currently the primary way to access 
Facebook's social graph data (users, posts, likes, comments, etc).

GraphQL 
=========
GraphQL is both a query language for APIs and a runtime for executing those queries.
It provides a complete and intuitive description of all the resources available 
in the API, giving developers the ability to ask for exactly the data they 
need in one query. The structure of the response matches the structure in which
the request was sent. Unlike REST, where you will have to request multiple
entities one by one, GraphQL allows you to include many nested fields and related
entities in one query so you can pull the data all at once. 


Voice Assistant APIs
======================

Voice Assistant APIs are the brains of smart speakers and voice assistants like 
Amazon’s Alexa and Apple’s Siri. They let developers create apps or services that, 
through natural language processing, understand and respond to voice commands 
spoken by the user. When you ask Alexa to play you a song or tell you about the 
weather, Alexa uses a voice recognition API to understand your intent and fetch 
the info or perform the action you asked for.

WebSocket API
==============

In a traditional HTTP transaction, the user's job is to send requests to a server, 
and the server’s job is to fulfill those requests. It's a bit like asking a 
question and getting a single answer each time. Once the server responds, the 
connection closes. And if the user (called client) wants more data, she has to send
another request, starting the process anew. WebSocket APIs make it possible to keep
a constant connection between the client and server until the server has some new 
data to push to the client. Instead of sending individual requests, the client 
and server establish a continuous connection that allows them to send messages 
back and forth at any time without having to make new requests each time. This 
allows real-time data transfer and is suitable for applications that require 
continuous updates, like chat apps and online games.

Internet of Things (IoT) APIs
===============================

IoT APIs simply refer to the growing number of gadgets, or "things," that connect 
to the Internet and communicate with other devices and services on the network. 
Smart fridges, smart TVs, smart copiers, smart thermostats --- these 
internet-enabled devices (often with "smart" in their names) can generate and 
transmit data over the internet using IoT APIs. In other words, IoT APIs allow 
devices like electric cars and smart fridges to talk to each other.

As you may have noted, these APIs all serve different purposes. The choice of what 
API type to use or focus on often depends on what you want your app to do, the data 
requirements, performance needs, and your team's preferences or constraints. 
And now, knowing their strengths and weaknesses, you're better equipped to make 
informed choices about which one is appropriate for a given use case.





