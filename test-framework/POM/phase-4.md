# Phase 4: Best Practices & Common Mistakes
## What to DO and What to AVOID in POM Framework

---

## Prerequisites

✅ Phase 1, 2, 3 completed

---

## Section 1: Page Object Model Best Practices

### ✅ DO: Use By Locators

**Correct Approach:**
```java
public class LoginPage extends BasePage {
    // Store locator strategy, NOT WebElement
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");

    public void enterUsername(String username) {
        type(usernameField, username);  // Element found fresh each time
    }
}
```

**Why?**
- Element located fresh every time
- No `StaleElementReferenceException`
- Works with dynamic content

---

### ❌ DON'T: Use @FindBy with PageFactory

**Wrong Approach:**
```java
public class LoginPage {
    @FindBy(id = "username")
    private WebElement usernameField;  // BAD - Element stored once

    public LoginPage(WebDriver driver) {
        PageFactory.initElements(driver, this);  // BAD - Outdated pattern
    }

    public void enterUsername(String username) {
        usernameField.sendKeys(username);  // Can throw StaleElementReferenceException
    }
}
```

**Problems:**
- Element found only once during initialization
- Causes `StaleElementReferenceException` frequently
- Doesn't work well with dynamic pages
- Difficult to add explicit waits

---

### ✅ DO: Return Page Objects for Method Chaining

```java
public class LoginPage extends BasePage {

    public LoginPage enterUsername(String username) {
        type(usernameField, username);
        return this;  // Returns current page
    }

    public LoginPage enterPassword(String password) {
        type(passwordField, password);
        return this;  // Returns current page
    }

    public HomePage clickLogin() {
        click(loginButton);
        return new HomePage(driver);  // Returns next page
    }
}

// Usage - Method chaining
loginPage.enterUsername("user")
         .enterPassword("pass")
         .clickLogin();
```

---

### ❌ DON'T: Use void Return Type

```java
// BAD
public void enterUsername(String username) {
    type(usernameField, username);
    // No return - Can't chain methods
}

// Usage - Multiple statements needed
loginPage.enterUsername("user");
loginPage.enterPassword("pass");
loginPage.clickLogin();
```

---

## Section 2: Locator Strategy

### ✅ DO: Follow Locator Priority

**Priority Order (Best to Worst):**
1. **id** - Fast, unique
2. **name** - Fast, usually unique
3. **CSS Selector** - Fast, flexible
4. **XPath** - Flexible but slower

```java
// BEST - Using ID
private final By loginButton = By.id("login-btn");

// GOOD - Using CSS
private final By loginButton = By.cssSelector(".login-form button[type='submit']");

// OK - Using XPath (when no other option)
private final By loginButton = By.xpath("//button[@type='submit' and contains(text(),'Login')]");
```

---

### ❌ DON'T: Use Complex or Fragile XPaths

```java
// BAD - Absolute XPath (breaks easily)
By.xpath("/html/body/div[1]/div[2]/form/button");

// BAD - Too complex
By.xpath("//div[@class='container']//div[@class='row']//div[@class='col-md-6']//form//button[1]");

// GOOD - Simple and relative
By.xpath("//button[@id='login']");

// BETTER - Use CSS instead
By.cssSelector("#login");
```

---

### ✅ DO: Use Descriptive Locator Names

```java
// GOOD - Clear and descriptive
private final By usernameField = By.id("username");
private final By passwordField = By.id("password");
private final By loginButton = By.id("login-btn");
private final By errorMessage = By.className("error-msg");

// BAD - Not descriptive
private final By field1 = By.id("username");
private final By btn = By.id("login-btn");
private final By msg = By.className("error-msg");
```

---

## Section 3: Wait Strategies

### ✅ DO: Use Explicit Waits

