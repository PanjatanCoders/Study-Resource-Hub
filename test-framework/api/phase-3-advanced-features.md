# RestAssured API Testing Framework - Phase 3: Advanced Features
## Part 1: Introduction and Dependencies

---

## 🎯 What You'll Learn in Phase 3
- Data-Driven Testing using TestNG DataProvider
- Reading test data from Excel, JSON, and CSV files
- Parallel test execution
- API chaining (using response from one API in another)
- JSON Schema validation
- Custom assertions and matchers
- Performance testing with response time assertions
- Retry logic for flaky tests

---

## 📋 Prerequisites
- ✅ Completed Phase 1 and Phase 2
- ✅ All Phase 2 features working correctly
- ✅ Understanding of TestNG and RestAssured basics

---

## 🏗️ Project Structure (Phase 3)

```
restassured-api-automation/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── api/
│   │   │           ├── config/
│   │   │           │   └── ConfigReader.java
│   │   │           ├── listeners/
│   │   │           │   ├── TestListener.java
│   │   │           │   └── ✓ RetryAnalyzer.java (NEW)
│   │   │           ├── specifications/
│   │   │           │   └── RequestSpecifications.java
│   │   │           ├── ✓ utils/
│   │   │           │   ├── ✓ ExcelReader.java (NEW)
│   │   │           │   ├── ✓ JsonReader.java (NEW)
│   │   │           │   ├── ✓ CSVReader.java (NEW)
│   │   │           │   └── ✓ APIUtils.java (NEW)
│   │   │           ├── ✓ models/
│   │   │           │   ├── ✓ Post.java (NEW)
│   │   │           │   └── ✓ User.java (NEW)
│   │   │           └── ✓ assertions/
│   │   │               └── ✓ CustomAssertions.java (NEW)
│   │   └── resources/
│   │       ├── config.properties
│   │       ├── log4j2.xml
│   │       └── ✓ testdata/
│   │           ├── ✓ posts.xlsx (NEW)
│   │           ├── ✓ users.json (NEW)
│   │           ├── ✓ testdata.csv (NEW)
│   │           └── ✓ schemas/
│   │               ├── ✓ post-schema.json (NEW)
│   │               └── ✓ user-schema.json (NEW)
│   └── test/
│       └── java/
│           └── com/
│               └── api/
│                   └── tests/
│                       ├── FirstAPITest.java
│                       ├── UserAPITest.java
│                       ├── ✓ DataDrivenTest.java (NEW)
│                       ├── ✓ APIChainTest.java (NEW)
│                       ├── ✓ SchemaValidationTest.java (NEW)
│                       ├── ✓ PerformanceTest.java (NEW)
│                       └── ✓ ParallelExecutionTest.java (NEW)
├── pom.xml (UPDATED)
├── ✓ testng-parallel.xml (NEW)
└── testng.xml (UPDATED)
```

---

## Step 1: Update pom.xml with Advanced Dependencies

Add these **new dependencies** to your existing `pom.xml` (after the existing dependencies from Phase 2):

```xml
<!-- ========== NEW DEPENDENCIES FOR PHASE 3 ========== -->

<!-- Apache POI - Excel File Processing -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.5</version>
</dependency>

<!-- Gson - JSON Processing (Alternative to Jackson) -->
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
</dependency>

<!-- OpenCSV - CSV File Processing -->
<dependency>
    <groupId>com.opencsv</groupId>
    <artifactId>opencsv</artifactId>
    <version>5.9</version>
</dependency>

<!-- Lombok - Reduce Boilerplate Code -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.30</version>
    <scope>provided</scope>
</dependency>

<!-- Awaitility - For Async API Testing -->
<dependency>
    <groupId>org.awaitility</groupId>
    <artifactId>awaitility</artifactId>
    <version>4.2.0</version>
    <scope>test</scope>
</dependency>
```

### 🤔 Why These New Dependencies?

| Dependency | Purpose | Why Include? |
|------------|---------|--------------|
| **poi-ooxml** | Read/write Excel files (.xlsx) | Data-driven testing from Excel |
| **gson** | JSON parsing and serialization | Alternative to Jackson, simpler API |
| **opencsv** | CSV file operations | Data-driven testing from CSV |
| **lombok** | Auto-generate getters, setters, constructors | Reduce POJO boilerplate code |
| **awaitility** | Wait for async operations | Testing async/polling APIs |

---

## Step 2: Download Dependencies

**Run to download all new dependencies:**
```bash
mvn clean install
```

**Expected Output:**
```
[INFO] BUILD SUCCESS
[INFO] Total time: 20.456 s
```

---

## Step 3: Configure Lombok in IDE

### For IntelliJ IDEA:

1. **Install Lombok Plugin:**
    - File → Settings → Plugins
    - Search for "Lombok"
    - Install and restart IDE

2. **Enable Annotation Processing:**
    - File → Settings → Build, Execution, Deployment → Compiler → Annotation Processors
    - Check ✅ "Enable annotation processing"
    - Click Apply and OK

### For Eclipse:

1. **Download Lombok JAR:**
    - Download from: https://projectlombok.org/download
    - Or find in `.m2/repository/org/projectlombok/lombok/1.18.30/lombok-1.18.30.jar`

2. **Install Lombok:**
    - Double-click the lombok JAR
    - Select Eclipse installation
    - Click "Install/Update"
    - Restart Eclipse

3. **Enable Annotation Processing:**
    - Project Properties → Java Compiler → Annotation Processing
    - Check ✅ "Enable annotation processing"
    - Apply and Close

---

## ⚠️ Troubleshooting

### Issue 1: POI Dependencies Conflict

**Error:**
```
NoClassDefFoundError: org/apache/poi/ss/usermodel/Workbook
```

**Solution:**
```bash
# Check dependency tree
mvn dependency:tree

# Clean and reinstall
mvn clean install -U
```

### Issue 2: Lombok Not Working

**Error:**
```
Cannot resolve method 'builder()'
```

**Solution:**
1. Verify Lombok plugin is installed in IDE
2. Enable annotation processing (see instructions above)
3. Rebuild project: Build → Rebuild Project
4. Restart IDE

### Issue 3: OpenCSV Conflicts

**Error:**
```
java.lang.NoSuchMethodError: com.opencsv.CSVReader
```

**Solution:**
```xml
<!-- Ensure correct version -->
<dependency>
    <groupId>com.opencsv</groupId>
    <artifactId>opencsv</artifactId>
    <version>5.9</version>
</dependency>
```

---

## ✅ Verification Checklist for Part 1

Before proceeding to Part 2, verify:

- [ ] All Phase 3 dependencies added to `pom.xml`
- [ ] `mvn clean install` completed successfully
- [ ] No dependency conflicts in output
- [ ] Lombok plugin installed in IDE
- [ ] Annotation processing enabled in IDE
- [ ] IDE restarted after Lombok setup
- [ ] Project builds without errors

---

## 🔗 Quick Commands Reference

```bash
# Install dependencies
mvn clean install

# Force update dependencies
mvn clean install -U

# Check dependency tree
mvn dependency:tree

# Check for dependency updates
mvn versions:display-dependency-updates

# Verify project structure
mvn validate

# Clean and compile
mvn clean compile
```

---

## 📝 Notes

- **Lombok scope is `provided`**: It's only needed at compile time, not runtime
- **Awaitility scope is `test`**: Only used in test code
- **POI is large**: First download may take time due to library size
- **Gson vs Jackson**: We use both - Jackson for RestAssured, Gson for test data

---

**✅ Part 1 Complete!**

Once you've verified all items in the checklist, type **"go to next part"** to proceed to Part 2: POJO Models.

---

## Part 2: POJO Models with Lombok

---

## 🎯 What You'll Learn in Part 2
- Create POJO (Plain Old Java Object) models
- Use Lombok annotations to reduce boilerplate code
- Implement Builder pattern for flexible object creation
- Map JSON properties to Java objects
- Handle nested objects in POJOs

---

## Step 1: Create Post Model

Create folder: `src/main/java/com/api/models/`

Create file: `Post.java`

```java
package com.api.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Post POJO - Plain Old Java Object for Post entity
 * Uses Lombok to reduce boilerplate code
 */
@Data                    // Generates getters, setters, toString, equals, hashCode
@NoArgsConstructor       // Generates no-argument constructor
@AllArgsConstructor      // Generates constructor with all fields
@Builder                 // Implements Builder pattern
public class Post {

    @JsonProperty("userId")
    private int userId;

    @JsonProperty("id")
    private Integer id;  // Integer allows null for new posts

    @JsonProperty("title")
    private String title;

    @JsonProperty("body")
    private String body;

    /**
     * Create Post with required fields only
     */
    public Post(int userId, String title, String body) {
        this.userId = userId;
        this.title = title;
        this.body = body;
    }
}
```

---

## Step 2: Create User Model with Nested Classes

Create file: `User.java`

```java
package com.api.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * User POJO - Plain Old Java Object for User entity
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {

    @JsonProperty("id")
    private Integer id;

    @JsonProperty("name")
    private String name;

    @JsonProperty("username")
    private String username;

    @JsonProperty("email")
    private String email;

    @JsonProperty("phone")
    private String phone;

    @JsonProperty("website")
    private String website;

    @JsonProperty("address")
    private Address address;

    @JsonProperty("company")
    private Company company;

    /**
     * Nested Address class
     */
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Address {
        @JsonProperty("street")
        private String street;

        @JsonProperty("suite")
        private String suite;

        @JsonProperty("city")
        private String city;

        @JsonProperty("zipcode")
        private String zipcode;

        @JsonProperty("geo")
        private Geo geo;

        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        @Builder
        public static class Geo {
            @JsonProperty("lat")
            private String lat;

            @JsonProperty("lng")
            private String lng;
        }
    }

    /**
     * Nested Company class
     */
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Company {
        @JsonProperty("name")
        private String name;

        @JsonProperty("catchPhrase")
        private String catchPhrase;

        @JsonProperty("bs")
        private String bs;
    }
}
```

---

## 🤔 Understanding Lombok Annotations

### @Data Annotation

**What it generates:**
```java
// Without Lombok - You would write:
public class Post {
    private int userId;
    private String title;
    
    // Getter for userId
    public int getUserId() {
        return userId;
    }
    
    // Setter for userId
    public void setUserId(int userId) {
        this.userId = userId;
    }
    
    // Getter for title
    public String getTitle() {
        return title;
    }
    
    // Setter for title
    public void setTitle(String title) {
        this.title = title;
    }
    
    // toString method
    @Override
    public String toString() {
        return "Post{userId=" + userId + ", title='" + title + "'}";
    }
    
    // equals method
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Post post = (Post) o;
        return userId == post.userId && 
               Objects.equals(title, post.title);
    }
    
    // hashCode method
    @Override
    public int hashCode() {
        return Objects.hash(userId, title);
    }
}

// With Lombok - You write:
@Data
public class Post {
    private int userId;
    private String title;
}
// That's it! Lombok generates all the above code!
```

