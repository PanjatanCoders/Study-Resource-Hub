# Cucumber Phase 2: Allure Reporting Setup
## Integrate Allure Reports with Cucumber + TestNG

---

## Prerequisites

✅ Cucumber Phase 1 completed (Basic setup done)

---

## Why Allure with Cucumber?

**Benefits:**
- Beautiful, interactive HTML reports
- Test execution trends and history
- Screenshots attached automatically
- Step-by-step execution details
- Tags and categories visualization
- Time-based analysis
- Integration with CI/CD

---

## Step 1: Add Allure Dependencies

Update `pom.xml` with Allure dependencies:

```xml
<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <cucumber.version>7.14.0</cucumber.version>
    <selenium.version>4.15.0</selenium.version>
    <testng.version>7.8.0</testng.version>
    <allure.version>2.24.0</allure.version>
    <aspectj.version>1.9.20</aspectj.version>
</properties>

<dependencies>
    <!-- Existing dependencies -->
    
    <!-- Allure Cucumber7 JVM -->
    <dependency>
        <groupId>io.qameta.allure</groupId>
        <artifactId>allure-cucumber7-jvm</artifactId>
        <version>${allure.version}</version>
    </dependency>

    <!-- Allure TestNG -->
    <dependency>
        <groupId>io.qameta.allure</groupId>
        <artifactId>allure-testng</artifactId>
        <version>${allure.version}</version>
    </dependency>
</dependencies>
```

**Save and run:**
```bash
mvn clean install
```

---

## Step 2: Configure Maven Surefire Plugin

Add/Update in `<build>` → `<plugins>` section:

```xml
<build>
    <plugins>
        <!-- Maven Surefire Plugin -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0</version>
            <configuration>
                <suiteXmlFiles>
                    <suiteXmlFile>testng.xml</suiteXmlFile>
                </suiteXmlFiles>
                <argLine>
                    -javaagent:"${settings.localRepository}/org/aspectj/aspectjweaver/${aspectj.version}/aspectjweaver-${aspectj.version}.jar"
                </argLine>
                <systemProperties>
                    <property>
                        <name>allure.results.directory</name>
                        <value>${project.build.directory}/allure-results</value>
                    </property>
                </systemProperties>
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>org.aspectj</groupId>
                    <artifactId>aspectjweaver</artifactId>
                    <version>${aspectj.version}</version>
                </dependency>
            </dependencies>
        </plugin>

        <!-- Allure Maven Plugin -->
        <plugin>
            <groupId>io.qameta.allure</groupId>
            <artifactId>allure-maven</artifactId>
            <version>2.12.0</version>
            <configuration>
                <reportVersion>${allure.version}</reportVersion>
                <resultsDirectory>${project.build.directory}/allure-results</resultsDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

## Step 3: Update Test Runner with Allure Plugin

Update `TestRunner.java`:

```java
package com.automation.runners;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;
import org.testng.annotations.DataProvider;

@CucumberOptions(
        features = "src/test/resources/features",
        glue = {"com.automation.stepdefinitions"},
        tags = "@smoke or @regression",
        plugin = {
                "pretty",
                "html:target/cucumber-reports/cucumber.html",
                "json:target/cucumber-reports/cucumber.json",
                "junit:target/cucumber-reports/cucumber.xml",
                "io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"  // Add this line
        },
        monochrome = true,
        dryRun = false
)
public class TestRunner extends AbstractTestNGCucumberTests {
    
    // Enable parallel execution (optional)
    @Override
    @DataProvider(parallel = false)
    public Object[][] scenarios() {
        return super.scenarios();
    }
}
```

**Key Addition:**
```java
"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"
```
This plugin generates Allure-compatible results.

---

## Step 4: Install Allure Command Line

### Windows (Using Scoop)
```bash
scoop install allure
```

### Windows (Manual)
1. Download: https://github.com/allure-framework/allure2/releases
2. Extract to `C:\allure`
3. Add `C:\allure\bin` to System PATH

### Mac
```bash
brew install allure
```

### Linux
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

**Verify installation:**
```bash
allure --version
```

---

## Step 5: Add Allure Annotations to Step Definitions

Update `LoginStepDefinitions.java`:

```java
package com.automation.stepdefinitions;

import com.automation.context.TestContext;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import com.automation.utils.DriverManager;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.qameta.allure.Step;
import org.testng.Assert;

public class LoginStepDefinitions {
    private TestContext testContext;
    private LoginPage loginPage;
    private HomePage homePage;

