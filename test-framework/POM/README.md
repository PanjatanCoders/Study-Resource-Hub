# Complete Page Object Model Setup Guide
## Java Selenium + TestNG + Allure Reporting + Logger

---

## Prerequisites
- Java JDK 11 or higher
- Maven installed
- IDE (IntelliJ IDEA/Eclipse)
- Basic understanding of Selenium WebDriver

---

## Phase 1: Basic POM Setup

### Step 1: Create Maven Project

1. Open your IDE
2. Create New Maven Project
3. Set:
    - GroupId: `com.automation`
    - ArtifactId: `selenium-pom-framework`
    - Version: `1.0-SNAPSHOT`

### Step 2: Configure `pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.automation</groupId>
    <artifactId>selenium-pom-framework</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <selenium.version>4.15.0</selenium.version>
        <testng.version>7.8.0</testng.version>
        <allure.version>2.24.0</allure.version>
        <aspectj.version>1.9.20</aspectj.version>
    </properties>

    <dependencies>
        <!-- Selenium -->
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

        <!-- Allure TestNG -->
        <dependency>
            <groupId>io.qameta.allure</groupId>
            <artifactId>allure-testng</artifactId>
            <version>${allure.version}</version>
        </dependency>

        <!-- Log4j API -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>2.20.0</version>
        </dependency>

        <!-- Log4j Core -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.20.0</version>
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
</project>
```

### Step 3: Create Folder Structure

```
selenium-pom-framework/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/automation/
│   │   │       ├── base/
│   │   │       │   ├── BasePage.java
│   │   │       │   └── BaseTest.java
│   │   │       ├── pages/
│   │   │       │   ├── LoginPage.java
│   │   │       │   └── HomePage.java
│   │   │       └── utils/
│   │   │           ├── ConfigReader.java
│   │   │           └── LoggerUtil.java
│   │   └── resources/
│   │       ├── config.properties
│   │       └── log4j2.xml
│   └── test/
│       ├── java/
│       │   └── com/automation/tests/
│       │       └── LoginTest.java
│       └── resources/
│           └── testng.xml
├── target/
│   └── allure-results/  (generated after test execution)
└── pom.xml
```

### Step 4: Create `BasePage.java`

**Location:** `src/main/java/com/automation/base/BasePage.java`

```java
package com.automation.base;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import com.automation.utils.LoggerUtil;

import java.time.Duration;

public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;
    protected LoggerUtil logger;

    public BasePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        this.logger = new LoggerUtil(this.getClass());
    }

    // Find element with explicit wait
    protected WebElement findElement(By locator) {
        logger.info("Finding element: " + locator);
        return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    // Click element
    protected void click(By locator) {
        logger.info("Clicking on element: " + locator);
        findElement(locator).click();
    }

    // Type text
    protected void type(By locator, String text) {
        logger.info("Typing '" + text + "' in element: " + locator);
        WebElement element = findElement(locator);
        element.clear();
        element.sendKeys(text);
    }

    // Get text
    protected String getText(By locator) {
        logger.info("Getting text from element: " + locator);
        return findElement(locator).getText();
    }

    // Check if element is displayed
    protected boolean isDisplayed(By locator) {
        try {
            logger.info("Checking if element is displayed: " + locator);
            return findElement(locator).isDisplayed();
        } catch (Exception e) {
            logger.error("Element not displayed: " + locator);
            return false;
        }
    }
}
```

**Why By locators instead of WebElement variables?**
- Using `By` locators finds elements fresh every time
- Prevents `StaleElementReferenceException`
- Elements are located at runtime, not during initialization
- More reliable for dynamic web pages

### Step 5: Create `BaseTest.java`

**Location:** `src/main/java/com/automation/base/BaseTest.java`

```java
package com.automation.base;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import com.automation.utils.ConfigReader;
import com.automation.utils.LoggerUtil;

import java.time.Duration;

public class BaseTest {
    protected WebDriver driver;
    protected LoggerUtil logger = new LoggerUtil(BaseTest.class);