### @Builder Annotation

**Usage example:**
```java
// Without Builder - Constructor hell:
Post post = new Post(1, 101, "My Title", "My Body");
// What's 1? What's 101? Hard to read!

// With Builder - Clear and flexible:
Post post = Post.builder()
    .userId(1)
    .id(101)
    .title("My Title")
    .body("My Body")
    .build();
// Much more readable!

// Builder allows optional parameters:
Post post = Post.builder()
    .userId(1)
    .title("My Title")
    .body("My Body")
    // id is optional - will be null
    .build();
```

### @NoArgsConstructor

```java
// Generates:
public Post() {
    // Empty constructor
}

// Why needed?
// Jackson/Gson need empty constructor for deserialization
Post post = mapper.readValue(json, Post.class);
```

### @AllArgsConstructor

```java
// Generates:
public Post(int userId, Integer id, String title, String body) {
    this.userId = userId;
    this.id = id;
    this.title = title;
    this.body = body;
}

// Useful for creating test data:
Post post = new Post(1, 101, "Title", "Body");
```

---

## Step 3: Using POJO Models in Tests

Create file: `src/test/java/com/api/tests/POJOExampleTest.java`

```java
package com.api.tests;

import com.api.models.Post;
import com.api.models.User;
import com.api.specifications.RequestSpecifications;
import io.restassured.response.Response;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.Assert;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

/**
 * POJOExampleTest - Examples of using POJO models
 */
public class POJOExampleTest {

    private static final Logger logger = LogManager.getLogger(POJOExampleTest.class);

    /**
     * Example 1: Create Post using Builder pattern
     */
    @Test(priority = 1, description = "Create post using POJO with Builder")
    public void testCreatePostWithBuilder() {
        logger.info("Creating post using Builder pattern");

        // Create Post object using Builder
        Post post = Post.builder()
                .userId(1)
                .title("Test Post via Builder")
                .body("This post was created using Builder pattern")
                .build();

        logger.info("Post created: {}", post);

        // Send POST request with POJO
        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(post)  // RestAssured automatically serializes POJO to JSON
        .when()
                .post("/posts")
        .then()
                .statusCode(201)
                .body("userId", equalTo(post.getUserId()))
                .body("title", equalTo(post.getTitle()))
                .extract().response();

        // Deserialize response to Post object
        Post createdPost = response.as(Post.class);
        logger.info("Created post ID: {}", createdPost.getId());
        
        Assert.assertNotNull(createdPost.getId(), "Created post should have ID");
        Assert.assertEquals(createdPost.getTitle(), post.getTitle());
    }

    /**
     * Example 2: Get user and deserialize to POJO
     */
    @Test(priority = 2, description = "Get user and deserialize to POJO")
    public void testGetUserWithPOJO() {
        logger.info("Fetching user and deserializing to POJO");

        // Send GET request and deserialize to User object
        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/users/1")
        .then()
                .statusCode(200)
                .extract().response();

        // Deserialize JSON response to User POJO
        User user = response.as(User.class);

        logger.info("User name: {}", user.getName());
        logger.info("User email: {}", user.getEmail());
        logger.info("User city: {}", user.getAddress().getCity());
        logger.info("User company: {}", user.getCompany().getName());

        // Assert using POJO getters
        Assert.assertNotNull(user.getId());
        Assert.assertNotNull(user.getName());
        Assert.assertNotNull(user.getEmail());
        Assert.assertTrue(user.getEmail().contains("@"));
        
        // Assert nested objects
        Assert.assertNotNull(user.getAddress());
        Assert.assertNotNull(user.getAddress().getCity());
        Assert.assertNotNull(user.getCompany());
        Assert.assertNotNull(user.getCompany().getName());
    }

    /**
     * Example 3: Update post using POJO
     */
    @Test(priority = 3, description = "Update post using POJO")
    public void testUpdatePostWithPOJO() {
        logger.info("Updating post using POJO");

        // Create updated Post object
        Post updatedPost = Post.builder()
                .userId(1)
                .id(1)
                .title("Updated Post Title")
                .body("Updated post body content")
                .build();

        // Send PUT request
        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(updatedPost)
        .when()
                .put("/posts/1")
        .then()
                .statusCode(200)
                .extract().response();

        Post responsePost = response.as(Post.class);
        
        Assert.assertEquals(responsePost.getId(), updatedPost.getId());
        Assert.assertEquals(responsePost.getTitle(), updatedPost.getTitle());
        Assert.assertEquals(responsePost.getBody(), updatedPost.getBody());
        
        logger.info("✅ Post updated successfully");
    }

    /**
     * Example 4: Get all posts and deserialize to array
     */
    @Test(priority = 4, description = "Get all posts as POJO array")
    public void testGetAllPostsAsArray() {
        logger.info("Fetching all posts as POJO array");

        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/posts")
        .then()
                .statusCode(200)
                .extract().response();

        // Deserialize to array of Post objects
        Post[] posts = response.as(Post[].class);

        logger.info("Total posts retrieved: {}", posts.length);
        
        Assert.assertTrue(posts.length > 0, "Should have at least one post");
        
        // Iterate through posts
        for (Post post : posts) {
            Assert.assertNotNull(post.getId());
            Assert.assertNotNull(post.getTitle());
            logger.debug("Post {}: {}", post.getId(), post.getTitle());
        }
        
        logger.info("✅ All posts deserialized successfully");
    }

    /**
     * Example 5: Compare POJO objects
     */
    @Test(priority = 5, description = "Compare POJO objects using equals")
    public void testComparePOJOs() {
        logger.info("Comparing POJO objects");

        Post post1 = Post.builder()
                .userId(1)
                .id(1)
                .title("Test Post")
                .body("Test Body")
                .build();

        Post post2 = Post.builder()
                .userId(1)
                .id(1)
                .title("Test Post")
                .body("Test Body")
                .build();

        Post post3 = Post.builder()
                .userId(2)
                .id(1)
                .title("Test Post")
                .body("Test Body")
                .build();

        // Lombok @Data generates equals() method
        Assert.assertEquals(post1, post2, "Posts with same data should be equal");
        Assert.assertNotEquals(post1, post3, "Posts with different userId should not be equal");

        logger.info("✅ POJO comparison working correctly");
    }
}
```

---

## 🤔 Why Use POJO Models?

### Benefits Comparison

| Without POJO | With POJO |
|--------------|-----------|
| String JSON = "{\"userId\":1,\"title\":\"Test\"}" | Post post = Post.builder().userId(1).title("Test").build() |
| Hard to maintain | Type-safe and IDE autocomplete |
| Error-prone (typos, wrong types) | Compile-time error checking |
| No validation | Can add validation in POJO |
| Difficult to read | Clean, readable code |
| Manual JSON parsing | Automatic serialization/deserialization |

### Before POJO (Bad):
```java
// BAD - Manual JSON string construction
String json = "{" +
    "\"userId\":" + userId + "," +
    "\"title\":\"" + title + "\"," +
    "\"body\":\"" + body + "\"" +
"}";

given().body(json).post("/posts");

// BAD - Manual JSON parsing
String title = response.jsonPath().getString("title");
int userId = response.jsonPath().getInt("userId");
String body = response.jsonPath().getString("body");
```

### After POJO (Good):
```java
// GOOD - Clean object creation
Post post = Post.builder()
    .userId(userId)
    .title(title)
    .body(body)
    .build();

given().body(post).post("/posts");

// GOOD - Automatic deserialization
Post responsePost = response.as(Post.class);
String title = responsePost.getTitle();
int userId = responsePost.getUserId();
String body = responsePost.getBody();
```

---

## ✅ DO and ❌ DON'T

### Creating POJOs

| ✅ DO | ❌ DON'T |
|------|---------|
| Use Lombok annotations | Write getters/setters manually |
| Use @Builder for flexibility | Use multiple constructors |
| Use @JsonProperty for mapping | Rely on field name matching |
| Keep POJOs in separate package | Mix POJOs with test code |
| Include both constructors (@NoArgsConstructor, @AllArgsConstructor) | Skip no-arg constructor |

### Using POJOs in Tests

| ✅ DO | ❌ DON'T |
|------|---------|
| Use Builder pattern for object creation | Use constructor with many parameters |
| Deserialize responses to POJOs | Parse JSON manually with jsonPath |
| Use POJO getters for assertions | Access fields directly |
| Create test data builders | Create POJOs inline in tests |

---

## 🔧 Troubleshooting

### Issue 1: Lombok Annotations Not Working

**Error:**
```
Cannot resolve method 'builder()'
Cannot resolve method 'getTitle()'
```

**Solution:**
1. Install Lombok plugin in IDE (see Part 1)
2. Enable annotation processing
3. Rebuild project: Build → Rebuild Project
4. Restart IDE
5. Verify Lombok dependency in pom.xml

### Issue 2: JSON Deserialization Fails

**Error:**
```
JsonMappingException: Can not construct instance
```

**Solution:**
```java
// Ensure @NoArgsConstructor is present
@Data
@NoArgsConstructor  // THIS IS REQUIRED for Jackson
@AllArgsConstructor
@Builder
public class Post {
    // fields
}
```

### Issue 3: Nested Objects Return Null

**Error:**
```
NullPointerException: user.getAddress().getCity()
```

**Solution:**
```java
// Check for null before accessing nested objects
if (user.getAddress() != null) {
    String city = user.getAddress().getCity();
}

// Or use Optional
Optional.ofNullable(user.getAddress())
    .map(Address::getCity)
    .ifPresent(city -> logger.info("City: {}", city));
```

### Issue 4: Field Names Don't Match JSON

**Error:**
```
JSON field "user_id" doesn't map to "userId"
```

**Solution:**
```java
// Use @JsonProperty to map different names
@JsonProperty("user_id")  // JSON field name
private int userId;        // Java field name
```

---

## ✅ Verification Checklist for Part 2

Before proceeding to Part 3, verify:

- [ ] `Post.java` created in `src/main/java/com/api/models/`
- [ ] `User.java` created with nested Address and Company classes
- [ ] All Lombok annotations present (@Data, @Builder, etc.)
- [ ] `POJOExampleTest.java` created and tests pass
- [ ] Project compiles without errors
- [ ] Builder pattern works (no "cannot resolve method" errors)
- [ ] Getters/setters are auto-generated by Lombok
- [ ] JSON serialization/deserialization working

---

## 🔗 Quick Test Commands