```java
// In BasePage
protected WebElement findElement(By locator) {
    return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
}

// Specific waits when needed
protected void waitForElementToBeClickable(By locator) {
    wait.until(ExpectedConditions.elementToBeClickable(locator));
}

protected void waitForTextToBePresentInElement(By locator, String text) {
    wait.until(ExpectedConditions.textToBePresentInElementLocated(locator, text));
}
```

---

### ❌ DON'T: Use Thread.sleep()

```java
// BAD - Fixed wait time
Thread.sleep(5000);  // Always waits 5 seconds even if element appears in 1 second

// GOOD - Dynamic wait
wait.until(ExpectedConditions.visibilityOfElementLocated(locator));  // Waits only as long as needed
```

**Why Thread.sleep is bad:**
- Slows down tests unnecessarily
- Not reliable for dynamic content
- Makes tests flaky
- Wastes time

---

### ✅ DO: Set Appropriate Timeout Values

```java
// In config.properties
implicit.wait=10
explicit.wait=20
page.load.timeout=30

// In BaseTest
        driver.manage().timeouts().implicitlyWait(
        Duration.ofSeconds(ConfigReader.getIntProperty("implicit.wait"))
        );

// In BasePage
        this.wait = new WebDriverWait(driver,
                                      Duration.ofSeconds(ConfigReader.getIntProperty("explicit.wait"))
        );
```

---

## Section 4: Test Organization

### ✅ DO: Keep Tests Independent

```java
// GOOD - Each test is independent
@Test
public void testLogin() {
    // Complete login flow in one test
    LoginPage loginPage = new LoginPage(driver);
    HomePage homePage = loginPage.login("user", "pass");
    Assert.assertTrue(homePage.isUserLoggedIn());
}

@Test
public void testLogout() {
    // This test doesn't depend on testLogin
    LoginPage loginPage = new LoginPage(driver);
    HomePage homePage = loginPage.login("user", "pass");
    LoginPage logoutPage = homePage.logout();
    Assert.assertTrue(logoutPage.isDisplayed());
}
```

---

### ❌ DON'T: Create Test Dependencies

```java
// BAD - Test2 depends on Test1
@Test(priority = 1)
public void test1Login() {
    loginPage.login("user", "pass");
    // Don't quit driver
}

@Test(priority = 2, dependsOnMethods = "test1Login")
public void test2Logout() {
    // Assumes user is already logged in from test1
    homePage.logout();  // Will fail if test1 fails
}
```

**Problems:**
- If test1 fails, test2 also fails
- Can't run tests in parallel
- Can't run test2 independently
- Difficult to debug

---

### ✅ DO: One Assertion Per Test Concept

```java
// GOOD - Testing one thing
@Test
public void testLoginSuccess() {
    HomePage homePage = loginPage.login("user", "pass");
    Assert.assertTrue(homePage.isUserLoggedIn());
}

@Test
public void testWelcomeMessageDisplayed() {
    HomePage homePage = loginPage.login("user", "pass");
    String message = homePage.getWelcomeMessage();
    Assert.assertTrue(message.contains("Welcome"));
}
```

---

### ❌ DON'T: Test Too Many Things in One Test

```java
// BAD - Testing multiple unrelated things
@Test
public void testEntireApplication() {
    loginPage.login("user", "pass");
    Assert.assertTrue(homePage.isUserLoggedIn());  // Login test

    homePage.clickProducts();
    Assert.assertTrue(productsPage.isDisplayed());  // Navigation test

    productsPage.addToCart();
    Assert.assertEquals(cartPage.getItemCount(), 1);  // Cart test

    // ... many more assertions
}
```

**Problems:**
- Hard to identify which part failed
- Long execution time
- Difficult to maintain
- Not focused

---

## Section 5: Code Organization

### ✅ DO: Separate Concerns

**Test Class - Assertions and test logic:**
```java
public class LoginTest extends BaseTest {
    @Test
    public void testLogin() {
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.login("user", "pass");
        Assert.assertTrue(homePage.isUserLoggedIn());  // Assertion in test
    }
}
```