    @BeforeMethod
    public void setUp() {
        logger.info("Starting test setup");
        String browser = ConfigReader.getProperty("browser");
        
        switch (browser.toLowerCase()) {
            case "chrome":
                WebDriverManager.chromedriver().setup();
                driver = new ChromeDriver();
                break;
            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                driver = new FirefoxDriver();
                break;
            case "edge":
                WebDriverManager.edgedriver().setup();
                driver = new EdgeDriver();
                break;
            default:
                throw new IllegalArgumentException("Browser not supported: " + browser);
        }

        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(
            Duration.ofSeconds(Integer.parseInt(ConfigReader.getProperty("implicit.wait")))
        );
        
        String url = ConfigReader.getProperty("app.url");
        logger.info("Navigating to: " + url);
        driver.get(url);
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            logger.info("Closing browser");
            driver.quit();
        }
    }
}
```

### Step 6: Create Page Classes

**Example: LoginPage.java**

**Location:** `src/main/java/com/automation/pages/LoginPage.java`

```java
package com.automation.pages;

import com.automation.base.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import io.qameta.allure.Step;

public class LoginPage extends BasePage {
    
    // Locators as By objects (NOT WebElements)
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");
    private final By loginButton = By.xpath("//button[@type='submit']");
    private final By errorMessage = By.className("error-message");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    @Step("Enter username: {username}")
    public LoginPage enterUsername(String username) {
        type(usernameField, username);
        return this;
    }

    @Step("Enter password")
    public LoginPage enterPassword(String password) {
        type(passwordField, password);
        return this;
    }

    @Step("Click login button")
    public HomePage clickLogin() {
        click(loginButton);
        return new HomePage(driver);
    }

    @Step("Get error message")
    public String getErrorMessage() {
        return getText(errorMessage);
    }

    @Step("Login with credentials: {username}")
    public HomePage login(String username, String password) {
        enterUsername(username);
        enterPassword(password);
        return clickLogin();
    }
}
```

**Example: HomePage.java**

**Location:** `src/main/java/com/automation/pages/HomePage.java`

```java
package com.automation.pages;

import com.automation.base.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import io.qameta.allure.Step;

public class HomePage extends BasePage {
    
    private final By welcomeMessage = By.className("welcome-text");
    private final By logoutButton = By.id("logout");

    public HomePage(WebDriver driver) {
        super(driver);
    }

    @Step("Verify user is logged in")
    public boolean isUserLoggedIn() {
        return isDisplayed(welcomeMessage);
    }

    @Step("Get welcome message")
    public String getWelcomeMessage() {
        return getText(welcomeMessage);
    }

    @Step("Click logout")
    public LoginPage logout() {
        click(logoutButton);
        return new LoginPage(driver);
    }
}
```

### Step 7: Create Test Class

**Location:** `src/test/java/com/automation/tests/LoginTest.java`

```java
package com.automation.tests;

import com.automation.base.BaseTest;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
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
        logger.info("Starting successful login test");
        
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.login("testuser", "testpass123");
        
        Assert.assertTrue(homePage.isUserLoggedIn(), "User should be logged in");
        logger.info("Login test passed successfully");
    }

    @Test(priority = 2)
    @Description("Verify login fails with invalid credentials")
    @Severity(SeverityLevel.NORMAL)
    public void testInvalidLogin() {
        logger.info("Starting invalid login test");
        
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterUsername("invaliduser")
                .enterPassword("wrongpass")
                .clickLogin();
        
        String errorMsg = loginPage.getErrorMessage();
        Assert.assertTrue(errorMsg.contains("Invalid"), "Error message should be displayed");
        logger.info("Invalid login test passed");
    }
}
```

---

## Phase 2: Reporting Setup (Allure)

### Step 1: Create `testng.xml`

**Location:** `src/test/resources/testng.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Automation Test Suite">
    <listeners>
        <listener class-name="io.qameta.allure.testng.AllureTestNg"/>
    </listeners>
    
    <test name="Login Tests">
        <classes>
            <class name="com.automation.tests.LoginTest"/>
        </classes>
    </test>
