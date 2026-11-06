---
id: "javascript_063"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 63
source_url: "https://developer.mozilla.org/en-US/blog/modernizing-test-automation-with-test-grid"
language: "en"
retrieved_at: "2026-11-01 21:53:23"
content_hash: "32328475ce9e4e7b79b5000851312ec67aeddf5c0d99710c5c5fc74eab08cf87"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/modernizing-test-automation-with-test-grid

---

# Modernizing conventional test automation with TestGrid

It has become a standard practice for teams to automate their software testing using various tools and scripts. However, the conventional test automation methods have not evolved at the same pace as application development practices. This gap highlights the need to modernize the test automation methods to keep up with faster software development cycles.

[TestGrid](https://testgrid.io/)'s unified testing platform aims to simplify the testing processes by providing easily accessible end-to-end test automation and seamless support for popular tools like Selenium and Appium.

In this article, we will cover both conventional and newer methods for automated testing of web and mobile applications. We'll start by looking at the commonly used test automation methods, see where they are lacking, and discuss ways to increase their efficiency. We'll then dive into the more modern approaches.

## [Using conventional test automation methods](https://developer.mozilla.org#using_conventional_test_automation_methods)

Test automation focuses on scripting user journeys and application functionalities to validate that the application works as expected. The conventional approach to test automation relies primarily on writing test scripts.

One major drawback of this approach is that these scripts can become difficult to maintain as the application functionality grows, leading to a high maintenance overhead. The scripts may also become flaky and result in intermittent failures.

Let's look at two widely adopted approaches for test automation of using Selenium and Appium.

### [Using Selenium to automate web application testing](https://developer.mozilla.org#using_selenium_to_automate_web_application_testing)

Selenium is a popular test automation tool used by developers and testers to write automated UI tests for web applications. These tests can be executed across different web browsers and can be written in one of the many languages supported by Selenium.

Let's look at an example of writing an automated test using Selenium. We'll use a [demo testing website](https://demoqa.com/login) to execute the following steps:

1. Launch a browser of your choice.
2. Navigate to the login page of [demoqa.com](https://demoqa.com/login).
3. Enter a username and password.
4. Click the **Login** button.
5. Verify that the user is logged in and the username is displayed on the screen.

**Note:** You can create a user using the **New User** button so that you have valid credentials for the test automation scenario.


Ensure that you have the necessary prerequisites to start working with Selenium. You can follow the [step-by-step guide to set up Selenium with Java](https://testgrid.io/blog/selenium-with-java-tutorial/) on your system.

This is the Selenium code we'll use to automate the execution of the above steps.

```
public class Login {
  @Test
  public void loginTest() throws InterruptedException {
    WebDriver driver = new ChromeDriver(); // Instantiating the webdriver instance
    driver.get("https://demoqa.com/login"); // Launching the website
    driver.manage().window().maximize(); // Maximizing browser window
    String user = "your user name";
    String pass = "your password";
    // Locating web elements for username, password, and the Login button
    driver.findElement(By.id("userName")).sendKeys(user);
    driver.findElement(By.id("password")).sendKeys(pass);
    driver.findElement(By.id("login")).click();
    // Using sleep to load web elements on page
    Thread.sleep(5000);
    // Capturing the displayed username after login
    String uName = driver.findElement(By.id("userName-value")).getText();
    // Asserting that the logged-in username matches the expected username
    Assert.assertEquals(uName, user);
    // Locating the web element for the Logout button and closing the webdriver instance
    driver.findElement(By.id("submit")).click();
    driver.quit();
  }
}
```
As described in the comments, in this code we are launching our website, locating the web elements, and then performing the needed actions on them. After this code is executed, you should see the successful execution logs.

The above automated test verifies a critical user login functionality. However, building and maintaining such tests can be time-consuming. Any minor change in the application might require updating this code across the test suites, hence adding to the overhead. Additionally, the combination of test environments may be limited with the conventional test automation approach.

### [Using Selenium with TestGrid to automate web application testing](https://developer.mozilla.org#using_selenium_with_testgrid_to_automate_web_application_testing)

Let's use [TestGrid's real device cloud](https://testgrid.io/real-device-testing) to run the Selenium code shown in the previous section on a cloud browser and a platform of our choice. TestGrid allows the reuse of your existing Selenium test scripts and the scaling of your automated test execution.

[Log in to TestGrid](https://public.testgrid.io/signup) and follow the [step-by-step guide for executing your local Selenium code on web browsers](https://testgrid.io/docs/document/executing-your-local-selenium-code-for-web-browsers/).

The image below shows TestGrid's real device cloud dashboard. For our example, we've selected the Firefox browser on a Linux platform.

After following the steps in the guide linked above and setting the desired capabilities, we get the following code:

```
public class TestGridDemoQaLogin {
  @Test
  public void loginTest() throws InterruptedException, MalformedURLException {
    // Setting the desired capabilities to use the TestGrid platform
    DesiredCapabilities dc = new DesiredCapabilities();
    dc.setCapability("browserName", "firefox");
    dc.setCapability("platformName", "linux");
    dc.setCapability("tg:userToken", "Your Token");
    dc.setCapability("tg:udid", "201");
    // Instantiating the remote webdriver instance and passing desired capabilities to it
    WebDriver driver = new RemoteWebDriver(new URL("Your Browser Run URL(Public)"),dc);
    // Remaining steps are the same as in the previous Selenium code
    driver.get("https://demoqa.com/login");
    driver.manage().window().maximize();
    String user = "your user name";
    String pass = "your password";
    driver.findElement(By.id("userName")).sendKeys(user);
    driver.findElement(By.id("password")).sendKeys(pass);
    driver.findElement(By.id("login")).click();
    Thread.sleep(5000);
    String uName = driver.findElement(By.id("userName-value")).getText();
    Assert.assertEquals(uName, user);
    driver.findElement(By.id("submit")).click();
    driver.quit();
  }
}
```
When you execute this code locally on your system, you'll notice that it gets executed on TestGrid's real device cloud. You can view the remote execution from the portal. You can also view the execution status, recording, and run summary on the **Automation Sessions** tab by simply selecting the device on which you executed your test.

### [Using Appium to automate mobile application testing](https://developer.mozilla.org#using_appium_to_automate_mobile_application_testing)

Appium is a popular open-source automation framework for testing native, hybrid, and mobile web applications. Writing Appium scripts requires knowledge of mobile operating systems and an understanding of programming languages such as Java, C++, and Python. For automated testing of mobile applications, maintaining test scripts can be challenging due to the fast-evolving tech stacks and updates to devices and operating systems.

For the demo here, we are using the basic Calculator app. We'll automate the following use case testing with Appium:

1. Launch the Calculator app.
2. Perform multiplication of two numbers.
3. Record the result of the mathematical operation.
4. Assert the result.

We're using Appium with Java here. The test runs on a virtual device (an emulator). You can use a real or a virtual device for your test execution. Follow this [Appium Tutorial](https://testgrid.io/blog/appium-testing-tutorial/) for the setup and other prerequisites.

This is the Appium code we've used, which will be executed locally on the system to perform the above steps.

```
package appium;
import java.net.MalformedURLException;
import java.net.URL;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.Test;
import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
public class Calculator {
  @Test
  public void calculator() throws MalformedURLException {
    DesiredCapabilities dc = new DesiredCapabilities();
    // Setting the desired capabilities for the android device
    dc.setCapability("platformName", "android");
    dc.setCapability("platformVersion","14");
    dc.setCapability("deviceName", "Pixel6_TestGrid");
    dc.setCapability("automationName", "UiAutomator2");
    // Setting capability for the application we want to test
    dc.setCapability("app", "/Users/macair/Downloads/calculator.apk");
    // Instantiating Android Driver and using Appium server host and port
    AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), dc);
    // Locating numbers, mathematical operators, and the equals button in the Calculator app
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/digit_4")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/op_mul")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/digit_9")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/eq")).click();
    // Storing the result in a string variable
    String result = driver.findElement(
      AppiumBy.id("com.google.android.calculator:id/result_final")
    ).getText();
    System.out.println("The result is - "+result);
    Assert.assertEquals(result, "36");
    driver.quit();
  }
}
```
Our test code works seamlessly. However, it requires professionals with the necessary skills and knowledge for its implementation. Additionally, the limited availability of devices to execute these tests can make it challenging to achieve optimal test coverage.

### [Using Appium with TestGrid to automate mobile application testing](https://developer.mozilla.org#using_appium_with_testgrid_to_automate_mobile_application_testing)

Let's see how to execute the Appium test script on the real device cloud. The approach to using our local Appium mobile tests is quite similar to what we have seen above for web apps. You can follow this [step-by-step guide to execute local Appium code on device cloud](https://testgrid.io/docs/document/test-your-local-execution-mobile-appium-code-java-python/).

Let's look at the updated code that includes the `DesiredCapabilities` that align with the TestGrid device we've chosen. For example, we've specified the `udid`, `systemPort`, and `userToken`.

```
package appium;
import java.net.MalformedURLException;
import java.net.URL;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.Test;
import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
public class CalculatorTestGrid {
  @Test
  public void calculator() throws MalformedURLException {
    DesiredCapabilities dc = new DesiredCapabilities();
    // Setting the desired capabilities for the android device
    dc.setCapability("platformName", "android");
    dc.setCapability("platformVersion","12");
    dc.setCapability("deviceName", "Samsung Galaxy S21");
    dc.setCapability("automationName", "UiAutomator2");
    dc.setCapability("udid", "R5CRC28KGKB");
    dc.setCapability("tg:systemPort", "4005");
    dc.setCapability("tg:userToken", "Your user token");
    // Since the application is installed on the device, we directly use
    // the package name and main activity
    dc.setCapability("appPackage", "com.google.android.calculator");
    dc.setCapability("appActivity", "com.android.calculator2.Calculator");
    AndroidDriver driver = new AndroidDriver(new URL("Your TestGrid Appium URL"), dc);
    // Remaining steps are the same as in the previous Appium code
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/digit_4")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/op_mul")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/digit_9")).click();
    driver.findElement(AppiumBy.id("com.google.android.calculator:id/eq")).click();
    String result = driver.findElement(
      AppiumBy.id("com.google.android.calculator:id/result_final")
    ).getText();
    System.out.println("The result is - "+result);
    Assert.assertEquals(result, "36");
    driver.quit();
  }
}
```
On executing this updated code, you should be able to see the successful execution logs in your IDE. You can also view the execution results (or ongoing execution summary) by navigating to the **Automaton Sessions** tab in the left panel and selecting the device on which you executed the code.

You will be able to see the status of each step of the execution, along with their screenshots. Additionally, you will be able to look at the logs and visual testing results (if enabled) for these tests.

## [Leveraging TestGrid's modern automation testing solutions](https://developer.mozilla.org#leveraging_testgrids_modern_automation_testing_solutions)

[TestGrid's codeless test automation platform](https://testgrid.io/codeless-testing) allows users with minimal or no programming knowledge to start automating tests. By using codeless automation, you can record user journeys visually. The recording automatically generates test scripts, and therefore, no coding is required. This feature also helps to drastically reduce the script maintenance overhead.

### [Using TestGrid's test script generator for web application testing](https://developer.mozilla.org#using_testgrids_test_script_generator_for_web_application_testing)

Let's see how we can automate the same "Login" use case for the [demoqa](https://demoqa.com/login) website without any code using TestGrid's [scriptless web test case writer](https://testgrid.io/docs/scriptless-web-test-case-writer/). Follow the steps as prompted when you add a test case using the test case generator. Enter the URL, choose a browser and the webpage, and then add actions to the different elements on the page as required.

As you'll notice in the screenshot below, when you click on the area of a web element you want to interact with, the locator for the element is automatically detected. You will also see different locators being specified and you can select the desired one. You also have the option to manually write the locator, in case the system is unable to detect one for your web element.

After you have the required test data, you can add the actions for login with the necessary details to generate the test function for your test case. You can then run your test case. As the execution progresses, you can start observing the logs and test status being generated.

Click on **Build Summary** in the left panel to view details like the number of steps passed and failed, screenshots of the execution steps (if enabled), the start and end times, and the test status.

After the execution is complete, you can access various analysis reports available in the **Transaction Analysis** in the left panel.

Another feature provided by TestGrid's codeless test generator is "record and play". It lets you turn your app or browser actions into robust automated tests. After you create a project and module, you can click on **Add Test Case with Scriptless** to use this feature. You will notice a **Start Recording** button in the right panel, clicking on which will start recording your actions. You can click on **Stop** when you are done. Note that **Live View** and **Element Picker** get locked during execution.

After you stop the recording, you can edit the parameters in the **Action** column or even work with **Element Picker** for making more changes to the steps added using the recording.

You can then navigate back to **Test Cases** and execute the test just like we did before. You will be able to see the execution as well as the results in different analysis reports. Using **Network Log**, you can view the requests sent to the domain and the time taken by each of them.

This section demonstrated how you can easily write scriptless automation tests for your use cases, and add custom scripts when required. TestGrid's test script generator can help you boost the speed and reliability of automated testing of modern web applications.

### [Using TestGrid's test script generator for mobile application testing](https://developer.mozilla.org#using_testgrids_test_script_generator_for_mobile_application_testing)

As with web application testing, you can use TestGrid's [scriptless mobile app test case writing](https://testgrid.io/docs/scriptless-mobile-app-test-case-writing/) for testing mobile apps. Using this feature, you can quickly start automating mobile applications without the need to manually set up the server, clients, devices, and other configurations required to run automated tests.

On clicking the **Add Test Function with TestCase Generator** button, you'll see a pop-up asking for the apk/ipa/bundle ID of the application you want to test. Upload the application, select the device on which you want to execute your test, and click **Run**.

The next steps are similar to the test case creation for web apps.

After you save the steps of applying multiplication operation on two numbers and checking the result, the test function is added. Note that you can directly write the test case without having to write the test function, as we've done below. You may create test functions for steps that are repeated across test cases. These can be reused as common functions.

After you **Run** the test cases, select the build and the device on which we want to execute the tests. After the merging and compilation, you can see the execution happening in real-time along with the logs getting generated.

To explore any details about the execution, you can look at the **Build Summary**.

Similar to web applications, you can use the "record and play" feature for mobile apps as well.

Additionally, you can leverage the multiple reports and logs provided by TestGrid, which make it easy to analyze the performance of executions. The Insights feature shows graphical representations of various performance parameters corresponding to the execution, such as the CPU load, memory usage, request and response data size, and more.

Moreover, **Transaction Analysis** provides various downloadable reports about the performance benchmarks, including the device information.

This section demonstrated how you can leverage the elaborate reports, analytics, and ease of execution to scale your automation scope. With TestGrid's real device cloud, you can expand your test coverage to a wide range of devices. Whether you have established test frameworks or starting from scratch, TestGrid enables you to resume from your last point.

### [Using TestGrid's visual testing feature](https://developer.mozilla.org#using_testgrids_visual_testing_feature)

Visual testing goes beyond functional checks and allows you to detect visual regressions during agile developments.

TestGrid helps make [visual testing](https://testgrid.io/visual-testing) scalable through smart test automation. It enables teams to auto-capture screenshots across all platforms and also uses AI-based image comparison to find the differences. The in-depth heatmaps and metrics along with the analytics dashboard aid the testing teams to automate visual validations across web and mobile applications. This feature helps testing teams achieve a great user experience by ensuring design consistency.

After following the [steps to configure visual testing](https://testgrid.io/docs/document/visual-testing/) in your Selenium or Appium code, you can view the visual testing results in the **Visual Testing** tab in the **Automation Sessions** results for the selected device.

Visual testing plays a key role in ensuring the overall quality of any application. Testing user interface thoroughly with a meticulous emphasis on details enhances user satisfaction and retention. TestGrid offers an easy integration of the visual testing capability into existing tests, thereby providing a way to increase the overall coverage of the system under test.

## [Conclusion](https://developer.mozilla.org#conclusion)

With the acceleration of software delivery, testing practices need to be updated to remain relevant. Modern applications require high-quality benchmarks, which are lacking in conventional test automation methods. Writing test scripts for Selenium or Appium is complex and time-consuming. The frequent changes make these scripts unreliable and add a maintenance overhead.

[TestGrid](https://testgrid.io/) enhances traditional capabilities to deliver test automation that is future-proof. It provides modern features like codeless automation, easy integrations, and powerful analytics and reporting. Scriptless testing with computer vision and AI help in achieving scale as well as stability. Testing teams can easily and efficiently achieve test coverage across browsers, devices, and platforms and visualize UI issues before any business impact.

*This post is sponsored by TestGrid. TestGrid is a leading provider of end-to-end automation testing solutions, both on cloud and on-premise. With a focus on simplifying the testing process, TestGrid offers cutting-edge features enabling teams to significantly save on costs and time, while accelerating their go-to-market strategies.*