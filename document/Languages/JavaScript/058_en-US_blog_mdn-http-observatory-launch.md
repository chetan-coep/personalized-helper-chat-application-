---
id: "javascript_058"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 58
source_url: "https://developer.mozilla.org/en-US/blog/mdn-http-observatory-launch"
language: "en"
retrieved_at: "2026-11-01 21:53:13"
content_hash: "a026034de207bf87c40521f646414eba85ffd55ed756e2d0c6182472a92e7c2b"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/mdn-http-observatory-launch

---

# Introducing the MDN HTTP Observatory

In its lifespan, Mozilla's HTTP Observatory tool has scanned over 6.9 million websites, providing useful, actionable insights into how developers can improve web security and guard their sites against would-be attackers.

The HTTP Observatory tests website compliance with security best practices, mainly concerning the correct usage of HTTP headers. When a scan is complete, it provides a report to tell the user how well their site is doing, with an overall score and grade, and links to documentation explaining what they need to do to improve their security.

Today, we are delighted to announce that the HTTP Observatory's new home is MDN! This blog post explains a little bit of the history behind the tool, how we got to where we are now, what the migration means for Observatory and MDN, and what Observatory tests.

Check out the [new HTTP Observatory](https://developer.mozilla.org/en-US/observatory) now.

## [A brief history of the MDN HTTP Observatory](https://developer.mozilla.org#a_brief_history_of_the_mdn_http_observatory)

In 2016, then-Mozilla security engineer [April King](https://grayduck.mn/) [announced the original release of the HTTP Observatory tool](https://grayduck.mn/2016/08/25/observatory-by-mozilla-a-new-tool/). Originally conceived as an internal testing tool to help Mozilla developers apply security best practices to their own websites, the HTTP Observatory was packaged into a website that anyone could use after April looked in dismay around the web and saw how few sites were applying those best practices.

Since then, HTTP Observatory has exploded in popularity, with over 6.9 million websites being scanned a total of 47 million times! Mozilla's Infrastructure Security Team has regularly maintained the tool to improve the service, adding new tests as security best practices and standards are updated, and removing tests related to older technologies as they become obsolete.

That isn't the full story, however. The success of the HTTP Observatory hinges on two things.

- First of all, the site gamifies the process of improving website security â each set of test results comes with a score and a grade, and developers over the years have shown great enthusiasm about achieving that sometimes-elusive A+ Observatory rating!
- Second, HTTP Observatory helps developers make sense of website security requirements â which can often be rather opaque and difficult to understand â by providing understandable feedback on how to fix issues highlighted by its dozen or so tests. Related documentation can be found all in one place.

## [Moving the HTTP Observatory to MDN](https://developer.mozilla.org#moving_the_http_observatory_to_mdn)

So what prompted the move to MDN? The short answer is that MDN and HTTP Observatory complement each other very well â they both have developer education and improving the health of the internet as core driving principles.

The longer answer is that HTTP Observatory is a well-respected tool in the web and security communities, but it hasn't seen a major update for quite some time. Mozilla decided that the tool deserved to evolve and find new audience members to benefit from the security knowledge contained within.

MDN is a popular site with a large audience of web developers who could benefit from this knowledge, so it seemed like a perfect new home. In addition, our team was very excited to update the tool's UI, functionality, and documentation, bringing it up-to-date and giving it some polish. This update was done in collaboration with Mozilla's Infrastructure and Security Risk teams; they provided expert advice to help us update the HTTP Observatory tests and documentation with confidence.

See the [HTTP Observatory on MDN](https://developer.mozilla.org/en-US/observatory), and the [Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides) that accompany it.

## [What does the HTTP Observatory test?](https://developer.mozilla.org#what_does_the_http_observatory_test)

The HTTP Observatory tests the following security features:

- Secure [cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) configuration: Access to cookies should be locked down as much as possible, to prevent attacks such as [Cross-site scripting](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) (XSS) and [Cross-site request forgery](https://developer.mozilla.org/en-US/docs/Glossary/CSRF) (CSRF).
- [Cross-origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) (CORS): Limit cross-origin resource access to no more than necessary.
- [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) (CSP): Provides fine-grained control over the locations from which resources on a site can be loaded.
- [`Strict-Transport-Security`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security): Enforces site connections via HTTPS only, to prevent [manipulator-in-the-middle](https://developer.mozilla.org/en-US/docs/Glossary/MitM) (MiTM) attacks.
- Correct [redirection behavior](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/TLS#http_redirections) to HTTPS on initial loading: Prevents attacks during initial loading.
- [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy): Prevents leaking of sensitive information.
- [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity) (SRI): Verify that fetched resources are delivered without unexpected manipulation.
- [`X-Content-Type-Options`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options): Enforce correct resource MIME types, to further mitigate XSS attacks.
- [`Content-Security-Policy: frame-ancestors`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors) and [`X-Frame-Options`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options): Limit the ability of other sites to embed your site in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe), helping to prevent [clickjacking](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Clickjacking).
- [`Cross-Origin-Resource-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Resource-Policy): Prevent certain requests from other origins accessing resources on your site, to mitigate speculative side-channel attacks like [Spectre](<https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)>).

## [FAQ](https://developer.mozilla.org#faq)

>
  ### [Should I implement all recommendations?](https://developer.mozilla.org#should_i_implement_all_recommendations)

Yes, you should do it if possible. There is no way to programmatically determine the risk level of any given site. However, while your site may not be high-risk, it is still worth learning about the defensive security standards highlighted by Observatory, and implementing them wherever you can.

### [If I get an A+ grade, does that mean my site is secure?](https://developer.mozilla.org#if_i_get_an_a_grade_does_that_mean_my_site_is_secure)

We'd love to say that any site that gets an A+ Observatory grade is perfectly secure, but there are a lot of security considerations that we can't test. Observatory tests for preventative measures against [Cross-site scripting (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) attacks, [manipulator-in-the-middle (MiTM)](https://developer.mozilla.org/en-US/docs/Glossary/MitM) attacks, cross-domain information leakage, insecure [cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies), [Content Delivery Network](https://developer.mozilla.org/en-US/docs/Glossary/CDN) (CDN) compromises, and improperly issued certificates.

However, it does not test for outdated software versions, [SQL injection](https://developer.mozilla.org/en-US/docs/Glossary/SQL_Injection) vulnerabilities, vulnerable content management system plugins, improper creation or storage of passwords, and more. These are just as important as the issues Observatory *does* test for, and site operators should not be neglectful of them simply because they score well on Observatory.

### [Can I scan non-websites, such as API endpoints?](https://developer.mozilla.org#can_i_scan_non-websites_such_as_api_endpoints)

The HTTP Observatory is designed for scanning websites, not API endpoints. It can be used for API endpoints, and the security headers expected by Observatory shouldn't cause any negative impact for APIs that return exclusively data, such as JSON or XML. However, the results may not accurately reflect the security posture of the API. API endpoints generally should only be accessible over HTTPS. The recommended configuration for API endpoints is:

```
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
Strict-Transport-Security: max-age=63072000
X-Content-Type-Options: nosniff
```
### [Can other people see my test results?](https://developer.mozilla.org#can_other_people_see_my_test_results)

Anyone can choose to scan any domain, and the scan history for each domain is public. However, HTTP Observatory does not store user data related to each scan. In the old version of HTTP Observatory, users could choose to set their scan to "public" or keep it private (the default), and there was a "recent scans" list where domain names were listed. "Recent scans" was the main feature that users would potentially wish to opt-out from, but it is no longer supported, hence there is now no reason to provide the "public" flag.

### [When did the move occur?](https://developer.mozilla.org#when_did_the_move_occur)

The new HTTP Observatory was launched on MDN on July 2, 2024. The [old Mozilla Observatory](https://observatory.mozilla.org/) â containing HTTP Observatory plus other tools like TLS Observatory, SSH Observatory, and Third-party tests â has been deprecated and will be sunset in September 2024.

**Note:** Historic scan data has been preserved, and is included in the provided scan history for each domain.


### [What has changed after the migration?](https://developer.mozilla.org#what_has_changed_after_the_migration)

The MDN team has:

- Updated the user experience to improve the site's look and make it easier to use. For example, the recommendations highlighted by the test results are all shown together, instead of one at a time.
- Updated the [accompanying documentation](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides#content_security_fundamentals) to bring it up to date and improve legibility.
- Changed the "rescan" checkbox and its underlying mechanics:
  - There is no longer a rescan parameter.
  - A site can only be scanned and a new result returned every 60 seconds.
  - Deep-linking into a report initiates a rescan if the previous scan data is older than 24 hours.
- Updated the [tests](https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring#tests-and-score-modifiers) to bring them up-to-date with latest security best practices:
  - Removed the out-of-date `X-XSS-Protection` test.
  - Removed the out-of-date Flash and Silverlight (`clientaccesspolicy.xml` and `crossdomain.xml`) embedding tests.
  - Added a [`Cross-Origin-Resource-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Resource-Policy) (CORP) test.
  - Updated the [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy) test to update the score modifier for `referrer-policy-unsafe` and remove the `referrer-policy-no-referrer-when-downgrade` result.

### [Has the HTTP Observatory API been updated to use the new tests?](https://developer.mozilla.org#has_the_http_observatory_api_been_updated_to_use_the_new_tests)

Not yet. The API will continue using the old test infrastructure for a while, therefore you will see some small differences between test scores returned by the API and the website. The API will be updated to use the new tests in a near-future iteration.

### [Does the new HTTP Observatory provide specific TLS and certificate data?](https://developer.mozilla.org#does_the_new_http_observatory_provide_specific_tls_and_certificate_data)

The previous Observatory site included specific results tabs containing TLS and certificate analysis data. The new one does not, and there are currently no plans to include these features: it provides a clear focus on HTTP data.

### [(Redirection) What is the](https://developer.mozilla.org#redirection_what_is_the_http_redirection_test_assessing) [HTTP redirection test](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/TLS#http_redirection) assessing?

This test is checking whether your web server is making its initial redirection from HTTP to HTTPS, on the same hostname, before doing any further redirections. This allows the HTTP [`Strict-Transport-Security`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) (HSTS) header to be applied properly.

For example, this redirection order is correct:

`http://example.com` â `https://example.com` â `https://www.example.com`

An incorrect (and penalized) redirection looks like this:

`http://example.com` â `https://www.example.com`

### [(X-Frame-Options) What if I want to allow my site to be framed?](https://developer.mozilla.org#x-frame-options_what_if_i_want_to_allow_my_site_to_be_framed)

As long as you are explicit about your preference by using the `Content-Security-Policy`[`frame-ancestors`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors) directive, you will pass the [`X-Frame-Options`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) test. For example, to allow your site to be framed by any HTTPS site:

```
Content-Security-Policy: frame-ancestors https:
```
## [Try it out](https://developer.mozilla.org#try_it_out)

We would love you to [try out the HTTP Observatory on MDN](https://developer.mozilla.org/en-US/observatory)! Visit it now, scan your site, and fill out our [HTTP Observatory survey](https://survey.alchemer.com/s3/7897385/MDN-HTTP-Observatory) to let us know what you think of the experience.

HTTP Observatory's documentation, which is linked from the test results, is now also found on MDN, in our [Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides) section. Again, read through it and let us know how it can be improved.