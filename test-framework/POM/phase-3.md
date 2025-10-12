# Phase 3: Logger Setup & Configuration
## Log4j2 Logger with config.properties Integration

---

## Prerequisites

✅ Phase 1 completed (Basic POM setup)
✅ Phase 2 completed (Allure reporting)

---

## Step 1: Add Log4j2 Dependencies

Open `pom.xml` and add these dependencies:

```xml
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
```

**Save and run:**
```bash
mvn clean install
```

---

## Step 2: Create `log4j2.xml`

**Location:** `src/main/resources/log4j2.xml`

Right-click on `src/main/resources` → **New** → **File** → Name: `log4j2.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    
    <!-- Properties -->
    <Properties>
        <Property name="logPath">target/logs</Property>
        <Property name="pattern">%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n</Property>
    </Properties>

    <!-- Appenders -->
    <Appenders>
        <!-- Console Output -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="${pattern}"/>
        </Console>

        <!-- File Output with Rolling -->
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

    <!-- Loggers -->
    <Loggers>
        <!-- Root Logger -->
        <Root level="${sys:log.level:-info}">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="FileAppender"/>
        </Root>
        
        <!-- Project Logger -->
        <Logger name="com.automation" level="debug" additivity="false">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="FileAppender"/>
        </Logger>
    </Loggers>
    
</Configuration>
```

**Explanation:**
- **Console Appender**: Prints logs to console
- **File Appender**: Saves logs to `target/logs/automation.log`
- **Rolling Policy**: Creates new file daily or when size exceeds 10MB
- **Log Levels**: debug, info, warn, error, fatal

---

## Step 3: Create `config.properties`

**Location:** `src/main/resources/config.properties`

Right-click on `src/main/resources` → **New** → **File** → Name: `config.properties`

```properties
# Browser Configuration
browser=chrome

# Application URL
app.url=https://example.com

# Timeouts (in seconds)
implicit.wait=10
explicit.wait=20
page.load.timeout=30

# Logging Configuration
log.level=info
log.path=target/logs

# Screenshot Configuration
screenshot.path=target/screenshots
capture.screenshot.on.failure=true

# Test Data
test.username=testuser
test.password=testpass123
```

---

## Step 4: Create `ConfigReader.java`

**Location:** `src/main/java/com/automation/utils/ConfigReader.java`

Right-click on `utils` package → **New** → **Java Class** → Name: `ConfigReader`

```java
package com.automation.utils;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigReader {
    private static Properties properties;
    private static final String CONFIG_PATH = "src/main/resources/config.properties";

    // Static block to load properties file once
    static {
        try {
            FileInputStream fis = new FileInputStream(CONFIG_PATH);
            properties = new Properties();
            properties.load(fis);
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException("Failed to load config.properties file at: " + CONFIG_PATH);
        }
    }

    // Get String property
    public static String getProperty(String key) {
        String value = properties.getProperty(key);
        if (value == null) {
            throw new RuntimeException("Property '" + key + "' not found in config.properties");
        }
        return value;
    }

    // Get Integer property
    public static int getIntProperty(String key) {
        return Integer.parseInt(getProperty(key));
    }

    // Get Boolean property
    public static boolean getBooleanProperty(String key) {
        return Boolean.parseBoolean(getProperty(key));
    }
}
```

---

## Step 5: Create `LoggerUtil.java`

**Location:** `src/main/java/com/automation/utils/LoggerUtil.java`

Right-click on `utils` package → **New** → **Java Class** → Name: `LoggerUtil`

```java
package com.automation.utils;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoggerUtil {
    private Logger logger;

    // Constructor - Pass the class for which logger is needed
    public LoggerUtil(Class<?> clazz) {
        this.logger = LogManager.getLogger(clazz);
    }

    // Info level log
    public void info(String message) {
        logger.info(message);
    }

    // Debug level log
    public void debug(String message) {
        logger.debug(message);
    }

    // Warning level log
    public void warn(String message) {
        logger.warn(message);
    }

    // Error level log
    public void error(String message) {
        logger.error(message);
    }

    // Error with exception
    public void error(String message, Throwable throwable) {
        logger.error(message, throwable);
    }

    // Fatal level log
    public void fatal(String message) {
        logger.fatal(message);
    }
}
```

