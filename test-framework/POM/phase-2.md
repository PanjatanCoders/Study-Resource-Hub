# Phase 2: Allure Reporting Setup
## Configure Allure Reports in target/allure-results

---

## Prerequisites

✅ Phase 1 completed (Basic POM setup done)

---

## Step 1: Add Allure Dependencies to `pom.xml`

Open your `pom.xml` and add these dependencies inside `<dependencies>` section:

```xml
<!-- Allure TestNG -->
<dependency>
    <groupId>io.qameta.allure</groupId>
    <artifactId>allure-testng</artifactId>
    <version>2.24.0</version>
</dependency>
```

Add this property in `<properties>` section:

```xml
<allure.version>2.24.0</allure.version>
<aspectj.version>1.9.20</aspectj.version>
```

---

## Step 2: Configure Maven Surefire Plugin

Add this plugin configuration in `<build>` → `<plugins>` section of `pom.xml`:

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
                    <suiteXmlFile>src/test/resources/testng.xml</suiteXmlFile>
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

**Save file and run:**
```bash
mvn clean install
```

---

## Step 3: Update `testng.xml` with Allure Listener

Open `src/test/resources/testng.xml` and add listener:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Automation Test Suite">
    
    <!-- Add Allure Listener -->
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

---

## Step 4: Add Allure Annotations to Tests

Update your `LoginTest.java` with Allure annotations:

```java
package com.automation.tests;

import com.automation.base.BaseTest;
import com.automation.pages.HomePage;
import com.automation.pages.LoginPage;
import io.qameta.allure.Description;
import io.qameta.allure.Severity;
import io.qameta.allure.SeverityLevel;
import io.qameta.allure.Step;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test(priority = 1)
    @Description("Verify user can login with valid credentials")
    @Severity(SeverityLevel.CRITICAL)
    public void testSuccessfulLogin() {
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.login("testuser", "testpass123");
        Assert.assertTrue(homePage.isUserLoggedIn(), "User should be logged in");
    }

    @Test(priority = 2)
    @Description("Verify login fails with invalid credentials")
    @Severity(SeverityLevel.NORMAL)
    public void testInvalidLogin() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterUsername("invaliduser")
                .enterPassword("wrongpass")
                .clickLogin();
        
        String errorMsg = loginPage.getErrorMessage();
        Assert.assertTrue(errorMsg.contains("Invalid"), "Error message should be displayed");
    }
}
```

---

## Step 5: Add @Step Annotations to Page Classes

Update `LoginPage.java`:

```java
package com.automation.pages;

import com.automation.base.BasePage;
import io.qameta.allure.Step;
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

Update `HomePage.java`:

```java
package com.automation.pages;

import com.automation.base.BasePage;
import io.qameta.allure.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

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

---

## Step 6: Install Allure Command Line

### Windows (Using Scoop)
```bash
# Install Scoop first (if not installed)
# Visit: https://scoop.sh

# Install Allure
scoop install allure
```

### Windows (Manual)
1. Download from: https://github.com/allure-framework/allure2/releases
2. Extract to `C:\allure`
3. Add `C:\allure\bin` to System PATH

### Mac
```bash
brew install allure
```

### Linux (Ubuntu/Debian)
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

## Step 7: Run Tests and Generate Allure Reports

### Run Tests
```bash
mvn clean test
```

**This will create `target/allure-results/` folder with JSON files**

### Generate and View Report

**Option 1: Generate HTML report**
```bash
mvn allure:report
```
Report generated at: `target/site/allure-maven-plugin/index.html`

**Option 2: Serve report (Opens in browser automatically)**
```bash
mvn allure:serve
```

**Option 3: Using Allure CLI**
```bash
# Generate report
allure generate target/allure-results --clean -o target/allure-report

# Open report
allure open target/allure-report
```

---

## Understanding Allure Annotations

### @Description
Adds test description in report
```java
@Description("This test verifies login functionality")
```

### @Severity
Sets test priority/importance
```java
@Severity(SeverityLevel.CRITICAL)   // Blocker, Critical, Normal, Minor, Trivial
```

