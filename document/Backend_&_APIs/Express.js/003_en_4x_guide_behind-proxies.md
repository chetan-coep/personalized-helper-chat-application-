---
id: "express.js_003"
technology: "Express.js"
category: "Backend & APIs"
title: "Express behind proxies · Express.js 4.x"
doc_order: 3
source_url: "https://expressjs.com/en/4x/guide/behind-proxies"
language: "en"
retrieved_at: "2026-11-03 17:40:21"
content_hash: "8565614ff09bcf8f275ce9464192b930c033401421d8757da34ca7a769aa56c5"
---

# Express behind proxies · Express.js 4.x

Source: https://expressjs.com/en/4x/guide/behind-proxies

---

When running an Express app behind a reverse proxy, some of the Express APIs may return different values than expected. In order to adjust for this, the `trust proxy` application setting may be used to expose information provided by the reverse proxy in the Express APIs. The most common issue is express APIs that expose the client’s IP address may instead show an internal IP address of the reverse proxy.

### Note

When configuring the `trust proxy` setting, it is important to understand the exact setup of the
reverse proxy. Since this setting will trust values provided in the request, it is important that
the combination of the setting in Express matches how the reverse proxy operates.

The application setting `trust proxy` may be set to one of the values listed in the following table.

| Type | Value | 
|---|---|
| Boolean | If `true`, the client’s IP address is understood as the left-most entry in the `X-Forwarded-For` header. If `false`, the app is understood as directly facing the client and the client’s IP address is derived from `req.socket.remoteAddress`. This is the default setting. Warning When setting to `true`, it is important to ensure that the last reverse proxy trusted is removing/overwriting all of the following HTTP headers: `X-Forwarded-For`, `X-Forwarded-Host`, and `X-Forwarded-Proto`, otherwise it may be possible for the client to provide any value. | 
| IP addresses | An IP address, subnet, or an array of IP addresses and subnets to trust as being a reverse proxy. The following list shows the pre-configured subnet names: You can set IP addresses in any of the following ways: When specified, the IP addresses or the subnets are excluded from the address determination process, and the untrusted IP address nearest to the application server is determined as the client’s IP address. This works by checking if `req.socket.remoteAddress` is trusted. If so, then each address in `X-Forwarded-For` is checked from right to left until the first non-trusted address. | 
| Number | Use the address that is at most `n` number of hops away from the Express application. `req.socket.remoteAddress` is the first hop, and the rest are looked for in the `X-Forwarded-For` header from right to left. A value of `0` means that the first untrusted address would be `req.socket.remoteAddress`, i.e. there is no reverse proxy. Warning When using this setting, it is important to ensure there are not multiple, different-length paths to the Express application such that the client can be less than the configured number of hops away, otherwise it may be possible for the client to provide any value. | 
| Function | Custom trust implementation. | 

Enabling `trust proxy` will have the following impact:

- The value of [req.hostname](https://expressjs.com/en/4x/api/request/#reqhostname) is derived from the value set in the `X-Forwarded-Host` header, which can be set by the client or by the proxy.
- `X-Forwarded-Proto` can be set by the reverse proxy to tell the app whether it is `https` or `http` or even an invalid name. This value is reflected by [req.protocol](https://expressjs.com/en/4x/api/request/#reqprotocol).
- The [req.ip](https://expressjs.com/en/4x/api/request/#reqip) and [req.ips](https://expressjs.com/en/4x/api/request/#reqips) values are populated based
on the socket address and `X-Forwarded-For` header, starting at the first untrusted address.

The `trust proxy` setting is implemented using the [proxy-addr](https://www.npmjs.com/package/proxy-addr) package. For more information, see its documentation.