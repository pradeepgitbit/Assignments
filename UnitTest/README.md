Below is a **simple sample Java project** that demonstrates:

* **Unit Tests** → using **JUnit**
* **Integration Tests** → testing service + repository together
* **End-to-End Tests (E2E)** → using **Selenium**
* **Build tool** → Maven
* Includes a **README.md**

The example app is a small **User Management System**.

---

# 1. Project Structure

```
sample-testing-app/
│
├── pom.xml
├── README.md
│
├── src/
│   ├── main/
│   │   └── java/com/example/app/
│   │       ├── model/
│   │       │   └── User.java
│   │       ├── repository/
│   │       │   └── UserRepository.java
│   │       ├── service/
│   │       │   └── UserService.java
│   │       └── controller/
│   │           └── UserController.java
│
│   └── test/
│       └── java/com/example/app/
│           ├── unit/
│           │   └── UserServiceTest.java
│           │
│           ├── integration/
│           │   └── UserIntegrationTest.java
│           │
│           └── e2e/
│               └── UserE2ETest.java
```

---

# 2. pom.xml (Dependencies)

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>sample-testing-app</artifactId>
    <version>1.0</version>

    <dependencies>

        <!-- JUnit 5 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>

        <!-- TestNG -->
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>7.8.0</version>
            <scope>test</scope>
        </dependency>

        <!-- Selenium -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>4.19.0</version>
        </dependency>

    </dependencies>

</project>
```

---

# 3. Application Code

## User Model

```java
package com.example.app.model;

public class User {

    private int id;
    private String name;
    private String email;

    public User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }
}
```

---

## Repository

```java
package com.example.app.repository;

import com.example.app.model.User;
import java.util.*;

public class UserRepository {

    private List<User> users = new ArrayList<>();

    public void save(User user) {
        users.add(user);
    }

    public List<User> findAll() {
        return users;
    }

    public User findById(int id) {
        return users.stream()
                .filter(u -> u.getId() == id)
                .findFirst()
                .orElse(null);
    }
}
```

---

## Service

```java
package com.example.app.service;

import com.example.app.model.User;
import com.example.app.repository.UserRepository;

public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public void registerUser(User user) {
        repository.save(user);
    }

    public User getUser(int id) {
        return repository.findById(id);
    }
}
```

---

# 4. Unit Test (JUnit)

Tests **single class logic only**

```
src/test/java/com/example/app/unit/UserServiceTest.java
```

```java
package com.example.app.unit;

import com.example.app.model.User;
import com.example.app.repository.UserRepository;
import com.example.app.service.UserService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UserServiceTest {

    @Test
    void testRegisterUser() {

        UserRepository repo = new UserRepository();
        UserService service = new UserService(repo);

        User user = new User(1,"John","john@test.com");
        service.registerUser(user);

        assertEquals(1, repo.findAll().size());
    }
}
```

---

# 5. Integration Test

Tests **multiple layers working together**

```
src/test/java/com/example/app/integration/UserIntegrationTest.java
```

```java
package com.example.app.integration;

import com.example.app.model.User;
import com.example.app.repository.UserRepository;
import com.example.app.service.UserService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UserIntegrationTest {

    @Test
    void testUserFlow() {

        UserRepository repo = new UserRepository();
        UserService service = new UserService(repo);

        service.registerUser(new User(1,"Alice","alice@test.com"));

        User result = service.getUser(1);

        assertNotNull(result);
        assertEquals("Alice", result.getName());
    }
}
```

---

# 6. End-to-End Test (Selenium)

Simulates **real user browser interaction**

```
src/test/java/com/example/app/e2e/UserE2ETest.java
```

```java
package com.example.app.e2e;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.testng.annotations.*;

public class UserE2ETest {

    WebDriver driver;

    @BeforeTest
    public void setup() {
        driver = new ChromeDriver();
    }

    @Test
    public void testLoginPage() {

        driver.get("https://example.com/login");

        driver.findElement(By.id("username")).sendKeys("testuser");
        driver.findElement(By.id("password")).sendKeys("password");

        driver.findElement(By.id("loginBtn")).click();
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
    }
}
```

---

# 7. README.md

```markdown
# Sample Testing Application

This project demonstrates different testing approaches in Java:

- Unit Testing using JUnit
- Integration Testing
- End-to-End Testing using Selenium
- TestNG for test execution

---

## Technologies

- Java
- Maven
- JUnit 5
- TestNG
- Selenium WebDriver

---

## Project Structure

src/main/java
Application source code

src/test/java
Unit, integration, and end-to-end tests

---

## Running Tests

Run all tests:

```

mvn test

```

Run TestNG tests:

```

mvn test -DsuiteXmlFile=testng.xml

```

---

## Test Types

### Unit Tests
Test individual classes.

Example:
UserServiceTest

### Integration Tests
Test interaction between modules.

Example:
UserIntegrationTest

### End-to-End Tests
Simulate user behaviour using Selenium.

Example:
UserE2ETest

---

## Requirements

- Java 17+
- Maven
- ChromeDriver for Selenium

---

## Future Improvements

- Add Spring Boot
- Add CI/CD pipeline
- Add Docker support
```

---

# 8. How Tests Work (Quick Summary)

| Test Type   | What it Tests                  |
| ----------- | ------------------------------ |
| Unit        | Single method/class            |
| Integration | Service + Repository           |
| E2E         | Full application using browser |

---


