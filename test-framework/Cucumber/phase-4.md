# Cucumber Phase 4: Best Practices & Common Mistakes
## What to DO and What to AVOID

---

## Section 1: Feature File Best Practices

### ✅ DO: Write User-Focused Scenarios

```gherkin
# GOOD - Business language
Scenario: Customer purchases a product
  Given customer is logged in
  When customer adds "Laptop" to cart
  And customer proceeds to checkout
  Then order should be confirmed

# BAD - Technical language
Scenario: Test cart functionality
  Given driver.get("http://example.com/login")
  When click element with id "addToCart"
  And navigate to "/checkout"
  Then verify order_id is not null
```

**Why?**
- Non-technical stakeholders can read GOOD version
- BAD version is too technical and implementation-focused

---

### ✅ DO: Keep Scenarios Independent

```gherkin
# GOOD - Independent scenarios
Scenario: Add product to cart
  Given user is logged in
  When user adds "Laptop" to cart
  Then cart should show 1 item

Scenario: Remove product from cart
  Given user is logged in
  And user has "Mouse" in cart
  When user removes "Mouse" from cart
  Then cart should be empty

# BAD - Dependent scenarios
Scenario: Add product
  When user adds "Laptop" to cart
  # Leaves product in cart

Scenario: Remove product  
  # Assumes product from previous scenario exists
  When user removes "Laptop" from cart
```

---

### ❌ DON'T: Mix Multiple Features in One File

```gherkin
# BAD - Mixing login and checkout
Feature: Application Tests
  Scenario: User logs in
    ...
  
  Scenario: User checks out
    ...
  
  Scenario: User searches product
    ...

# GOOD - Separate features
Feature: Login
  Scenario: User logs in
    ...

Feature: Checkout
  Scenario: User checks out
    ...
```

---

### ✅ DO: Use Background for Common Setup

```gherkin
# GOOD - Common steps in Background
Feature: Shopping Cart

  Background:
    Given user is logged in as "testuser"
    And user is on products page

  Scenario: Add single product
    When user adds "Laptop" to cart
    Then cart shows 1 item

  Scenario: Add multiple products
    When user adds "Laptop" to cart
    And user adds "Mouse" to cart
    Then cart shows 2 items

# BAD - Repeating same steps
Scenario: Add single product
  Given user is logged in as "testuser"
  And user is on products page
  When user adds "Laptop" to cart
  
Scenario: Add multiple products
  Given user is logged in as "testuser"
  And user is on products page
  When user adds "Laptop" to cart
```

---

### ❌ DON'T: Put Too Many Steps in Background

```gherkin
# BAD - Background too complex
Background:
  Given user is logged in
  And user navigates to products
  And user filters by category "Electronics"
  And user sorts by "Price"
  And user sets page size to 20
  # Too many steps - not all scenarios need these

# GOOD - Only essential steps
Background:
  Given user is logged in
  And user is on products page
```

---

### ✅ DO: Write Declarative Steps (What, not How)

```gherkin
# GOOD - Declarative (What)
When user logs in with valid credentials
Then user should see dashboard

# BAD - Imperative (How)
When user enters "username" in field with id "user_input"
And user enters "password" in field with id "pass_input"
And user clicks button with xpath "//button[@type='submit']"
Then user should see element with class "dashboard"
```

---

### ✅ DO: Use Scenario Outline for Similar Scenarios

```gherkin
# GOOD - Using Scenario Outline
Scenario Outline: Login with different credentials
  When user logs in with "<username>" and "<password>"
  Then result should be "<result>"
  
  Examples:
    | username  | password | result  |
    | valid     | valid123 | success |
    | invalid   | wrong    | failure |
    | empty     | pass123  | failure |

# BAD - Repeating scenarios
Scenario: Login with valid user
  When user logs in with "valid" and "valid123"
  Then result should be "success"

Scenario: Login with invalid user
  When user logs in with "invalid" and "wrong"
  Then result should be "failure"
  
# ... more repetition
```

---

### ❌ DON'T: Create Scenarios That Are Too Long

