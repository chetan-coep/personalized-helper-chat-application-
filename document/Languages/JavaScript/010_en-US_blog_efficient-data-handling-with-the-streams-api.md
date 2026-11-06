---
id: "javascript_010"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 10
source_url: "https://developer.mozilla.org/en-US/blog/efficient-data-handling-with-the-streams-api"
language: "en"
retrieved_at: "2026-11-01 21:52:19"
content_hash: "64fd073290ebc40f0ed401bc9586d90fba3440a0beddbeb07cccfef337d33771"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/efficient-data-handling-with-the-streams-api

---

# Efficient data handling with the Streams API

[The Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API) enables you to access streams of data received over the network and process them using JavaScript on your web page.
Previously, if you wanted to process data fetched over the network, you'd have to download the entire resource, wait for it to be in a format you could work with, and then start to process it.
With the Streams API, you can process raw data with JavaScript as it arrives, making it ideal for handling continuous data sources, transforming data on the fly, canceling streams when you've received what you need, and more.

In this article, we'll explore Streams API concepts, usage, and real-world applications. We'll also walk through a practical example of building a small application that uses the API to transform a data stream.

## [Understanding the Streams API](https://developer.mozilla.org#understanding_the_streams_api)

The Streams API provides a standard way to work with streaming data in JavaScript. It allows you to process data chunk by chunk, making it efficient for handling large resources or real-time data in web applications. You should be aware of these key concepts in the Streams API:

