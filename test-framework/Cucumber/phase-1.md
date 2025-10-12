# Cucumber Phase 1: Basic Setup
## Cucumber + Java + Selenium + TestNG Integration

---

## What is Cucumber?

Cucumber is a **Behavior-Driven Development (BDD)** tool that allows you to write tests in plain English using **Gherkin syntax**.

### Why Cucumber is Most Loved

**1. Business-Readable Tests**
```gherkin
Feature: Login Functionality
  Scenario: Successful login with valid credentials
    Given user is on login page
    When user enters valid username and password
    Then user should be logged in successfully
```
- **Non-technical stakeholders** can read and understand
- **Product owners** can write scenarios
- **Developers** and **Testers** implement the same scenarios

**2. Living Documentation**
- Tests serve as documentation
- Always up-to-date with application behavior
- Bridges communication gap between business and technical teams

**3. Reusability**
```gherkin
Scenario: Login as admin
  Given user is on login page
  When user enters "admin" and "admin123"
  
Scenario: Login as regular user
  Given user is on login page    # Same step reused
  When user enters "user" and "pass123"
```

**4. Natural Language**
- Easy to read: `Given`, `When`, `Then`, `And`, `But`
- No programming knowledge needed to write scenarios
- Reduces learning curve

**5. Collaboration**
- Business analysts write scenarios
- Developers implement step definitions
- QA validates behavior
- Everyone speaks the same language

**6. Maintainability**
- One step definition used by multiple scenarios
- Change once, applies everywhere
- Reduces code duplication

---

## Prerequisites

- Java JDK 11 or higher installed
- Maven installed
- IDE (IntelliJ IDEA recommended for Cucumber plugins)
- Basic understanding of Selenium

---

## Step 1: Create Maven Project

1. Open IntelliJ IDEA / Eclipse
2. **File** → **New** → **Maven Project**
3. Enter details:
    - **GroupId**: `com.automation`
    - **ArtifactId**: `cucumber-selenium-framework`
    - **Version**: `1.0-SNAPSHOT`
4. Click **Finish**

---

## Step 2: Configure `pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.automation</groupId>
    <artifactId>cucumber-selenium-framework</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <cucumber.version>7.14.0</cucumber.version>
        <selenium.version>4.15.0</selenium.version>
        <testng.version>7.8.0</testng.version>
    </properties>

    <dependencies>
        <!-- Cucumber Java -->
        <dependency>
            <groupId>io.cucumber</groupId>
            <artifactId>cucumber-java</artifactId>
            <version>${cucumber.version}</version>
        </dependency>

        <!-- Cucumber TestNG -->
        <dependency>
            <groupId>io.cucumber</groupId>
            <artifactId>cucumber-testng</artifactId>
            <version>${cucumber.version}</version>
        </dependency>

        <!-- Selenium WebDriver -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>${selenium.version}</version>
        </dependency>

        <!-- TestNG -->
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>${testng.version}</version>
        </dependency>

        <!-- WebDriverManager -->
        <dependency>
            <groupId>io.github.bonigarcia</groupId>
            <artifactId>webdrivermanager</artifactId>
            <version>5.6.2</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <suiteXmlFiles>
                        <suiteXmlFile>testng.xml</suiteXmlFile>
                    </suiteXmlFiles>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

**Save and run:**
```bash
mvn clean install
```

---

## Step 3: Install Cucumber Plugins (IntelliJ IDEA)

1. **File** → **Settings** → **Plugins**
2. Search for **"Cucumber for Java"**
3. Click **Install**
4. **Restart IDE**

**Benefits:**
- Syntax highlighting for `.feature` files
- Navigation from steps to step definitions
- Auto-complete for Gherkin keywords
- Run feature files directly from IDE

---

## Step 4: Create Project Structure

```
cucumber-selenium-framework/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/automation/
│   │   │       ├── pages/
│   │   │       │   ├── BasePage.java
│   │   │       │   ├── LoginPage.java
│   │   │       │   └── HomePage.java
│   │   │       └── utils/
│   │   │           └── DriverManager.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/automation/
│       │       ├── runners/
│       │       │   └── TestRunner.java
│       │       ├── stepdefinitions/
│       │       │   ├── Hooks.java
│       │       │   └── LoginStepDefinitions.java
│       │       └── context/
│       │           └── TestContext.java
│       └── resources/
│           └── features/
│               └── Login.feature
├── testng.xml
└── pom.xml
```