```bash
# Compile and verify POJOs
mvn clean compile

# Run POJO example tests
mvn test -Dtest=POJOExampleTest

# Run specific test method
mvn test -Dtest=POJOExampleTest#testCreatePostWithBuilder

# Verify Lombok is working
mvn clean compile -X | grep lombok
```

---

**✅ Part 2 Complete!**

You now have:
- ✅ Post POJO model with Lombok
- ✅ User POJO model with nested classes
- ✅ Example tests using POJOs
- ✅ Understanding of Builder pattern
- ✅ Type-safe API testing

---

## Part 3: Utility Classes

---

## 🎯 What You'll Learn in Part 3
- Create ExcelReader utility for reading Excel files
- Create JsonReader utility for JSON data
- Create CSVReader utility for CSV files
- Create APIUtils for common API operations
- Implement reusable helper methods
- Handle different data file formats

---

## Step 1: Create ExcelReader Utility

Create folder: `src/main/java/com/api/utils/`

Create file: `ExcelReader.java`

```java
package com.api.utils;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * ExcelReader - Utility to read test data from Excel files
 */
public class ExcelReader {

    private static final Logger logger = LogManager.getLogger(ExcelReader.class);

    /**
     * Read Excel file and return data as List of Maps
     * Each map represents a row with column names as keys
     *
     * @param filePath Path to Excel file
     * @param sheetName Name of the sheet to read
     * @return List of Maps containing row data
     */
    public static List<Map<String, String>> readExcel(String filePath, String sheetName) {
        List<Map<String, String>> data = new ArrayList<>();

        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = new XSSFWorkbook(fis)) {

            Sheet sheet = workbook.getSheet(sheetName);
            if (sheet == null) {
                logger.error("Sheet '{}' not found in file: {}", sheetName, filePath);
                throw new RuntimeException("Sheet not found: " + sheetName);
            }

            // Get header row
            Row headerRow = sheet.getRow(0);
            if (headerRow == null) {
                logger.error("Header row not found in sheet: {}", sheetName);
                throw new RuntimeException("Header row is missing");
            }

            List<String> headers = new ArrayList<>();
            for (Cell cell : headerRow) {
                headers.add(getCellValueAsString(cell));
            }

            logger.info("Headers found: {}", headers);

            // Read data rows
            for (int i = 1; i <= sheet.getLastRowNum(); i++) {
                Row row = sheet.getRow(i);
                if (row == null) continue;

                Map<String, String> rowData = new HashMap<>();
                for (int j = 0; j < headers.size(); j++) {
                    Cell cell = row.getCell(j);
                    String cellValue = getCellValueAsString(cell);
                    rowData.put(headers.get(j), cellValue);
                }
                data.add(rowData);
            }

            logger.info("Successfully read {} rows from Excel file", data.size());

        } catch (IOException e) {
            logger.error("Error reading Excel file: {}", filePath, e);
            throw new RuntimeException("Failed to read Excel file", e);
        }

        return data;
    }

    /**
     * Convert cell value to String regardless of cell type
     */
    private static String getCellValueAsString(Cell cell) {
        if (cell == null) {
            return "";
        }

        return switch (cell.getCellType()) {
            case STRING -> cell.getStringCellValue();
            case NUMERIC -> {
                if (DateUtil.isCellDateFormatted(cell)) {
                    yield cell.getDateCellValue().toString();
                } else {
                    yield String.valueOf((int) cell.getNumericCellValue());
                }
            }
            case BOOLEAN -> String.valueOf(cell.getBooleanCellValue());
            case FORMULA -> cell.getCellFormula();
            default -> "";
        };
    }

    /**
     * Read specific row from Excel
     */
    public static Map<String, String> readRow(String filePath, String sheetName, int rowNumber) {
        List<Map<String, String>> allData = readExcel(filePath, sheetName);
        if (rowNumber < 0 || rowNumber >= allData.size()) {
            throw new IndexOutOfBoundsException("Row number out of bounds: " + rowNumber);
        }
        return allData.get(rowNumber);
    }

    /**
     * Get row count (excluding header)
     */
    public static int getRowCount(String filePath, String sheetName) {
        return readExcel(filePath, sheetName).size();
    }

    /**
     * Read specific column from Excel
     */
    public static List<String> readColumn(String filePath, String sheetName, String columnName) {
        List<String> columnData = new ArrayList<>();
        List<Map<String, String>> allData = readExcel(filePath, sheetName);

        for (Map<String, String> row : allData) {
            if (row.containsKey(columnName)) {
                columnData.add(row.get(columnName));
            }
        }

        logger.info("Read {} values from column '{}'", columnData.size(), columnName);
        return columnData;
    }

    /**
     * Check if Excel file has specific sheet
     */
    public static boolean hasSheet(String filePath, String sheetName) {
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = new XSSFWorkbook(fis)) {
            return workbook.getSheet(sheetName) != null;
        } catch (IOException e) {
            logger.error("Error checking sheet existence: {}", filePath, e);
            return false;
        }
    }
}
```

---

## Step 2: Create JsonReader Utility

Create file: `JsonReader.java`

```java
package com.api.utils;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

/**
 * JsonReader - Utility to read test data from JSON files
 */
public class JsonReader {

    private static final Logger logger = LogManager.getLogger(JsonReader.class);
    private static final Gson gson = new Gson();

    /**
     * Read JSON file and return as List of Maps
     */
    public static List<Map<String, Object>> readJsonAsList(String filePath) {
        try (FileReader reader = new FileReader(filePath)) {
            Type listType = new TypeToken<List<Map<String, Object>>>() {}.getType();
            List<Map<String, Object>> data = gson.fromJson(reader, listType);
            logger.info("Successfully read {} records from JSON file: {}", data.size(), filePath);
            return data;
        } catch (IOException e) {
            logger.error("Error reading JSON file: {}", filePath, e);
            throw new RuntimeException("Failed to read JSON file", e);
        }
    }

    /**
     * Read JSON file and return as specific Object type
     */
    public static <T> T readJson(String filePath, Class<T> classType) {
        try (FileReader reader = new FileReader(filePath)) {
            T data = gson.fromJson(reader, classType);
            logger.info("Successfully parsed JSON file to {}", classType.getSimpleName());
            return data;
        } catch (IOException e) {
            logger.error("Error reading JSON file: {}", filePath, e);
            throw new RuntimeException("Failed to read JSON file", e);
        }
    }

    /**
     * Read JSON file and return as List of specific Object type
     */
    public static <T> List<T> readJsonAsListOfObjects(String filePath, Class<T> classType) {
        try (FileReader reader = new FileReader(filePath)) {
            Type listType = TypeToken.getParameterized(List.class, classType).getType();
            List<T> data = gson.fromJson(reader, listType);
            logger.info("Successfully read {} objects from JSON file", data.size());
            return data;
        } catch (IOException e) {
            logger.error("Error reading JSON file: {}", filePath, e);
            throw new RuntimeException("Failed to read JSON file", e);
        }
    }

    /**
     * Convert Object to JSON String
     */
    public static String toJson(Object obj) {
        String json = gson.toJson(obj);
        logger.debug("Converted object to JSON: {}", json);
        return json;
    }

    /**
     * Convert JSON String to Object
     */
    public static <T> T fromJson(String json, Class<T> classType) {
        T obj = gson.fromJson(json, classType);
        logger.debug("Converted JSON to {}", classType.getSimpleName());
        return obj;
    }

    /**
     * Pretty print JSON string
     */
    public static String toPrettyJson(Object obj) {
        Gson prettyGson = new com.google.gson.GsonBuilder().setPrettyPrinting().create();
        return prettyGson.toJson(obj);
    }

    /**
     * Read JSON as Map
     */
    public static Map<String, Object> readJsonAsMap(String filePath) {
        try (FileReader reader = new FileReader(filePath)) {
            Type mapType = new TypeToken<Map<String, Object>>() {}.getType();
            Map<String, Object> data = gson.fromJson(reader, mapType);
            logger.info("Successfully read JSON as Map from: {}", filePath);
            return data;
        } catch (IOException e) {
            logger.error("Error reading JSON file: {}", filePath, e);
            throw new RuntimeException("Failed to read JSON file", e);
        }
    }
}
```

---

## Step 3: Create CSVReader Utility

Create file: `CSVReader.java`

```java
package com.api.utils;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * CSVReader - Utility to read test data from CSV files
 */
public class CSVReader {

    private static final Logger logger = LogManager.getLogger(CSVReader.class);

    /**
     * Read CSV file and return as List of Maps
     */
    public static List<Map<String, String>> readCSV(String filePath) {
        List<Map<String, String>> data = new ArrayList<>();

        try (com.opencsv.CSVReader reader = new com.opencsv.CSVReader(new FileReader(filePath))) {
            List<String[]> allRows = reader.readAll();
            
            if (allRows.isEmpty()) {
                logger.warn("CSV file is empty: {}", filePath);
                return data;
            }

            // First row as headers
            String[] headers = allRows.get(0);
            logger.info("CSV Headers: {}", String.join(", ", headers));

            // Read data rows
            for (int i = 1; i < allRows.size(); i++) {
                String[] row = allRows.get(i);
                Map<String, String> rowData = new HashMap<>();
                
                for (int j = 0; j < headers.length && j < row.length; j++) {
                    rowData.put(headers[j].trim(), row[j].trim());
                }
                data.add(rowData);
            }

            logger.info("Successfully read {} rows from CSV file", data.size());

        } catch (IOException | CsvException e) {
            logger.error("Error reading CSV file: {}", filePath, e);
            throw new RuntimeException("Failed to read CSV file", e);
        }

        return data;
    }

    /**
     * Read specific column from CSV
     */
    public static List<String> readColumn(String filePath, String columnName) {
        List<String> columnData = new ArrayList<>();
        List<Map<String, String>> allData = readCSV(filePath);

        for (Map<String, String> row : allData) {
            if (row.containsKey(columnName)) {
                columnData.add(row.get(columnName));
            }
        }

        logger.info("Read {} values from column '{}'", columnData.size(), columnName);
        return columnData;
    }

    /**
     * Get row count (excluding header)
     */
    public static int getRowCount(String filePath) {
        return readCSV(filePath).size();
    }

    /**
     * Read specific row from CSV
     */
    public static Map<String, String> readRow(String filePath, int rowNumber) {
        List<Map<String, String>> allData = readCSV(filePath);
        if (rowNumber < 0 || rowNumber >= allData.size()) {
            throw new IndexOutOfBoundsException("Row number out of bounds: " + rowNumber);
        }
        return allData.get(rowNumber);
    }

    /**
     * Check if CSV has specific column
     */
    public static boolean hasColumn(String filePath, String columnName) {
        List<Map<String, String>> data = readCSV(filePath);
        if (data.isEmpty()) {
            return false;
        }
        return data.get(0).containsKey(columnName);
    }

    /**
     * Get all column names from CSV
     */
    public static List<String> getColumnNames(String filePath) {
        try (com.opencsv.CSVReader reader = new com.opencsv.CSVReader(new FileReader(filePath))) {
            List<String[]> rows = reader.readAll();
            if (!rows.isEmpty()) {
                return List.of(rows.get(0));
            }
        } catch (IOException | CsvException e) {
            logger.error("Error reading CSV headers: {}", filePath, e);
        }
        return new ArrayList<>();
    }
}
```