**Page Class - Actions only:**
```java
public class HomePage extends BasePage {
    public boolean isUserLoggedIn() {
        return isDisplayed(welcomeMessage);  // Returns data, no assertion
    }
}
```

---

### ❌ DON'T: Put Assertions in Page Classes

```java
// BAD - Assertion in page class
public class HomePage extends BasePage {
    public void verifyUserLoggedIn() {
        Assert.assertTrue(isDisplayed(welcomeMessage));  // BAD - Assertion in page
    }
}
```

**Why it's bad:**
- Page classes should only perform actions
- Assertions belong in test classes
- Makes page classes less reusable
- Violates single responsibility principle

---

### ✅ DO: Use Descriptive Method Names

```java
// GOOD
public boolean isUserLoggedIn() { }
public String getWelcomeMessage() { }
public void clickLoginButton() { }
public HomePage performLogin(String username, String password) { }

// BAD
public boolean check() { }
public String get() { }
public void click() { }
public HomePage doIt(String s1, String s2) { }
```

---

## Section 6: Data Management

### ✅ DO: Externalize Test Data

```java
// config.properties
test.username=validuser
test.password=validpass123
app.url=https://example.com

// Test class
@Test
public void testLogin() {
    String username = ConfigReader.getProperty("test.username");
    String password = ConfigReader.getProperty("test.password");
    loginPage.login(username, password);
}
```

---

### ❌ DON'T: Hardcode Test Data

```java
// BAD - Hardcoded values
@Test
public void testLogin() {
    loginPage.login("hardcodeduser", "hardcodedpass");  // BAD
    driver.get("https://hardcoded.com");  // BAD
}
```

**Problems:**
- Difficult to change
- Not reusable across environments
- Can't easily test different data sets

---

### ✅ DO: Use Data Providers for Multiple Test Data

```java
@DataProvider(name = "loginData")
public Object[][] getLoginData() {
    return new Object[][] {
        {"validuser", "validpass", true},
        {"invaliduser", "wrongpass", false},
        {"", "validpass", false},
        {"validuser", "", false}
    };
}

@Test(dataProvider = "loginData")
public void testLoginWithMultipleData(String username, String password, boolean shouldSucceed) {
    loginPage.login(username, password);
    if (shouldSucceed) {
        Assert.assertTrue(homePage.isUserLoggedIn());
    } else {
        Assert.assertTrue(loginPage.getErrorMessage().contains("Invalid"));
    }
}
```

---

## Section 7: Exception Handling

### ✅ DO: Handle Exceptions Properly

```java
protected boolean isDisplayed(By locator) {
    try {
        logger.info("Checking if element is displayed: " + locator);
        return findElement(locator).isDisplayed();
    } catch (NoSuchElementException e) {
        logger.error("Element not found: " + locator);
        return false;
    } catch (TimeoutException e) {
        logger.error("Element not visible within timeout: " + locator);
        return false;
    }
}
```

---

### ❌ DON'T: Ignore Exceptions

```java
// BAD - Empty catch block
try {
    element.click();
} catch (Exception e) {
    // Silently ignoring exception - BAD
}

// BAD - Catching generic Exception
try {
    element.click();
} catch (Exception e) {
    // Too broad - catch specific exceptions
}
```

---

### ✅ DO: Log Exceptions

```java
try {
    click(loginButton);
} catch (ElementNotInteractableException e) {
    logger.error("Login button not clickable", e);
    throw e;  // Re-throw to fail the test
}
```

---

## Section 8: Browser Management

### ✅ DO: Close Browser After Each Test

```java
@AfterMethod
public void tearDown() {
    if (driver != null) {
        logger.info("Closing browser");
        driver.quit();  // Closes browser and ends session
    }
}
```

---

### ❌ DON'T: Use driver.close() Instead of driver.quit()