</suite>
```

### Step 2: Install Allure Command Line

**Windows:**
```bash
# Using Scoop
scoop install allure

# OR download from: https://github.com/allure-framework/allure2/releases
# Extract and add to PATH
```

**Mac:**
```bash
brew install allure
```

**Linux:**
```bash
# Download and extract
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Step 3: Run Tests and Generate Reports

```bash
# Clean and run tests
mvn clean test

# Generate Allure report
mvn allure:report

# OR serve report directly
mvn allure:serve
```

**allure-results** will be generated in `target/allure-results/` automatically!

---

## Phase 3: Logger Setup

### Step 1: Create `log4j2.xml`

**Location:** `src/main/resources/log4j2.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Properties>
        <Property name="logPath">target/logs</Property>
        <Property name="pattern">%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n</Property>
    </Properties>

    <Appenders>
        <!-- Console Appender -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="${pattern}"/>
        </Console>

        <!-- File Appender -->
        <RollingFile name="FileAppender" 
                     fileName="${logPath}/automation.log"
                     filePattern="${logPath}/automation-%d{yyyy-MM-dd}-%i.log">
            <PatternLayout pattern="${pattern}"/>
            <Policies>
                <TimeBasedTriggeringPolicy interval="1"/>
                <SizeBasedTriggeringPolicy size="10MB"/>
            </Policies>
            <DefaultRolloverStrategy max="10"/>
        </RollingFile>
    </Appenders>

    <Loggers>
        <Root level="${sys:log.level:-info}">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="FileAppender"/>
        </Root>
        
        <Logger name="com.automation" level="debug" additivity="false">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="FileAppender"/>
        </Logger>
    </Loggers>
</Configuration>
```

### Step 2: Create `config.properties`

**Location:** `src/main/resources/config.properties`

```properties
# Browser Configuration
browser=chrome

# Application URL
app.url=https://example.com

# Timeouts (in seconds)
implicit.wait=10
explicit.wait=20
page.load.timeout=30

# Logging
log.level=info
log.path=target/logs

# Screenshots
screenshot.path=target/screenshots
capture.screenshot.on.failure=true

# Test Data
test.username=testuser
test.password=testpass123
```

### Step 3: Create `ConfigReader.java`

**Location:** `src/main/java/com/automation/utils/ConfigReader.java`

```java
package com.automation.utils;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigReader {
    private static Properties properties;
    private static final String CONFIG_PATH = "src/main/resources/config.properties";

    static {
        try {
            FileInputStream fis = new FileInputStream(CONFIG_PATH);
            properties = new Properties();
            properties.load(fis);
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException("Failed to load config.properties file");
        }
    }

    public static String getProperty(String key) {
        return properties.getProperty(key);
    }

    public static int getIntProperty(String key) {
        return Integer.parseInt(properties.getProperty(key));
    }

    public static boolean getBooleanProperty(String key) {
        return Boolean.parseBoolean(properties.getProperty(key));
    }
}
```

### Step 4: Create `LoggerUtil.java`

**Location:** `src/main/java/com/automation/utils/LoggerUtil.java`

```java
package com.automation.utils;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoggerUtil {
    private Logger logger;

    public LoggerUtil(Class<?> clazz) {
        this.logger = LogManager.getLogger(clazz);
    }

    public void info(String message) {
        logger.info(message);
    }

    public void debug(String message) {
        logger.debug(message);
    }

    public void warn(String message) {
        logger.warn(message);
    }

    public void error(String message) {
        logger.error(message);
    }

    public void error(String message, Throwable throwable) {
        logger.error(message, throwable);
    }

    public void fatal(String message) {
        logger.fatal(message);
    }
}
```

---

## Phase 4: Best Practices & Practices to Avoid

### ✅ DO's (Best Practices)

