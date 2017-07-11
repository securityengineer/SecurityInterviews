Security Questions
==================

Cryptography
------------

* What’s the difference between encoding, encryption, and hashing?

* How should you store a password?

* What’s the difference between symmetric and public-key (asymmetric) cryptography?
* What are some scenarios where one is more appropriate then the other?

* What’s the difference between diffie-hellman and RSA?
	Diffie-Hellman is a key-exchange protocol, and RSA is an encryption/signing protocol. RSA requires you to have key material beforehand, DH does not.
* What kind of attack is a standard diffie-hellman exchange vulnerable to?
	MITM

* How do you generate a random number?
* What's wrong with your standard RNG?

* Describe HMAC in detail.

* Describe encryption modes, CTR, ECB, CBC.


DNS
---
* How does DNS work?
* When does DNS use TCP?
	DNS goes over TCP when the size of the request or the response is greater than a single packet such as with responses that have many records or many IPv6 responses or most DNSSEC responses. Some resolver implementations use TCP for all queries.
* How does a DNS Amplification Attack work?
	Open Recursion + Amplification = DDoS on Steroids
	Spoofed ANY requests.
* What are some different DNS record types and when are they used?
* What do you have to worry about when running your own DNS servers?

Incident Response
-----------------
* What sort of anomalies would you look for to identify a compromised system?

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
* Why are you interested in working at Company?
* Have you ever used the product before?
* Describe what happens when you type www.google.com?
* What type of work environment would you dislike and why?
* What kind of work do you enjoy the most and why?
* If you had unlimited time and money what would you work on?

Mobile
------
* What makes iOS more secure than Android?

Networking
----------

* How does traceroute work, in full detail?
* List and describe TCP/IP flags

Network Security
----------------
* What is the difference between the VPN model and the BeyondCorp model?
* What is a SYN flood?
* What are SYN Cookies?
* How can you defend again a network level DoS attack?
* How does an IDS work?
* How does an IPS work?
* How can an IDS or IPS be bypassed?
* How would you go about securing a web server?


Programming Languages (Computer Science)
----------------------------------------
* Strong typing vs Weak typing
* What is the difference between a strongly typed language and a statically typed language?
	https://stackoverflow.com/questions/2690544/what-is-the-difference-between-a-strongly-typed-language-and-a-statically-typed


SSL/TLS
-------
* How does SSL work?
* How would you design an internal CA?
* Describe the process of a TLS session being set up when someone visits a secure website.
* How does HSTS work?
* How does HPKP work?
* How can HPKP be used for evil purposes?
* How does CRL work?
* How does OCSP work?


TCP and UDP
-----------
* What are the differences between TCP and UDP?
* Which is more secure? 
* How does TCP work?
* What is the purpose of the 3 way handshake?


Web Security
------------
* How do you approach assessing a web application?
* What is CSRF?
	CSRF stands for cross-site request forgery, it is when an attacker makes a victim's browser make request that takes an action on behalf of the user without their knowledge, say /change_password?pw=foo and the victims password is changed without their knowledge.
* Can you CSRF a POST request?
	Sure, via hidden form-fields. You'd have to make the user click a button to send the request, perhaps a 'click here to win a million bucks' button. 
* How do you mitigate CSRF?
	Create a token 

	There is also the newer way of marking cookies as Same-Site, but it's only supported on the latest browser versions.

* Can you put the CSRF token in a cookie header?
* If the CSRF token isn't sent automatically, how does it get sent back and forth each time by legitimate code?
* What is bad about the double-submit mitigation?
* How do you fake a Referer header?

* What is XSS?
* How do you mitigate XSS?
	Input validation and output sanitization, with focus on the latter.

* What is an open-redirect?
* How do you mitigate open-redirects?

* What is SSRF?
* How do you mitigate SSRF?

* What is XXE?
* How do you mitigate XXE?

* What are the different flags of a cookie?
* What is an origin?
* What is CORS?
* What are some examples of application level DoS and how do you mitigate them?

* What can you do with Burp Suite?

* How does OAuth work?
* How does SAML work?