```java
// BAD
@AfterMethod
public void tearDown() {
    driver.close();  // Only closes current window, doesn't end session
}

// GOOD
@AfterMethod
public void tearDown() {
    driver.quit();  // Closes all windows and ends session
}
```

---

### ✅ DO: Maximize Browser Window

```java
@BeforeMethod
public void setUp() {
    driver = new ChromeDriver();
    driver.manage().window().maximize();  // Ensures consistent element visibility
}
```

---

## Section 9: Logging Best Practices

### ✅ DO: Log at Appropriate Levels

```java
// Test flow
logger.info("Starting login test");

// Actions
logger.info("Clicking login button");

// Debugging
logger.debug("Element coordinates: x=" + x + ", y=" + y);

// Warnings
logger.warn("Element took longer than expected");

// Errors
logger.error("Failed to find element", exception);
```

---

### ❌ DON'T: Log Sensitive Information

```java
// BAD - Security risk
logger.info("User password: " + password);
logger.info("API key: " + apiKey);
logger.info("Credit card: " + ccNumber);

// GOOD - Log safely
logger.info("User authenticated successfully");
logger.info("API call successful");
logger.info("Payment processed");
```

---

### ❌ DON'T: Use System.out.println

```java
// BAD
System.out.println("Test started");  // Not logged to file

// GOOD
logger.info("Test started");  // Logged to console and file
```

---

## Section 10: Configuration Management

### ✅ DO: Use config.properties for Environment Settings

```properties
# Development
app.url=https://dev.example.com
api.url=https://api-dev.example.com

# Staging
app.url=https://staging.example.com
api.url=https://api-staging.example.com

# Production
app.url=https://example.com
api.url=https://api.example.com
```

---

### ✅ DO: Use Different Config Files for Different Environments

```java
public class ConfigReader {
    private static Properties properties;
    
    static {
        String env = System.getProperty("env", "dev");  // Default to dev
        String configPath = "src/main/resources/config-" + env + ".properties";
        // Load config-dev.properties, config-staging.properties, etc.
    }
}

// Run with different environments
// mvn test -Denv=staging
// mvn test -Denv=production
```

---

## Section 11: Naming Conventions

### ✅ DO: Follow Consistent Naming

**Classes:**
```java
LoginPage.java      // Page classes end with "Page"
LoginTest.java      // Test classes end with "Test"
ConfigReader.java   // Utility classes - descriptive names
```

**Methods:**
```java
// Page classes - action-oriented
public void clickLoginButton() { }
public void enterUsername(String username) { }
public HomePage performLogin(String user, String pass) { }

// Test classes - should be descriptive
public void testSuccessfulLogin() { }
public void testLoginWithInvalidCredentials() { }
public void verifyErrorMessageDisplayedForEmptyUsername() { }
```

**Variables:**
```java
// Locators - noun form
private final By loginButton = By.id("login");
private final By usernameField = By.id("username");

// WebDriver
protected WebDriver driver;

// Wait objects
protected WebDriverWait wait;
```

---

### ❌ DON'T: Use Unclear Names

```java
// BAD
private final By btn1 = By.id("login");
private final By field = By.id("username");
public void test1() { }
public void doSomething() { }
```

---

## Section 12: Package Structure

### ✅ DO: Organize Packages Logically

```
com.automation/
├── base/           // Base classes
│   ├── BasePage.java
│   └── BaseTest.java
├── pages/          // Page objects
│   ├── LoginPage.java
│   ├── HomePage.java
│   └── ProductsPage.java
├── utils/          // Utilities
│   ├── ConfigReader.java
│   ├── LoggerUtil.java
│   └── ScreenshotUtil.java
└── tests/          // Test classes
    ├── LoginTest.java
    └── ProductsTest.java
```

---

## Section 13: Screenshot Practices

### ✅ DO: Take Screenshots on Failure

