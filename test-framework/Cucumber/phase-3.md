# Cucumber Phase 3: Advanced Features
## Data Tables, Hooks, Tags, and More

---

## Prerequisites

✅ Cucumber Phase 1 & 2 completed

---

## Section 1: Data Tables

### What are Data Tables?

Data Tables allow passing multiple rows of data to a single step.

### Example: Simple Data Table

**Feature File:**
```gherkin
Scenario: Register user with details
  When user registers with following details
    | firstName | lastName | email            | phone      |
    | John      | Doe      | john@test.com    | 1234567890 |
```

**Step Definition:**
```java
@When("user registers with following details")
public void userRegistersWithDetails(DataTable dataTable) {
    // Convert to Map
    Map<String, String> data = dataTable.asMap(String.class, String.class);
    
    String firstName = data.get("firstName");
    String lastName = data.get("lastName");
    String email = data.get("email");
    String phone = data.get("phone");
    
    registerPage.enterFirstName(firstName);
    registerPage.enterLastName(lastName);
    registerPage.enterEmail(email);
    registerPage.enterPhone(phone);
}
```

### Example: Multiple Rows Data Table

**Feature File:**
```gherkin
Scenario: Add multiple products to cart
  When user adds following products to cart
    | productName | quantity | price |
    | Laptop      | 1        | 999   |
    | Mouse       | 2        | 25    |
    | Keyboard    | 1        | 75    |
```

**Step Definition:**
```java
@When("user adds following products to cart")
public void userAddsProductsToCart(DataTable dataTable) {
    // Convert to List of Maps
    List<Map<String, String>> products = dataTable.asMaps(String.class, String.class);
    
    for (Map<String, String> product : products) {
        String name = product.get("productName");
        int quantity = Integer.parseInt(product.get("quantity"));
        double price = Double.parseDouble(product.get("price"));
        
        productPage.searchProduct(name);
        productPage.addToCart(quantity);
    }
}
```

### Example: Vertical Data Table

**Feature File:**
```gherkin
Scenario: Create user account
  When user creates account with
    | Username | testuser    |
    | Password | pass123     |
    | Email    | test@qa.com |
    | Age      | 25          |
```

**Step Definition:**
```java
@When("user creates account with")
public void userCreatesAccount(DataTable dataTable) {
    Map<String, String> userDetails = dataTable.asMap(String.class, String.class);
    
    accountPage.enterUsername(userDetails.get("Username"));
    accountPage.enterPassword(userDetails.get("Password"));
    accountPage.enterEmail(userDetails.get("Email"));
    accountPage.enterAge(userDetails.get("Age"));
}
```

### Example: List of Strings

**Feature File:**
```gherkin
Scenario: User has multiple roles
  Given user has the following roles
    | Admin      |
    | Editor     |
    | Moderator  |
```

**Step Definition:**
```java
@Given("user has the following roles")
public void userHasRoles(DataTable dataTable) {
    List<String> roles = dataTable.asList(String.class);
    
    for (String role : roles) {
        userPage.assignRole(role);
    }
}
```

---

## Section 2: Hooks in Detail

### Hook Types

**@Before** - Runs before each scenario
**@After** - Runs after each scenario
**@BeforeStep** - Runs before each step
**@AfterStep** - Runs after each step

### Hook with Order

```java
@Before(order = 1)
public void setUp1() {
    // Runs first
    System.out.println("Setup 1");
}

@Before(order = 2)
public void setUp2() {
    // Runs second
    System.out.println("Setup 2");
}
```

### Hook with Tags

```java
@Before("@database")
public void setUpDatabase() {
    // Only runs for scenarios tagged with @database
    System.out.println("Setting up database connection");
}

@After("@database")
public void tearDownDatabase() {
    // Only runs for scenarios tagged with @database
    System.out.println("Closing database connection");
}

@Before("@api")
public void setUpAPI() {
    // Only runs for scenarios tagged with @api
    System.out.println("Setting up API client");
}
```

### Complete Hooks Example