---

## Step 6: Update `BasePage.java` with Logger

Update your `BasePage.java`:

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

---

## Step 7: Update `BaseTest.java` with Logger & ConfigReader

Update your `BaseTest.java`:

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
        logger.info("==== Starting Test Setup ====");
        
        // Read browser from config.properties
        String browser = ConfigReader.getProperty("browser");
        logger.info("Browser selected: " + browser);
        
        // Initialize WebDriver based on browser
        switch (browser.toLowerCase()) {
            case "chrome":
                WebDriverManager.chromedriver().setup();
                driver = new ChromeDriver();
                logger.info("Chrome browser launched");
                break;
                
            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                driver = new FirefoxDriver();
                logger.info("Firefox browser launched");
                break;
                
            case "edge":
                WebDriverManager.edgedriver().setup();
                driver = new EdgeDriver();
                logger.info("Edge browser launched");
                break;
                
            default:
                logger.error("Browser not supported: " + browser);
                throw new IllegalArgumentException("Browser not supported: " + browser);
        }

        // Maximize window
        driver.manage().window().maximize();
        logger.info("Browser window maximized");
        
        // Set timeouts from config
        int implicitWait = ConfigReader.getIntProperty("implicit.wait");
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(implicitWait));
        logger.info("Implicit wait set to: " + implicitWait + " seconds");
        
        // Navigate to URL from config
        String url = ConfigReader.getProperty("app.url");
        logger.info("Navigating to URL: " + url);
        driver.get(url);
        
        logger.info("==== Test Setup Complete ====");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            logger.info("==== Closing Browser ====");
            driver.quit();
            logger.info("Browser closed successfully");
        }
    }
}
```

---

## Step 8: Update Tests with Logger

Update `LoginTest.java`:

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
    @Description("Verify user can login with valid credentials")
    @Severity(SeverityLevel.CRITICAL)
    public void testSuccessfulLogin() {
        logger.info("===== Starting Test: testSuccessfulLogin =====");
        
        // Get credentials from config
        String username = ConfigReader.getProperty("test.username");
        String password = ConfigReader.getProperty("test.password");
        logger.info("Using username: " + username);
        
        // Perform login
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.login(username, password);
        
        // Verify login
        Assert.assertTrue(homePage.isUserLoggedIn(), "User should be logged in");
        logger.info("Login verification successful");
        
        logger.info("===== Test Passed: testSuccessfulLogin =====");
    }

    @Test(priority = 2)
    @Description("Verify login fails with invalid credentials")
    @Severity(SeverityLevel.NORMAL)
    public void testInvalidLogin() {
        logger.info("===== Starting Test: testInvalidLogin =====");
        
        LoginPage loginPage = new LoginPage(driver);
        logger.info("Attempting login with invalid credentials");
        
        loginPage.enterUsername("invaliduser")
                .enterPassword("wrongpass")
                .clickLogin();
        
        String errorMsg = loginPage.getErrorMessage();
        logger.info("Error message received: " + errorMsg);
        
        Assert.assertTrue(errorMsg.contains("Invalid"), "Error message should be displayed");
        logger.info("Error message validation successful");
        
        logger.info("===== Test Passed: testInvalidLogin =====");
    }
}
```

---

## Step 9: Run Tests and Check Logs

### Run Tests
```bash
mvn clean test
```

### Check Log Files

**Console Output:**
You'll see logs in console like:
```
2025-10-12 10:30:15 [main] INFO  BaseTest - ==== Starting Test Setup ====
2025-10-12 10:30:15 [main] INFO  BaseTest - Browser selected: chrome
2025-10-12 10:30:16 [main] INFO  BaseTest - Chrome browser launched
2025-10-12 10:30:16 [main] INFO  BaseTest - Browser window maximized
...
```