    public LoginStepDefinitions(TestContext testContext) {
        this.testContext = testContext;
    }

    @Given("user is on the login page")
    @Step("Navigate to login page")
    public void userIsOnTheLoginPage() {
        DriverManager.getDriver().get("https://example.com/login");
        loginPage = testContext.getLoginPage();
    }

    @When("user enters username {string} and password {string}")
    @Step("Enter username: {0} and password")
    public void userEntersUsernameAndPassword(String username, String password) {
        loginPage = testContext.getLoginPage();
        loginPage.enterUsername(username);
        loginPage.enterPassword(password);
    }

    @And("user clicks on login button")
    @Step("Click on login button")
    public void userClicksOnLoginButton() {
        loginPage.clickLoginButton();
    }

    @Then("user should be logged in successfully")
    @Step("Verify user is logged in")
    public void userShouldBeLoggedInSuccessfully() {
        homePage = testContext.getHomePage();
        Assert.assertTrue(homePage.isWelcomeMessageDisplayed(), 
                         "User should be logged in");
    }

    @And("welcome message should be displayed")
    @Step("Verify welcome message is displayed")
    public void welcomeMessageShouldBeDisplayed() {
        homePage = testContext.getHomePage();
        String message = homePage.getWelcomeMessage();
        Assert.assertTrue(message.contains("Welcome"), 
                         "Welcome message should be displayed");
    }

    @Then("user should see an error message")
    @Step("Verify error message is displayed")
    public void userShouldSeeAnErrorMessage() {
        Assert.assertTrue(loginPage.isErrorMessageDisplayed(), 
                         "Error message should be displayed");
    }

    @And("user should remain on login page")
    @Step("Verify user remains on login page")
    public void userShouldRemainOnLoginPage() {
        String currentUrl = DriverManager.getDriver().getCurrentUrl();
        Assert.assertTrue(currentUrl.contains("login"), 
                         "User should remain on login page");
    }

    @Then("login result should be {string}")
    @Step("Verify login result is: {0}")
    public void loginResultShouldBe(String expectedResult) {
        if (expectedResult.equals("success")) {
            homePage = testContext.getHomePage();
            Assert.assertTrue(homePage.isWelcomeMessageDisplayed());
        } else {
            Assert.assertTrue(loginPage.isErrorMessageDisplayed());
        }
    }
}
```

---

## Step 6: Add Screenshot Support

Create `ScreenshotUtil.java`:

**Location:** `src/main/java/com/automation/utils/ScreenshotUtil.java`

```java
package com.automation.utils;

import io.qameta.allure.Attachment;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

public class ScreenshotUtil {
    
    @Attachment(value = "Screenshot", type = "image/png")
    public static byte[] captureScreenshot(WebDriver driver) {
        return ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
    }
    
    @Attachment(value = "Page Screenshot on Failure", type = "image/png")
    public static byte[] captureFailureScreenshot(WebDriver driver) {
        return ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
    }
}
```

---

## Step 7: Update Hooks with Screenshots

Update `Hooks.java`:

```java
package com.automation.stepdefinitions;

import com.automation.utils.DriverManager;
import com.automation.utils.ScreenshotUtil;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.Scenario;
import io.qameta.allure.Allure;

public class Hooks {

    @Before
    public void setUp(Scenario scenario) {
        System.out.println("Starting Scenario: " + scenario.getName());
        
        // Add scenario info to Allure
        Allure.getLifecycle().updateTestCase(testResult -> {
            testResult.setName(scenario.getName());
        });
        
        DriverManager.setDriver("chrome");
    }

    @After
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed()) {
            System.out.println("Scenario Failed: " + scenario.getName());
            
            // Attach screenshot to Allure report
            ScreenshotUtil.captureFailureScreenshot(DriverManager.getDriver());
        }
        
        System.out.println("Scenario Status: " + scenario.getStatus());
        DriverManager.quitDriver();
    }
}
```

---

## Step 8: Add Allure Descriptions to Feature File

Update `Login.feature` with better descriptions:

```gherkin
@severity=critical
Feature: Login Functionality
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given user is on the login page

  @smoke @regression @severity=blocker
  Scenario: Successful login with valid credentials
    When user enters username "testuser" and password "testpass123"
    And user clicks on login button
    Then user should be logged in successfully
    And welcome message should be displayed

  @regression @severity=critical
  Scenario: Login fails with invalid credentials
    When user enters username "invaliduser" and password "wrongpass"
    And user clicks on login button
    Then user should see an error message
    And user should remain on login page

  @regression @severity=normal
  Scenario: Login fails with empty username
    When user enters username "" and password "testpass123"
    And user clicks on login button
    Then user should see an error message

  @regression @data-driven @severity=normal
  Scenario Outline: Login with multiple credentials
    When user enters username "<username>" and password "<password>"
    And user clicks on login button
    Then login result should be "<result>"

    Examples:
      | username    | password    | result  |
      | validuser   | validpass   | success |
      | invaliduser | wrongpass   | failure |
      | testuser    | testpass123 | success |
      | ''          | validpass   | failure |
