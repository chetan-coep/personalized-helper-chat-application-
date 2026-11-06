---
id: "node.js_065"
technology: "Node.js"
category: "Backend & APIs"
title: "Node.js"
doc_order: 65
source_url: "https://nodejs.org/en/blog/weekly/weekly-update2015-11-27"
language: "en"
retrieved_at: "2026-11-01 21:59:24"
content_hash: "b270734b07ca0c255a1ed8719078363b32c92bb609a8df672a45d716f588671d"
---

# Node.js

Source: https://nodejs.org/en/blog/weekly/weekly-update2015-11-27

---

# Weekly Update - Nov 27th, 2015

Minwoo Jung

### [Node.js News — November 27th](https://nodejs.org#nodejs-news--november-27th)

Node v0.12.8 (LTS) is released

### [Node v0.12.8 (LTS) Releases](https://nodejs.org#node-v0128-lts-releases)

This week we have one release: [Node v0.12.8 (LTS)](https://nodejs.org/en/blog/release/v0.12.8/). Complete changelog from previous releases can be found [on GitHub](https://github.com/nodejs/node/blob/main/CHANGELOG.md).

### [Notable changes](https://nodejs.org#notable-changes)

- \[[`7d11208f68`](https://github.com/nodejs/node/commit/7d11208f68)\] - **build**: backport tools/release.sh (Rod Vagg) [#3642](https://github.com/nodejs/node/pull/3642)
- \[[`6fb0b92fa0`](https://github.com/nodejs/node/commit/6fb0b92fa0)\] - **build**: backport config for new CI infrastructure (Rod Vagg) [#3642](https://github.com/nodejs/node/pull/3642)
- \[[`83441616a5`](https://github.com/nodejs/node/commit/83441616a5)\] - **build**: fix --without-ssl compile time error (Ben Noordhuis) [#3825](https://github.com/nodejs/node/pull/3825)

### [CVE-2015-8027 Denial of Service Vulnerability / CVE-2015-6764 V8 Out-of-bounds Access Vulnerability](https://nodejs.org#cve-2015-8027-denial-of-service-vulnerability--cve-2015-6764-v8-out-of-bounds-access-vulnerability)

- Security release coming on December 1 or December 2 (depending on your timezone) will resolve a denial-of-service vulnerability. Be prepared to update!
- New releases of v0.12.x, v4.x and v5.x will be made available with appropriate fixes for CVE-2015-8027 and CVE-2015-6764 (for v4.x and v5.x only)
- Please contact [\[email protected\]](https://nodejs.org/cdn-cgi/l/email-protection#dba8beb8aea9b2afa29bb5b4bfbeb1a8f5b4a9bc) if you wish to report a vulnerability in Node.js.

See /blog/vulnerability/cve-2015-8027\_cve-2015-6764/ for more information.

### [NodeUp](https://nodejs.org#nodeup)

- [NodeUp 96](http://nodeup.com/ninetysix): "A Node v5.0 Show" with Rebecca Turner, Rod Vagg, and Rich Trott".

### [Community Updates](https://nodejs.org#community-updates)

- [Top Node.js metrics to watch](https://www.oreilly.com/ideas/top-nodejs-metrics-to-watch), "Track key metrics to keep your Node.js apps running smoothly."
- [Why we stopped vendoring our npm dependencies](http://blog.bithound.io/why-we-stopped-vendoring-our-npm-dependencies/), "Should I check my node\_modules directory into my repository?"
- [Clearing the air: Is WordPress being rewritten in Node.js and React?](http://wesbos.com/wordpress-calypso-react/), "Almost all front-end tooling is built in Node.js."
- [Massive Memory Gains in Node.js 4.2](http://goldfirestudios.com/blog/140/Massive-Memory-Gains-in-Node.js-4.2), "Not only did we see our memory graphs smooth out significantly, but the total memory usage dropped."

If you have spotted or written something about Node.js, do come over to our [Evangelism team repo](https://github.com/nodejs/evangelism) and suggest it on the [Issues page](https://github.com/nodejs/evangelism/issues), specifically the Weekly Updates issue.

### [Upcoming Events](https://nodejs.org#upcoming-events)

- [Node.js Interactive](http://events.linuxfoundation.org/events/node-interactive), December 8th - 9th at Portland, US.

Have an event about Node.js coming up? You can put your events here through the [Evangelism team repo](https://github.com/nodejs/evangelism) and announce it in the [Issues page](https://github.com/nodejs/evangelism/issues), specifically the Weekly Updates issue.