```gherkin
# BAD - Too long (15+ steps)
Scenario: Complete order flow
  Given user is on homepage
  When user searches for "laptop"
  And user clicks first result
  And user views product details
  And user adds to cart
  And user goes to cart
  And user updates quantity to 2
  And user applies coupon "SAVE10"
  And user proceeds to checkout
  And user enters shipping address
  And user selects express shipping
  And user enters payment details
  And user places order
  And user receives confirmation
  Then order should be successful
  # Too many steps - hard to maintain

# GOOD - Split into focused scenarios
Scenario: Add product to cart
  # 3-5 steps

Scenario: Apply coupon
  # 3-5 steps

Scenario: Complete checkout
  # 3-5 steps
```

**Rule of Thumb:** Keep scenarios under 10 steps

---

## Section 2: Step Definition Best Practices

### ✅ DO: Keep Step Definitions Reusable

```java
// GOOD - Reusable
@When("user enters {string} in {string} field")
public void enterTextInField(String text, String fieldName) {
    // Can be used for any field
    page.enterText(fieldName, text);
}

// Usage in multiple scenarios:
// When user enters "John" in "firstName" field
// When user enters "test@test.com" in "email" field

// BAD - Too specific
@When("user enters John in first name field")
public void enterJohnInFirstName() {
    page.enterText("firstName", "John");
}
```

---

### ✅ DO: Use Page Object Pattern

```java
// GOOD - Using Page Objects
@When("user logs in with {string} and {string}")
public void userLogsIn(String username, String password) {
    LoginPage loginPage = context.getLoginPage();
    loginPage.enterUsername(username);
    loginPage.enterPassword(password);
    loginPage.clickLogin();
}

// BAD - Direct WebDriver calls
@When("user logs in with {string} and {string}")
public void userLogsIn(String username, String password) {
    driver.findElement(By.id("username")).sendKeys(username);
    driver.findElement(By.id("password")).sendKeys(password);
    driver.findElement(By.id("login")).click();
}
```

---

### ❌ DON'T: Put Business Logic in Step Definitions

```java
// BAD - Business logic in step
@Then("user should see correct discount")
public void verifyDiscount() {
    double price = productPage.getPrice();
    double discount = 0.10; // 10% discount
    double expectedPrice = price - (price * discount);
    double actualPrice = cartPage.getTotalPrice();
    Assert.assertEquals(actualPrice, expectedPrice);
}

// GOOD - Logic in helper class
@Then("user should see correct discount")
public void verifyDiscount() {
    PriceCalculator calculator = new PriceCalculator();
    double expected = calculator.calculateDiscountedPrice();
    double actual = cartPage.getTotalPrice();
    Assert.assertEquals(actual, expected);
}
```

---

### ✅ DO: Use Meaningful Assertions

```java
// GOOD - Clear assertion messages
@Then("user should be logged in")
public void verifyUserLoggedIn() {
    boolean isLoggedIn = homePage.isWelcomeMessageDisplayed();
    Assert.assertTrue(isLoggedIn, 
        "User should be logged in - Welcome message not displayed");
}

// BAD - No assertion message
@Then("user should be logged in")
public void verifyUserLoggedIn() {
    Assert.assertTrue(homePage.isWelcomeMessageDisplayed());
    // If fails, no clear reason why
}
```

---

### ❌ DON'T: Hardcode Test Data in Step Definitions

```java
// BAD - Hardcoded data
@Given("user is logged in")
public void userLoggedIn() {
    loginPage.login("hardcodeduser", "hardcodedpass");
}

// GOOD - Data from config or parameters
@Given("user is logged in")
public void userLoggedIn() {
    String username = ConfigReader.getProperty("test.username");
    String password = ConfigReader.getProperty("test.password");
    loginPage.login(username, password);
}

// BETTER - Parameterized
@Given("user {string} is logged in")
public void specificUserLoggedIn(String username) {
    String password = ConfigReader.getProperty("test.password");
    loginPage.login(username, password);
}
```

---

### ✅ DO: Handle Waits Properly

```java
// GOOD - Explicit waits in Page Objects
public class LoginPage extends BasePage {
    public void clickLogin() {
        waitForElementToBeClickable(loginButton);
        click(loginButton);
    }
}

// BAD - Thread.sleep in step definitions
@When("user clicks login")
public void clickLogin() throws InterruptedException {
    loginPage.clickLogin();
    Thread.sleep(3000);  // BAD!
}
```

---

## Section 3: Tagging Best Practices

### ✅ DO: Use Consistent Tag Naming