1. **Use By locators, NOT WebElement variables**
   ```java
   // GOOD
   private final By loginButton = By.id("login");
   
   // BAD - Causes StaleElementReferenceException
   @FindBy(id = "login")
   private WebElement loginButton;
   ```

2. **Return Page Objects for method chaining**
   ```java
   public LoginPage enterUsername(String username) {
       type(usernameField, username);
       return this; // Allows chaining
   }
   ```

3. **Use descriptive method names**
   ```java
   // GOOD
   public boolean isUserLoggedIn() { }
   
   // BAD
   public boolean check() { }
   ```

4. **Keep test logic in tests, NOT in page classes**
   ```java
   // GOOD - Test class
   Assert.assertTrue(homePage.isUserLoggedIn());
   
   // BAD - Page class
   Assert.assertTrue(isDisplayed(welcomeMsg)); // No assertions in pages!
   ```

5. **Use explicit waits over implicit waits**
    - Implemented in BasePage with WebDriverWait

6. **Log all actions**
   ```java
   logger.info("Clicking login button");
   ```

7. **Use @Step annotations for Allure**
   ```java
   @Step("Enter username: {username}")
   ```

8. **Externalize test data in config.properties**

9. **Use meaningful locator strategies**
    - Priority: id > name > css > xpath

10. **Separate concerns: Page classes for actions, Test classes for assertions**

### ❌ DON'Ts (Practices to Avoid)

1. **DON'T use PageFactory.initElements()**
   ```java
   // BAD - Outdated and causes issues
   PageFactory.initElements(driver, this);
   @FindBy(id = "login")
   private WebElement loginButton;
   ```

2. **DON'T store WebElement as class variables**
    - Elements become stale
    - Use By locators instead

3. **DON'T use Thread.sleep()**
   ```java
   // BAD
   Thread.sleep(5000);
   
   // GOOD
   wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
   ```

4. **DON'T hardcode values in test methods**
   ```java
   // BAD
   loginPage.login("user123", "pass456");
   
   // GOOD
   loginPage.login(ConfigReader.getProperty("test.username"), 
                   ConfigReader.getProperty("test.password"));
   ```

5. **DON'T put business logic in page classes**
    - Page classes = actions only
    - Test classes = logic + assertions

6. **DON'T repeat code - use helper methods in BasePage**

7. **DON'T mix different page actions in one test**
    - Keep tests focused and atomic

8. **DON'T ignore exceptions**
   ```java
   // BAD
   catch(Exception e) { }
   
   // GOOD
   catch(Exception e) { 
       logger.error("Error occurred", e);
       throw e;
   }
   ```

---

## Phase 5: PageFactory Issues & Solutions

### Problem with PageFactory.initElements()

**Old Approach (PROBLEMATIC):**

```java
public class LoginPage {
    WebDriver driver;
    
    @FindBy(id = "username")
    private WebElement usernameField; // Stored as variable
    
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this); // Initializes once
    }
    
    public void enterUsername(String username) {
        usernameField.sendKeys(username); // May throw StaleElementReferenceException
    }
}
```

**Issues:**
1. **StaleElementReferenceException**: Element is found once during initialization. If page refreshes or DOM changes, the reference becomes stale
2. **No dynamic element location**: Elements can't be re-located
3. **Difficult to add explicit waits**: Can't use fresh waits for each action
4. **Not suitable for dynamic SPAs**: Modern web apps update DOM frequently

### Solution: Use By Locators

**New Approach (RECOMMENDED):**

```java
public class LoginPage extends BasePage {
    
    // Store locator strategy, NOT the element
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");
    
    public LoginPage(WebDriver driver) {
        super(driver);
        // No PageFactory initialization needed!
    }
    
    public void enterUsername(String username) {
        // Element is found FRESH every time
        type(usernameField, username); // No stale exception
    }
}
```

**BasePage handles element location:**

```java
protected WebElement findElement(By locator) {
    // Fresh wait and element location every time
    return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
}
```

### Why By Locators Are Better

