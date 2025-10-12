# RestAssured API Testing Framework - Phase 1: Basic Setup

## 🎯 What You'll Learn in Phase 1
- Create a Maven project from scratch
- Add RestAssured dependencies
- Write your first API test
- Execute and verify tests
- Understand the project structure

---

## 📋 Prerequisites
- JDK 11 or higher installed
- Maven 3.6+ installed
- IDE (IntelliJ IDEA / Eclipse)
- Basic Java knowledge
- Internet connection (for downloading dependencies)

---

## 🏗️ Project Structure (Phase 1)

```
restassured-api-automation/
├── src/
│   ├── main/
│   │   └── java/
│   └── test/
│       └── java/
│           └── com/
│               └── api/
│                   └── tests/
│                       ✓ FirstAPITest.java (NEW)
├── ✓ pom.xml (NEW)
└── ✓ README.md (NEW)
```

---

## Step 1: Create Maven Project

### Option A: Using Command Line

```bash
mvn archetype:generate \
  -DgroupId=com.api.automation \
  -DartifactId=restassured-api-automation \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DarchetypeVersion=1.4 \
  -DinteractiveMode=false

cd restassured-api-automation
```

### Option B: Using IntelliJ IDEA

1. File → New → Project
2. Select "Maven" (NOT "Maven Archetype")
3. Name: `restassured-api-automation`
4. GroupId: `com.api.automation`
5. ArtifactId: `restassured-api-automation`
6. Click "Finish"

### Option C: Using Eclipse

1. File → New → Maven Project
2. Check "Create a simple project (skip archetype selection)"
3. Group Id: `com.api.automation`
4. Artifact Id: `restassured-api-automation`
5. Click "Finish"

### ✅ Verification Checkpoint
- [ ] Project created successfully
- [ ] `pom.xml` file exists in root directory
- [ ] `src/main/java` and `src/test/java` folders exist

---

## Step 2: Configure pom.xml with Dependencies