```java
@AfterMethod
public void tearDown(ITestResult result) {
    if (result.getStatus() == ITestResult.FAILURE) {
        logger.error("Test Failed: " + result.getName());
        String screenshotPath = ScreenshotUtil.captureScreenshot(driver, result.getName());
        logger.info("Screenshot saved at: " + screenshotPath);
    }
    driver.quit();
}
```

---

### ❌ DON'T: Take Screenshots After Every Action

```java
// BAD - Slows down tests significantly
public void click(By locator) {
    findElement(locator).click();
    ScreenshotUtil.captureScreenshot(driver, "after_click");  // BAD - Unnecessary
}
```

---

## Section 14: Comments and Documentation

### ✅ DO: Add Meaningful Comments

```java
/**
 * Performs login with given credentials
 * @param username User's username
 * @param password User's password
 * @return HomePage object if login successful
 */
public HomePage login(String username, String password) {
    enterUsername(username);
    enterPassword(password);
    return clickLogin();
}
```

---

### ❌ DON'T: Add Obvious Comments

```java
// BAD - Comment states the obvious
// Click login button
public void clickLoginButton() {
    click(loginButton);
}

// BAD - Redundant comment
int count = 0;  // Initialize count to 0
```

---

## Section 15: Performance Optimization

### ✅ DO: Reuse Browser Sessions (When Appropriate)

For tests that don't need clean state:
```java
@BeforeClass  // Once per class
public void setUpClass() {
    driver = new ChromeDriver();
    driver.get(ConfigReader.getProperty("app.url"));
}

@AfterClass  // Once per class
public void tearDownClass() {
    driver.quit();
}
```

---

### ❌ DON'T: Keep Browser Open Unnecessarily

```java
// BAD - Browser never closes
@BeforeMethod
public void setUp() {
    driver = new ChromeDriver();
}

// Missing @AfterMethod to close browser
```

---

## Section 16: Parallel Execution

### ✅ DO: Make Tests Thread-Safe for Parallel Execution

```java
public class BaseTest {
    protected ThreadLocal<WebDriver> driver = new ThreadLocal<>();
    
    @BeforeMethod
    public void setUp() {
        driver.set(new ChromeDriver());
        driver.get().manage().window().maximize();
    }
    
    @AfterMethod
    public void tearDown() {
        driver.get().quit();
        driver.remove();
    }
    
    protected WebDriver getDriver() {
        return driver.get();
    }
}
```

---

## Common Mistakes Summary Table

| Mistake | Impact | Solution |
|---------|--------|----------|
| Using PageFactory | StaleElementReferenceException | Use By locators |
| Using Thread.sleep() | Slow, unreliable tests | Use explicit waits |
| Hardcoding data | Not reusable | Use config.properties |
| Test dependencies | Can't run in parallel | Make tests independent |
| Assertions in pages | Low reusability | Keep assertions in tests |
| Complex XPath | Fragile, slow | Use ID or CSS |
| No logging | Hard to debug | Add proper logging |
| driver.close() | Incomplete cleanup | Use driver.quit() |
| Logging passwords | Security risk | Don't log sensitive data |
| Empty catch blocks | Hidden failures | Log and re-throw |

---

## Quick Reference Checklist

### Before Writing Tests
- [ ] Page classes use By locators, not WebElements
- [ ] BasePage and BaseTest are properly configured
- [ ] Config.properties contains all settings
- [ ] Logger is set up and working
- [ ] Allure reporting is configured

### While Writing Tests
- [ ] Each test is independent
- [ ] Test methods have descriptive names
- [ ] Using explicit waits, not Thread.sleep()
- [ ] Test data is externalized
- [ ] Proper logging at each step
- [ ] Assertions only in test classes
- [ ] Methods return page objects for chaining

### After Writing Tests
- [ ] Tests can run individually
- [ ] Tests can run in any order
- [ ] Browser closes after each test
- [ ] Screenshots captured on failure
- [ ] Logs are readable and helpful
- [ ] No hardcoded values
- [ ] Code is properly commented

