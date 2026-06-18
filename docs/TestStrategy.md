# RR QA Automation Assignment - Test Strategy

## 1. Objective

The objective of this test strategy is to validate the functionality, reliability, and usability of the TMDB Discover demo application.

The testing effort focuses on:

* Filter functionality
* Pagination behavior
* UI and API consistency
* Negative scenarios
* Known application limitations
* Regression coverage

The goal is to identify defects, provide reliable automated validation, and demonstrate maintainable test automation practices.

---

## 2. Abbreviations

| Acronym | Description                       |
| ------- | --------------------------------- |
| TMDB    | The Movie Database                |
| API     | Application Programming Interface |
| CI      | Continuous Integration            |

---

## 3. Application Under Test

**URL**

https://tmdb-discover.surge.sh/

The application allows users to discover Movies and TV Shows using various filtering criteria.

### Supported Filters

#### Category

* Popular
* Trending
* Newest
* Top Rated

#### Additional Filters

* Title Search
* Type

  * Movie
  * TV Show
* Year of Release
* Rating
* Genre

### Additional Functionality

* Pagination

### Known Issues

* Refreshing pages with route slugs may fail.
* Pagination may fail on the last few pages.

---

## 4. Test Scope

### In Scope

#### Filtering

* Category selection
* Title search
* Type filter
* Year filter
* Rating filter
* Genre filter
* Combined filter behavior

#### Pagination

* Next page navigation
* Previous page navigation
* Page number selection
* Data refresh during pagination

#### API Validation

* API response status
* API response structure
* UI data matches API data

#### Error Handling

* Invalid filter combinations
* Empty search results
* Known route refresh issues

---

### Out of Scope

* Performance testing
* Security testing
* Accessibility testing
* Cross-browser compatibility testing
* Mobile responsiveness testing
* Backend API contract testing

These areas are excluded because they are outside the scope of the assignment.

---

## 5. Testing Approach

### Functional Testing

Validate application behavior from an end-user perspective.

**Example**

**Scenario:** User selects **Top Rated**

**Expected Result:** Only top-rated content should be displayed.

---

### UI Testing

Validate:

* Visibility
* Filter interaction
* Pagination interaction
* Search functionality

---

### API Validation

Browser network calls will be intercepted and validated.

**Checks**

* Status code
* Response payload
* Returned content count
* Consistency with UI

**Example**

Movie title displayed in the UI should match the API response.

---

### Negative Testing

Examples:

* Search for a non-existing title
* Invalid year combinations
* Navigate beyond available pages
* Refresh direct route URLs

---

## 6. Test Design Techniques

The following test design techniques will be used.

### Equivalence Partitioning

**Example: Rating Filter**

| Valid Inputs | Invalid Inputs  |
| ------------ | --------------- |
| 0 - 10       | Less than 0     |
|              | Greater than 10 |

---

### Boundary Value Analysis

#### Pagination

* First page
* Second page
* Last page
* Last page minus one

#### Year

* Earliest supported year
* Current year
* Future year

---

### Decision Table Testing

Example combinations:

| Type    | Genre  |
| ------- | ------ |
| Movie   | Action |
| Movie   | Comedy |
| TV Show | Drama  |
| TV Show | Sci-Fi |

Expected combinations will be validated.

---

### Exploratory Testing

Additional exploratory testing will be performed around:

* Routing
* Pagination
* Multiple filters
* State retention

---

## 7. Risk Analysis

| Area            | Risk                     | Impact |
| --------------- | ------------------------ | ------ |
| Filtering       | Incorrect data displayed | High   |
| Search          | Missing results          | High   |
| Pagination      | Navigation failure       | High   |
| Routing         | Broken deep links        | Medium |
| API Integration | UI/API mismatch          | High   |

---

## 8. Automation Strategy

### Framework

* Python
* Playwright
* PyTest

### Design Pattern

* Page Object Model (POM)

### Supporting Components

* Logging
* HTML Reporting
* Screenshot Capture
* API Assertions

### Execution Types

* Local Execution
* CI Execution

---

## 9. Entry Criteria

* Application is accessible
* Dependencies are installed
* Test environment is available

---

## 10. Exit Criteria

Testing is considered complete when:

* All planned scenarios are executed
* Critical defects are documented
* Reports are generated
* Evidence is attached
* Automation suite passes successfully

---

## 11. Deliverables

The final submission will include:

* Test Strategy
* Test Case Document
* Automated Test Suite
* HTML Reports
* Logs
* Screenshots
* Defect Report
* CI Integration Approach
* Source Code Repository