```gherkin
# GOOD - Consistent naming convention
@smoke
@regression
@login-feature
@high-priority
@api-test

# BAD - Inconsistent naming
@Smoke
@REGRESSION
@Login_Feature
@HighPriority
@ApiTest
```

---

### ✅ DO: Organize Tags by Purpose

```gherkin
# Test Type Tags
@smoke
@regression
@sanity

# Feature Tags
@login
@checkout
@search

# Priority Tags
@critical
@high
@medium

# Layer Tags
@ui
@api
@database

# Example: Combine tags
@smoke @login @critical
Scenario: Admin login
```

---

### ❌ DON'T: Overuse Tags

```gherkin
# BAD - Too many tags
@smoke @regression @sanity @ui @login @high @critical @fast @important @stable
Scenario: User login
  # Hard to manage and understand

# GOOD - Essential tags only
@smoke @login @critical
Scenario: User login
  # Clear and manageable
```

---

## Section 4: Data Management

### ✅ DO: Use External Data Sources

```gherkin
# GOOD - Data from Examples table
Scenario Outline: Login with different users
  When user logs in with "<username>" and "<password>"
  Then result should be "<result>"
  
  Examples:
    | username | password | result  |
    | user1    | pass1    | success |
    | user2    | pass2    | failure |

# BETTER - Data from external file (if many rows)
# Use Excel/CSV with DataProvider
```

---

### ✅ DO: Use Data Tables for Structured Data

```gherkin
# GOOD - Using Data Table
Scenario: Register new user
  When user registers with details
    | firstName | lastName | email          | phone      |
    | John      | Doe      | john@test.com  | 1234567890 |
  Then registration should be successful

# BAD - Multiple parameters
Scenario: Register new user
  When user registers with "John" "Doe" "john@test.com" "1234567890"
  # Hard to read and maintain
```

---

### ❌ DON'T: Store Sensitive Data in Feature Files

```gherkin
# BAD - Passwords visible
Scenario: Admin login
  When user logs in with "admin" and "SuperSecret123!"
  # Password exposed in version control

# GOOD - Reference from config
Scenario: Admin login
  When admin user logs in
  # Step definition reads from config/vault
```

---

## Section 5: Hook Management

### ✅ DO: Use Hook Order Appropriately

```java
// GOOD - Proper ordering
@Before(order = 1)
public void globalSetup() {
    // Initialize framework
}

@Before(order = 2)
public void browserSetup() {
    // Start browser
}

@After(order = 1)
public void takeScreenshot() {
    // Screenshot before closing browser
}

@After(order = 2)
public void closeBrowser() {
    // Close browser
}
```

---

### ✅ DO: Use Tagged Hooks for Specific Scenarios

```java
// GOOD - Tagged hooks
@Before("@database")
public void setupDatabase() {
    // Only runs for @database scenarios
}

@After("@database")
public void cleanDatabase() {
    // Only runs for @database scenarios
}

@Before("@api")
public void setupAPI() {
    // Only runs for @api scenarios
}
```

---

### ❌ DON'T: Put Test Logic in Hooks

```java
// BAD - Test logic in hooks
@Before
public void setUp() {
    driver = new ChromeDriver();
    driver.get("https://example.com");
    loginPage.login("user", "pass");  // BAD - This is test logic
}

// GOOD - Only setup in hooks
@Before
public void setUp() {
    driver = new ChromeDriver();
    // Navigation and login should be in Given steps
}
```

---

## Section 6: Reporting Best Practices

### ✅ DO: Attach Screenshots on Failure

```java
@After
public void tearDown(Scenario scenario) {
    if (scenario.isFailed()) {
        byte[] screenshot = ((TakesScreenshot) driver)
            .getScreenshotAs(OutputType.BYTES);
        scenario.attach(screenshot, "image/png", "Failure Screenshot");
    }
}
```

---

### ✅ DO: Add Contextual Information to Reports

```java
@Step("User logs in with username: {0}")
@When("user logs in with {string} and {string}")
public void userLogsIn(String username, String password) {
    Allure.addAttachment("Username", username);
    Allure.addAttachment("Login URL", driver.getCurrentUrl());
    
    loginPage.enterUsername(username);
    loginPage.enterPassword(password);
    loginPage.clickLogin();
}
```

---

### ❌ DON'T: Log Sensitive Information