```java
package com.automation.stepdefinitions;

import com.automation.utils.DriverManager;
import com.automation.utils.ScreenshotUtil;
import io.cucumber.java.*;
import io.qameta.allure.Allure;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

public class Hooks {

    @Before(order = 1)
    public void globalSetup(Scenario scenario) {
        System.out.println("========================================");
        System.out.println("Starting Scenario: " + scenario.getName());
        System.out.println("Tags: " + scenario.getSourceTagNames());
        System.out.println("========================================");
    }

    @Before(order = 2)
    public void setUpBrowser(Scenario scenario) {
        DriverManager.setDriver("chrome");
    }

    @Before(value = "@database", order = 3)
    public void setUpDatabase() {
        System.out.println("Connecting to database...");
        // Database connection logic
    }

    @BeforeStep
    public void beforeEachStep(Scenario scenario) {
        System.out.println("Executing step in: " + scenario.getName());
    }

    @AfterStep
    public void afterEachStep(Scenario scenario) {
        if (scenario.isFailed()) {
            // Take screenshot after failed step
            byte[] screenshot = ((TakesScreenshot) DriverManager.getDriver())
                    .getScreenshotAs(OutputType.BYTES);
            scenario.attach(screenshot, "image/png", "Failed Step Screenshot");
        }
    }

    @After(order = 2)
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed()) {
            System.out.println("Scenario Failed: " + scenario.getName());
            ScreenshotUtil.captureFailureScreenshot(DriverManager.getDriver());
        } else if (scenario.getStatus() == Status.PASSED) {
            System.out.println("Scenario Passed: " + scenario.getName());
        }
    }

    @After(value = "@database", order = 1)
    public void tearDownDatabase() {
        System.out.println("Closing database connection...");
        // Close database connection
    }

    @After(order = 3)
    public void closeBrowser() {
        DriverManager.quitDriver();
        System.out.println("========================================\n");
    }
}
```

---

## Section 3: Advanced Tagging

### Logical Expressions

**Feature File:**
```gherkin
@smoke @regression
Scenario: Important test
  # Runs with @smoke OR @regression

@smoke @api
Scenario: API smoke test
  # Runs with both @smoke AND @api

@skip
Scenario: Skip this test
  # Can be excluded
```

**Test Runner:**
```java
@CucumberOptions(
    tags = "@smoke and not @skip"
    // Runs smoke tests but excludes skipped ones
)
```

### Common Tag Combinations

```java
// Run only smoke tests
tags = "@smoke"

// Run smoke OR regression
tags = "@smoke or @regression"

// Run smoke AND regression (both must be present)
tags = "@smoke and @regression"

// Exclude specific tests
tags = "not @skip"
tags = "not @wip"  // WIP = Work In Progress

// Complex expressions
tags = "(@smoke or @regression) and not @skip"
tags = "@critical and @backend and not @bug"

// Run specific feature
tags = "@login"

// Multiple conditions
tags = "(@smoke and @ui) or (@regression and @api)"
```

### Tag Organization Strategy

```gherkin
# By Test Type
@smoke
@regression
@sanity

# By Priority
@critical
@high
@medium
@low

# By Feature
@login
@checkout
@payment
@search

# By Layer
@ui
@api
@database

# By Status
@wip          # Work in progress
@bug          # Known bug
@skip         # Skip execution
@flaky        # Unstable test

# By Environment
@prod-ready
@staging-only
@dev-only

# Example Usage
@smoke @login @critical
Scenario: Admin login
  # Critical smoke test for login feature
```

---

## Section 4: Background

### What is Background?

Background runs before EVERY scenario in a feature file. Use it for common setup steps.

**Example:**
```gherkin
Feature: Shopping Cart

  Background:
    Given user is logged in
    And user is on products page

  Scenario: Add single product to cart
    When user adds "Laptop" to cart
    Then cart should show 1 item

  Scenario: Add multiple products to cart
    When user adds "Laptop" to cart
    And user adds "Mouse" to cart
    Then cart should show 2 items
```

**Good for Background:**
- Login steps
- Navigation to common pages
- Setting up test data
- Preconditions needed by all scenarios

**NOT good for Background:**
- Steps specific to only some scenarios
- Steps that change between scenarios
- Complex setup that only few scenarios need

---

## Section 5: Scenario Outline with Examples

### Multiple Examples Sets

```gherkin
Scenario Outline: Login with different users
  Given user is on login page
  When user enters "<username>" and "<password>"
  Then login should be "<result>"

  @valid-users
  Examples: Valid Credentials
    | username  | password  | result  |
    | admin     | admin123  | success |
    | user1     | pass123   | success |

  @invalid-users
  Examples: Invalid Credentials
    | username     | password  | result  |
    | invaliduser  | wrong     | failure |
    | ''           | pass123   | failure |
    | admin        | wrong     | failure |
```