### @Step
Shows detailed steps in report
```java
@Step("Enter username: {username}")
public void enterUsername(String username) { }
```

### @Feature
Groups tests by feature
```java
@Feature("Login Module")
```

### @Story
Groups tests by user story
```java
@Story("User Authentication")
```

### Example with all annotations:
```java
@Test
@Description("Verify successful login with valid credentials")
@Severity(SeverityLevel.CRITICAL)
@Feature("Login")
@Story("User Login")
public void testLogin() {
    // Test code
}
```

---

## Verify Allure Setup

After running tests, check:

1. **Folder created:**
   ```
   target/
   └── allure-results/
       ├── xxxxxxxxx-result.json
       ├── xxxxxxxxx-container.json
       └── ... (multiple JSON files)
   ```

2. **Run report command:**
   ```bash
   mvn allure:serve
   ```

3. **Browser opens showing:**
    - Test overview
    - Test details with steps
    - Graphs and charts
    - Timeline
    - Categories

---

## Allure Report Features

### Overview Dashboard
- Total tests, passed, failed
- Success rate
- Execution time
- Severity distribution

### Suites View
- Tests grouped by test classes
- Expandable test details

### Graphs
- Status chart
- Severity chart
- Duration trend

### Timeline
- Test execution timeline
- Parallel execution visualization

### Behaviors
- Tests grouped by features/stories

---

## Troubleshooting

### Issue 1: allure-results not created in target folder

**Check pom.xml:**
```xml
<systemProperties>
    <property>
        <name>allure.results.directory</name>
        <value>${project.build.directory}/allure-results</value>
    </property>
</systemProperties>
```

### Issue 2: AspectJ weaver error

**Solution:** Add aspectj dependency in surefire plugin:
```xml
<dependencies>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjweaver</artifactId>
        <version>1.9.20</version>
    </dependency>
</dependencies>
```

### Issue 3: Allure command not found

**Solution:** Install Allure CLI and add to PATH (See Step 6)

### Issue 4: Empty allure report

**Solution:**
- Ensure tests ran: Check `target/allure-results/` has JSON files
- Run: `mvn clean test` again
- Then: `mvn allure:serve`

---

## Verification Checklist

- ✅ Allure dependencies added to `pom.xml`
- ✅ Maven Surefire plugin configured
- ✅ Allure Maven plugin configured
- ✅ Allure listener added to `testng.xml`
- ✅ @Description and @Severity added to tests
- ✅ @Step added to page methods
- ✅ Allure CLI installed
- ✅ Tests executed: `mvn clean test`
- ✅ `target/allure-results/` folder created with JSON files
- ✅ Report generated: `mvn allure:serve`
- ✅ Report opens in browser successfully

---

## Complete pom.xml Reference

Your `pom.xml` should now look like:

```xml
<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
    <selenium.version>4.15.0</selenium.version>
    <testng.version>7.8.0</testng.version>
    <allure.version>2.24.0</allure.version>
    <aspectj.version>1.9.20</aspectj.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.seleniumhq.selenium</groupId>
        <artifactId>selenium-java</artifactId>
        <version>${selenium.version}</version>
    </dependency>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>${testng.version}</version>
    </dependency>
    <dependency>
        <groupId>io.qameta.allure</groupId>
        <artifactId>allure-testng</artifactId>
        <version>${allure.version}</version>
    </dependency>
    <dependency>
        <groupId>io.github.bonigarcia</groupId>
        <artifactId>webdrivermanager</artifactId>
        <version>5.6.2</version>
    </dependency>
</dependencies>
```

---

## Quick Commands Summary

```bash
# Clean and run tests
mvn clean test

# Generate and serve report
mvn allure:serve

# Generate report only
mvn allure:report

# View existing report
allure open target/allure-report
```

---

## Next Steps

✅ **Phase 2 Complete!**

Proceed to:
- **Phase 3**: Logger Setup & Configuration

---

**Allure Reporting Setup Complete! 📊**