```java
// BAD - Logging password
@When("user logs in with {string} and {string}")
public void userLogsIn(String username, String password) {
    System.out.println("Password: " + password);  // BAD!
    Allure.addAttachment("Password", password);   // BAD!
    loginPage.login(username, password);
}

// GOOD - Don't log sensitive data
@When("user logs in with {string} and {string}")
public void userLogsIn(String username, String password) {
    System.out.println("Logging in as: " + username);
    Allure.addAttachment("Username", username);
    loginPage.login(username, password);
}
```

---

## Section 7: Performance Best Practices

### ✅ DO: Use Parallel Execution When Possible

```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"com.automation.stepdefinitions"},
    tags = "@regression"
)
public class TestRunner extends AbstractTestNGCucumberTests {
    
    @Override
    @DataProvider(parallel = true)
    public Object[][] scenarios() {
        return super.scenarios();
    }
}
```

**testng.xml:**
```xml
<suite name="Parallel Suite" parallel="methods" thread-count="3">
    <test name="Tests">
        <classes>
            <class name="com.automation.runners.TestRunner"/>
        </classes>
    </test>
</suite>
```

---

### ❌ DON'T: Share State Between Scenarios (in Parallel)

```java
// BAD - Static shared state
public class StepDefinitions {
    private static String sharedUsername;  // BAD in parallel execution
    
    @Given("user logs in")
    public void login() {
        sharedUsername = "testuser";  // Race condition!
    }
}

// GOOD - Use context/dependency injection
public class StepDefinitions {
    private TestContext context;
    
    public StepDefinitions(TestContext context) {
        this.context = context;  // Each scenario gets own instance
    }
    
    @Given("user logs in")
    public void login() {
        context.setUsername("testuser");  // Thread-safe
    }
}
```

---

## Section 8: Maintenance Best Practices

### ✅ DO: Keep Step Definitions DRY (Don't Repeat Yourself)

```java
// GOOD - Reusable method
@When("user enters {string} in {string} field")
public void enterTextInField(String text, String fieldName) {
    page.enterText(fieldName, text);
}

// Can be used multiple times:
// When user enters "John" in "firstName" field
// When user enters "Doe" in "lastName" field
// When user enters "john@test.com" in "email" field

// BAD - Separate methods for each field
@When("user enters first name {string}")
public void enterFirstName(String name) {
    page.enterFirstName(name);
}

@When("user enters last name {string}")
public void enterLastName(String name) {
    page.enterLastName(name);
}
// ... More repetition
```

---

### ✅ DO: Use Regular Expressions Wisely

```java
// GOOD - Simple and readable
@When("user adds {int} items to cart")
public void addItems(int count) {
    cartPage.addItems(count);
}

// AVOID - Complex regex when not needed
@When("^user adds (\\d+) items? to (?:cart|basket)$")
public void addItems(int count) {
    // Overly complex for simple case
}
```

---

### ✅ DO: Document Complex Step Definitions

```java
/**
 * Verifies that the user's cart contains the expected items with correct quantities.
 * This step performs the following validations:
 * 1. Checks total item count
 * 2. Verifies individual product quantities
 * 3. Validates total price calculation
 * 
 * @param expectedItems DataTable containing product names and quantities
 */
@Then("cart should contain following items")
public void verifyCartItems(DataTable expectedItems) {
    // Implementation
}
```

---

## Section 9: Common Mistakes to Avoid

### ❌ Mistake 1: Writing Technical Scenarios

```gherkin
# BAD - Too technical
Scenario: Test login API
  Given POST request to "/api/login"
  When send JSON payload with username and password
  Then response code should be 200
  And verify JWT token in response

# GOOD - Business focused
Scenario: User logs in successfully
  Given user has valid credentials
  When user attempts to login
  Then user should be authenticated
  And user should access their dashboard
```

---

### ❌ Mistake 2: Testing Through UI When Not Needed

```gherkin
# BAD - Unnecessary UI steps for data setup
Scenario: User creates order
  Given user logs in through UI
  And user navigates to products through UI
  And user adds product through UI
  And user proceeds to checkout through UI
  When user completes payment through UI
  Then order should be created

# GOOD - API for setup, UI for test
Scenario: User views order details
  Given user has an existing order via API
  When user navigates to order history
  Then user should see order details
```

---

### ❌ Mistake 3: Coupling Tests to Implementation