**Create these packages:**
- Right-click on `src/test/java` → **New** → **Package**
- Create: `com.automation.runners`
- Create: `com.automation.stepdefinitions`
- Create: `com.automation.context`

**Create resources folder:**
- Right-click on `src/test` → **New** → **Directory** → Name: `resources`
- Right-click on `resources` → **New** → **Directory** → Name: `features`

---

## Step 5: Create Base Page

**Location:** `src/main/java/com/automation/pages/BasePage.java`

```java
package com.automation.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;

    public BasePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    protected WebElement findElement(By locator) {
        return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    protected void click(By locator) {
        findElement(locator).click();
    }

    protected void type(By locator, String text) {
        WebElement element = findElement(locator);
        element.clear();
        element.sendKeys(text);
    }

    protected String getText(By locator) {
        return findElement(locator).getText();
    }

    protected boolean isDisplayed(By locator) {
        try {
            return findElement(locator).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}
```

---

## Step 6: Create Page Classes

**LoginPage.java**

**Location:** `src/main/java/com/automation/pages/LoginPage.java`

```java
package com.automation.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {
    
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");
    private final By loginButton = By.xpath("//button[@type='submit']");
    private final By errorMessage = By.className("error-message");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void enterUsername(String username) {
        type(usernameField, username);
    }

    public void enterPassword(String password) {
        type(passwordField, password);
    }

    public void clickLoginButton() {
        click(loginButton);
    }

    public String getErrorMessage() {
        return getText(errorMessage);
    }

    public boolean isErrorMessageDisplayed() {
        return isDisplayed(errorMessage);
    }
}
```

**HomePage.java**

**Location:** `src/main/java/com/automation/pages/HomePage.java`

```java
package com.automation.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage extends BasePage {
    
    private final By welcomeMessage = By.className("welcome-text");
    private final By logoutButton = By.id("logout");

    public HomePage(WebDriver driver) {
        super(driver);
    }

    public boolean isWelcomeMessageDisplayed() {
        return isDisplayed(welcomeMessage);
    }

    public String getWelcomeMessage() {
        return getText(welcomeMessage);
    }

    public void clickLogout() {
        click(logoutButton);
    }
}
```

---

## Step 7: Create Driver Manager

**Location:** `src/main/java/com/automation/utils/DriverManager.java`

```java
package com.automation.utils;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.time.Duration;

public class DriverManager {
    private static ThreadLocal<WebDriver> driver = new ThreadLocal<>();

    public static WebDriver getDriver() {
        return driver.get();
    }

    public static void setDriver(String browser) {
        WebDriver webDriver;
        
        switch (browser.toLowerCase()) {
            case "chrome":
                WebDriverManager.chromedriver().setup();
                webDriver = new ChromeDriver();
                break;
            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                webDriver = new FirefoxDriver();
                break;
            case "edge":
                WebDriverManager.edgedriver().setup();
                webDriver = new EdgeDriver();
                break;
            default:
                throw new IllegalArgumentException("Browser not supported: " + browser);
        }
        
        webDriver.manage().window().maximize();
        webDriver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.set(webDriver);
    }

    public static void quitDriver() {
        if (driver.get() != null) {
            driver.get().quit();
            driver.remove();
        }
    }
}
```

---

## Step 8: Create Test Context

**Location:** `src/test/java/com/automation/context/TestContext.java`

```java
package com.automation.context;

import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import com.automation.utils.DriverManager;
import org.openqa.selenium.WebDriver;

public class TestContext {
    private LoginPage loginPage;
    private HomePage homePage;

    public TestContext() {
        // Pages initialized when needed
    }

    public LoginPage getLoginPage() {
        if (loginPage == null) {
            loginPage = new LoginPage(getDriver());
        }
        return loginPage;
    }

    public HomePage getHomePage() {
        if (homePage == null) {
            homePage = new HomePage(getDriver());
        }
        return homePage;
    }

    private WebDriver getDriver() {
        return DriverManager.getDriver();
    }
}
```

---

## Step 9: Create Feature File

**Location:** `src/test/resources/features/Login.feature`