---

## Example: Complete Good Practice Implementation

**LoginPage.java:**
```java
package com.automation.pages;

import com.automation.base.BasePage;
import io.qameta.allure.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {
    
    // Descriptive locator names using By objects
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");
    private final By loginButton = By.cssSelector("button[type='submit']");
    private final By errorMessage = By.className("error-message");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    // Methods return page objects for chaining
    @Step("Enter username: {username}")
    public LoginPage enterUsername(String username) {
        logger.info("Entering username: " + username);
        type(usernameField, username);
        return this;
    }

    @Step("Enter password")
    public LoginPage enterPassword(String password) {
        logger.info("Entering password");
        type(passwordField, password);
        return this;
    }

    @Step("Click login button")
    public HomePage clickLogin() {
        logger.info("Clicking login button");
        click(loginButton);
        return new HomePage(driver);
    }

    @Step("Get error message")
    public String getErrorMessage() {
        logger.info("Getting error message");
        return getText(errorMessage);
    }

    // Compound action for convenience
    @Step("Perform login with username: {username}")
    public HomePage login(String username, String password) {
        return enterUsername(username)
                .enterPassword(password)
                .clickLogin();
    }
}
```

**LoginTest.java:**
```java
package com.automation.tests;

import com.automation.base.BaseTest;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import com.automation.utils.ConfigReader;
import io.qameta.allure.Description;
import io.qameta.allure.Severity;
import io.qameta.allure.SeverityLevel;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test(priority = 1)
    @Description("Verify successful login with valid credentials")
    @Severity(SeverityLevel.CRITICAL)
    public void testSuccessfulLogin() {
        logger.info("===== Test: testSuccessfulLogin =====");
        
        // Get data from config
        String username = ConfigReader.getProperty("test.username");
        String password = ConfigReader.getProperty("test.password");
        
        // Perform actions
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.login(username, password);
        
        // Assertions in test class only
        Assert.assertTrue(homePage.isUserLoggedIn(), "User should be logged in");
        logger.info("Test Passed: User logged in successfully");
    }

    @Test(priority = 2)
    @Description("Verify login fails with invalid credentials")
    @Severity(SeverityLevel.NORMAL)
    public void testLoginWithInvalidCredentials() {
        logger.info("===== Test: testLoginWithInvalidCredentials =====");
        
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterUsername("invaliduser")
                 .enterPassword("wrongpassword")
                 .clickLogin();
        
        String errorMsg = loginPage.getErrorMessage();
        Assert.assertTrue(errorMsg.contains("Invalid"), 
                         "Error message should be displayed for invalid login");
        logger.info("Test Passed: Error message displayed correctly");
    }
}
```

---

## Advanced Tips

### Tip 1: Custom Wait Conditions

```java
// In BasePage
protected void waitForElementToDisappear(By locator) {
    wait.until(ExpectedConditions.invisibilityOfElementLocated(locator));
}

protected void waitForTextToChange(By locator, String oldText) {
    wait.until(driver -> !getText(locator).equals(oldText));
}

protected void waitForAttributeToContain(By locator, String attribute, String value) {
    wait.until(ExpectedConditions.attributeContains(locator, attribute, value));
}
```

### Tip 2: Smart Element Interaction

```java
// In BasePage - Retry mechanism
protected void clickWithRetry(By locator, int maxAttempts) {
    for (int i = 0; i < maxAttempts; i++) {
        try {
            click(locator);
            return;
        } catch (ElementClickInterceptedException e) {
            logger.warn("Click intercepted, retrying... Attempt " + (i + 1));
            if (i == maxAttempts - 1) throw e;
        }
    }
}

// JavaScript click fallback
protected void clickWithJS(By locator) {
    WebElement element = findElement(locator);
    JavascriptExecutor js = (JavascriptExecutor) driver;
    js.executeScript("arguments[0].click();", element);
}
```

### Tip 3: Dynamic Waits Based on Environment