```gherkin
# BAD - Coupled to implementation
Scenario: Update profile
  When user clicks element with id "profile_edit"
  And user enters "John" in field with xpath "//input[@name='firstName']"
  And user clicks button with class "save-btn"
  
# GOOD - Independent of implementation
Scenario: Update profile
  When user edits their profile
  And user enters "John" as first name
  And user saves changes
```

---

### ❌ Mistake 4: Not Using Background Properly

```gherkin
# BAD - Repeating login in every scenario
Scenario: View products
  Given user logs in
  When user views products
  
Scenario: Add to cart
  Given user logs in
  When user adds product to cart

# GOOD - Using Background
Feature: Shopping

  Background:
    Given user is logged in
  
  Scenario: View products
    When user views products
  
  Scenario: Add to cart
    When user adds product to cart
```

---

### ❌ Mistake 5: Creating God Step Definitions

```java
// BAD - One step does everything
@When("user completes entire order flow")
public void completeOrder() {
    loginPage.login();
    productPage.selectProduct();
    productPage.addToCart();
    cartPage.proceedToCheckout();
    checkoutPage.enterDetails();
    checkoutPage.makePayment();
    // Too much in one step!
}

// GOOD - Separate focused steps
@When("user logs in")
public void login() { }

@When("user adds product to cart")
public void addToCart() { }

@When("user proceeds to checkout")
public void checkout() { }

@When("user completes payment")
public void payment() { }
```

---

### ❌ Mistake 6: Ignoring Cucumber Dry Run

```java
// DON'T skip dry run during development
@CucumberOptions(
    dryRun = false  // Always false in committed code
)

// DO use dry run to check step definitions
@CucumberOptions(
    dryRun = true  // Temporarily set to true to verify steps
)
```

---

### ❌ Mistake 7: Not Cleaning Up Test Data

```java
// BAD - Leaving test data
@After
public void tearDown(Scenario scenario) {
    driver.quit();
    // Forgot to clean test data!
}

// GOOD - Cleanup test data
@After
public void tearDown(Scenario scenario) {
    if (scenario.getSourceTagNames().contains("@database")) {
        DatabaseHelper.cleanTestData();
    }
    driver.quit();
}
```

---

## Section 10: Anti-Patterns Summary

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Technical scenarios | Not readable by business | Use business language |
| Scenario coupling | Tests depend on each other | Make independent |
| No Page Objects | WebDriver code everywhere | Use Page Object Pattern |
| Hardcoded data | Not reusable | Externalize data |
| Long scenarios | Hard to maintain | Split into smaller scenarios |
| No tags | Can't filter tests | Use organized tagging |
| Missing waits | Flaky tests | Use explicit waits |
| Logging passwords | Security risk | Never log sensitive data |
| Shared state | Parallel execution fails | Use dependency injection |
| God steps | Low reusability | Create focused steps |

---

## Section 11: BDD Best Practices Summary

### The Three Amigos Rule

**Who:** Product Owner + Developer + Tester
**When:** Before implementation
**What:** Discuss and write scenarios together

```gherkin
# Result of Three Amigos discussion:
Feature: User Registration
  
  Scenario: Successful registration
    Given user is on registration page
    When user enters valid details
    And user submits registration form
    Then user account should be created
    And welcome email should be sent
    
  # Everyone agrees on this behavior
```

---

### Given-When-Then Structure

**Given:** Setup/Precondition (Arrange)
**When:** Action (Act)
**Then:** Verification (Assert)

```gherkin
# GOOD - Clear structure
Scenario: Add product to cart
  Given user is logged in                    # Setup
  And user is on products page              # Setup
  When user adds "Laptop" to cart           # Action
  Then cart should show 1 item              # Verify
  And product price should be displayed     # Verify

# BAD - Mixed up
Scenario: Confusing flow
  When user is logged in                    # Should be Given
  Then user views products                  # Should be When
  Given user adds to cart                   # Should be When
```

---

### Living Documentation Principle

Scenarios should:
1. Be readable by all stakeholders
2. Describe behavior, not implementation
3. Serve as current documentation
4. Drive development (TDD/BDD)

```gherkin
# GOOD - Living documentation
Feature: Password Reset
  As a user who forgot password
  I want to reset my password
  So that I can access my account again

  Scenario: Request password reset
    Given user is on login page
    When user clicks "Forgot Password"
    And user enters registered email
    Then password reset email should be sent
    And user should see confirmation message
```

