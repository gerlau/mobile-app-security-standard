# authn-bp01 - \[Authentication\] Use multi-factor authentication (MFA)

## Control Statement

Insert here

## Control Assessment Objective

Insert here

## Control Description

Traditional authentication methods typically require only a username and password, or other single-factor authentication to validate a user’s identity. However, attackers can easily bypass these authentication mechanisms by stealing credentials to impersonate the user.

Developers should use MFA to validate users’ identity. This involves using multiple layers of identity  verification, requiring users to provide more than one type of authentication factor to verify their identity. This security control protects the authenticity of the user and the confidentiality, integrity and privacy of sensitive data

## Control Implementation Guidance

Implement best practices, such as the following:
- **Select multiple authentication methods** – Implement authentication methods from at least two of the following authentication factors:
    - **Knowledge-based factors (AUTHN-BP01a)** – Knowledge-based factors, also known as “something you know”, are memorised secrets that rely on information that users remember. These factors include authentication methods such as Personal Identification Numbers (PINs) and passwords.
    - **Possession-based factors (AUTHN-BP01b)** – Possession-based factors, also known as “something you have”, are items that users possess. For instance, users can possess items such as a trusted hardware device, a SIM card or an email account. Users then present generated One-Time Passwords (OTPs) or cryptographic keys as proof of possession.
    - **Inherence-based factors (AUTHN-BP01c)** – Inherence-based factors, also known as “something you are”, are biometric identifiers that rely on users’ unique physical characteristics. These factors include authentication methods such as fingerprint, retina, facial or voice scans.
- **Use authentication methods with lower risks** – Assess the risks of account takeover through stolen credentials using the table below. Minimise these risks to prevent phishing attacks and provide higher assurance of the user’s identity.
    - **Knowledge-based authentication methods**, such as passwords or passphrases, are considered highly risky because they can easily be stolen and used for account takeovers. These methods are especially vulnerable to phishing attacks, where fake websites deceive users into revealing their credentials.
    - **Possession-based authentication methods**
        - **One-time passwords (OTPs)**, such as SMS or email OTPs, are considered risky because they can be stolen and used for account takeovers. These methods are especially vulnerable to real-time phishing attacks, where fake websites deceive users into revealing their OTPs and replay them in real time.
        - **Cryptographic keys**, such as public key infrastructure (PKI) certificates or Passkeys, are considered less risky because they are resistant to phishing. These methods are difficult to steal, as they are stored in secure elements on mobile devices.
    - **Inherence-based authentication methods**, such as fingerprint or facial verification, are considered less risky because they are resistant to phishing. These methods are difficult to steal, as they are stored in secure elements on mobile devices.

The overall MFA risk is determined by the most vulnerable authentication method used. For example, combining a password (high risk) with fingerprint verification (low risk) does not mitigate the inherent vulnerabilities of passwords, thereby undermining the effectiveness of MFA.

To achieve optimal security, minimise risks across all authentication factors. For instance, using a combination of Passkeys (low risk) and facial verification (low risk) employs two phishing-resistant methods, significantly reducing the likelihood of account compromise through stolen credentials.

## Control Additional Notes

Firstly, Single Sign-On (SSO) allows users to access multiple apps with a single login, streamlining the login process and reducing reliance on multiple authentication methods, making it more difficult for attackers to gain access. However, this creates a single point of failure whereby if the SSO system is compromised, attackers can gain access to all apps a user can access through SSO. Hence, implement SSO with MFA for a robust security posture.

Next, Passkeys offer a modern alternative to traditional passwords. Passkeys simplify authentication while adhering to 2FA by combining PIN or biometrics with a possession-based factor like a device or security token. Passkeys can be set up in synchronised mode or device-bound.

Lastly, consider the difference between first-party and third-party authentication. First-party authentication involves developers building and maintaining the method themselves. While this grants more control and customisation, it can be time-consuming and expensive. On the other hand, third-party authentication involves using pre-built methods from another established company. While they can be integrated quickly and offer regular security patches, developers will have less control and customisation over such authentication methods.

## Control References

This security control is referenced from the following standards:
- OWASP Mobile Application Security Verification Standard v2.1.0 (January 2024), MASVS-AUTH-1 and MASVS-AUTH-3.
- MAS Technology Risk Management Guidelines (January 2021), section(s) 9.1.5 and 14.2.1.
- ENISA Smartphone Secure Development Guidelines (December 2016), section(s) 2.10.

Details of security best practices are referenced from the following documents:
- OWASP Mobile Application Security Testing Guide v1.7.0 (October 2023),
    - Mobile App Authentication Architectures, General Guidelines on Testing Authentication, page 51,
    - Mobile App Authentication Architectures, Two-factor Authentication, page 56.
- Android Developers, Identity, Guides, Add a sign-in workflow, https://developer.android.com/identity/sign-in.
- Apple Developer, Documentation, Authentication Services, https://developer.apple.com/documentation/AuthenticationServices.
- Apple Developer, Documentation, Local Authentication, https://developer.apple.com/documentation/LocalAuthentication.
- CISA, Implementing Phishing-Resistant MFA (October 2022).
