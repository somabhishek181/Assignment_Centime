**Project Overview:**
This project leverages Python, Selenium WebDriver, and Pytest to create an automated testing framework. 
I use the Page Object Model (POM) design pattern to organize the code for easier maintenance and scalability.


**Setup Instructions:**
Before running tests, ensure your environment is ready:
1. Install Python: Make sure Python 3.x is installed
2. Install Dependencies: Install the required Python packages by running the following command:
   pip install -r requirements.txt
3. Download WebDriver: For Chrome:Download the appropriate version of ChromeDriver for your Chrome browser.
    Ensure the WebDriver executable is added to your system PATH.

**How to Run the Tests**
    We can run the tests as a whole or individually based on our needs.
    **Run All Tests:** To run the entire test suite and generate an HTML report:
        pytest --html=report.html 
    **Run a Specific Test File**
        pytest tests/test_addressPage.py --html=address_report.html 
    **Run Tests by Marker**
        pytest -m login --html=login_report.html --self-contained-html

**Test Case Details**:
1. **TestAccountPage (tests/test_account_page.py)**
   * test_Registration: Automates user registration and verifies the success message.
   * test_Login: Tests login functionality using valid credentials.
2. **TestAddressPage (tests/test_addressPage.py)**
   *   test_billingAddress: Fills in billing details, selects country and state, saves, and verifies the success message.

3. **TestCartPage (tests/test_cartPage.py)**
    * test_CartPage: Adds products to the cart, retrieves, and validates product details.
    * test_removeItems_Cart: Removes a product from the cart and verifies the removal.

**Folder Structure:**
Project/
├── POMpages/                   # Contains Page Object Model classes
│   ├── AccountPage.py          # For Registration and Login actions
│   ├── AddressPage.py          # For Address management actions
│   ├── CartPage.py             # For Shopping Cart-related actions
├── tests/                      # Contains test files
│   ├── test_account_page.py    # Tests for Registration and Login
│   ├── test_addressPage.py     # Tests for Address Management
│   ├── test_cartPage.py        # Tests for Shopping Cart functionality
├── utilities/                  # Utility files like base classes and fixtures
│   ├── BaseClass.py            # Base class for setup and reusable methods
│   ├── conftest.py             # Common pytest fixtures
└── README.md                   # Instructions to execute the test suite

**Generating HTML Reports**
An HTML report is generated after test execution. Open the file (e.g., report.html) in any browser to view detailed results, 
including:
* Test statuses (passed, failed, or skipped).
* Logs and stack traces for debugging.
* Timestamps for execution.