**Replace** your entire `pom.xml` content with the following:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.api.automation</groupId>
    <artifactId>restassured-api-automation</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>RestAssured API Automation</name>
    <description>API Testing Framework using RestAssured</description>

    <properties>
        <!-- Java Version -->
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>

        <!-- Dependency Versions -->
        <restassured.version>5.4.0</restassured.version>
        <testng.version>7.9.0</testng.version>
        <jackson.version>2.16.1</jackson.version>
        <maven.surefire.version>3.2.5</maven.surefire.version>
    </properties>

    <dependencies>
        <!-- RestAssured - Core API Testing Library -->
        <dependency>
            <groupId>io.rest-assured</groupId>
            <artifactId>rest-assured</artifactId>
            <version>${restassured.version}</version>
            <scope>test</scope>
        </dependency>

        <!-- TestNG - Test Framework -->
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>${testng.version}</version>
            <scope>test</scope>
        </dependency>

        <!-- Jackson - JSON Processing -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>${jackson.version}</version>
        </dependency>

        <!-- JSON Schema Validator -->
        <dependency>
            <groupId>io.rest-assured</groupId>
            <artifactId>json-schema-validator</artifactId>
            <version>${restassured.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven Surefire Plugin - Test Execution -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${maven.surefire.version}</version>
                <configuration>
                    <suiteXmlFiles>
                        <suiteXmlFile>testng.xml</suiteXmlFile>
                    </suiteXmlFiles>
                </configuration>
            </plugin>

            <!-- Maven Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.12.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### 🤔 Why This Configuration?

| Dependency | Purpose | Why Include? |
|------------|---------|--------------|
| **rest-assured** | Core library for API testing | Makes HTTP requests simple and readable |
| **testng** | Test framework | Provides annotations, assertions, parallel execution |
| **jackson-databind** | JSON serialization/deserialization | Convert Java objects to JSON and vice versa |
| **json-schema-validator** | Validate JSON structure | Ensure API responses match expected schema |

### ✅ DO
✅ Use version properties for easy updates  
✅ Keep dependencies up-to-date  
✅ Use `<scope>test</scope>` for testing libraries  
✅ Include all necessary plugins in `<build>` section

### ❌ DON'T
❌ Hardcode versions in dependency tags  
❌ Mix different versions of related libraries  
❌ Skip the maven-surefire-plugin configuration  
❌ Use snapshot versions in production code

---

## Step 3: Download Dependencies

Run the following command in your project root:

```bash
mvn clean install
```

**Expected Output:**
```
[INFO] BUILD SUCCESS
[INFO] Total time: 15.234 s
```

### ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Maven not found" | Add Maven to PATH or use IDE's embedded Maven |
| Dependencies fail to download | Check internet connection, try `mvn clean install -U` |
| Java version error | Ensure JDK 11+ is installed and JAVA_HOME is set |
| "Parent POM not found" | Remove `<parent>` tag if it exists |

### ✅ Verification Checkpoint
- [ ] Maven build successful
- [ ] Dependencies downloaded to `.m2` repository
- [ ] No compilation errors

---

## Step 4: Create First API Test

Create the folder structure: `src/test/java/com/api/tests/`

Create file: `FirstAPITest.java`

```java
package com.api.tests;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

/**
 * First API Test - JSONPlaceholder Public API
 * API Documentation: https://jsonplaceholder.typicode.com/
 */
public class FirstAPITest {

    // Base URL for the API
    private static final String BASE_URL = "https://jsonplaceholder.typicode.com";

    /**
     * Test 1: GET Request - Retrieve all posts
     * Endpoint: /posts
     * Expected: Status Code 200, Response body contains data
     */
    @Test(priority = 1, description = "Verify GET request returns all posts")
    public void testGetAllPosts() {
        // Set base URI
        RestAssured.baseURI = BASE_URL;

        // Send GET request and validate
        given()
                .log().all()  // Log request details
        .when()
                .get("/posts")
        .then()
                .log().all()  // Log response details
                .statusCode(200)  // Verify status code
                .body("size()", greaterThan(0))  // Verify response has data
                .body("[0].userId", notNullValue())  // Verify first item has userId
                .body("[0].title", notNullValue());  // Verify first item has title

        System.out.println("✅ Test Passed: GET all posts successful");
    }

    /**
     * Test 2: GET Request - Retrieve single post by ID
     * Endpoint: /posts/1
     * Expected: Status Code 200, Specific post details
     */
    @Test(priority = 2, description = "Verify GET request returns specific post")
    public void testGetSinglePost() {
        RestAssured.baseURI = BASE_URL;

        Response response = given()
                .log().all()
        .when()
                .get("/posts/1")
        .then()
                .log().all()
                .statusCode(200)
                .body("userId", equalTo(1))
                .body("id", equalTo(1))
                .body("title", notNullValue())
                .extract().response();

        // Additional assertions using TestNG
        Assert.assertEquals(response.statusCode(), 200, "Status code should be 200");
        Assert.assertTrue(response.getTime() < 3000, "Response time should be less than 3 seconds");

        System.out.println("✅ Test Passed: GET single post successful");
        System.out.println("Response Time: " + response.getTime() + "ms");
    }

    /**
     * Test 3: POST Request - Create a new post
     * Endpoint: /posts
     * Expected: Status Code 201, Response contains created data
     */
    @Test(priority = 3, description = "Verify POST request creates new post")
    public void testCreatePost() {
        RestAssured.baseURI = BASE_URL;

        // Request body as JSON string
        String requestBody = """
                {
                    "userId": 1,
                    "title": "My Test Post",
                    "body": "This is a test post created via RestAssured"
                }
                """;

        Response response = given()
                .header("Content-Type", "application/json")
                .body(requestBody)
                .log().all()
        .when()
                .post("/posts")
        .then()
                .log().all()
                .statusCode(201)  // 201 = Created
                .body("userId", equalTo(1))
                .body("title", equalTo("My Test Post"))
                .body("id", notNullValue())  // API assigns an ID
                .extract().response();

        // Extract and print the created post ID
        int createdId = response.jsonPath().getInt("id");
        System.out.println("✅ Test Passed: POST created new post with ID: " + createdId);
    }

    /**
     * Test 4: PUT Request - Update existing post
     * Endpoint: /posts/1
     * Expected: Status Code 200, Updated data in response
     */
    @Test(priority = 4, description = "Verify PUT request updates post")
    public void testUpdatePost() {
        RestAssured.baseURI = BASE_URL;

        String updateBody = """
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Updated Title",
                    "body": "Updated body content"
                }
                """;

        given()
                .header("Content-Type", "application/json")
                .body(updateBody)
                .log().all()
        .when()
                .put("/posts/1")
        .then()
                .log().all()
                .statusCode(200)
                .body("title", equalTo("Updated Title"))
                .body("body", equalTo("Updated body content"));

        System.out.println("✅ Test Passed: PUT updated post successfully");
    }

    /**
     * Test 5: DELETE Request - Delete a post
     * Endpoint: /posts/1
     * Expected: Status Code 200
     */
    @Test(priority = 5, description = "Verify DELETE request removes post")
    public void testDeletePost() {
        RestAssured.baseURI = BASE_URL;

        given()
                .log().all()
        .when()
                .delete("/posts/1")
        .then()
                .log().all()
                .statusCode(200);

        System.out.println("✅ Test Passed: DELETE removed post successfully");
    }
}
```

### 🤔 Why This Code Structure?

**Given-When-Then Pattern:**
- `given()` - Setup (headers, body, parameters)
- `when()` - Action (HTTP method and endpoint)
- `then()` - Validation (assertions)

**Why use static imports?**
```java
import static io.restassured.RestAssured.*;
```
Makes code cleaner: `given()` instead of `RestAssured.given()`

### ✅ DO
✅ Use descriptive test method names  
✅ Add test descriptions in `@Test` annotation  
✅ Log requests and responses during development  
✅ Use Hamcrest matchers for readable assertions  
✅ Set priorities to control test execution order

### ❌ DON'T
❌ Hardcode URLs in test methods (use constants)  
❌ Skip logging during initial development  
❌ Write tests without assertions  
❌ Use generic method names like `test1()`, `test2()`  
❌ Test dependent tests (each should be independent)

---

## Step 5: Create testng.xml

Create `testng.xml` in project root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="RestAssured API Test Suite" verbose="1">
    <test name="API Tests">
        <classes>
            <class name="com.api.tests.FirstAPITest"/>
        </classes>
    </test>
</suite>
```

### 🤔 Why testng.xml?

| Feature | Benefit |
|---------|---------|
| Test grouping | Run specific test categories |
| Parallel execution | Faster test execution (covered in Phase 3) |
| Test ordering | Control execution sequence |
| Parameters | Pass data to tests |
| Listeners | Custom reporting (covered in Phase 2) |

---

## Step 6: Execute Tests

### Method 1: Using Maven Command

```bash
mvn clean test
```

### Method 2: Using IDE (IntelliJ)

1. Right-click on `FirstAPITest.java`
2. Select "Run 'FirstAPITest'"

### Method 3: Using testng.xml

1. Right-click on `testng.xml`
2. Select "Run"

### Expected Output

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running TestSuite
✅ Test Passed: GET all posts successful
✅ Test Passed: GET single post successful
✅ Test Passed: POST created new post with ID: 101
✅ Test Passed: PUT updated post successfully
✅ Test Passed: DELETE removed post successfully
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### ✅ Verification Checkpoint
- [ ] All 5 tests pass
- [ ] No compilation errors
- [ ] Request/Response logs visible in console
- [ ] Test report generated in `target/surefire-reports/`

---

## 📊 Understanding Test Results

Navigate to: `target/surefire-reports/`

You'll find:
- `index.html` - HTML test report
- `emailable-report.html` - Email-friendly report
- `testng-results.xml` - XML results

**Open `emailable-report.html` in a browser to view results.**

---

## 🔧 Troubleshooting Common Issues

### Issue 1: Tests Fail with Connection Timeout

**Error:**
```
java.net.SocketTimeoutException: Read timed out
```

**Solution:**
```java
RestAssured.config = RestAssuredConfig.config()
    .httpClient(HttpClientConfig.httpClientConfig()
        .setParam(CoreConnectionPNames.CONNECTION_TIMEOUT, 10000)
        .setParam(CoreConnectionPNames.SO_TIMEOUT, 10000));
```

### Issue 2: JSON Body Not Recognized

**Error:**
```
Cannot parse JSON body
```

**Solution:**
Ensure Content-Type header is set:
```java
.header("Content-Type", "application/json")
```

### Issue 3: Hamcrest Matchers Not Found

**Error:**
```
Cannot resolve symbol 'greaterThan'
```

**Solution:**
Add static import:
```java
import static org.hamcrest.Matchers.*;
```

### Issue 4: TestNG Tests Not Running

**Solution:**
1. Verify `testng.xml` is in project root
2. Check `maven-surefire-plugin` configuration in `pom.xml`
3. Run `mvn clean install` to refresh

---

## 📚 Key Concepts Learned

### 1. RestAssured Request Structure
```java
given()           // Setup phase
    .headers()    // Add headers
    .body()       // Add request body
.when()           // Action phase
    .get()        // HTTP method
.then()           // Validation phase
    .statusCode() // Assertions
    .body()       // Body assertions
```

### 2. HTTP Methods

| Method | Purpose | Status Code |
|--------|---------|-------------|
| GET | Retrieve data | 200 OK |
| POST | Create new resource | 201 Created |
| PUT | Update existing resource | 200 OK |
| DELETE | Remove resource | 200 OK / 204 No Content |

### 3. Hamcrest Matchers

```java
equalTo(value)           // Exact match
notNullValue()           // Not null
greaterThan(value)       // Greater than
lessThan(value)          // Less than
hasSize(size)            // Collection size
containsString(string)   // String contains
```

---

## ✅ Phase 1 Final Checklist

Before moving to Phase 2, ensure:

- [ ] Maven project created successfully
- [ ] `pom.xml` configured with all dependencies
- [ ] Dependencies downloaded (`mvn clean install`)
- [ ] First test class created with 5 tests
- [ ] `testng.xml` created and configured
- [ ] All tests execute and pass
- [ ] Test reports generated in `target/surefire-reports/`
- [ ] You understand Given-When-Then pattern
- [ ] You can run tests via Maven and IDE
- [ ] Project structure is clean and organized

---

## 🎯 What's Next in Phase 2?

- ✓ Allure Reporting Integration
- ✓ Log4j2 Logging Configuration
- ✓ Config.properties for Environment Management
- ✓ Request/Response Specifications
- ✓ Custom Test Listeners
- ✓ Enhanced Project Structure

---

## 🔗 Quick Command Reference

```bash
# Create Maven project
mvn archetype:generate -DgroupId=com.api.automation -DartifactId=restassured-api-automation

# Install dependencies
mvn clean install

# Run tests
mvn clean test

# Run specific test
mvn test -Dtest=FirstAPITest

# Skip tests
mvn clean install -DskipTests

# Update dependencies
mvn clean install -U

# View dependency tree
mvn dependency:tree
```

---

## 📖 Additional Resources

- [RestAssured Documentation](https://rest-assured.io/)
- [TestNG Documentation](https://testng.org/doc/documentation-main.html)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Hamcrest Matchers](http://hamcrest.org/JavaHamcrest/javadoc/)

---

**🎉 Congratulations! You've completed Phase 1!**