**File Output:**
Check file: `target/logs/automation.log`

```
2025-10-12 10:30:15 [main] INFO  BaseTest - ==== Starting Test Setup ====
2025-10-12 10:30:15 [main] INFO  BaseTest - Browser selected: chrome
2025-10-12 10:30:16 [main] INFO  BasePage - Finding element: By.id: username
2025-10-12 10:30:16 [main] INFO  BasePage - Typing 'testuser' in element: By.id: username
...
```

---

## Understanding Log Levels

### Log Level Hierarchy
```
ALL < DEBUG < INFO < WARN < ERROR < FATAL < OFF
```

### When to Use Each Level

**DEBUG**: Detailed information for debugging
```java
logger.debug("Element found at coordinates: " + x + ", " + y);
```

**INFO**: General information about application flow
```java
logger.info("User logged in successfully");
```

**WARN**: Warning messages (not errors, but potential issues)
```java
logger.warn("Element took longer than expected to load");
```

**ERROR**: Error messages (recoverable errors)
```java
logger.error("Failed to find element: " + locator);
```

**FATAL**: Critical errors (application cannot continue)
```java
logger.fatal("Database connection failed");
```

---

## Configuring Log Levels

### Option 1: In log4j2.xml
```xml
<Logger name="com.automation" level="debug" additivity="false">
```

Change `level="debug"` to:
- `debug` - Shows all logs
- `info` - Shows info, warn, error, fatal
- `warn` - Shows warn, error, fatal
- `error` - Shows error, fatal only

### Option 2: Using System Property
```bash
mvn test -Dlog.level=debug
```

### Option 3: In config.properties
```properties
log.level=info
```

Then update `log4j2.xml`:
```xml
<Root level="${sys:log.level:-info}">
```

---

## Log File Structure

### Pattern Explained
```xml
<Property name="pattern">%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n</Property>
```

**Output:**
```
2025-10-12 10:30:15 [main] INFO  BaseTest - Starting test setup
```

- `%d{yyyy-MM-dd HH:mm:ss}` - Date and time
- `[%t]` - Thread name
- `%-5level` - Log level (INFO, ERROR, etc.)
- `%logger{36}` - Logger name (class name)
- `%msg` - Actual log message
- `%n` - New line

### Customize Pattern

**Add method name:**
```xml
%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36}.%M - %msg%n
```

**Add line number:**
```xml
%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36}:%L - %msg%n
```

---

## Advanced Configuration

### Multiple Log Files

Update `log4j2.xml` to create separate files for different levels:

```xml
<Appenders>
    <!-- Info and above -->
    <RollingFile name="InfoFile" 
                 fileName="${logPath}/info.log"
                 filePattern="${logPath}/info-%d{yyyy-MM-dd}-%i.log">
        <PatternLayout pattern="${pattern}"/>
        <Policies>
            <TimeBasedTriggeringPolicy interval="1"/>
            <SizeBasedTriggeringPolicy size="10MB"/>
        </Policies>
    </RollingFile>

    <!-- Error only -->
    <RollingFile name="ErrorFile" 
                 fileName="${logPath}/error.log"
                 filePattern="${logPath}/error-%d{yyyy-MM-dd}-%i.log">
        <PatternLayout pattern="${pattern}"/>
        <ThresholdFilter level="error" onMatch="ACCEPT" onMismatch="DENY"/>
        <Policies>
            <TimeBasedTriggeringPolicy interval="1"/>
            <SizeBasedTriggeringPolicy size="10MB"/>
        </Policies>
    </RollingFile>
</Appenders>

<Loggers>
    <Logger name="com.automation" level="debug" additivity="false">
        <AppenderRef ref="Console"/>
        <AppenderRef ref="InfoFile"/>
        <AppenderRef ref="ErrorFile"/>
    </Logger>
</Loggers>
```

---

## Folder Structure After Setup

