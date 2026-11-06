---
id: "node.js_069"
technology: "Node.js"
category: "Backend & APIs"
title: "Node.js"
doc_order: 69
source_url: "https://nodejs.org/en/blog/weekly/weekly-update2016-01-11"
language: "en"
retrieved_at: "2026-11-01 21:59:29"
content_hash: "82c43cf8fcab595eba6eeb656754e3896161077ecb30e1e8d1a4a53244fbc1ec"
---

# Node.js

Source: https://nodejs.org/en/blog/weekly/weekly-update2016-01-11

---

# Weekly Update - Jan 11th, 2016

Minwoo Jung

### [Node.js News](https://nodejs.org#nodejs-news)

Node v5.4.0 (Current) is released

### [Node v5.4.0 (Current) Releases](https://nodejs.org#node-v540-current-releases)

Last week we had one release: [Node v5.4.0 (Current)](https://nodejs.org/en/blog/release/v5.4.0/). Complete changelog from previous releases can be found [on GitHub](https://github.com/nodejs/node/blob/main/CHANGELOG.md).

### [Notable changes](https://nodejs.org#notable-changes)

- **http**:
- This release also includes several minor performance improvements:
  - **assert**: deepEqual is now speedier when comparing TypedArrays (Claudio Rodriguez) [#4330](https://github.com/nodejs/node/pull/4330).
  - **lib**: Use arrow functions instead of bind where possible (Minwoo Jung) [node#3622](https://github.com/nodejs/node/pull/3622).
  - **node**: Improved accessor perf of `process.env` (Trevor Norris) [#3780](https://github.com/nodejs/node/pull/3780).
  - **node**: Improved performance of `process.hrtime()` (Trevor Norris) [#3780](https://github.com/nodejs/node/pull/3780), (Evan Lucas) [#4484](https://github.com/nodejs/node/pull/4484).
  - **node**: Improved GetActiveHandles performance (Trevor Norris) [#3780](https://github.com/nodejs/node/pull/3780).
  - **util**: Use faster iteration in `util.format()` (Jackson Tian) [#3964](https://github.com/nodejs/node/pull/3964).

### [Community Updates](https://nodejs.org#community-updates)

- [History of Node.js on a Timeline](https://blog.risingstack.com/history-of-node-js/), "This is the history of Node.js on a timeline, from 2009 until now (December 2015)"
- [What the web platform can learn from Node.js](https://developer.atlassian.com/blog/2015/11/what-the-web-platform-can-learn-from-nodejs/), "Evolving the platform"

If you have spotted or written something about Node.js, do come over to our [Evangelism team repo](https://github.com/nodejs/evangelism) and suggest it on the [Issues page](https://github.com/nodejs/evangelism/issues), specifically the Weekly Updates issue.

### [Upcoming Events](https://nodejs.org#upcoming-events)

- [NodeConf Adventure 2016](https://ti.to/nodeconf/adventure-2016), "First batch of NodeConf Adventure tickets are up!", June 9th–12th, 2016 - Walker Creek Ranch, Marin, CA, USA
- [NationJS Node Day Conference](http://nationjs.com/), TICKETS ARE AVAILABLE NOW, March 11, 2016 - Washington, DC

Have an event about Node.js coming up? You can put your events here through the [Evangelism team repo](https://github.com/nodejs/evangelism) and announce it in the [Issues page](https://github.com/nodejs/evangelism/issues), specifically the Weekly Updates issue.