```java
// In BaseTest
@BeforeMethod
public void setUp() {
    String env = ConfigReader.getProperty("environment");
    int waitTime = env.equals("production") ? 30 : 10;
    
    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(waitTime));
}
```

### Tip 4: Reusable Assertions

```java
// Create AssertionHelper utility
public class AssertionHelper {
    
    public static void assertElementDisplayed(WebDriver driver, By locator, String message) {
        WebElement element = driver.findElement(locator);
        Assert.assertTrue(element.isDisplayed(), message);
    }
    
    public static void assertTextContains(String actual, String expected, String message) {
        Assert.assertTrue(actual.contains(expected), 
            message + ". Expected text to contain: " + expected + ", but was: " + actual);
    }
}
```

### Tip 5: Page Load Verification

```java
// In BasePage
protected void verifyPageLoaded(By uniqueElement) {
    try {
        wait.until(ExpectedConditions.visibilityOfElementLocated(uniqueElement));
        logger.info("Page loaded successfully");
    } catch (TimeoutException e) {
        logger.error("Page failed to load");
        throw new RuntimeException("Page did not load within timeout", e);
    }
}

// In LoginPage
public LoginPage(WebDriver driver) {
    super(driver);
    verifyPageLoaded(loginButton);  // Verify login page loaded
}
```

---

## Troubleshooting Common Issues

### Issue 1: Flaky Tests

**Symptoms:** Tests pass sometimes, fail other times

**Solutions:**
```java
// Add proper waits
protected WebElement findElement(By locator) {
    return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
}

// Wait for page to stabilize
protected void waitForPageToLoad() {
    wait.until(driver -> ((JavascriptExecutor) driver)
        .executeScript("return document.readyState").equals("complete"));
}

// Increase timeout for slow environments
wait = new WebDriverWait(driver, Duration.ofSeconds(30));
```

### Issue 2: Element Not Interactable

**Solutions:**
```java
// Wait for element to be clickable
protected void clickWhenReady(By locator) {
    wait.until(ExpectedConditions.elementToBeClickable(locator)).click();
}

// Scroll into view first
protected void scrollIntoView(By locator) {
    WebElement element = driver.findElement(locator);
    JavascriptExecutor js = (JavascriptExecutor) driver;
    js.executeScript("arguments[0].scrollIntoView(true);", element);
}
```

### Issue 3: Tests Take Too Long

**Solutions:**
```java
// Reduce implicit wait
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));

// Use targeted explicit waits
wait.until(ExpectedConditions.visibilityOfElementLocated(specificElement));

// Run tests in parallel
// In testng.xml: parallel="methods" thread-count="3"
```

---

## Final Best Practices Summary

### Critical Rules (Never Break These!)

1. **ALWAYS use By locators, NEVER PageFactory**
2. **NEVER use Thread.sleep()**
3. **NEVER hardcode test data**
4. **NEVER put assertions in Page classes**
5. **ALWAYS close browser with driver.quit()**
6. **ALWAYS log important actions**
7. **NEVER log sensitive information**
8. **ALWAYS make tests independent**
9. **ALWAYS use explicit waits**
10. **NEVER ignore exceptions**

### Golden Rules for Clean Tests

✅ **One test = One scenario**
✅ **One assertion = One thing to verify**
✅ **Page classes = Actions only**
✅ **Test classes = Logic + Assertions**
✅ **Tests should be readable like plain English**

---

## Next Steps

✅ **Phase 4 Complete!**

You now understand:
- ✅ What to DO in POM framework
- ✅ What NOT to do
- ✅ Common mistakes and solutions
- ✅ Best practices for all aspects
- ✅ Real-world examples

Proceed to:
- **Phase 5**: PageFactory Issues & Why By Locators Are Superior

---

**Best Practices Guide Complete! ✨**

Remember: Good practices lead to maintainable, reliable, and scalable test automation frameworks!