```gherkin
Feature: Login Functionality
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given user is on the login page

  @smoke @regression
  Scenario: Successful login with valid credentials
    When user enters username "testuser" and password "testpass123"
    And user clicks on login button
    Then user should be logged in successfully
    And welcome message should be displayed

  @regression
  Scenario: Login fails with invalid credentials
    When user enters username "invaliduser" and password "wrongpass"
    And user clicks on login button
    Then user should see an error message
    And user should remain on login page

  @regression
  Scenario: Login fails with empty username
    When user enters username "" and password "testpass123"
    And user clicks on login button
    Then user should see an error message

  @regression
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

**Gherkin Keywords Explained:**
- **Feature**: High-level description of functionality
- **Scenario**: Specific test case
- **Given**: Precondition/setup
- **When**: Action/event
- **Then**: Expected outcome
- **And/But**: Additional steps
- **Background**: Steps common to all scenarios
- **Scenario Outline**: Data-driven testing with Examples

---

## Step 10: Create Hooks

**Location:** `src/test/java/com/automation/stepdefinitions/Hooks.java`

```java
package com.automation.stepdefinitions;

import com.automation.utils.DriverManager;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.Scenario;

public class Hooks {

    @Before
    public void setUp(Scenario scenario) {
        System.out.println("Starting Scenario: " + scenario.getName());
        DriverManager.setDriver("chrome");
    }

    @After
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed()) {
            System.out.println("Scenario Failed: " + scenario.getName());
            // Screenshot logic will be added later
        }
        System.out.println("Scenario Status: " + scenario.getStatus());
        DriverManager.quitDriver();
    }
}
```

**Hooks Explained:**
- `@Before`: Runs before each scenario
- `@After`: Runs after each scenario
- `Scenario` object provides scenario information
- Perfect place for setup/teardown logic

---

## Step 11: Create Step Definitions

**Location:** `src/test/java/com/automation/stepdefinitions/LoginStepDefinitions.java`

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
import org.testng.Assert;

public class LoginStepDefinitions {
    private TestContext testContext;
    private LoginPage loginPage;
    private HomePage homePage;

    public LoginStepDefinitions(TestContext testContext) {
        this.testContext = testContext;
    }

    @Given("user is on the login page")
    public void userIsOnTheLoginPage() {
        DriverManager.getDriver().get("https://example.com/login");
        loginPage = testContext.getLoginPage();
    }

    @When("user enters username {string} and password {string}")
    public void userEntersUsernameAndPassword(String username, String password) {
        loginPage = testContext.getLoginPage();
        loginPage.enterUsername(username);
        loginPage.enterPassword(password);
    }

    @And("user clicks on login button")
    public void userClicksOnLoginButton() {
        loginPage.clickLoginButton();
    }

    @Then("user should be logged in successfully")
    public void userShouldBeLoggedInSuccessfully() {
        homePage = testContext.getHomePage();
        Assert.assertTrue(homePage.isWelcomeMessageDisplayed(), 
                         "User should be logged in");
    }

    @And("welcome message should be displayed")
    public void welcomeMessageShouldBeDisplayed() {
        homePage = testContext.getHomePage();
        String message = homePage.getWelcomeMessage();
        Assert.assertTrue(message.contains("Welcome"), 
                         "Welcome message should be displayed");
    }

    @Then("user should see an error message")
    public void userShouldSeeAnErrorMessage() {
        Assert.assertTrue(loginPage.isErrorMessageDisplayed(), 
                         "Error message should be displayed");
    }

    @And("user should remain on login page")
    public void userShouldRemainOnLoginPage() {
        String currentUrl = DriverManager.getDriver().getCurrentUrl();
        Assert.assertTrue(currentUrl.contains("login"), 
                         "User should remain on login page");
    }

    @Then("login result should be {string}")
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

**Step Definition Tips:**
- Use dependency injection (TestContext) to share data
- Parameters in `{string}`, `{int}`, `{double}` etc.
- One step definition can be reused by multiple scenarios
- Keep step definitions focused and simple

---

## Step 12: Create Test Runner

**Location:** `src/test/java/com/automation/runners/TestRunner.java`

```java
package com.automation.runners;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions(
        features = "src/test/resources/features",
        glue = {"com.automation.stepdefinitions"},
        tags = "@smoke or @regression",
        plugin = {
                "pretty",
                "html:target/cucumber-reports/cucumber.html",
                "json:target/cucumber-reports/cucumber.json",
                "junit:target/cucumber-reports/cucumber.xml"
        },
        monochrome = true,
        dryRun = false
)
public class TestRunner extends AbstractTestNGCucumberTests {
    // This class will be empty - annotations do all the work
}
```

**@CucumberOptions Explained:**
- `features`: Location of .feature files
- `glue`: Package containing step definitions
- `tags`: Which scenarios to run (explained later)
- `plugin`: Report formats
- `monochrome`: Readable console output
- `dryRun`: Check if all steps have definitions (true = don't run tests)

---

## Step 13: Create testng.xml

**Location:** `testng.xml` (project root)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Cucumber Test Suite">
    <test name="Cucumber Tests">
        <classes>
            <class name="com.automation.runners.TestRunner"/>
        </classes>
    </test>
</suite>
```