---

## Section 12: Checklist for Review

### Before Committing Feature Files

- [ ] Scenarios use business language, not technical
- [ ] Each scenario is independent
- [ ] Scenarios follow Given-When-Then structure
- [ ] Background used for common setup
- [ ] Tags are consistent and meaningful
- [ ] No hardcoded sensitive data
- [ ] Scenarios are concise (under 10 steps)
- [ ] Step descriptions are clear
- [ ] No coupling between scenarios

### Before Committing Step Definitions

- [ ] Step definitions are reusable
- [ ] Using Page Object Pattern
- [ ] No WebDriver code in steps
- [ ] Proper waits implemented
- [ ] Meaningful assertion messages
- [ ] No hardcoded test data
- [ ] Exception handling present
- [ ] No sensitive data logged
- [ ] Documentation for complex steps

### General Project Health

- [ ] Tests run successfully
- [ ] Parallel execution works
- [ ] Reports generate correctly
- [ ] Screenshots captured on failure
- [ ] No flaky tests
- [ ] Execution time reasonable
- [ ] Test data cleanup working
- [ ] CI/CD integration functional

---

## Section 13: Real-World Examples

### Example 1: E-commerce Complete Flow

**GOOD Implementation:**

**Feature File:**
```gherkin
@regression @ecommerce
Feature: E-commerce Shopping Flow

  Background:
    Given user "john@test.com" is logged in
    And user is on products page

  @smoke @critical
  Scenario: Complete purchase flow
    When user searches for "Laptop"
    And user adds first product to cart
    And user proceeds to checkout
    And user enters shipping address
    And user completes payment with valid card
    Then order should be confirmed
    And confirmation email should be sent

  @data-driven
  Scenario Outline: Purchase with different payment methods
    When user adds "Mouse" to cart
    And user proceeds to checkout
    And user pays with "<paymentMethod>"
    Then order should be "<status>"

    Examples:
      | paymentMethod | status    |
      | Credit Card   | confirmed |
      | PayPal        | confirmed |
      | Invalid Card  | failed    |
```

**Step Definitions:**
```java
@Epic("E-commerce")
@Feature("Shopping Flow")
public class ShoppingSteps {
    private TestContext context;
    
    public ShoppingSteps(TestContext context) {
        this.context = context;
    }

    @Step("User searches for: {0}")
    @When("user searches for {string}")
    public void searchProduct(String productName) {
        ProductPage productPage = context.getProductPage();
        productPage.searchFor(productName);
        Allure.addAttachment("Search Term", productName);
    }

    @Step("Add first product to cart")
    @When("user adds first product to cart")
    public void addFirstProductToCart() {
        ProductPage productPage = context.getProductPage();
        String productName = productPage.getFirstProductName();
        productPage.addFirstProductToCart();
        
        context.setSelectedProduct(productName);
        Allure.addAttachment("Product Added", productName);
    }

    @Step("Proceed to checkout")
    @When("user proceeds to checkout")
    public void proceedToCheckout() {
        CartPage cartPage = context.getCartPage();
        cartPage.clickCheckout();
    }

    @Step("Enter shipping address")
    @When("user enters shipping address")
    public void enterShippingAddress() {
        CheckoutPage checkoutPage = context.getCheckoutPage();
        Address address = TestDataFactory.getDefaultAddress();
        checkoutPage.enterShippingAddress(address);
    }

    @Step("Complete payment")
    @When("user completes payment with valid card")
    public void completePayment() {
        PaymentPage paymentPage = context.getPaymentPage();
        CreditCard card = TestDataFactory.getValidCard();
        paymentPage.enterCardDetails(card);
        paymentPage.submitPayment();
    }

    @Step("Verify order confirmation")
    @Then("order should be confirmed")
    public void verifyOrderConfirmation() {
        ConfirmationPage confirmationPage = context.getConfirmationPage();
        String orderId = confirmationPage.getOrderId();
        
        Assert.assertNotNull(orderId, "Order ID should be generated");
        Assert.assertTrue(confirmationPage.isConfirmationDisplayed(),
            "Order confirmation should be displayed");
        
        context.setOrderId(orderId);
        Allure.addAttachment("Order ID", orderId);
    }

    @Step("Verify confirmation email")
    @Then("confirmation email should be sent")
    public void verifyConfirmationEmail() {
        String email = context.getCurrentUser().getEmail();
        EmailHelper emailHelper = new EmailHelper();
        
        boolean emailReceived = emailHelper.waitForEmail(email, 
            "Order Confirmation", 30);
        
        Assert.assertTrue(emailReceived, 
            "Confirmation email should be received");
    }
}
```