---

## Step 4: Create APIUtils Utility

Create file: `APIUtils.java`

```java
package com.api.utils;

import io.restassured.response.Response;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * APIUtils - Common utility methods for API testing
 */
public class APIUtils {

    private static final Logger logger = LogManager.getLogger(APIUtils.class);

    /**
     * Extract JSON path value from Response
     */
    public static <T> T extractJsonPath(Response response, String path) {
        logger.debug("Extracting JSON path: {}", path);
        return response.jsonPath().get(path);
    }

    /**
     * Extract multiple values from Response
     */
    public static <T> List<T> extractJsonPathList(Response response, String path) {
        logger.debug("Extracting JSON path list: {}", path);
        return response.jsonPath().getList(path);
    }

    /**
     * Verify response contains specific field
     */
    public static boolean hasField(Response response, String fieldPath) {
        try {
            Object value = response.jsonPath().get(fieldPath);
            return value != null;
        } catch (Exception e) {
            return false;
        }
    }

    /**
     * Get response as Map
     */
    public static Map<String, Object> getResponseAsMap(Response response) {
        return response.jsonPath().getMap("$");
    }

    /**
     * Get response time in milliseconds
     */
    public static long getResponseTime(Response response) {
        return response.getTime();
    }

    /**
     * Check if response time is acceptable
     */
    public static boolean isResponseTimeFast(Response response, long maxTimeMs) {
        long responseTime = response.getTime();
        boolean isFast = responseTime <= maxTimeMs;
        logger.info("Response time: {}ms (Max allowed: {}ms) - {}", 
            responseTime, maxTimeMs, isFast ? "PASS" : "FAIL");
        return isFast;
    }

    /**
     * Print response body in readable format
     */
    public static void printResponseBody(Response response) {
        logger.info("Response Body:\n{}", response.getBody().asPrettyString());
    }

    /**
     * Get all headers from response
     */
    public static Map<String, String> getAllHeaders(Response response) {
        return response.getHeaders().asList()
            .stream()
            .collect(Collectors.toMap(
                header -> header.getName(),
                header -> header.getValue(),
                (existing, replacement) -> existing  // Keep first value if duplicate
            ));
    }

    /**
     * Wait for API to be available (polling)
     */
    public static boolean waitForAPIAvailability(String endpoint, int maxRetries, int delayMs) {
        for (int i = 0; i < maxRetries; i++) {
            try {
                Response response = io.restassured.RestAssured.get(endpoint);
                if (response.getStatusCode() == 200) {
                    logger.info("API is available after {} attempts", i + 1);
                    return true;
                }
            } catch (Exception e) {
                logger.debug("API not available yet, attempt {}/{}", i + 1, maxRetries);
            }
            
            try {
                Thread.sleep(delayMs);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                logger.warn("Wait interrupted");
                return false;
            }
        }
        logger.error("API not available after {} attempts", maxRetries);
        return false;
    }

    /**
     * Get specific header value
     */
    public static String getHeader(Response response, String headerName) {
        return response.getHeader(headerName);
    }

    /**
     * Check if response has specific header
     */
    public static boolean hasHeader(Response response, String headerName) {
        return response.getHeader(headerName) != null;
    }

    /**
     * Get status code from response
     */
    public static int getStatusCode(Response response) {
        return response.getStatusCode();
    }

    /**
     * Check if status code is success (2xx)
     */
    public static boolean isSuccessStatusCode(Response response) {
        int statusCode = response.getStatusCode();
        return statusCode >= 200 && statusCode < 300;
    }

    /**
     * Get content type from response
     */
    public static String getContentType(Response response) {
        return response.getContentType();
    }

    /**
     * Extract cookie value
     */
    public static String getCookie(Response response, String cookieName) {
        return response.getCookie(cookieName);
    }

    /**
     * Get all cookies from response
     */
    public static Map<String, String> getAllCookies(Response response) {
        return response.getCookies();
    }

    /**
     * Validate JSON response structure
     */
    public static boolean isValidJsonResponse(Response response) {
        try {
            response.jsonPath().getMap("$");
            return true;
        } catch (Exception e) {
            logger.error("Invalid JSON response", e);
            return false;
        }
    }

    /**
     * Get response size in bytes
     */
    public static long getResponseSize(Response response) {
        return response.getBody().asByteArray().length;
    }

    /**
     * Log response details
     */
    public static void logResponseDetails(Response response) {
        logger.info("=== Response Details ===");
        logger.info("Status Code: {}", response.getStatusCode());
        logger.info("Status Line: {}", response.getStatusLine());
        logger.info("Response Time: {}ms", response.getTime());
        logger.info("Content Type: {}", response.getContentType());
        logger.info("Response Size: {} bytes", getResponseSize(response));
        logger.info("========================");
    }
}
```

---

## 🤔 Understanding Utility Classes

### When to Use Each Utility

| Utility | Use For | Example |
|---------|---------|---------|
| **ExcelReader** | Complex test data with multiple columns | User registration data with 10+ fields |
| **JsonReader** | Structured test data, API payloads | Sample API request/response bodies |
| **CSVReader** | Simple tabular data | User IDs, email lists, test scenarios |
| **APIUtils** | Common API operations | Extract response data, validate response time |

### Benefits of Utility Classes

**Without Utilities:**
```java
// BAD - Repeated code in every test
@Test
public void test1() {
    FileInputStream fis = new FileInputStream("data.xlsx");
    Workbook workbook = new XSSFWorkbook(fis);
    Sheet sheet = workbook.getSheet("Sheet1");
    // ... 20 more lines to read data
}

@Test
public void test2() {
    FileInputStream fis = new FileInputStream("data.xlsx");
    Workbook workbook = new XSSFWorkbook(fis);
    Sheet sheet = workbook.getSheet("Sheet1");
    // ... same 20 lines repeated
}
```

**With Utilities:**
```java
// GOOD - One line to read data
@Test
public void test1() {
    List<Map<String, String>> data = ExcelReader.readExcel("data.xlsx", "Sheet1");
}

@Test
public void test2() {
    List<Map<String, String>> data = ExcelReader.readExcel("data.xlsx", "Sheet1");
}
```

---

## ✅ DO and ❌ DON'T

### Using Utility Classes

| ✅ DO | ❌ DON'T |
|------|---------|
| Make utility methods static | Create utility instances |
| Add comprehensive logging | Skip error logging |
| Handle exceptions properly | Let exceptions propagate |
| Validate input parameters | Assume inputs are always valid |
| Make methods reusable | Make methods too specific |

### Error Handling

| ✅ DO | ❌ DON'T |
|------|---------|
| Log errors with context | Silently swallow exceptions |
| Throw meaningful exceptions | Throw generic Exception |
| Provide helpful error messages | Return null without logging |
| Clean up resources (use try-with-resources) | Leave files/streams open |

---

## 🔧 Troubleshooting

### Issue 1: Excel File Not Found

**Error:**
```
FileNotFoundException: posts.xlsx
```

**Solution:**
```java
// Use absolute path or verify relative path
String filePath = "src/main/resources/testdata/posts.xlsx";

// Or get from classpath
String filePath = ClassLoader.getSystemResource("testdata/posts.xlsx").getPath();

// Check file exists before reading
File file = new File(filePath);
if (!file.exists()) {
    logger.error("File not found: {}", filePath);
}
```

### Issue 2: POI Memory Issues with Large Excel Files

**Error:**
```
OutOfMemoryError: Java heap space
```

**Solution:**
```java
// For large files, process row by row instead of loading all
public static void readLargeExcel(String filePath, String sheetName) {
    try (FileInputStream fis = new FileInputStream(filePath);
         Workbook workbook = new XSSFWorkbook(fis)) {
        
        Sheet sheet = workbook.getSheet(sheetName);
        
        // Process each row individually
        for (Row row : sheet) {
            // Process row immediately
            processRow(row);
            // Don't store in memory
        }
    }
}
```

### Issue 3: CSV Encoding Issues

**Error:**
```
Characters displaying as ??? or �
```

**Solution:**
```java
// Specify encoding when reading CSV
try (CSVReader reader = new CSVReaderBuilder(
        new InputStreamReader(new FileInputStream(filePath), StandardCharsets.UTF_8))
        .build()) {
    // Read CSV with UTF-8 encoding
}
```

### Issue 4: JSON Parsing Errors

**Error:**
```
JsonSyntaxException: Expected BEGIN_OBJECT but was BEGIN_ARRAY
```

**Solution:**
```java
// Check JSON structure first
// If JSON is an array: [{...}, {...}]
List<Map<String, Object>> data = JsonReader.readJsonAsList(filePath);

// If JSON is an object: {...}
Map<String, Object> data = JsonReader.readJsonAsMap(filePath);
```

---

## ✅ Verification Checklist for Part 3

Before proceeding to Part 4, verify:

- [ ] `ExcelReader.java` created in `src/main/java/com/api/utils/`
- [ ] `JsonReader.java` created with all methods
- [ ] `CSVReader.java` created with CSV parsing logic
- [ ] `APIUtils.java` created with common API helpers
- [ ] All utility classes compile without errors
- [ ] Proper logging added to all utility methods
- [ ] Exception handling implemented correctly
- [ ] Resource cleanup (try-with-resources) used

---

## 🔗 Quick Test Commands

```bash
# Compile utilities
mvn clean compile

# Run tests using utilities
mvn test

# Check for compilation errors
mvn compile
```

---

**✅ Part 3 Complete!**

You now have:
- ✅ ExcelReader for reading Excel data
- ✅ JsonReader for JSON file operations
- ✅ CSVReader for CSV file parsing
- ✅ APIUtils for common API operations
- ✅ Reusable utilities across all tests

---
## Part 4: Test Data Files, RetryAnalyzer, and CustomAssertions

---

## 🎯 What You'll Learn in Part 4
- Create Excel test data files
- Create JSON test data files
- Create CSV test data files
- Create JSON schema files for validation
- Implement RetryAnalyzer for flaky tests
- Create CustomAssertions for reusable validations

---

## Step 1: Create Test Data Folder Structure

Create folders:
```
src/main/resources/testdata/
src/main/resources/testdata/schemas/
```

---

## Step 2: Create Excel Test Data

### Manual Creation in Excel/Google Sheets

