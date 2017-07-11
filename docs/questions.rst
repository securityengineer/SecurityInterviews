Security Questions
==================

Cryptography
------------

* What’s the difference between encoding, encryption, and hashing?

* How should you safely store a password?

* What’s the difference between symmetric and public-key (asymmetric) cryptography?
* What are some scenarios where one is more appropriate then the other?

* What’s the difference between diffie-hellman and RSA?
	Diffie-Hellman is a key-exchange protocol, and RSA is an encryption/signing protocol. RSA requires you to have key material beforehand, DH does not.
* What kind of attack is a standard diffie-hellman exchange vulnerable to?
	MITM

* How do you safely generate a random number?
* What's wrong with your standard RNG?

* Describe HMAC in detail.

* Describe encryption modes, CTR, ECB, CBC, GCM.

* What's good and bad about TOFU?

* How do collisions in hash functions affect security (in theory and in practice)?

* Should you authenticate then encrypt, or encrypt then authenticate or encrypt and authenticate at the same time? Why?
	Encrypt and then authenticate, because otherwise you'll have to decrypt before checking the authenticity of the plaintext. This has caused all sorts of problems with, for example, SSL, leading to POODLE, Lucky13, BEAST, CRIME and other acronyms. See https://moxie.org/blog/the-cryptographic-doom-principle/ for more information.

DNS
---
* How does DNS work?
* When does DNS use TCP?
	DNS goes over TCP when the size of the request or the response is greater than a single packet such as with responses that have many records or many IPv6 responses or most DNSSEC responses. Some resolver implementations use TCP for all queries.
* How does a DNS Amplification Attack work?
	Open Recursion + Amplification = DDoS on Steroids

	ANY requests normally give the biggest response, so they're typically used.
* What are some different DNS record types and when are they used?
* What do you have to worry about when running your own DNS servers?
* How can you use DNS for instrusion detection?
	https://blogs.technet.microsoft.com/office365security/dns-intrusion-detection-in-office-365/
* How many root servers are there?

Infrastructure Security
-----------------------

* How do you bootstrap trust amongst hosts?
* How do you handle SSH host keys?
* ssh(1) warns you about a hostkey fingerprint mismatch. What do you do? (No, be honest.) How do you solve this problem?
* What are the top 3 things you do to improve a system's security?
* How do you manage / utilize shared jumpboxes in your environment? What are some of the implications and pitfalls of having them?
* Are there alternatives to storing passwords?
* Why should or shouldn't you have . (dot) in your PATH?
* Explain how SSH tunneling / port forwarding works. What are some pitfalls or risks?
* How does sudo(1) work? What are common related pitfalls?
* What is the difference in permissions on a directory that is mode 0777 and one that is mode 1777?
	The 1 is what is called the sticky bit. A directory whose sticky bit is set becomes an append-only directory, or, more accurately, a directory in which the deletion of files is restricted. A file in a sticky directory may only be removed or renamed by a user if the user has write permission for the directory and the user is the owner of the file, the owner of the directory, or the super-user.

Incident Response
-----------------
* What sort of anomalies would you look for to identify a compromised system?
* Tell me about a security incident you've taken part in, what was your role in the response?

Memory Corruption
-----------------
* What are common pitfalls in string handling?
* What is a buffer overflow?
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
* Describe what happens when you type www.google.com and hit Enter?
* What type of work environment would you dislike and why?
* What kind of work do you enjoy the most and why?
* If you had unlimited time and money and could work on anything, what would you work on?
* Describe your past relationships with other engineering teams.
* Have you ever had to stop an engineer from pushing code that had security issues?
* Where do you see yourself in 5 years?
* Open ended threat modeling questions.
	Maybe read https://www.amazon.com/Threat-Modeling-Designing-Adam-Shostack/dp/1118809998 but if you're a competent security professional these should be the easier part of the interview.

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
* How does nmap work?


Programming Languages (Computer Science)
----------------------------------------
* Strong typing vs Weak typing
* What is the difference between a strongly typed language and a statically typed language?
	https://stackoverflow.com/questions/2690544/what-is-the-difference-between-a-strongly-typed-language-and-a-statically-typed

Reverse Engineering
-------------------

* Calling conventions, x86 and x64
* If you were given a binary that was stripped of it's symbols, how would you get them back?
* If you were given a DLL whose preferred base address conflicted with another, how in IDA would you make the addresses match what you see in say, OllyDbg?

SSL/TLS
-------
* How does SSL work?
* How does SSL certificate verification work?
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

* Your login process requires a password. Talk about the UI decisions around this. What tradeoffs do you make between password complexity requirements and usability? How do you design the user feedback for repeatedly entered wrong passwords?