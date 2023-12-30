# 0x09. Web infrastructure design

In this Project me and my team we designed a web infrastructure, and I'm the the who was responsible  
to design for Task-2 which is [Secured and monitored web infrastructure]. and the image of the design
can be found on [imgur](https://imgur.com/C1C0xpj).

I really loved this project, as it helped to understand what happens when i type a domain name on website,
and how each component is related or connected to the other from client sendind http request up to getting the response.
This is uselful because it give a clear picture of the web infrastructure and can give more info on what you need to build
and launch a web application or a website, like the resources you will need can also be seen in the design, the database you will use and soon..

## What is DNS

## Basics

DNS is, in simple words, the technology that translates human-adapted,  
text-based domain names to machine-adapted, numerical-based IP

## Monitoring

Just as the heart monitor in a hospital that is making sure that a patient’s heart is beating and at the right beat, software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

You cannot fix or improve what you cannot measure is a famous saying in the tech industry. In the age of the data-ism, monitoring how our software systems are doing is an important thing.

Web stack monitoring can be broken down into 2 categories:

- Application monitoring: getting data about your running software and making sure it is behaving as expected
- Server monitoring: getting data about your virtual or physical server and making sure they  
are not overloaded (could be CPU, memory, disk or network overload)

## Web Server

### Do not mix up web server and server.

A web server is a software that delivers web pages. A server is an actual computer.

But you might hear people referring to a web server using the word server. (Check out the server concept page to learn more about this.)

As mentioned above, a server is a physical machine, an actual computer, but in the Cloud era that could also be a virtual computer, generally called a VM (Virtual Machine) or container.

## Network basics

Networking is a big part of what made computers so powerful and why  
the Internet exists. It allows machines to communicate with each other.

- What is a protocol
- What is an IP address
- What is TCP/IP
- What is an Internet Protocol (IP) port?

## Load balancer

Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such  
huge amounts of traffic? They don’t have just one server, but tens of thousands of them.  
In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

When you have an enterprise application or website that gets lot of hits, your server  
might be under heavy load. In that case, you may want to consider distributing the load across multiple servers.

Load balancer will distribute the work-load of your system to multiple individual systems,  
or group of systems to to reduce the amount of load on an individual system, which in turn increases  
the reliability, efficiency and availability of your enterprise application or website.

# Server

Servers are located in datacenters which are buildings that host hundreds, or even thousands  
of computers (servers). You can think of a server as a computer without a keyboard, mouse,  
or screen, that is accessible only by a network. A server can be physical or virtual. A server runs an OS (operating system).

In computing, a server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients". This architecture is called the client–server model. Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple clients or performing computations for a client. A single server can serve multiple clients, and a single client can use multiple servers. A client process may run on the same device or may connect over a network to a server on a different device. Typical servers are database servers, file servers, mail servers, print servers, web servers, game servers, and application servers.

[Copied from Wikipedia, Intranet and other resources for the purpose of saving short notes on those concepts Learned in ALX SE]