**File:** `src/main/resources/testdata/posts.xlsx`

**Sheet Name:** Sheet1

| userId | title | body |
|--------|-------|------|
| 1 | Test Post 1 | This is test post body 1 |
| 2 | Test Post 2 | This is test post body 2 |
| 1 | Test Post 3 | This is test post body 3 |
| 3 | API Test Post | Created via API automation |
| 1 | Sample Post | Sample post content |

**Steps to create:**
1. Open Excel or Google Sheets
2. Create headers in Row 1: `userId`, `title`, `body`
3. Add test data in subsequent rows
4. Save as `posts.xlsx`
5. Place in `src/main/resources/testdata/` folder

### Alternative: Programmatic Creation

If you prefer to create Excel programmatically:

```java
// Helper to create Excel file (run once)
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;

public class CreateExcelTestData {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Sheet1");
        
        // Header row
        Row headerRow = sheet.createRow(0);
        headerRow.createCell(0).setCellValue("userId");
        headerRow.createCell(1).setCellValue("title");
        headerRow.createCell(2).setCellValue("body");
        
        // Data rows
        Row row1 = sheet.createRow(1);
        row1.createCell(0).setCellValue(1);
        row1.createCell(1).setCellValue("Test Post 1");
        row1.createCell(2).setCellValue("This is test post body 1");
        
        Row row2 = sheet.createRow(2);
        row2.createCell(0).setCellValue(2);
        row2.createCell(1).setCellValue("Test Post 2");
        row2.createCell(2).setCellValue("This is test post body 2");
        
        Row row3 = sheet.createRow(3);
        row3.createCell(0).setCellValue(1);
        row3.createCell(1).setCellValue("Test Post 3");
        row3.createCell(2).setCellValue("This is test post body 3");
        
        // Save file
        FileOutputStream fos = new FileOutputStream("src/main/resources/testdata/posts.xlsx");
        workbook.write(fos);
        workbook.close();
        fos.close();
        
        System.out.println("Excel file created successfully!");
    }
}
```

---

## Step 3: Create JSON Test Data

Create file: `src/main/resources/testdata/users.json`

```json
[
  {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john.doe@example.com",
    "phone": "1-555-123-4567",
    "website": "johndoe.com"
  },
  {
    "name": "Jane Smith",
    "username": "janesmith",
    "email": "jane.smith@example.com",
    "phone": "1-555-987-6543",
    "website": "janesmith.com"
  },
  {
    "name": "Bob Johnson",
    "username": "bobjohnson",
    "email": "bob.johnson@example.com",
    "phone": "1-555-456-7890",
    "website": "bobjohnson.com"
  },
  {
    "name": "Alice Williams",
    "username": "alicewilliams",
    "email": "alice.williams@example.com",
    "phone": "1-555-111-2222",
    "website": "alicewilliams.com"
  },
  {
    "name": "Charlie Brown",
    "username": "charliebrown",
    "email": "charlie.brown@example.com",
    "phone": "1-555-333-4444",
    "website": "charliebrown.com"
  }
]
```

### Alternative: Create Posts JSON Data

Create file: `src/main/resources/testdata/posts.json`

```json
[
  {
    "userId": 1,
    "title": "Introduction to API Testing",
    "body": "API testing is crucial for modern applications"
  },
  {
    "userId": 2,
    "title": "RestAssured Framework Guide",
    "body": "RestAssured makes API testing simple and readable"
  },
  {
    "userId": 1,
    "title": "Data-Driven Testing Best Practices",
    "body": "Separate test data from test logic for maintainability"
  }
]
```

---

## Step 4: Create CSV Test Data

Create file: `src/main/resources/testdata/testdata.csv`

```csv
userId,postId,expectedStatusCode
1,1,200
2,2,200
1,3,200
1,999,404
5,50,200
10,100,200
1,9999,404
```

### Alternative: Create User Test Data CSV

Create file: `src/main/resources/testdata/users.csv`

```csv
name,username,email,phone
John Doe,johndoe,john@example.com,555-1234
Jane Smith,janesmith,jane@example.com,555-5678
Bob Johnson,bobjohnson,bob@example.com,555-9012
Alice Williams,alicewilliams,alice@example.com,555-3456
```

---

## Step 5: Create JSON Schema Files

### Post Schema

Create file: `src/main/resources/testdata/schemas/post-schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Post Schema",
  "description": "Schema for validating Post API responses",
  "type": "object",
  "required": ["userId", "id", "title", "body"],
  "properties": {
    "userId": {
      "type": "integer",
      "minimum": 1,
      "description": "User ID who created the post"
    },
    "id": {
      "type": "integer",
      "minimum": 1,
      "description": "Unique post identifier"
    },
    "title": {
      "type": "string",
      "minLength": 1,
      "maxLength": 200,
      "description": "Post title"
    },
    "body": {
      "type": "string",
      "minLength": 1,
      "description": "Post body content"
    }
  },
  "additionalProperties": false
}
```

### User Schema

Create file: `src/main/resources/testdata/schemas/user-schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "User Schema",
  "description": "Schema for validating User API responses",
  "type": "object",
  "required": ["id", "name", "username", "email"],
  "properties": {
    "id": {
      "type": "integer",
      "minimum": 1,
      "description": "Unique user identifier"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "User's full name"
    },
    "username": {
      "type": "string",
      "minLength": 1,
      "description": "User's username"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "User's email address"
    },
    "phone": {
      "type": "string",
      "description": "User's phone number"
    },
    "website": {
      "type": "string",
      "description": "User's website"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": {
          "type": "string"
        },
        "suite": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "zipcode": {
          "type": "string"
        },
        "geo": {
          "type": "object",
          "properties": {
            "lat": {
              "type": "string"
            },
            "lng": {
              "type": "string"
            }
          }
        }
      }
    },
    "company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "catchPhrase": {
          "type": "string"
        },
        "bs": {
          "type": "string"
        }
      }
    }
  }
}
```

---

## Step 6: Create RetryAnalyzer

Create folder: `src/main/java/com/api/listeners/`

Create file: `RetryAnalyzer.java`

```java
package com.api.listeners;

import com.api.config.ConfigReader;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;

/**
 * RetryAnalyzer - Automatically retry failed tests
 * Useful for handling flaky tests caused by network issues, timeouts, etc.
 */
public class RetryAnalyzer implements IRetryAnalyzer {

    private static final Logger logger = LogManager.getLogger(RetryAnalyzer.class);
    private int retryCount = 0;
    private final ConfigReader config = ConfigReader.getInstance();

    @Override
    public boolean retry(ITestResult result) {
        // Check if retry is enabled in config
        if (!config.isRetryEnabled()) {
            logger.debug("Retry is disabled in configuration");
            return false;
        }

        int maxRetryCount = config.getRetryCount();

        if (retryCount < maxRetryCount) {
            retryCount++;
            logger.warn("⟳ Retrying test: {} (Attempt {}/{})",
                result.getMethod().getMethodName(),
                retryCount,
                maxRetryCount);
            
            // Log failure reason
            if (result.getThrowable() != null) {
                logger.warn("Retry reason: {}", result.getThrowable().getMessage());
            }
            
            return true;
        }

        logger.error("❌ Test failed after {} retries: {}",
            maxRetryCount,
            result.getMethod().getMethodName());
        return false;
    }

    /**
     * Get current retry count
     */
    public int getRetryCount() {
        return retryCount;
    }

    /**
     * Reset retry count (useful for test isolation)
     */
    public void resetRetryCount() {
        retryCount = 0;
    }
}
```

### Using RetryAnalyzer in Tests

```java
// Apply to specific test
@Test(retryAnalyzer = RetryAnalyzer.class)
public void testFlakyAPI() {
    // Test that might fail due to network issues
}

// Apply to all tests in a class
public class MyTestClass {
    @BeforeMethod
    public void setRetry(Method method) {
        method.getAnnotation(Test.class).retryAnalyzer();
    }
}
```

### 🤔 Why Use RetryAnalyzer?

**Common Flaky Test Causes:**
- Network timeouts
- Temporary service unavailability
- Database locks
- Race conditions
- Environment-specific issues

**Benefits:**
- ✅ Reduces false negatives
- ✅ Improves test stability in CI/CD
- ✅ Saves debugging time
- ✅ Better reliability metrics

**⚠️ Warning:**
- Don't use retry to hide real bugs
- Investigate why tests are flaky
- Fix root cause instead of relying on retry

---

## Step 7: Create CustomAssertions

Create folder: `src/main/java/com/api/assertions/`

Create file: `CustomAssertions.java`