---

### Example 2: API + UI Combined Test

**Feature File:**
```gherkin
@api-ui-integration
Feature: Order Management

  @smoke
  Scenario: View order created via API
    Given order is created via API with following details
      | productName | quantity | price |
      | Laptop      | 1        | 999   |
    When user logs in and navigates to order history
    Then user should see the order in history
    And order details should match API data

  Scenario: Cancel order through UI
    Given user has an active order via API
    When user cancels the order through UI
    Then order status should be "Cancelled" in database
    And refund should be initiated
```

**Step Definitions:**
```java
public class OrderSteps {
    private TestContext context;
    private APIHelper apiHelper;
    
    public OrderSteps(TestContext context) {
        this.context = context;
        this.apiHelper = new APIHelper();
    }

    @Given("order is created via API with following details")
    public void createOrderViaAPI(DataTable dataTable) {
        List<Map<String, String>> items = dataTable.asMaps();
        
        OrderRequest orderRequest = OrderRequest.builder()
            .userId(context.getCurrentUser().getId())
            .items(items)
            .build();
        
        Response response = apiHelper.createOrder(orderRequest);
        Assert.assertEquals(response.getStatusCode(), 201);
        
        String orderId = response.jsonPath().getString("orderId");
        context.setOrderId(orderId);
        
        Allure.addAttachment("API Response", 
            response.getBody().asString());
    }

    @When("user logs in and navigates to order history")
    public void navigateToOrderHistory() {
        LoginPage loginPage = context.getLoginPage();
        loginPage.login(context.getCurrentUser().getEmail(), "password");
        
        HomePage homePage = context.getHomePage();
        homePage.clickOrderHistory();
    }

    @Then("user should see the order in history")
    public void verifyOrderInHistory() {
        OrderHistoryPage orderHistoryPage = context.getOrderHistoryPage();
        String expectedOrderId = context.getOrderId();
        
        boolean orderExists = orderHistoryPage.isOrderDisplayed(expectedOrderId);
        Assert.assertTrue(orderExists, 
            "Order " + expectedOrderId + " should be visible in history");
    }
}
```

---

## Final Best Practices Summary

### Golden Rules

1. **Write for humans first** - Scenarios should be readable by non-technical people
2. **Keep it simple** - Each scenario should test one thing
3. **Make tests independent** - No dependencies between scenarios
4. **Use layers properly** - Feature → Steps → Pages → WebDriver
5. **Don't repeat yourself** - Reuse steps and methods
6. **Tag strategically** - Organize tests for easy filtering
7. **Handle data wisely** - External, encrypted, or generated
8. **Wait intelligently** - Explicit waits, never Thread.sleep()
9. **Report clearly** - Screenshots, logs, and context
10. **Maintain continuously** - Refactor and update regularly

---

## Quick Reference Card

### DO's
✅ Write user-focused scenarios
✅ Use Page Object Pattern
✅ Keep scenarios independent
✅ Use Background for common steps
✅ Tag scenarios consistently
✅ Use Scenario Outline for data
✅ Handle waits properly
✅ Take screenshots on failure
✅ Use dependency injection
✅ Document complex logic

### DON'Ts
❌ Write technical scenarios
❌ Put WebDriver in step definitions
❌ Create dependent scenarios
❌ Repeat steps across scenarios
❌ Use random tagging
❌ Hardcode test data
❌ Use Thread.sleep()
❌ Ignore failures
❌ Share state in parallel tests
❌ Log sensitive data

---

## Next Steps

✅ **All Cucumber Phases Complete!**

You now have:
- Phase 1: Basic Setup ✓
- Phase 2: Allure Reporting ✓
- Phase 3: Advanced Features ✓
- Phase 4: Best Practices ✓

**Your Cucumber framework is production-ready! 🥒🚀**

---

**Best Practices Guide Complete! Happy BDD Testing! ✨**