### Running Specific Example Sets

```java
@CucumberOptions(
    tags = "@valid-users"
    // Runs only valid user examples
)
```

---

## Section 6: DocStrings

### What are DocStrings?

DocStrings allow passing large text blocks to steps.

**Example 1: JSON Data**

**Feature File:**
```gherkin
Scenario: Create user via API
  When user creates account with JSON
    """
    {
      "username": "testuser",
      "email": "test@example.com",
      "firstName": "Test",
      "lastName": "User",
      "age": 25
    }
    """
  Then account should be created successfully
```

**Step Definition:**
```java
@When("user creates account with JSON")
public void createAccountWithJSON(String jsonData) {
    // jsonData contains the entire JSON string
    JSONObject userData = new JSONObject(jsonData);
    
    String username = userData.getString("username");
    String email = userData.getString("email");
    
    apiClient.createUser(jsonData);
}
```

**Example 2: Multi-line Text**

**Feature File:**
```gherkin
Scenario: Send email with custom message
  When user sends email with message
    """
    Dear Customer,
    
    Thank you for your order.
    Your order number is 12345.
    
    Best Regards,
    Support Team
    """
  Then email should be sent successfully
```

**Step Definition:**
```java
@When("user sends email with message")
public void sendEmailWithMessage(String emailBody) {
    emailPage.composeEmail();
    emailPage.enterMessage(emailBody);
    emailPage.clickSend();
}
```

---

## Section 7: Custom Parameter Types

### Define Custom Types

Create `ParameterTypes.java`:

**Location:** `src/test/java/com/automation/stepdefinitions/ParameterTypes.java`

```java
package com.automation.stepdefinitions;

import io.cucumber.java.ParameterType;

public class ParameterTypes {

    @ParameterType(".*")
    public User user(String userName) {
        return new User(userName);
    }

    @ParameterType("true|false|yes|no")
    public Boolean booleanValue(String value) {
        return value.equalsIgnoreCase("true") || value.equalsIgnoreCase("yes");
    }

    @ParameterType("[0-9]+")
    public Integer number(String value) {
        return Integer.parseInt(value);
    }
}

class User {
    private String name;
    
    public User(String name) {
        this.name = name;
    }
    
    public String getName() {
        return name;
    }
}
```

**Usage in Feature:**
```gherkin
Scenario: Custom parameter example
  Given {user} is logged in
  When {user} sets notification to {booleanValue}
  Then {user} should have {number} notifications
```

**Step Definition:**
```java
@Given("{user} is logged in")
public void userIsLoggedIn(User user) {
    loginPage.login(user.getName());
}

@When("{user} sets notification to {booleanValue}")
public void setNotification(User user, Boolean value) {
    settingsPage.setNotifications(value);
}
```

---

## Section 8: Dependency Injection with PicoContainer

### Add Dependency

Add to `pom.xml`:

```xml
<dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-picocontainer</artifactId>
    <version>${cucumber.version}</version>
</dependency>
```

### Shared Context Example

**TestContext.java:**
```java
package com.automation.context;

import com.automation.pages.*;
import com.automation.utils.DriverManager;
import org.openqa.selenium.WebDriver;

public class TestContext {
    private LoginPage loginPage;
    private HomePage homePage;
    private ProductPage productPage;
    private CartPage cartPage;
    
    // Shared data
    private String currentUser;
    private int cartItemCount;

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

    public ProductPage getProductPage() {
        if (productPage == null) {
            productPage = new ProductPage(getDriver());
        }
        return productPage;
    }

    public CartPage getCartPage() {
        if (cartPage == null) {
            cartPage = new CartPage(getDriver());
        }
        return cartPage;
    }

    private WebDriver getDriver() {
        return DriverManager.getDriver();
    }

    // Shared state
    public void setCurrentUser(String username) {
        this.currentUser = username;
    }

    public String getCurrentUser() {
        return currentUser;
    }

    public void setCartItemCount(int count) {
        this.cartItemCount = count;
    }

    public int getCartItemCount() {
        return cartItemCount;
    }
}
```