- [**Chunks**](https://developer.mozilla.org#chunks)
- The data is read sequentially in pieces called chunks.
A chunk can be one byte or something larger, like a [typed array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays) of a specific size.
A single stream can have chunks of different sizes and types.
- [**Backpressure**](https://developer.mozilla.org#backpressure)
- The API automatically manages backpressure, ensuring that fast producers don't overwhelm slow consumers. This is handled through internal queuing mechanisms.
- [**Piping**](https://developer.mozilla.org#piping)
- The API provides methods like [`pipeThrough()`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/pipeThrough) and [`pipeTo()`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/pipeTo) to connect streams, allowing for chained processing of data.

The API includes the following abstractions for different types of streams:

- [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)
- Represents a source from which data can be read. It can be created from various sources like fetch responses or file inputs.
- [`WritableStream`](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)
- Represents a destination to which data can be written. It can be used for tasks like writing to files or sending data to servers.
- [`TransformStream`](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream)
- Allows modification of data as it passes from a readable stream to a writable stream. It's useful for tasks like compression or encryption.

## [Building a Node application](https://developer.mozilla.org#building_a_node_application)

To begin, deploy a server by following the steps outlined in the [Deploying a server on Vultr](https://developer.mozilla.org/en-US/blog/deploying-node-js-applications-with-pm2-on-vultr/#deploying_a_server_on_vultr) section in our previous article.
Next, access the server terminal [via SSH](https://docs.vultr.com/how-to-use-ssh-with-vultr-servers) and set up a project for our web application.

We'll be using the [Nano](https://help.ubuntu.com/community/Nano) text editor to create and edit our project files on the server.
You can check the [shortcuts cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) for help using Nano.
We'll also be using [Uncomplicated Firewall (UFW)](https://help.ubuntu.com/community/UFW) to control the traffic that is allowed in and out of the server.
In our application, Node.js serves the index of our application and runs the application using [`http-server`](https://www.npmjs.com/package/http-server).
Servers such as Python and [Apache](https://docs.vultr.com/all?page_number=1&searchQuery=apache) can also be used to achieve similar results.
We enable incoming traffic through port 8000 using UFW.

1. Create a project directory, and navigate into it. bash```
mkdir streaming-app && cd streaming-app
```
2. Initialize a Node.js project. bash```
npm init -y
```
3. Install an HTTP server. bash```
npm install http-server
```
4. Create an HTML file. bash```
nano index.html
```
5. Copy and paste the code below into the index.html file. html```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>File Stream Transformer</title>
  </head>
  <body>
    <h1>File Stream Transformer</h1>
    <button id="loadFileButton">Load and Transform File</button>
    <br />
    <h2>Transformed Content:</h2>
    <pre id="outputText"></pre>
    <script src="app.js"></script>
  </body>
</html>
```
6. Save and exit the file.
7. Create a text file `textfile.txt` in the project directory, and provide some sample text.
You can use the contents of [this text file](https://raw.githubusercontent.com/mdn/dom-examples/main/streams/strings-transform-stream/goethe-faust-1.txt) for convenience.

## [Creating a sample Streams API app](https://developer.mozilla.org#creating_a_sample_streams_api_app)

1. In the streaming-app directory, create a JavaScript file. bash```
nano app.js
```
2. Copy and paste the JavaScript code below into app.js. js```
document.addEventListener("DOMContentLoaded", initializeApp);
function initializeApp() {
  const loadFileButton = document.getElementById("loadFileButton");
  const outputText = document.getElementById("outputText");
  loadFileButton.addEventListener("click", () =>
    fetchAndTransformFile(outputText),
  );
}
async function fetchAndTransformFile(outputElement) {
  clearOutput(outputElement);
  try {
    const response = await fetch("textfile.txt");
    const readableStream = response.body;
    const transformStream = createTransformStream();
    const writableStream = createWritableStream(outputElement);
    await readableStream.pipeThrough(transformStream).pipeTo(writableStream);
    console.log("File stream processing completed");
  } catch (error) {
    handleError(error, outputElement);
  }
}
function createTransformStream() {
  return new TransformStream({
    transform(chunk, controller) {
      const text = new TextDecoder().decode(chunk);
      const upperCaseChunk = text.toUpperCase();
      controller.enqueue(new TextEncoder().encode(upperCaseChunk));
    },
  });
}
function createWritableStream(outputElement) {
  return new WritableStream({
    write(chunk) {
      const text = new TextDecoder().decode(chunk);
      outputElement.textContent += text;
    },
  });
}
function clearOutput(outputElement) {
  outputElement.textContent = "";
  outputElement.style.color = "black";
}
function handleError(error, outputElement) {
  console.error("Error during stream processing:", error);
  outputElement.textContent = `An error occurred: ${error.message}`;
  outputElement.style.color = "red";
}
```
3. Save and exit the file.
4. Allow incoming connections to port 8080. bash```
ufw allow 8080
```
5. Start a file server. bash```
npx http-server
```
6. Visit the application URL at `http://<server-ip>:8080`, and click the **Load and Transform** button.
You will see that the entire text file is fetched and converted into uppercase characters.

When the **Load and Transform** button is clicked, the `fetchAndTransformFile()` function fetches `textfile.txt` from the server's filesystem.
The server responds with the data as a `ReadableStream`, which allows the file to be processed in chunks.
On the client side, this `ReadableStream` is piped through a `TransformStream` that converts each chunk of text to uppercase.
The transformed chunks are then piped to a `WritableStream`, which appends the resulting text to an HTML element for display.
This shows how you can use the Streams API to fetch files, and process, transform, and display the data in the browser as it's fetched instead of performing operations on the entire file in-memory.

## [Real-world use cases and examples](https://developer.mozilla.org#real-world_use_cases_and_examples)

1. In video streaming platforms
  - **Use case:** For efficient processing and delivery of large video files.
  - **Example:** A video streaming service can use Streams API to break down large video files into smaller chunks, process them (e.g., apply filters or compress), and deliver them to the user progressively.
This allows for smoother playback and reduced initial loading times.
2. In data visualization applications
  - **Use case:** For real-time processing and visualization of large datasets or continuous data streams.
  - **Example:** A financial dashboard can use Streams API to process market data in real time.
As new data arrives, it can be transformed, filtered, and immediately displayed on charts or graphs, allowing for live updates without overwhelming the browser's resources.
3. In file upload/download systems
  - **Use case:** For handling large file transfers with progress tracking and on-the-fly processing.
  - **Example:** A cloud storage service can use the Streams API to upload large files.
The file can be read as a stream, compressed or encrypted on-the-fly, and sent to the server in chunks.
This allows for progress tracking, pausing and resuming of transfers, and efficient use of memory, especially for very large files.

## [Conclusion](https://developer.mozilla.org#conclusion)

In this article, we delved into the concepts, usage, and practical implementation of the Streams API. We developed a basic application that demonstrates how to use the Streams API to fetch and transform data. Through this hands-on example, we learned how to read, write, and manipulate data streams. We hope this will inspire you to create efficient, responsive, and modern web applications.

Some good next steps to learn more about this API would be to perform more complex processing.
You can look at [one of the MDN Streams API examples](https://github.com/mdn/dom-examples/tree/main/streams/strings-transform-stream), which is very similar to this project, except that it loops over chunks manually and logs each new chunk to the console as it arrives.
The other [examples](https://github.com/mdn/dom-examples/tree/main/streams) show different ways of using this API, and the [Canceling a fetch](https://jakearchibald.com/2016/streams-ftw/#cancelling-a-fetch) demo shows how to stop in-progress network operations when the client has received the data they need.

*This is a sponsored article by Vultr. Vultr is the world's largest privately-held cloud computing platform. A favorite with developers, Vultr has served over 1.5 million customers across 185 countries with flexible, scalable, global Cloud Compute, Cloud GPU, Bare Metal, and Cloud Storage solutions. Learn more about [Vultr](https://www.vultr.com/campaign/compute/).*