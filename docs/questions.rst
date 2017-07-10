Security Questions
==================

DNS
---
* When does DNS use TCP?
	DNS goes over TCP when the size of the request or the response is greater than a single packet such as with responses that have many records or many IPv6 responses or most DNSSEC responses. Some resolver implementations use TCP for all queries.
* How does a DNS Amplification Attack work?
	Open Recursion + Amplification = DDoS on Steroids
	Spoofed ANY requests.
* What are some different DNS record types and when are they used?
* What do you have to worry about when running your own DNS servers?


Memory Corruption
-----------------
* What is DEP?
* What is ASLR?
* How does ROP work?
* What are some examples of information leaks?
* What is undefined behaviour?
* What are some examples of undefined behaviour?
* How does AFL work?
* How does CFG (or CFI) work?
* How does EMET work?
* If an IDS was looking for a NOP slide, how could you try to bypass it?
* How does ASAN work?
* How does UBSAN work?


Miscellaneous
-------------
* Why did you leave your last job?
* Have you ever worked with someone you disliked before?


Mobile
------
* What makes iOS more secure than Android?


Network Security
----------------
* What is the difference between the VPN model and the BeyondCorp model?
* What is a SYN flood?
* What are SYN Cookies?
* How can you defend again a network level DoS attack?
* How does an IDS work?
* How does an IPS work?
* How can an IDS or IPS be bypassed?


Programming Languages (Computer Science)
----------------------------------------
* Strong typing vs Weak typing
* What is the difference between a strongly typed language and a statically typed language?
	https://stackoverflow.com/questions/2690544/what-is-the-difference-between-a-strongly-typed-language-and-a-statically-typed


SSL/TLS
-------
* How does SSL work?
* How would you design an internal CA?
* How does HSTS work?
* How does HPKP work?
* How can HPKP be used for evil?
* How does CRL work?
* How does OCSP work?


TCP and UDP
-----------
* How does TCP work?
* What is the purpose of the 3 way handshake?


Web Security
------------
* How do you approach assessing a web application?
* What is CSRF?
* How do you mitigate CSRF?
* What is bad about the double-submit mitigation?
* How do you fake a Referer header?

* What is XSS?
* How do you mitigate XSS?

* What is an open-redirect?
* How do you mitigate open-redirects?

* What are the different flags of a cookie?
* What is an origin?
* What is CORS?
* What are some examples of application level DoS and how do you mitigate them?

* What can you do with Burp Suite?