**Using in Step Definitions:**
```java
package com.automation.stepdefinitions;

import com.automation.context.TestContext;
import io.cucumber.java.en.*;

public class LoginSteps {
    private TestContext context;

    // PicoContainer automatically injects TestContext
    public LoginSteps(TestContext context) {
        this.context = context;
    }

    @Given("user {string} logs in")
    public void userLogsIn(String username) {
        context.getLoginPage().login(username, "password");
        context.setCurrentUser(username);  // Save to shared context
    }
}

public class CartSteps {
    private TestContext context;

    public CartSteps(TestContext context) {
        this.context = context;
    }

    @When("user adds product to cart")
    public void addProductToCart() {
        String currentUser = context.getCurrentUser();  // Get from shared context
        System.out.println("Adding product for user: " + currentUser);
        
        context.getProductPage().addToCart();
        context.setCartItemCount(context.getCartItemCount() + 1);
    }

    @Then("cart should show correct items")
    public void verifyCart() {
        int expectedCount = context.getCartItemCount();
        int actualCount = context.getCartPage().getItemCount();
        Assert.assertEquals(actualCount, expectedCount);
    }
}
```

---

## Section 9: Running Tests with Different Configurations

### Multiple Test Runners

**SmokeSuite.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@smoke",
    plugin = {"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"}
)
public class SmokeSuite extends AbstractTestNGCucumberTests {
}
```

**RegressionSuite.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@regression",
    plugin = {"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"}
)
public class RegressionSuite extends AbstractTestNGCucumberTests {
}
```

**APITestSuite.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@api",
    plugin = {"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"}
)
public class APITestSuite extends AbstractTestNGCucumberTests {
}
```

### Run from Command Line

```bash
# Run smoke tests
mvn test -Dtest=SmokeSuite

# Run regression tests
mvn test -Dtest=RegressionSuite

# Run API tests
mvn test -Dtest=APITestSuite

# Run with tags
mvn test -Dcucumber.filter.tags="@smoke and not @skip"
```

---

## Section 10: Parallel Execution

### Scenario-Level Parallelism

**testng.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Parallel Cucumber Suite" parallel="methods" thread-count="5">
    <test name="Cucumber Tests">
        <classes>
            <class name="com.automation.runners.TestRunner"/>
        </classes>
    </test>
</suite>
```

**TestRunner.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@regression",
    plugin = {"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"}
)
public class TestRunner extends AbstractTestNGCucumberTests {
    
    @Override
    @DataProvider(parallel = true)
    public Object[][] scenarios() {
        return super.scenarios();
    }
}
```

### Feature-Level Parallelism

Create multiple runners for different features:

**LoginRunner.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features/Login.feature",
    glue = {"com.automation.stepdefinitions"}
)
public class LoginRunner extends AbstractTestNGCucumberTests {
}
```

**CheckoutRunner.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features/Checkout.feature",
    glue = {"com.automation.stepdefinitions"}
)
public class CheckoutRunner extends AbstractTestNGCucumberTests {
}
```

**testng.xml:**
```xml
<suite name="Parallel Features" parallel="tests" thread-count="3">
    <test name="Login Tests">
        <classes>
            <class name="com.automation.runners.LoginRunner"/>
        </classes>
    </test>
    <test name="Checkout Tests">
        <classes>
            <class name="com.automation.runners.CheckoutRunner"/>
        </classes>
    </test>
</suite>
```

---

## Section 11: Rerun Failed Scenarios

### Create Rerun Plugin

**TestRunner.java:**
```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@regression",
    plugin = {
        "io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm",
        "rerun:target/rerun.txt"  // Saves failed scenarios
    }
)
public class TestRunner extends AbstractTestNGCucumberTests {
}
```

### Create Rerun Runner

**FailedTestRunner.java:**
```java
@CucumberOptions(
    features = "@target/rerun.txt",  // Reads from rerun file
    glue = {"com.automation.stepdefinitions"},
    plugin = {"io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"}
)
public class FailedTestRunner extends AbstractTestNGCucumberTests {
}
```

### Run Failed Tests

```bash
# First run - some tests fail
mvn test -Dtest=TestRunner

# Rerun only failed tests
mvn test -Dtest=FailedTestRunner
```

---

## Section 12: Cucumber Expressions vs Regular Expressions

### Cucumber Expressions (Recommended)

```java
// Simpler and more readable
@When("user adds {int} items to cart")
public void addItems(int count) {
    // count is automatically converted to int
}

@When("user enters {string} as username")
public void enterUsername(String username) {
    // Matches any string in quotes
}