```

**Allure Severity Levels:**
- `@severity=blocker` - Critical, blocks testing
- `@severity=critical` - Critical functionality
- `@severity=normal` - Normal priority
- `@severity=minor` - Minor issue
- `@severity=trivial` - Trivial issue

---

## Step 9: Create allure.properties (Optional)

**Location:** `src/test/resources/allure.properties`

```properties
allure.results.directory=target/allure-results
allure.link.issue.pattern=https://jira.company.com/browse/{}
allure.link.tms.pattern=https://testmanagement.company.com/{}
```

---

## Step 10: Run Tests and Generate Allure Report

### Run Tests
```bash
mvn clean test
```

**This creates:** `target/allure-results/` with JSON files

### Generate and View Report

**Option 1: Serve report (opens browser automatically)**
```bash
mvn allure:serve
```

**Option 2: Generate HTML report**
```bash
mvn allure:report
```
Report location: `target/site/allure-maven-plugin/index.html`

**Option 3: Using Allure CLI**
```bash
# Generate report
allure generate target/allure-results --clean -o target/allure-report

# Open report
allure open target/allure-report
```

---

## Step 11: Understanding Allure Report Sections

### Overview Dashboard
- **Total tests**: Passed, Failed, Broken, Skipped
- **Success rate**: Percentage
- **Execution time**: Total duration
- **Trend**: Historical comparison

### Suites
- Tests grouped by feature files
- Expandable scenarios
- Step-by-step execution details

### Graphs
- **Status chart**: Pass/Fail distribution
- **Severity chart**: By priority
- **Duration chart**: Longest tests
- **Categories**: Failure categories

### Timeline
- Visual timeline of test execution
- Shows parallel execution
- Identifies bottlenecks

### Behaviors
- Tests grouped by features
- BDD-style view
- Stories and scenarios

### Packages
- Tests organized by Java packages
- Technical view

---

## Step 12: Add Custom Allure Annotations

Create enhanced step definitions with more Allure features:

```java
package com.automation.stepdefinitions;

import com.automation.context.TestContext;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import com.automation.utils.DriverManager;
import io.cucumber.java.en.*;
import io.qameta.allure.*;
import org.testng.Assert;

@Epic("User Authentication")
@Feature("Login Functionality")
public class LoginStepDefinitions {
    private TestContext testContext;
    private LoginPage loginPage;
    private HomePage homePage;

    public LoginStepDefinitions(TestContext testContext) {
        this.testContext = testContext;
    }

    @Given("user is on the login page")
    @Step("Navigate to login page")
    @Description("User navigates to the login page of the application")
    public void userIsOnTheLoginPage() {
        DriverManager.getDriver().get("https://example.com/login");
        loginPage = testContext.getLoginPage();
        Allure.addAttachment("Login URL", "https://example.com/login");
    }

    @When("user enters username {string} and password {string}")
    @Step("Enter credentials: username={0}")
    public void userEntersUsernameAndPassword(String username, String password) {
        loginPage = testContext.getLoginPage();
        
        Allure.step("Enter username: " + username, () -> {
            loginPage.enterUsername(username);
        });
        
        Allure.step("Enter password", () -> {
            loginPage.enterPassword(password);
        });
    }

    @And("user clicks on login button")
    @Step("Click login button")
    public void userClicksOnLoginButton() {
        loginPage.clickLoginButton();
    }

    @Then("user should be logged in successfully")
    @Step("Verify successful login")
    @Severity(SeverityLevel.CRITICAL)
    public void userShouldBeLoggedInSuccessfully() {
        homePage = testContext.getHomePage();
        boolean isLoggedIn = homePage.isWelcomeMessageDisplayed();
        
        Allure.step("Check if welcome message is displayed", () -> {
            Assert.assertTrue(isLoggedIn, "User should be logged in");
        });
    }