```
selenium-pom-framework/
├── src/
│   ├── main/
│   │   ├── java/com/automation/
│   │   │   ├── base/
│   │   │   │   ├── BasePage.java ✓ (with logger)
│   │   │   │   └── BaseTest.java ✓ (with logger & config)
│   │   │   ├── pages/
│   │   │   │   ├── LoginPage.java
│   │   │   │   └── HomePage.java
│   │   │   └── utils/
│   │   │       ├── ConfigReader.java ✓ NEW
│   │   │       └── LoggerUtil.java ✓ NEW
│   │   └── resources/
│   │       ├── config.properties ✓ NEW
│   │       └── log4j2.xml ✓ NEW
│   └── test/
│       └── java/com/automation/tests/
│           └── LoginTest.java ✓ (with logger)
├── target/
│   ├── allure-results/
│   └── logs/
│       └── automation.log ✓ (generated after test)
└── pom.xml
```

---

## Troubleshooting

### Issue 1: Logs not appearing

**Solution:** Check `log4j2.xml` is in `src/main/resources/`

### Issue 2: FileNotFoundException for config.properties

**Solution:** Verify path in ConfigReader:
```java
private static final String CONFIG_PATH = "src/main/resources/config.properties";
```

### Issue 3: Property not found error

**Solution:** Check property key exists in `config.properties`:
```properties
browser=chrome
app.url=https://example.com
```

### Issue 4: Logs folder not created

**Solution:** Log4j creates folder automatically. Ensure write permissions.

### Issue 5: No logs in file, only console

**Solution:** Check log4j2.xml has FileAppender configured:
```xml
<AppenderRef ref="FileAppender"/>
```

---

## Best Practices for Logging

### ✅ DO's

1. **Log at appropriate levels**
   ```java
   logger.info("User logged in");        // Good
   logger.debug("Element coordinates: x=10, y=20");  // Good
   ```

2. **Log meaningful messages**
   ```java
   logger.info("Clicking login button");  // Good
   logger.info("Click");                  // Bad - not descriptive
   ```

3. **Log important actions**
   ```java
   logger.info("Navigating to: " + url);
   logger.info("Entering username: " + username);
   ```

4. **Log exceptions**
   ```java
   try {
       // code
   } catch (Exception e) {
       logger.error("Failed to login", e);
   }
   ```

5. **Use parameterized logging**
   ```java
   logger.info("User {} logged in successfully", username);
   ```

### ❌ DON'Ts

1. **Don't log sensitive data**
   ```java
   logger.info("Password: " + password);  // BAD - Security risk
   logger.info("Credit card: " + ccNum);  // BAD
   ```

2. **Don't log everything**
   ```java
   // Too verbose
   logger.debug("Variable i = " + i);
   logger.debug("Variable j = " + j);
   ```

3. **Don't use System.out.println**
   ```java
   System.out.println("Test");  // BAD - Use logger instead
   ```

4. **Don't log in loops excessively**
   ```java
   // Bad - logs 1000 times
   for (int i = 0; i < 1000; i++) {
       logger.info("Processing item: " + i);
   }
   ```

---

## Verification Checklist

- ✅ Log4j2 dependencies added to `pom.xml`
- ✅ `log4j2.xml` created in `src/main/resources/`
- ✅ `config.properties` created in `src/main/resources/`
- ✅ `ConfigReader.java` created
- ✅ `LoggerUtil.java` created
- ✅ `BasePage.java` updated with logger
- ✅ `BaseTest.java` updated with logger and ConfigReader
- ✅ Test classes updated with logger
- ✅ Tests run: `mvn clean test`
- ✅ Logs appear in console
- ✅ Log file created: `target/logs/automation.log`
- ✅ ConfigReader reads properties correctly

---

## Quick Commands

```bash
# Run tests
mvn clean test

# Check logs
cat target/logs/automation.log

# Run with specific log level
mvn test -Dlog.level=debug

# Run with specific browser (from config)
mvn test -Dbrowser=firefox
```

---

## Next Steps

✅ **Phase 3 Complete!**

Proceed to:
- **Phase 4**: Best Practices & Common Mistakes
- **Phase 5**: PageFactory Issues & Solutions

---

**Logger Setup Complete! 📝**