```java
package com.api.assertions;

import io.restassured.response.Response;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.Assert;

import java.util.List;

/**
 * CustomAssertions - Reusable assertion methods for API testing
 * Provides domain-specific assertions with clear error messages
 */
public class CustomAssertions {

    private static final Logger logger = LogManager.getLogger(CustomAssertions.class);

    /**
     * Assert response time is within acceptable limit
     */
    public static void assertResponseTime(Response response, long maxTimeMs) {
        long actualTime = response.getTime();
        logger.info("Asserting response time: {}ms <= {}ms", actualTime, maxTimeMs);
        Assert.assertTrue(actualTime <= maxTimeMs,
            String.format("Response time %dms exceeded maximum %dms", actualTime, maxTimeMs));
    }

    /**
     * Assert response time is within acceptable limit with custom message
     */
    public static void assertResponseTime(Response response, long maxTimeMs, String message) {
        long actualTime = response.getTime();
        logger.info("Asserting response time: {}ms <= {}ms - {}", actualTime, maxTimeMs, message);
        Assert.assertTrue(actualTime <= maxTimeMs, message);
    }

    /**
     * Assert status code is in list of expected codes
     */
    public static void assertStatusCodeIn(Response response, int... expectedCodes) {
        int actualCode = response.getStatusCode();
        for (int expected : expectedCodes) {
            if (actualCode == expected) {
                logger.info("Status code {} matches expected", actualCode);
                return;
            }
        }
        Assert.fail(String.format("Status code %d not in expected list: %s", 
            actualCode, java.util.Arrays.toString(expectedCodes)));
    }

    /**
     * Assert response contains specific field
     */
    public static void assertFieldExists(Response response, String fieldPath) {
        logger.info("Asserting field exists: {}", fieldPath);
        try {
            Object value = response.jsonPath().get(fieldPath);
            Assert.assertNotNull(value, "Field should exist: " + fieldPath);
        } catch (Exception e) {
            Assert.fail("Field not found: " + fieldPath);
        }
    }

    /**
     * Assert response field has specific value
     */
    public static void assertFieldEquals(Response response, String fieldPath, Object expectedValue) {
        logger.info("Asserting field '{}' equals '{}'", fieldPath, expectedValue);
        Object actualValue = response.jsonPath().get(fieldPath);
        Assert.assertEquals(actualValue, expectedValue,
            String.format("Field '%s' value mismatch", fieldPath));
    }

    /**
     * Assert response field is not null
     */
    public static void assertFieldNotNull(Response response, String fieldPath) {
        logger.info("Asserting field '{}' is not null", fieldPath);
        Object value = response.jsonPath().get(fieldPath);
        Assert.assertNotNull(value, String.format("Field '%s' should not be null", fieldPath));
    }

    /**
     * Assert list size
     */
    public static void assertListSize(Response response, String listPath, int expectedSize) {
        logger.info("Asserting list size at '{}' equals {}", listPath, expectedSize);
        List<?> list = response.jsonPath().getList(listPath);
        Assert.assertEquals(list.size(), expectedSize,
            String.format("List size mismatch at '%s'", listPath));
    }

    /**
     * Assert list is not empty
     */
    public static void assertListNotEmpty(Response response, String listPath) {
        logger.info("Asserting list at '{}' is not empty", listPath);
        List<?> list = response.jsonPath().getList(listPath);
        Assert.assertFalse(list.isEmpty(), 
            String.format("List at '%s' should not be empty", listPath));
    }

    /**
     * Assert list size is greater than
     */
    public static void assertListSizeGreaterThan(Response response, String listPath, int minSize) {
        logger.info("Asserting list size at '{}' > {}", listPath, minSize);
        List<?> list = response.jsonPath().getList(listPath);
        Assert.assertTrue(list.size() > minSize,
            String.format("List size %d should be greater than %d", list.size(), minSize));
    }

    /**
     * Assert response header exists
     */
    public static void assertHeaderExists(Response response, String headerName) {
        logger.info("Asserting header exists: {}", headerName);
        String headerValue = response.getHeader(headerName);
        Assert.assertNotNull(headerValue, "Header should exist: " + headerName);
    }

    /**
     * Assert response header has specific value
     */
    public static void assertHeaderEquals(Response response, String headerName, String expectedValue) {
        logger.info("Asserting header '{}' equals '{}'", headerName, expectedValue);
        String actualValue = response.getHeader(headerName);
        Assert.assertEquals(actualValue, expectedValue,
            String.format("Header '%s' value mismatch", headerName));
    }

    /**
     * Assert response header contains text
     */
    public static void assertHeaderContains(Response response, String headerName, String expectedText) {
        logger.info("Asserting header '{}' contains '{}'", headerName, expectedText);
        String actualValue = response.getHeader(headerName);
        Assert.assertNotNull(actualValue, "Header should exist: " + headerName);
        Assert.assertTrue(actualValue.contains(expectedText),
            String.format("Header '%s' should contain '%s'", headerName, expectedText));
    }

    /**
     * Assert response body contains text
     */
    public static void assertBodyContains(Response response, String expectedText) {
        logger.info("Asserting body contains: {}", expectedText);
        String body = response.getBody().asString();
        Assert.assertTrue(body.contains(expectedText),
            "Response body should contain: " + expectedText);
    }

    /**
     * Assert response body does not contain text
     */
    public static void assertBodyNotContains(Response response, String unexpectedText) {
        logger.info("Asserting body does not contain: {}", unexpectedText);
        String body = response.getBody().asString();
        Assert.assertFalse(body.contains(unexpectedText),
            "Response body should not contain: " + unexpectedText);
    }

    /**
     * Assert response is successful (2xx status code)
     */
    public static void assertSuccess(Response response) {
        int statusCode = response.getStatusCode();
        logger.info("Asserting successful response: {}", statusCode);
        Assert.assertTrue(statusCode >= 200 && statusCode < 300,
            "Status code should be 2xx, but was: " + statusCode);
    }

    /**
     * Assert response is client error (4xx status code)
     */
    public static void assertClientError(Response response) {
        int statusCode = response.getStatusCode();
        logger.info("Asserting client error response: {}", statusCode);
        Assert.assertTrue(statusCode >= 400 && statusCode < 500,
            "Status code should be 4xx, but was: " + statusCode);
    }

    /**
     * Assert response is server error (5xx status code)
     */
    public static void assertServerError(Response response) {
        int statusCode = response.getStatusCode();
        logger.info("Asserting server error response: {}", statusCode);
        Assert.assertTrue(statusCode >= 500 && statusCode < 600,
            "Status code should be 5xx, but was: " + statusCode);
    }

    /**
     * Assert content type
     */
    public static void assertContentType(Response response, String expectedContentType) {
        logger.info("Asserting content type: {}", expectedContentType);
        String actualContentType = response.getContentType();
        Assert.assertTrue(actualContentType.contains(expectedContentType),
            String.format("Expected content type '%s' but got '%s'", 
                expectedContentType, actualContentType));
    }

    /**
     * Assert JSON content type
     */
    public static void assertJsonContentType(Response response) {
        assertContentType(response, "application/json");
    }

    /**
     * Assert response is valid JSON
     */
    public static void assertValidJson(Response response) {
        logger.info("Asserting response is valid JSON");
        try {
            response.jsonPath().getMap("$");
        } catch (Exception e) {
            Assert.fail("Response is not valid JSON: " + e.getMessage());
        }
    }

    /**
     * Assert field matches regex pattern
     */
    public static void assertFieldMatchesPattern(Response response, String fieldPath, String regex) {
        logger.info("Asserting field '{}' matches pattern '{}'", fieldPath, regex);
        String value = response.jsonPath().getString(fieldPath);
        Assert.assertNotNull(value, "Field should exist: " + fieldPath);
        Assert.assertTrue(value.matches(regex),
            String.format("Field '%s' value '%s' does not match pattern '%s'", 
                fieldPath, value, regex));
    }

    /**
     * Assert email format
     */
    public static void assertValidEmail(Response response, String fieldPath) {
        String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
        assertFieldMatchesPattern(response, fieldPath, emailRegex);
    }

    /**
     * Assert all items in list have specific field
     */
    public static void assertAllItemsHaveField(Response response, String listPath, String fieldName) {
        logger.info("Asserting all items in '{}' have field '{}'", listPath, fieldName);
        List<Object> items = response.jsonPath().getList(listPath);
        Assert.assertFalse(items.isEmpty(), "List should not be empty");
        
        for (int i = 0; i < items.size(); i++) {
            String itemFieldPath = String.format("%s[%d].%s", listPath, i, fieldName);
            assertFieldExists(response, itemFieldPath);
        }
    }
}
```

---

## 🤔 Understanding JSON Schemas

### What is JSON Schema?

JSON Schema is a vocabulary that allows you to:
- Validate the structure of JSON data
- Define data types and constraints
- Document your API contract
- Ensure API compatibility

### Schema Validation Benefits

| Benefit | Description |
|---------|-------------|
| **Contract Testing** | Ensures API doesn't break unexpectedly |
| **Type Safety** | Validates field types (string, number, etc.) |
| **Required Fields** | Ensures mandatory fields are present |
| **Format Validation** | Validates email, date, URL formats |
| **Documentation** | Schema serves as API documentation |

### Schema Keywords

| Keyword | Purpose | Example |
|---------|---------|---------|
| `type` | Define data type | `"type": "string"` |
| `required` | Mandatory fields | `"required": ["id", "name"]` |
| `minimum` | Minimum numeric value | `"minimum": 1` |
| `maxLength` | Maximum string length | `"maxLength": 100` |
| `format` | String format | `"format": "email"` |
| `additionalProperties` | Allow extra fields | `"additionalProperties": false` |

---

## ✅ DO and ❌ DON'T

### Test Data Management

| ✅ DO | ❌ DON'T |
|------|---------|
| Keep test data in separate files | Hardcode test data in tests |
| Use meaningful file names | Use generic names like "data.xlsx" |
| Version control test data files | Put sensitive data in test files |
| Validate test data before using | Assume data format is correct |
| Document test data structure | Leave test data undocumented |

### RetryAnalyzer Usage

| ✅ DO | ❌ DON'T |
|------|---------|
| Use for genuinely flaky tests | Use to hide real bugs |
| Set reasonable retry count (2-3) | Set high retry counts (10+) |
| Log retry attempts | Silently retry without logging |
| Investigate flaky tests | Ignore why tests are flaky |

### Custom Assertions

| ✅ DO | ❌ DON'T |
|------|---------|
| Create domain-specific assertions | Rewrite TestNG assertions |
| Provide clear error messages | Use generic error messages |
| Log assertion details | Skip logging |
| Make assertions reusable | Create one-time use assertions |

---

## ✅ Verification Checklist for Part 4

Before proceeding to Part 5, verify:

- [ ] `testdata/` folder created in `src/main/resources/`
- [ ] `posts.xlsx` created with sample data
- [ ] `users.json` created with valid JSON
- [ ] `testdata.csv` created with test scenarios
- [ ] `schemas/` folder created
- [ ] `post-schema.json` created with validation rules
- [ ] `user-schema.json` created with nested structure
- [ ] `RetryAnalyzer.java` implemented
- [ ] `CustomAssertions.java` created with all methods
- [ ] All files compile without errors
- [ ] Test data files are readable by utilities

---

## 🔗 Quick Verification Commands

```bash
# Verify files exist
ls src/main/resources/testdata/
ls src/main/resources/testdata/schemas/

# Compile code
mvn clean compile

# Validate JSON files
cat src/main/resources/testdata/users.json | python -m json.tool

# Check file sizes
du -sh src/main/resources/testdata/*
```

---

**✅ Part 4 Complete!**

You now have:
- ✅ Excel test data files
- ✅ JSON test data files
- ✅ CSV test data files
- ✅ JSON schema files for validation
- ✅ RetryAnalyzer for flaky tests
- ✅ CustomAssertions for reusable validations

**When ready, say "go to next part" for Part 5: Data-Driven Tests and API Chaining**

---

## What's Coming in Part 5?
- DataDrivenTest using Excel, JSON, CSV
- DataProvider implementation
- APIChainTest for workflow testing
- CRUD operation chains
- Real-world API scenarios
---
# RestAssured API Testing Framework - Phase 3: Advanced Features
## Part 5: Data-Driven Tests and API Chaining

---

## 🎯 What You'll Learn in Part 5
- Create data-driven tests using TestNG DataProvider
- Use Excel, JSON, and CSV data in tests
- Implement API chaining (use response from one API in another)
- Create end-to-end workflow tests
- Test complete CRUD operations in sequence

---

## Step 1: Create DataDrivenTest Class

Create file: `src/test/java/com/api/tests/DataDrivenTest.java`