    @And("welcome message should be displayed")
    @Step("Verify welcome message")
    public void welcomeMessageShouldBeDisplayed() {
        homePage = testContext.getHomePage();
        String message = homePage.getWelcomeMessage();
        
        Allure.addAttachment("Welcome Message", "text/plain", message);
        
        Assert.assertTrue(message.contains("Welcome"), 
                         "Welcome message should be displayed");
    }

    @Then("user should see an error message")
    @Step("Verify error message is displayed")
    @Severity(SeverityLevel.NORMAL)
    public void userShouldSeeAnErrorMessage() {
        boolean errorDisplayed = loginPage.isErrorMessageDisplayed();
        
        if (errorDisplayed) {
            String errorMsg = loginPage.getErrorMessage();
            Allure.addAttachment("Error Message", "text/plain", errorMsg);
        }
        
        Assert.assertTrue(errorDisplayed, "Error message should be displayed");
    }

    @And("user should remain on login page")
    @Step("Verify user is still on login page")
    public void userShouldRemainOnLoginPage() {
        String currentUrl = DriverManager.getDriver().getCurrentUrl();
        Allure.addAttachment("Current URL", "text/plain", currentUrl);
        
        Assert.assertTrue(currentUrl.contains("login"), 
                         "User should remain on login page");
    }
}
```

**Allure Annotations Explained:**
- `@Epic`: Highest level grouping (e.g., "E-commerce")
- `@Feature`: Feature grouping (e.g., "Login")
- `@Story`: User story level (e.g., "User login")
- `@Step`: Step description in report
- `@Description`: Detailed description
- `@Severity`: Test importance level
- `@Link`: Link to external resources
- `@Issue`: Link to bug tracker
- `@TmsLink`: Link to test management system

---

## Step 13: Add Environment Information

Create `environment.properties`:

**Location:** `src/test/resources/environment.properties`

```properties
Browser=Chrome
Browser.Version=120.0
Stand=QA
Environment=Test
URL=https://example.com
Execution.Type=Local
Operating.System=Windows 11
Java.Version=11
```

**Copy to allure-results after test execution:**

Add this to your `Hooks.java` `@After` method:

```java
@After
public void tearDown(Scenario scenario) {
    if (scenario.isFailed()) {
        ScreenshotUtil.captureFailureScreenshot(DriverManager.getDriver());
    }
    
    // Add environment info
    addEnvironmentInformation();
    
    DriverManager.quitDriver();
}

private void addEnvironmentInformation() {
    Allure.addAttachment("Browser", "Chrome");
    Allure.addAttachment("Environment", "QA");
    Allure.addAttachment("OS", System.getProperty("os.name"));
    Allure.addAttachment("Java Version", System.getProperty("java.version"));
}
```

---

## Step 14: Add Categories for Failures

Create `categories.json`:

**Location:** `src/test/resources/categories.json`

```json
[
  {
    "name": "Product Defects",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*AssertionError.*"
  },
  {
    "name": "Element Not Found",
    "matchedStatuses": ["broken"],
    "messageRegex": ".*NoSuchElementException.*"
  },
  {
    "name": "Timeout Issues",
    "matchedStatuses": ["broken"],
    "messageRegex": ".*TimeoutException.*"
  },
  {
    "name": "Stale Element",
    "matchedStatuses": ["broken"],
    "messageRegex": ".*StaleElementReferenceException.*"
  },
  {
    "name": "Test Defects",
    "matchedStatuses": ["broken"]
  }
]
```

**Copy to allure-results:**

Create a Maven plugin to copy categories.json:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-resources-plugin</artifactId>
    <version>3.3.0</version>
    <executions>
        <execution>
            <id>copy-categories</id>
            <phase>test</phase>
            <goals>
                <goal>copy-resources</goal>
            </goals>
            <configuration>
                <outputDirectory>${project.build.directory}/allure-results</outputDirectory>
                <resources>
                    <resource>
                        <directory>src/test/resources</directory>
                        <includes>
                            <include>categories.json</include>
                        </includes>
                    </resource>
                </resources>
            </configuration>
        </execution>
    </executions>
</plugin>
```

---

## Step 15: Parallel Execution with Allure

For parallel execution, update `TestRunner.java`:

