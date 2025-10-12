# Phase 1: Basic POM Setup
## Project Initialization & Core Structure

---

## Step 1: Create Maven Project

1. Open your IDE (IntelliJ IDEA or Eclipse)
2. Click **File** → **New** → **Project**
3. Select **Maven** project
4. Enter details:
    - **GroupId**: `com.automation`
    - **ArtifactId**: `selenium-pom-framework`
    - **Version**: `1.0-SNAPSHOT`
5. Click **Finish**

---

## Step 2: Configure `pom.xml`

Replace the content of `pom.xml` with:

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
    </properties>

    <dependencies>
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
</project>
```

**Save and run:**
```bash
mvn clean install
```

---

## Step 3: Create Folder Structure

Create these folders manually in your project:

```
selenium-pom-framework/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/automation/
│   │   │       ├── base/
│   │   │       ├── pages/
│   │   │       └── utils/
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/automation/tests/
│       └── resources/
└── pom.xml
```

**How to create folders:**
- Right-click on `src/main/java` → **New** → **Package**
- Enter: `com.automation.base`
- Repeat for `com.automation.pages` and `com.automation.utils`
- Do the same for `src/test/java` → create `com.automation.tests`

---

## Step 4: Create `BasePage.java`

**Location:** `src/main/java/com/automation/base/BasePage.java`

Right-click on `base` package → **New** → **Java Class** → Name it `BasePage`

```java
package com.automation.base;

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

    // Find element with explicit wait
    protected WebElement findElement(By locator) {
        return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    // Click element
    protected void click(By locator) {
        findElement(locator).click();
    }

    // Type text
    protected void type(By locator, String text) {
        WebElement element = findElement(locator);
        element.clear();
        element.sendKeys(text);
    }

    // Get text
    protected String getText(By locator) {
        return findElement(locator).getText();
    }

    // Check if element is displayed
    protected boolean isDisplayed(By locator) {
        try {
            return findElement(locator).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}
```

**Why use By locators?**
- Elements are found fresh every time
- No `StaleElementReferenceException`
- Better for dynamic web pages

---

## Step 5: Create `BaseTest.java`

**Location:** `src/main/java/com/automation/base/BaseTest.java`

```java
package com.automation.base;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

import java.time.Duration;

public class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    public void setUp() {
        // Setup WebDriver
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        
        // Maximize window
        driver.manage().window().maximize();
        
        // Set implicit wait
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        
        // Navigate to application
        driver.get("https://example.com");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
```

---

## Step 6: Create Page Classes

### LoginPage.java

**Location:** `src/main/java/com/automation/pages/LoginPage.java`

```java
package com.automation.pages;

import com.automation.base.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {
    
    // Locators stored as By objects (NOT WebElements)
    private final By usernameField = By.id("username");
    private final By passwordField = By.id("password");
    private final By loginButton = By.xpath("//button[@type='submit']");
    private final By errorMessage = By.className("error-message");

    // Constructor
    public LoginPage(WebDriver driver) {
        super(driver);
    }

    // Page actions
    public LoginPage enterUsername(String username) {
        type(usernameField, username);
        return this;
    }

    public LoginPage enterPassword(String password) {
        type(passwordField, password);
        return this;
    }

    public HomePage clickLogin() {
        click(loginButton);
        return new HomePage(driver);
    }

    public String getErrorMessage() {
        return getText(errorMessage);
    }

    // Combined action
    public HomePage login(String username, String password) {
        enterUsername(username);
        enterPassword(password);
        return clickLogin();
    }
}
```

### HomePage.java

**Location:** `src/main/java/com/automation/pages/HomePage.java`

```java
package com.automation.pages;

import com.automation.base.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage extends BasePage {
    
    // Locators
    private final By welcomeMessage = By.className("welcome-text");
    private final By logoutButton = By.id("logout");

    // Constructor
    public HomePage(WebDriver driver) {
        super(driver);
    }

    // Page actions
    public boolean isUserLoggedIn() {
        return isDisplayed(welcomeMessage);
    }

    public String getWelcomeMessage() {
        return getText(welcomeMessage);
    }

    public LoginPage logout() {
        click(logoutButton);
        return new LoginPage(driver);
    }
}
```

---

## Step 7: Create Test Class

**Location:** `src/test/java/com/automation/tests/LoginTest.java`

```java
package com.automation.tests;

import com.automation.base.BaseTest;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test(priority = 1)
    public void testSuccessfulLogin() {
        // Create LoginPage object
        LoginPage loginPage = new LoginPage(driver);
        
        // Perform login
        HomePage homePage = loginPage.login("testuser", "testpass123");
        
        // Verify login successful
        Assert.assertTrue(homePage.isUserLoggedIn(), "User should be logged in");
    }

    @Test(priority = 2)
    public void testInvalidLogin() {
        // Create LoginPage object
        LoginPage loginPage = new LoginPage(driver);
        
        // Try login with invalid credentials
        loginPage.enterUsername("invaliduser")
                .enterPassword("wrongpass")
                .clickLogin();
        
        // Verify error message displayed
        String errorMsg = loginPage.getErrorMessage();
        Assert.assertTrue(errorMsg.contains("Invalid"), "Error message should appear");
    }
}
```

---

## Step 8: Create `testng.xml`

**Location:** `src/test/resources/testng.xml`

Right-click on `src/test/resources` → **New** → **File** → Name: `testng.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Automation Test Suite">
    <test name="Login Tests">
        <classes>
            <class name="com.automation.tests.LoginTest"/>
        </classes>
    </test>
</suite>
```

---

## Step 9: Run Tests

### Option 1: Using Maven
```bash
mvn clean test
```

### Option 2: Using IDE
1. Right-click on `testng.xml`
2. Select **Run**

---

## Verification Checklist

After setup, verify:

- ✅ `pom.xml` configured correctly
- ✅ All folders created
- ✅ `BasePage.java` created in `base` package
- ✅ `BaseTest.java` created in `base` package
- ✅ `LoginPage.java` created in `pages` package
- ✅ `HomePage.java` created in `pages` package
- ✅ `LoginTest.java` created in `tests` package
- ✅ `testng.xml` created in `src/test/resources`
- ✅ Tests run successfully

---

## Common Issues & Solutions

### Issue 1: Package does not exist
**Solution:** Run `mvn clean install` to download dependencies

### Issue 2: Cannot resolve symbol
**Solution:**
- Refresh Maven project
- IntelliJ: Right-click on project → **Maven** → **Reload Project**
- Eclipse: Right-click on project → **Maven** → **Update Project**

### Issue 3: WebDriver not found
**Solution:** Ensure `webdrivermanager` dependency is in `pom.xml`

---

## Next Steps

✅ **Phase 1 Complete!**

Proceed to:
- **Phase 2**: Allure Reporting Setup
- **Phase 3**: Logger Configuration
- **Phase 4**: Best Practices

---

## Quick Commands

```bash
# Build project
mvn clean install

# Run tests
mvn clean test

# Skip tests
mvn clean install -DskipTests
```

---

**Phase 1 Setup Complete! 🎉**