---

## Step 14: Run Tests

### Option 1: Using Maven
```bash
mvn clean test
```

### Option 2: Using TestNG XML
- Right-click on `testng.xml`
- Select **Run**

### Option 3: Using Feature File
- Right-click on `Login.feature`
- Select **Run Feature**

### Option 4: Using Test Runner
- Right-click on `TestRunner.java`
- Select **Run TestRunner**

---

## Step 15: Understanding Cucumber Tags

Tags help organize and filter scenarios:

```gherkin
@smoke
Scenario: Quick smoke test
  # This runs with tag @smoke

@regression
Scenario: Detailed regression test
  # This runs with tag @regression

@smoke @regression
Scenario: Important test
  # This runs with both tags
```

**Running specific tags:**

```java
// Run only smoke tests
tags = "@smoke"

// Run smoke OR regression
tags = "@smoke or @regression"

// Run smoke AND regression (both tags must be present)
tags = "@smoke and @regression"

// Exclude tests
tags = "not @skip"

// Complex expressions
tags = "(@smoke or @regression) and not @bug"
```

**Command line:**
```bash
mvn test -Dcucumber.filter.tags="@smoke"
mvn test -Dcucumber.filter.tags="@regression and not @skip"
```

---

## Step 16: View Reports

After running tests, check:

**HTML Report:**
```
target/cucumber-reports/cucumber.html
```
Open in browser to see detailed report

**JSON Report:**
```
target/cucumber-reports/cucumber.json
```
Used by CI/CD tools and Allure

**Console Output:**
```
Feature: Login Functionality

  Scenario: Successful login with valid credentials    # Login.feature:8
    Given user is on the login page                     # PASSED
    When user enters username "testuser" and password "testpass123"  # PASSED
    And user clicks on login button                     # PASSED
    Then user should be logged in successfully          # PASSED
    And welcome message should be displayed             # PASSED

1 Scenarios (1 passed)
5 Steps (5 passed)
0m12.345s
```

---

## Verification Checklist

- [ ] Maven project created
- [ ] pom.xml configured with Cucumber dependencies
- [ ] Cucumber plugin installed in IDE
- [ ] Project structure created correctly
- [ ] BasePage created
- [ ] Page classes (LoginPage, HomePage) created
- [ ] DriverManager created
- [ ] TestContext created
- [ ] Feature file created in `src/test/resources/features`
- [ ] Hooks created
- [ ] Step definitions created
- [ ] TestRunner created with @CucumberOptions
- [ ] testng.xml created
- [ ] Tests run successfully: `mvn clean test`
- [ ] Reports generated in `target/cucumber-reports`

---

## Common Issues & Solutions

### Issue 1: Undefined Step Definitions

**Error:**
```
You can implement missing steps with the snippets below:

@Given("user is on the login page")
public void user_is_on_the_login_page() {
    // Write code here
}
```

**Solution:** Copy the generated snippet and implement it in step definitions

### Issue 2: Feature files not found

**Solution:** Ensure feature files are in `src/test/resources/features`

### Issue 3: Step definitions not found

**Solution:** Check `glue` path in @CucumberOptions matches package name

### Issue 4: Cucumber plugin not working

**Solution:**
- Restart IDE after installing plugin
- File → Invalidate Caches / Restart

---

## Quick Commands

```bash
# Install dependencies
mvn clean install

# Run all tests
mvn clean test

# Run specific tags
mvn test -Dcucumber.filter.tags="@smoke"

# Dry run (check step definitions)
# Set dryRun = true in @CucumberOptions, then run
```

---

## Next Steps

✅ **Cucumber Phase 1 Complete!**

Proceed to:
- **Phase 2**: Allure Reporting Integration
- **Phase 3**: Advanced Cucumber Features
- **Phase 4**: Best Practices & Mistakes to Avoid

---

**Basic Cucumber Setup Complete! 🥒✨**