| Aspect | PageFactory (@FindBy) | By Locators |
|--------|----------------------|-------------|
| Element Location | Once at initialization | Every action (fresh) |
| Stale Element | Common issue | Prevented |
| Explicit Waits | Difficult to implement | Easy to implement |
| Dynamic Content | Not suitable | Perfect |
| Maintainability | Lower | Higher |
| Modern Best Practice | No | Yes |

### Example Comparison

**Scenario:** Button appears after AJAX call

```java
// PageFactory - FAILS
@FindBy(id = "submit")
private WebElement submitButton;

public void clickSubmit() {
    submitButton.click(); // Element not found or stale!
}

// By Locator - WORKS
private final By submitButton = By.id("submit");

public void clickSubmit() {
    click(submitButton); // Waits until visible, then clicks
}
```

---

## Running the Framework

### Command Line

```bash
# Run all tests
mvn clean test

# Run specific test class
mvn test -Dtest=LoginTest

# Run with specific browser
mvn test -Dbrowser=firefox

# Generate Allure report
mvn allure:serve

# View logs
cat target/logs/automation.log
```

### IDE (IntelliJ IDEA)
1. Right-click on `testng.xml`
2. Select "Run"
3. Check `target/allure-results/` after execution
4. Terminal: `mvn allure:serve` to view report

---

## Folder Structure Verification

After setup, verify this structure:

```
selenium-pom-framework/
├── src/
│   ├── main/
│   │   ├── java/com/automation/
│   │   │   ├── base/
│   │   │   │   ├── BasePage.java ✓
│   │   │   │   └── BaseTest.java ✓
│   │   │   ├── pages/
│   │   │   │   ├── LoginPage.java ✓
│   │   │   │   └── HomePage.java ✓
│   │   │   └── utils/
│   │   │       ├── ConfigReader.java ✓
│   │   │       └── LoggerUtil.java ✓
│   │   └── resources/
│   │       ├── config.properties ✓
│   │       └── log4j2.xml ✓
│   └── test/
│       ├── java/com/automation/tests/
│       │   └── LoginTest.java ✓
│       └── resources/
│           └── testng.xml ✓
├── target/
│   ├── allure-results/ (after test run)
│   └── logs/ (after test run)
└── pom.xml ✓
```

---

## Troubleshooting

### Issue 1: allure-results not in target folder
**Solution:** Check `pom.xml` maven-surefire-plugin configuration:
```xml
<systemProperties>
    <property>
        <name>allure.results.directory</name>
        <value>${project.build.directory}/allure-results</value>
    </property>
</systemProperties>
```

### Issue 2: Logger not working
**Solution:** Ensure `log4j2.xml` is in `src/main/resources/`

### Issue 3: Config properties not loading
**Solution:** Verify path in ConfigReader: `src/main/resources/config.properties`

### Issue 4: WebDriver not found
**Solution:** `mvn clean install` to download dependencies

### Issue 5: Allure command not found
**Solution:** Install Allure CLI and add to PATH

---

## Summary Checklist

- [ ] Maven project created with correct `pom.xml`
- [ ] Folder structure matches guide
- [ ] BasePage uses By locators (NOT WebElements)
- [ ] BaseTest initializes WebDriver from config
- [ ] Page classes extend BasePage
- [ ] Test classes extend BaseTest
- [ ] testng.xml includes Allure listener
- [ ] config.properties created with properties
- [ ] log4j2.xml configured
- [ ] ConfigReader and LoggerUtil implemented
- [ ] Tests run: `mvn clean test`
- [ ] allure-results generated in `target/allure-results/`
- [ ] Allure report opens: `mvn allure:serve`
- [ ] Logs created in `target/logs/`

---

## Quick Start Commands

```bash
# 1. Setup
mvn clean install

# 2. Run tests
mvn clean test

# 3. View Allure report
mvn allure:serve

# 4. Check logs
cat target/logs/automation.log
```

---

**Framework Ready! Happy Testing! 🚀**