```java
package com.api.tests;

import com.api.config.ConfigReader;
import com.api.models.Post;
import com.api.specifications.RequestSpecifications;
import com.api.utils.CSVReader;
import com.api.utils.ExcelReader;
import com.api.utils.JsonReader;
import io.qameta.allure.*;
import io.restassured.response.Response;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.util.List;
import java.util.Map;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

/**
 * DataDrivenTest - Tests using external data sources
 * Demonstrates data-driven testing with Excel, JSON, and CSV
 */
@Epic("Data-Driven Testing")
@Feature("External Data Sources")
public class DataDrivenTest {

    private static final Logger logger = LogManager.getLogger(DataDrivenTest.class);
    private static final ConfigReader config = ConfigReader.getInstance();

    /**
     * DataProvider - Read data from Excel
     */
    @DataProvider(name = "excelData")
    public Object[][] getExcelData() {
        String filePath = "src/main/resources/testdata/posts.xlsx";
        String sheetName = "Sheet1";
        
        List<Map<String, String>> data = ExcelReader.readExcel(filePath, sheetName);
        Object[][] testData = new Object[data.size()][3];

        for (int i = 0; i < data.size(); i++) {
            Map<String, String> row = data.get(i);
            testData[i][0] = Integer.parseInt(row.get("userId"));
            testData[i][1] = row.get("title");
            testData[i][2] = row.get("body");
        }

        logger.info("Loaded {} rows from Excel", testData.length);
        return testData;
    }

    /**
     * DataProvider - Read data from JSON
     */
    @DataProvider(name = "jsonData")
    public Object[][] getJsonData() {
        String filePath = "src/main/resources/testdata/users.json";
        List<Map<String, Object>> data = JsonReader.readJsonAsList(filePath);
        
        Object[][] testData = new Object[data.size()][1];
        for (int i = 0; i < data.size(); i++) {
            testData[i][0] = data.get(i);
        }

        logger.info("Loaded {} rows from JSON", testData.length);
        return testData;
    }

    /**
     * DataProvider - Read data from CSV
     */
    @DataProvider(name = "csvData")
    public Object[][] getCSVData() {
        String filePath = "src/main/resources/testdata/testdata.csv";
        List<Map<String, String>> data = CSVReader.readCSV(filePath);
        
        Object[][] testData = new Object[data.size()][3];
        for (int i = 0; i < data.size(); i++) {
            Map<String, String> row = data.get(i);
            testData[i][0] = Integer.parseInt(row.get("userId"));
            testData[i][1] = Integer.parseInt(row.get("postId"));
            testData[i][2] = Integer.parseInt(row.get("expectedStatusCode"));
        }

        logger.info("Loaded {} rows from CSV", testData.length);
        return testData;
    }

    /**
     * Test using Excel data
     */
    @Test(dataProvider = "excelData", description = "Create posts using Excel data")
    @Story("Excel Data-Driven Test")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify POST /posts creates posts with data from Excel file")
    public void testCreatePostFromExcel(int userId, String title, String body) {
        logger.info("Testing with Excel data - UserId: {}, Title: {}", userId, title);

        Post post = new Post(userId, title, body);

        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(post)
        .when()
                .post("/posts")
        .then()
                .spec(RequestSpecifications.getCreatedResponseSpec())
                .body("userId", equalTo(userId))
                .body("title", equalTo(title))
                .body("body", equalTo(body))
                .extract().response();

        int createdId = response.jsonPath().getInt("id");
        logger.info("✅ Post created with ID: {}", createdId);
        
        Assert.assertNotNull(createdId, "Created post should have an ID");
    }

    /**
     * Test using JSON data
     */
    @Test(dataProvider = "jsonData", description = "Validate user data from JSON")
    @Story("JSON Data-Driven Test")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify user data validation with data from JSON file")
    public void testUserDataFromJson(Map<String, Object> userData) {
        logger.info("Testing with JSON data - Name: {}", userData.get("name"));

        String email = (String) userData.get("email");
        String name = (String) userData.get("name");
        String username = (String) userData.get("username");

        // Validate email format
        Assert.assertTrue(email.contains("@"), "Email should contain @");
        Assert.assertTrue(email.contains("."), "Email should contain .");
        
        // Validate name is not empty
        Assert.assertFalse(name.isEmpty(), "Name should not be empty");
        
        // Validate username is not empty
        Assert.assertFalse(username.isEmpty(), "Username should not be empty");

        logger.info("✅ User data validated for: {}", userData.get("name"));
    }

    /**
     * Test using CSV data
     */
    @Test(dataProvider = "csvData", description = "Test various endpoints with CSV data")
    @Story("CSV Data-Driven Test")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify GET /posts/{id} returns expected status codes based on CSV data")
    public void testEndpointWithCSVData(int userId, int postId, int expectedStatusCode) {
        logger.info("Testing POST /{} with expected status: {}", postId, expectedStatusCode);

        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/posts/" + postId)
        .then()
                .extract().response();

        int actualStatusCode = response.getStatusCode();
        Assert.assertEquals(actualStatusCode, expectedStatusCode,
            String.format("Expected %d but got %d for post ID %d", 
                expectedStatusCode, actualStatusCode, postId));

        logger.info("✅ Status code matched: {} for post ID: {}", actualStatusCode, postId);
    }

    /**
     * Test with inline DataProvider
     */
    @DataProvider(name = "inlineData")
    public Object[][] getInlineData() {
        return new Object[][] {
            {1, "Test Title 1", "Test Body 1"},
            {2, "Test Title 2", "Test Body 2"},
            {1, "Test Title 3", "Test Body 3"}
        };
    }

    @Test(dataProvider = "inlineData", description = "Test with inline data provider")
    @Story("Inline Data Provider Test")
    @Severity(SeverityLevel.MINOR)
    public void testWithInlineData(int userId, String title, String body) {
        logger.info("Testing with inline data - UserId: {}, Title: {}", userId, title);

        Post post = Post.builder()
                .userId(userId)
                .title(title)
                .body(body)
                .build();

        Response response = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(post)
        .when()
                .post("/posts")
        .then()
                .statusCode(201)
                .extract().response();

        logger.info("✅ Post created successfully");
    }
}
```

---

## Step 2: Create APIChainTest Class

Create file: `src/test/java/com/api/tests/APIChainTest.java`

```java
package com.api.tests;

import com.api.models.Post;
import com.api.models.User;
import com.api.specifications.RequestSpecifications;
import io.qameta.allure.*;
import io.restassured.response.Response;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.Assert;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

/**
 * APIChainTest - Tests that chain multiple API calls
 * Uses response from one API as input to another
 */
@Epic("API Chaining")
@Feature("Dependent API Calls")
public class APIChainTest {

    private static final Logger logger = LogManager.getLogger(APIChainTest.class);

    /**
     * Scenario: Get user → Create post for that user → Verify post
     */
    @Test(priority = 1, description = "Chain: Get User → Create Post → Verify")
    @Story("End-to-End API Chain")
    @Severity(SeverityLevel.BLOCKER)
    @Description("Test complete workflow: fetch user, create post, verify post")
    public void testCompleteAPIChain() {
        logger.info("Starting API Chain Test");

        // Step 1: Get a user
        logger.info("Step 1: Fetching user details");
        Response userResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/users/1")
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec())
                .extract().response();

        User user = userResponse.as(User.class);
        logger.info("Retrieved user: {} (ID: {})", user.getName(), user.getId());

        // Step 2: Create a post for this user
        logger.info("Step 2: Creating post for user {}", user.getId());
        Post newPost = Post.builder()
                .userId(user.getId())
                .title("Post by " + user.getName())
                .body("This is a post created via API chaining test")
                .build();

        Response createResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(newPost)
        .when()
                .post("/posts")
        .then()
                .spec(RequestSpecifications.getCreatedResponseSpec())
                .body("userId", equalTo(user.getId()))
                .extract().response();

        int createdPostId = createResponse.jsonPath().getInt("id");
        logger.info("Created post with ID: {}", createdPostId);

        // Step 3: Verify the created post
        logger.info("Step 3: Verifying created post");
        Response verifyResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/posts/" + createdPostId)
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec())
                .body("id", equalTo(createdPostId))
                .body("userId", equalTo(user.getId()))
                .body("title", containsString(user.getName()))
                .extract().response();

        Post verifiedPost = verifyResponse.as(Post.class);
        Assert.assertEquals(verifiedPost.getUserId(), user.getId());
        Assert.assertEquals(verifiedPost.getId(), createdPostId);

        logger.info("✅ API Chain completed successfully");
    }

    /**
     * Scenario: Get all users → Get posts for each user → Verify count
     */
    @Test(priority = 2, description = "Get all users and their posts")
    @Story("Bulk Data Processing")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify all users have posts by chaining GET /users and GET /posts?userId={id}")
    public void testGetAllUsersAndTheirPosts() {
        logger.info("Starting bulk user-posts test");

        // Step 1: Get all users
        Response usersResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/users")
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec())
                .extract().response();

        User[] users = usersResponse.as(User[].class);
        logger.info("Retrieved {} users", users.length);

        // Step 2: For each user, get their posts
        for (User user : users) {
            logger.info("Fetching posts for user: {} (ID: {})", user.getName(), user.getId());

            Response postsResponse = given()
                    .spec(RequestSpecifications.getBaseRequestSpec())
                    .queryParam("userId", user.getId())
            .when()
                    .get("/posts")
            .then()
                    .spec(RequestSpecifications.getSuccessResponseSpec())
                    .body("", hasSize(greaterThan(0)))
                    .extract().response();

            int postCount = postsResponse.jsonPath().getList("$").size();
            logger.info("User {} has {} posts", user.getName(), postCount);
            Assert.assertTrue(postCount > 0, "User should have at least one post");
        }

        logger.info("✅ All users have posts verified");
    }

    /**
     * Scenario: Create → Update → Delete (Full CRUD chain)
     */
    @Test(priority = 3, description = "Complete CRUD operation chain")
    @Story("CRUD Chain")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Test CREATE → READ → UPDATE → DELETE operations in sequence")
    public void testCRUDChain() {
        logger.info("Starting CRUD chain test");

        // CREATE
        logger.info("Step 1: CREATE - Creating new post");
        Post newPost = Post.builder()
                .userId(1)
                .title("CRUD Test Post")
                .body("Testing complete CRUD operations")
                .build();

        Response createResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(newPost)
        .when()
                .post("/posts")
        .then()
                .spec(RequestSpecifications.getCreatedResponseSpec())
                .extract().response();

        int postId = createResponse.jsonPath().getInt("id");
        logger.info("Created post with ID: {}", postId);

        // READ
        logger.info("Step 2: READ - Fetching created post");
        Response readResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/posts/" + postId)
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec())
                .body("id", equalTo(postId))
                .extract().response();

        logger.info("Successfully read post: {}", readResponse.jsonPath().getString("title"));

        // UPDATE
        logger.info("Step 3: UPDATE - Updating the post");
        Post updatedPost = Post.builder()
                .userId(1)
                .id(postId)
                .title("Updated CRUD Test Post")
                .body("This post has been updated")
                .build();

        Response updateResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .body(updatedPost)
        .when()
                .put("/posts/" + postId)
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec())
                .body("title", equalTo("Updated CRUD Test Post"))
                .extract().response();

        logger.info("Post updated successfully");

        // DELETE
        logger.info("Step 4: DELETE - Deleting the post");
        given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .delete("/posts/" + postId)
        .then()
                .spec(RequestSpecifications.getSuccessResponseSpec());

        logger.info("Post deleted successfully");
        logger.info("✅ Complete CRUD chain executed successfully");
    }

    /**
     * Scenario: Create multiple posts → Get all posts by user → Verify count
     */
    @Test(priority = 4, description = "Create multiple posts and verify")
    @Story("Multiple Resource Creation")
    @Severity(SeverityLevel.NORMAL)
    public void testCreateMultiplePostsAndVerify() {
        logger.info("Creating multiple posts for user");

        int userId = 1;
        int postsToCreate = 3;
        int[] createdPostIds = new int[postsToCreate];

        // Create multiple posts
        for (int i = 0; i < postsToCreate; i++) {
            Post post = Post.builder()
                    .userId(userId)
                    .title("Bulk Test Post " + (i + 1))
                    .body("Post body " + (i + 1))
                    .build();

            Response response = given()
                    .spec(RequestSpecifications.getBaseRequestSpec())
                    .body(post)
            .when()
                    .post("/posts")
            .then()
                    .statusCode(201)
                    .extract().response();

            createdPostIds[i] = response.jsonPath().getInt("id");
            logger.info("Created post {}/{} with ID: {}", i + 1, postsToCreate, createdPostIds[i]);
        }

        // Verify all posts were created
        Response allPostsResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .queryParam("userId", userId)
        .when()
                .get("/posts")
        .then()
                .statusCode(200)
                .extract().response();

        int totalPosts = allPostsResponse.jsonPath().getList("$").size();
        logger.info("User {} has total {} posts", userId, totalPosts);

        Assert.assertTrue(totalPosts >= postsToCreate, 
            "Should have at least " + postsToCreate + " posts");

        logger.info("✅ Multiple posts created and verified successfully");
    }

    /**
     * Scenario: Get user → Get user's posts → Get comments on first post
     */
    @Test(priority = 5, description = "Three-level API chain")
    @Story("Multi-level API Chain")
    @Severity(SeverityLevel.NORMAL)
    @Description("Chain three API calls: User → Posts → Comments")
    public void testThreeLevelAPIChain() {
        logger.info("Starting three-level API chain");

        // Level 1: Get user
        logger.info("Level 1: Getting user");
        Response userResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
        .when()
                .get("/users/1")
        .then()
                .statusCode(200)
                .extract().response();

        int userId = userResponse.jsonPath().getInt("id");
        logger.info("User ID: {}", userId);

        // Level 2: Get user's posts
        logger.info("Level 2: Getting posts for user {}", userId);
        Response postsResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .queryParam("userId", userId)
        .when()
                .get("/posts")
        .then()
                .statusCode(200)
                .extract().response();

        int firstPostId = postsResponse.jsonPath().getInt("[0].id");
        logger.info("First post ID: {}", firstPostId);

        // Level 3: Get comments on first post
        logger.info("Level 3: Getting comments for post {}", firstPostId);
        Response commentsResponse = given()
                .spec(RequestSpecifications.getBaseRequestSpec())
                .queryParam("postId", firstPostId)
        .when()
                .get("/comments")
        .then()
                .statusCode(200)
                .body("", hasSize(greaterThan(0)))
                .extract().response();

        int commentCount = commentsResponse.jsonPath().getList("$").size();
        logger.info("Post {} has {} comments", firstPostId, commentCount);

        Assert.assertTrue(commentCount > 0, "Post should have comments");

        logger.info("✅ Three-level API chain completed successfully");
    }
}
```