@Then("price should be {double} dollars")
public void verifyPrice(double price) {
    // Automatically converts to double
}

@When("user is {word} years old")
public void setAge(String age) {
    // Matches single word
}
```

### Regular Expressions (Old Style)

```java
@When("^user adds (\\d+) items to cart$")
public void addItems(int count) {
    // More complex regex pattern
}

@When("^user enters \"([^\"]*)\" as username$")
public void enterUsername(String username) {
    // Complex regex for strings
}
```

**Use Cucumber Expressions for:**
- Simpler syntax
- Better readability
- Built-in type conversion
- Modern Cucumber versions

---

## Section 13: Conditional Execution

### Skip Scenarios Based on Environment

**Hooks.java:**
```java
@Before
public void checkEnvironment(Scenario scenario) {
    String environment = System.getProperty("env", "dev");
    
    if (scenario.getSourceTagNames().contains("@prod-only") && 
        !environment.equals("prod")) {
        throw new SkipException("Skipping - Prod only test");
    }
}
```

**Feature:**
```gherkin
@prod-only
Scenario: Production-only test
  Given user is in production
  # Skipped in dev/staging
```

---

## Section 14: Advanced Feature File Organization

### Folder Structure

```
features/
├── smoke/
│   ├── Login.feature
│   └── Checkout.feature
├── regression/
│   ├── Orders.feature
│   ├── Payment.feature
│   └── Search.feature
├── api/
│   ├── UserAPI.feature
│   └── ProductAPI.feature
└── integration/
    └── EndToEnd.feature
```

### Run Specific Folders

```java
@CucumberOptions(
    features = "src/test/resources/features/smoke"
    // Runs only smoke folder
)
```

---

## Section 15: Custom Formatters

### Create Custom Plugin

```java
package com.automation.plugins;

import io.cucumber.plugin.ConcurrentEventListener;
import io.cucumber.plugin.event.*;

public class CustomFormatter implements ConcurrentEventListener {
    
    @Override
    public void setEventPublisher(EventPublisher publisher) {
        publisher.registerHandlerFor(TestRunStarted.class, this::onTestRunStarted);
        publisher.registerHandlerFor(TestRunFinished.class, this::onTestRunFinished);
        publisher.registerHandlerFor(TestCaseStarted.class, this::onTestCaseStarted);
        publisher.registerHandlerFor(TestCaseFinished.class, this::onTestCaseFinished);
    }

    private void onTestRunStarted(TestRunStarted event) {
        System.out.println("===== TEST RUN STARTED =====");
    }

    private void onTestRunFinished(TestRunFinished event) {
        System.out.println("===== TEST RUN FINISHED =====");
    }

    private void onTestCaseStarted(TestCaseStarted event) {
        System.out.println("Starting: " + event.getTestCase().getName());
    }

    private void onTestCaseFinished(TestCaseFinished event) {
        System.out.println("Finished: " + event.getTestCase().getName());
        System.out.println("Status: " + event.getResult().getStatus());
    }
}
```

**Use in Runner:**
```java
@CucumberOptions(
    plugin = {"com.automation.plugins.CustomFormatter"}
)
```

---

## Verification Checklist

- [ ] Data Tables implemented correctly
- [ ] Hooks created with proper order
- [ ] Tags organized logically
- [ ] Background used for common steps
- [ ] Scenario Outline with multiple examples
- [ ] DocStrings for large text data
- [ ] Custom parameter types defined
- [ ] PicoContainer dependency injection working
- [ ] Multiple test runners created
- [ ] Parallel execution configured
- [ ] Rerun plugin setup for failed tests
- [ ] Cucumber expressions used

---

## Quick Reference

### Data Table Methods
```java
dataTable.asMap(String.class, String.class)
dataTable.asMaps(String.class, String.class)
dataTable.asList(String.class)
dataTable.asLists(String.class)
```

### Hook Annotations
```java
@Before
@After
@BeforeStep
@AfterStep
```

### Tag Expressions
```java
"@smoke"
"@smoke or @regression"
"@smoke and @api"
"not @skip"
"(@smoke or @regression) and not @skip"
```

---

## Next Steps

✅ **Cucumber Phase 3 Complete!**

Proceed to:
- **Phase 4**: Best Practices & Common Mistakes to Avoid

---

**Advanced Cucumber Features Complete! 🥒🚀**