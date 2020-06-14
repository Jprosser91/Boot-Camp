# OWASP Top 10 - A Primer
This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities
### A1:2017 - Injections
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of injection attacks
 - What kind of activity it can be used for (data exfiltration, backdooring, etc.)

#### How it Works
TODO: Explain how attackers build and deliver injection payloads. 
- **Hint**: They might start with identifying services they can connect to, then finding which languages they can inject...

#### Scenario
TODO: Navigate to DVWA's SQL Injection. Run and explain the following UNION injection: 
                                            
   - `%' UNION SELECT user, password from users #`

Specifically, explain:
- What the intended SQL query looks like
- What the SQL query looks like after injection
- What this query means (explain the queries to the left and right of the `UNION` keyword)
- Two strategies for patching this vulnerability

TODO: Find an example of a command injection payload. Explain how it gets delivered, and what it does. Compare/contrast this to a SQL injection.

---
### A2:2017 - Broken Authentication
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of broken authentication vulnerabilities
 - What kind of damage can be done (e.g., data stealing, account tampering, etc.)

#### How it Works
TODO: Do the **Scenario** exercise below, then explain why the **Brute Force** exercise in DVWA qualifies as a Broken Authentication vulnerability.

#### Scenario
TODO: Use Burp Intruder to solve the **Brute Force** exercise on DVWA. You'll need to:
- Intercept a request to the login form
- Set positions aroudn the username and password
- Provide a list of usernames and passwords to test
- Use Intruder to brute-force the login form
- **Hint**: [Intruder Attack Types](https://portswigger.net/burp/documentation/desktop/tools/intruder/positions#attack-type)
- **Hint**: [Grep - match](https://portswigger.net/burp/documentation/desktop/tools/intruder/options#grep-match)

As you complete the exercise, write down the steps of your attack, and document the following below:
- The raw request you captured in Proxy
- The request you set positions around in Intruder
- The raw response that contained the correct user credentials

---
##### Raw Request 
```
# Raw HTTP Request Here
```

##### Intruder Request 
```
# HTTP Request w/ Intruder Positions Here
```
##### Valid Response(s)
```
# HTTP Response w/ Valid Credentials Here
```

##### Mitigation
TODO: Explain two strategies for preventing this kind of attack.

---
### A6:2017 - Security Misconfiguration
#### Definition / Description
TODO: Use the OWASP document to explain:
 - The source, severity, and scope of security misconfigurations
 - What kind of damage it can do to a business

#### How it Works
TODO: Explain the following:
- How [allow_url_include](http://php.net/manual/en/filesystem.configuration.php) and [allow_url_fopen]() are responsible for the RFI vulnerability on DVWA
- The conditions under which RFI is possible. Refer to [this document](https://www.offensive-security.com/metasploit-unleashed/file-inclusion-vulnerabilities/)
- - Why the RFI on DVWA qualifies as a Security Misconfiguration vulnerability

#### Scenario
TODO: Figure out how to turn off `allow_url_fopen` and `allow_url_include`. Include the code you'd add to `php.ini` below.

  ```php
  // TODO: Disables allow_url_fopen
  // TODO: Disables allow_url_include
  ```
---
### A7:2017 - Cross-Site Scripting (XSS)
#### Definition / Description
TODO: Use the OWASP document to explain
- The source, scope, and severity of XSS vulnerabilities
- The three different classes of XSS vulnerabilities
- What kinds of attacks can be carried out with XSS
 
#### How it Works
TODO: Explain how a reflected XSS payload gets echoed from an HTTP request to an HTML document.

#### Scenario
TODO: Explain how the reflected XSS on DVWA works. Exploit it with Burp Repeater, and include the HTTP request containing your payload below.

```
# HTTP Request w/ Reflected XSS Payload Here
```
 
