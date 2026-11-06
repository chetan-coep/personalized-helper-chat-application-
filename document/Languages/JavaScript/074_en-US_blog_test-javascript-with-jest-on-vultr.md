---
id: "javascript_074"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 74
source_url: "https://developer.mozilla.org/en-US/blog/test-javascript-with-jest-on-vultr"
language: "en"
retrieved_at: "2026-11-01 21:53:49"
content_hash: "2c793094b10da4d32725b1f5174ff1ec3d487072515c393c038b27fec5ffcec2"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/test-javascript-with-jest-on-vultr

---

# Testing JavaScript with Jest on Vultr

[Jest](https://jestjs.io/) is a popular [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) testing framework used for testing React and JavaScript codebases. It offers a comprehensive set of matchers for making assertions, allowing users to write tests for many different types of projects. Jest organizes tests into test suites; this structured approach improves both maintainability and readability, leading to more efficient testing workflows.

In this article, we'll explore the various types of tests commonly used in software development and share some good practices and conventions for testing. We'll write JavaScript functions and test them using the Jest testing framework on a Vultr server with the [**NodeJS**](https://www.vultr.com/marketplace/apps/nodejs) marketplace application.

## [Types of tests](https://developer.mozilla.org#types_of_tests)

To ensure code quality and functionality, development typically involves three types of tests. Each type serves a specific purpose:

- **Unit tests**: These tests focus on testing individual units or components, such as functions, methods, or classes. This type of testing ensures that each code component functions correctly on its own.
- **Integration tests**: These tests focus on assessing whether different components of the application interact with each other as expected. Unlike unit tests, which test a single component, these tests involve interactions between multiple units to ensure they function as expected when combined.
- **End-to-end tests**: These tests simulate real user scenarios by testing the application flow from start to finish. These tests are usually automated and interact with the application like a real user, ensuring that the application works as intended in real-world situations.

## [Testing conventions](https://developer.mozilla.org#testing_conventions)

The Arrange-Act-Assert (AAA) pattern is a commonly used convention used to organize and structure unit test cases.

To understand each part, here's an example where we want to test if user emails are alphanumeric (letters and numbers) and use the `example.com` domain:

```
test("returns false for an invalid domain", () => {
  const email = "user123@example.net";
  const result = isValidEmail(email);
  expect(result).toBe(false);
});
```
- **Arrange**: In this phase, you set up the initial condition and prepare the test environment. This includes initializing objects, setting up inputs, and configuring the environment to create the scenario you wish to test. In the above example, we want to test if the `isValidEmail` function correctly identifies invalid emails. We've initialized the `email` variable with a string that does not meet our email criteria because it uses the `.net` TLD instead of `.com`.
- **Act**: In this phase, you perform the action or behavior that you want to test. This could involve calling a method, interacting with an object, or executing a specific piece of code. In the above example, this step involves calling the `isValidEmail` function and passing it the `email` variable as an argument.
- **Assert**: Finally, in this phase, you verify that the outcome of the "Act" phase meets your expectations. In the above example, we've used the `expect` function, provided by the Jest framework, to confirm that the `result` returned by the `isValidEmail` function is correctly identified as `false`, as expected for an invalid email.

## [Setting up the project directory on Vultr](https://developer.mozilla.org#setting_up_the_project_directory_on_vultr)

To begin, deploy a server by following the steps in the section [Deploying a server on Vultr](https://developer.mozilla.org/en-US/blog/deploying-node-js-applications-with-pm2-on-vultr/#deploying_a_server_on_vultr) in our previous article. Ensure that you select **NodeJS** in the **Marketplace Apps** tab. Next, let's proceed to set up a Node.js project and install the Jest framework. We'll then define two functions in separate JavaScript files, which we'll test in the subsequent sections.

1. Verify the Node.js installation by using the following command: bash```
node --version
```
2. Create a project directory, and navigate into it. bash```
mkdir sample
cd sample
```
3. Initialize a Node.js project. bash```
npm init -y
```
4. Install the Jest testing framework. bash```
npm install --save-dev jest
```
The `--save-dev` flag is used to specify that the package is installed as a development dependency. This means that it will be used only during development and testing phases, not for production.
5. Open the `package.json` file. We're using the [Nano text editor](https://www.nano-editor.org/docs.php). Check the [shortcuts cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) for help using Nano.
bash```
nano package.json
```
6. Add a test script. json```
"scripts": {
  "test": "jest"
}
```
7. Save and exit the file (`Ctrl` + `X` to close the file, `Y` when prompted to save the changes).
8. Create a JavaScript file. bash```
nano token.js
```
9. Copy and paste the code below into the `token.js` file. This code demonstrates how to calculate the expiry date of a [JSON Web Token](https://jwt.io/) (JWT) and check if it has expired.
**Note:** The hand-written expiry check shown here is purely for illustration purposes. When handling authentication tokens in real-world projects, relying on well-established libraries, such as [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken), is strongly recommended.
javascript```
/**
 *
 * @param {string} token
 * @returns {Date}
 */
function getTokenExpiryDate(token) {
  if (!token) return null;
  const tokenParts = token.split(".");
  const payload = tokenParts[1];
  const decodedPayload = Buffer.from(payload, "base64").toString();
  const payloadObject = JSON.parse(decodedPayload);
  const expiryDate = new Date(payloadObject.exp * 1000);
  return expiryDate;
}
/**
 *
 * @param {string} token
 * @returns {boolean}
 */
function isTokenExpired(token) {
  const expiryDate = getTokenExpiryDate(token);
  const currentDate = new Date();
  return currentDate > expiryDate;
}
module.exports = { isTokenExpired };
```
The code above defines two functions, `getTokenExpiryDate` and `isTokenExpired`, which calculate the expiry date of the provided JWT token and return `true` or `false` based on the expiration status of the token.
10. Save and exit the file.
11. Create another JavaScript file. bash```
nano email.js
```
12. Copy and paste the following code into the file: javascript```
function isValidEmail(email) {
  const emailRegex = /[a-zA-Z0-9]+@example\.com/;
  return emailRegex.test(email);
}
module.exports = { isValidEmail };
```
The code above defines an `isValidEmail` function that validates the structure of the provided email using a regex.
The regular expression lets us verify that all emails are alphanumeric and end with exactly `@example.com`.
13. Save and exit the file.

## [Writing unit tests with Jest](https://developer.mozilla.org#writing_unit_tests_with_jest)

In this section, you'll learn how to write unit tests for the JavaScript functions defined earlier by using the Jest framework. We'll place these tests in a separate directory within the same project. We recommend that you follow the file naming conventions demonstrated here because Jest automatically treats files ending in `.test.js` as test files.

1. Within the `sample` directory, create another directory called `tests` and navigate into it.
bash```
mkdir tests
cd tests
```
2. Create a JavaScript test file. bash```
nano token.test.js
```
3. Copy and paste the following code into the file: javascript```
const { isTokenExpired } = require("/root/sample/token.js");
describe("isTokenExpired", () => {
  test("should return false if the token is not expired", () => {
    const token = "eyJ0eXAiOiJKV1QiLCJhbGciOi...";
    const result = isTokenExpired(token);
    expect(result).toBe(false);
  });
  test("should return true if the token is expired", () => {
    const token = "eyJ0eXAiOiJKV1QiLCJhbGciOi...";
    const result = isTokenExpired(token);
    expect(result).toBe(true);
  });
});
```
The code above uses the `isTokenExpired` function defined earlier to determine if the function is behaving as expected, returning the correct boolean value based on whether a JWT is expired or not.
**Note:** If you want the `isTokenExpired` function to check real tokens, you can generate expired and non-expired JWTs using a [JSON Web Token Builder](http://jwtbuilder.jamiekurtz.com/) and use them instead of the placeholders in the tests above.
4. Save and exit the file.
5. Create another JavaScript test file. bash```
nano email.test.js
```
6. Copy and paste the following code into the file: javascript```
const { isValidEmail } = require("/root/sample/email.js");
describe("isValidEmail", () => {
  test("returns true for a valid email", () => {
    const email = "user123@example.com";
    const result = isValidEmail(email);
    expect(result).toBe(true);
  });
  test("returns false for an invalid domain", () => {
    const email = "user123@example.net";
    const result = isValidEmail(email);
    expect(result).toBe(false);
  });
});
```
The code above uses the `isValidEmail` function defined earlier and tests it by providing a valid and an invalid email. It checks the validation results by matching the expected output with the actual output.
7. Save and exit the file.

## [Running Jest tests on Vultr](https://developer.mozilla.org#running_jest_tests_on_vultr)

In this section, you'll learn how to run tests using the Jest framework by applying two approaches. In the first method, we'll run individual unit tests for each function defined in the previous sections. In the second method, we'll run tests for both the functions simultaneously.

### [Running individual unit tests](https://developer.mozilla.org#running_individual_unit_tests)

1. Run the token validation tests. bash```
npm test -- tests/token.test.js
```
If the tests pass successfully, your output will look as shown below: ```
 > sample@1.0.0 test
 > jest tests/token.test.js
 PASS  tests/token.test.js
 isTokenExpired
     â should return false if the token is not expired (2 ms)
     â should return true if the token is expired (1 ms)
 Test Suites: 1 passed, 1 total
 Tests:       2 passed, 2 total
 Snapshots:   0 total
 Time:        0.315 s, estimated 1 s
 Ran all test suites matching /tests\/token.test.js/i.
```
2. Next, run the email validation tests. bash```
npm test -- tests/email.test.js
```
If the tests pass successfully, your output will look as shown below: ```
> sample@1.0.0 test
> jest tests/email.test.js
PASS  tests/email.test.js
isValidEmail
    â returns true for a valid email (2 ms)
    â returns false for an invalid domain (1 ms)
Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        0.451 s
Ran all test suites matching /tests\/email.test.js/i.
```

### [Running all tests together](https://developer.mozilla.org#running_all_tests_together)

Run all the tests together by using the following command:

```
npm test
```
If the tests pass successfully, your output will look as shown below:

\> sample@1.0.0 test
> jest
PASS  tests/email.test.js
PASS  tests/token.test.js
Test Suites: 2 passed, 2 total
Tests:       4 passed, 4 total
Snapshots:   0 total
Time:        0.225 s, estimated 1 s
Ran all test suites.

## [Conclusion](https://developer.mozilla.org#conclusion)

In this article, we looked at various types of tests and testing conventions. We explored how to write and run unit tests for functions using Jest on a Vultr server with Node.js pre-installed. By leveraging tools like Jest, you can enhance the reliability and robustness of your code, to develop more stable and maintainable software.

*This is a sponsored article by Vultr. Vultr is the world's largest privately-held cloud computing platform. A favorite with developers, Vultr has served over 1.5 million customers across 185 countries with flexible, scalable, global Cloud Compute, Cloud GPU, Bare Metal, and Cloud Storage solutions. Learn more about [Vultr](https://www.vultr.com/campaign/compute/).*