```java
@CucumberOptions(
        features = "src/test/resources/features",
        glue = {"com.automation.stepdefinitions"},
        tags = "@smoke or @regression",
        plugin = {
                "pretty",
                "html:target/cucumber-reports/cucumber.html",
                "json:target/cucumber-reports/cucumber.json",
                "io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"
        },
        monochrome = true
)
public class TestRunner extends AbstractTestNGCucumberTests {
    
    @Override
    @DataProvider(parallel = true)
    public Object[][] scenarios() {
        return super.scenarios();
    }
}
```

Update `testng.xml` for parallel execution:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Cucumber Test Suite" parallel="methods" thread-count="3">
    <test name="Cucumber Tests">
        <classes>
            <class name="com.automation.runners.TestRunner"/>
        </classes>
    </test>
</suite>
```

---

## Step 16: CI/CD Integration Example

### GitHub Actions

Create `.github/workflows/cucumber-tests.yml`:

```yaml
name: Cucumber Tests with Allure

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up JDK 11
      uses: actions/setup-java@v3
      with:
        java-version: '11'
        distribution: 'adopt'
        
    - name: Run Tests
      run: mvn clean test
      
    - name: Generate Allure Report
      if: always()
      run: mvn allure:report
      
    - name: Deploy Allure Report
      if: always()
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: target/site/allure-maven-plugin
```

---

## Folder Structure After Setup

```
cucumber-selenium-framework/
├── src/
│   ├── main/java/com/automation/
│   │   ├── pages/
│   │   └── utils/
│   │       └── ScreenshotUtil.java ✓ NEW
│   └── test/
│       ├── java/com/automation/
│       │   ├── runners/
│       │   │   └── TestRunner.java ✓ UPDATED
│       │   └── stepdefinitions/
│       │       ├── Hooks.java ✓ UPDATED
│       │       └── LoginStepDefinitions.java ✓ UPDATED
│       └── resources/
│           ├── features/
│           │   └── Login.feature ✓ UPDATED
│           ├── allure.properties ✓ NEW
│           ├── categories.json ✓ NEW
│           └── environment.properties ✓ NEW
├── target/
│   ├── allure-results/ ✓ (generated after test run)
│   └── site/allure-maven-plugin/ ✓ (generated report)
├── testng.xml
└── pom.xml ✓ UPDATED
```

---

## Verification Checklist

- [ ] Allure dependencies added to pom.xml
- [ ] Maven Surefire plugin configured
- [ ] Allure Maven plugin configured
- [ ] TestRunner updated with Allure plugin
- [ ] Allure CLI installed
- [ ] ScreenshotUtil created
- [ ] Hooks updated with screenshot capture
- [ ] Step definitions have @Step annotations
- [ ] Feature file updated with @severity tags
- [ ] Tests run: `mvn clean test`
- [ ] allure-results folder created in target
- [ ] Report generated: `mvn allure:serve`
- [ ] Report opens in browser
- [ ] Screenshots visible in failed tests

---

## Troubleshooting

### Issue 1: allure-results not created

**Solution:** Check pom.xml surefire plugin configuration:
```xml
<systemProperties>
    <property>
        <n>allure.results.directory</n>
        <value>${project.build.directory}/allure-results</value>
    </property>
</systemProperties>
```

### Issue 2: Screenshots not appearing in report

**Solution:** Ensure `@Attachment` annotation is used in ScreenshotUtil

### Issue 3: Allure command not found

**Solution:** Install Allure CLI and add to PATH

### Issue 4: Old test results appearing

**Solution:** Clean before running:
```bash
mvn clean test
```

### Issue 5: Report shows "No data available"

**Solution:** Ensure tests actually ran and allure-results has JSON files

---

## Quick Commands

```bash
# Clean and run tests
mvn clean test

# Generate and serve report
mvn allure:serve

# Generate report only
mvn allure:report

# View generated report
allure open target/allure-report

# Run specific tags
mvn test -Dcucumber.filter.tags="@smoke"

# Clean allure results
rm -rf target/allure-results
```

---

## Allure Report Features Summary

### What You Get
✅ Beautiful interactive HTML reports
✅ Test execution timeline
✅ Screenshots on failure
✅ Step-by-step execution details
✅ Historical trends
✅ Categories for failures
✅ Severity-based grouping
✅ Tags visualization
✅ Environment information
✅ Execution statistics
✅ Duration analysis

---

## Next Steps

✅ **Cucumber Phase 2 Complete!**

Proceed to:
- **Phase 3**: Advanced Cucumber Features
- **Phase 4**: Best Practices & Common Mistakes

---

**Allure Reporting Integration Complete! 📊✨**