---

## 🤔 Understanding Data-Driven Testing

### Why Data-Driven Testing?

**Benefits:**
- ✅ **Reusability**: Same test logic for multiple data sets
- ✅ **Maintainability**: Update data without changing code
- ✅ **Coverage**: Test more scenarios with less code
- ✅ **Separation**: Test data separate from test logic
- ✅ **Collaboration**: Non-technical users can update data

### Data-Driven Flow

```
Test Data File → DataProvider → Test Method → Assert
     ↓               ↓              ↓             ↓
 (Excel/JSON)   (Read data)   (Execute API)  (Verify)
```

### DataProvider vs Hardcoded Data

**Without DataProvider (Bad):**
```java
@Test
public void testPost1() {
    createPost(1, "Title 1", "Body 1");
}

@Test
public void testPost2() {
    createPost(2, "Title 2", "Body 2");
}

@Test
public void testPost3() {
    createPost(1, "Title 3", "Body 3");
}
// Need to write 100 test methods for 100 data sets!
```

**With DataProvider (Good):**
```java
@DataProvider(name = "postData")
public Object[][] getData() {
    return ExcelReader.readExcel("posts.xlsx", "Sheet1");
}

@Test(dataProvider = "postData")
public void testCreatePost(int userId, String title, String body) {
    createPost(userId, title, body);
}
// One test method handles all 100 data sets!
```

---

## 🤔 Understanding API Chaining

### Why API Chaining?

**Real-world scenarios require multiple API calls:**
- Create user → Login → Update profile → Logout
- Search product → Add to cart → Checkout → Payment
- Create order → Get order details → Update order → Cancel order

### API Chain Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Sequential** | Each API depends on previous | Create → Read → Update → Delete |
| **Hierarchical** | Parent-child relationships | User → Posts → Comments |
| **Bulk Operations** | Multiple similar calls | Create 10 posts → Verify all |
| **Conditional** | Based on response | If user exists → Update, else Create |

### Chaining Best Practices

**✅ DO:**
```java
// Extract IDs for next call
int userId = response.jsonPath().getInt("id");
int postId = createPost(userId);
verifyPost(postId);
```

**❌ DON'T:**
```java
// Hardcode IDs
int userId = 1; // What if user 1 doesn't exist?
int postId = 100; // Assumes post 100 exists
```

---

## ✅ DO and ❌ DON'T

### Data-Driven Testing

| ✅ DO | ❌ DON'T |
|------|---------|
| Use descriptive DataProvider names | Use generic names like "data1" |
| Validate data before using | Assume data is always valid |
| Log which data set is being tested | Skip data identification |
| Handle empty or null data | Assume data always exists |
| Use appropriate data source | Use Excel for simple data |

### API Chaining

| ✅ DO | ❌ DON'T |
|------|---------|
| Extract IDs from responses | Hardcode IDs |
| Validate each step | Only validate final result |
| Log each step clearly | Skip intermediate logging |
| Handle failures gracefully | Let chain break silently |
| Clean up created resources | Leave test data in system |

---

## 🔧 Troubleshooting

### Issue 1: DataProvider Returns Empty

**Error:**
```
No tests found in class
```

**Solution:**
```java
// Check DataProvider returns data
@DataProvider(name = "testData")
public Object[][] getData() {
    Object[][] data = readData();
    logger.info("DataProvider loaded {} rows", data.length);
    Assert.assertTrue(data.length > 0, "DataProvider should return data");
    return data;
}
```

### Issue 2: API Chain Breaks

**Problem:** Test fails in middle of chain

**Solution:**
```java
// Add validation at each step
@Test
public void testAPIChain() {
    // Step 1
    int userId = createUser();
    Assert.assertTrue(userId > 0, "User creation failed");
    
    // Step 2
    int postId = createPost(userId);
    Assert.assertTrue(postId > 0, "Post creation failed");
    
    // Step 3
    verifyPost(postId);
}
```

### Issue 3: Data Type Mismatch

**Error:**
```
ClassCastException: String cannot be cast to Integer
```

**Solution:**
```java
// Parse data types correctly
@DataProvider
public Object[][] getData() {
    List<Map<String, String>> data = readCSV("data.csv");
    for (Map<String, String> row : data) {
        // Convert string to appropriate type
        int userId = Integer.parseInt(row.get("userId"));
        testData[i][0] = userId;
    }
}
```

### Issue 4: Parallel Execution with DataProvider

**Problem:** Data providers run in parallel causing issues

**Solution:**
```java
// Make DataProvider thread-safe
@DataProvider(name = "data", parallel = false)
public Object[][] getData() {
    // Read data safely
}

// Or use thread-local storage
```

---

## ✅ Verification Checklist for Part 5

Before proceeding to Part 6, verify:

- [ ] `DataDrivenTest.java` created in `src/test/java/com/api/tests/`
- [ ] Excel DataProvider working correctly
- [ ] JSON DataProvider loading data
- [ ] CSV DataProvider parsing files
- [ ] `APIChainTest.java` created with all chain scenarios
- [ ] Complete CRUD chain test passing
- [ ] Multi-level API chain working
- [ ] All tests compile without errors
- [ ] Tests execute successfully
- [ ] Proper logging in all tests

---

## 🔗 Quick Test Commands

```bash
# Run data-driven tests
mvn test -Dtest=DataDrivenTest

# Run specific data-driven test method
mvn test -Dtest=DataDrivenTest#testCreatePostFromExcel

# Run API chain tests
mvn test -Dtest=APIChainTest

# Run all Phase 3 tests
mvn test

# Run with specific data file
mvn test -DdataFile=posts.xlsx
```

---

## 📊 Expected Test Results

After running DataDrivenTest:
```
✅ testCreatePostFromExcel - 5 iterations (one per Excel row)
✅ testUserDataFromJson - 5 iterations (one per JSON object)
✅ testEndpointWithCSVData - 7 iterations (one per CSV row)
✅ testWithInlineData - 3 iterations (inline data)
Total: 20 test executions
```

After running APIChainTest:
```
✅ testCompleteAPIChain - 1 execution (3 API calls)
✅ testGetAllUsersAndTheirPosts - 1 execution (11 API calls: 1 + 10)
✅ testCRUDChain - 1 execution (4 API calls)
✅ testCreateMultiplePostsAndVerify - 1 execution (4 API calls)
✅ testThreeLevelAPIChain - 1 execution (3 API calls)
Total: 5 test executions with 25 API calls
```

---

**✅ Part 5 Complete!**

You now have:
- ✅ Data-driven tests with Excel, JSON, CSV
- ✅ TestNG DataProvider implementations
- ✅ API chaining scenarios
- ✅ Complete CRUD workflow tests
- ✅ Multi-level API chains
- ✅ Bulk operation handling
---
