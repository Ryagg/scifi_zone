## **Testing User Stories**

### **User Requirements and Expectations**

The following user requirements and expectations were developed based on the user stories.

#### **Expectation 1: being able to view a list of tickets**

-   Requirement: allow users to easily access an overview of available tickets
-   Implementation: both the page for all tickets and the page for all packages can be accessed through the navbar. The sticky navbar at the top of the page furthermore facilitates easy navigation. See the screenshots [here](documentation/testing/usertests/user-expectation-1.jpg), [here](documentation/testing/usertests/user-expectation-1-example-2.jpg), and [here](documentation/testing/usertests/user-expectation-1-example-3.jpg).

![user-expectation-1](documentation/testing/usertests/user-expectation-1.jpg)

![user-expectation-1-example-2](documentation/testing/usertests/user-expectation-1-example-2.jpg)

![user-expectation-1-example-3](documentation/testing/usertests/user-expectation-1-example-3.jpg)

#### **Expectation 2: being able to see a specific category of tickets**

-   Requirement: allow users to filter for ticket categories
-   Implementation: In addition to the navbar providing links to the tickets and packages pages and all tickets in each category being displayed there (see screenshots above), Django-Watson was used to implement full-text search across all relevant models.

![user-expectation-2](documentation/testing/usertests/user-expectation-2.jpg)

#### **Expectation 3: being able to see details about the tickets**

-   Requirement: give users detailed information about each ticket
-   Implementation: Views with detailed information about each ticket for each category were created. See examples [here](documentation/testing/usertests/user-expectation-3.jpg), [here](documentation/testing/usertests/user-expectation-3-example-2.jpg), and [here](documentation/testing/usertests/user-expectation-3-example-3.jpg).

![user-expectation-3](documentation/testing/usertests/user-expectation-3.jpg)

![user-expectation-3-example-2](documentation/testing/usertests/user-expectation-3-example-2.jpg)

![user-expectation-3-example-3](documentation/testing/usertests/user-expectation-3-example-3.jpg)

#### **Expectation 4: Being able to easily register an account and view the profile**

-   Requirement: Allow users to register an account and attach a profile
-   Implementation: For the registration, the built-in Django functionality was used. A profile app was created to store relevant information and display it on the user's profile page. See the profile for a new user [here](documentation/testing/usertests/user-expectation-4.jpg)

![user-expectation-4](documentation/testing/usertests/user-expectation-4.jpg)

#### **Expectation 5: Being able to verify the account registration was successful**

-   Requirement: Notify users about the account creation
-   Implementation: The built-in Django functionality was used for user registration and e-mail confirmation. See an example of the confirmation email [here](documentation/testing/usertests/user-expectation-5.jpg)

![user-expectation-5](documentation/testing/usertests/user-expectation-5.jpg)

#### **Expectation 6: being able to access a personalized user profile**

-   Requirement: Attach the order information to the user profile, display an order history on the profile page, and allow users to update their information.
-   Implementation: The checkout and profile views handle the business logic. The order history and billing address form are displayed on the [profile page](documentation/testing/usertests/user-expectation-6.jpg)

![user-expectation-6](documentation/testing/usertests/user-expectation-6.jpg)

#### **Expectation 7: being able to recover the account password**

-   Requirement: Allow users to reset their password and verify that the user is the account owner.
-   Implementation: The built-in Django functionality was used for this feature. Therefore, only one exemplary screenshot can be found [here](documentation/testing/usertests/user-expectation-7.jpg) to show how the template was adapted to style the site's theme.

![user-expectation-7](documentation/testing/usertests/user-expectation-7.jpg)

#### **Expectation 8: being able to sort specific categories of tickets**

-   Requirement: Add sort and direction parameters to corresponding views and the navbar.
-   Implementation: The maximum number of tickets per category is 3. Therefore, a sorting function would not add much to the user experience and has not been implemented.

#### **Expectation 9: being able to search for a ticket by category or actor name to easily find autograph or photoshoot tickets with selected actors**

-   Requirement: Implement a search function.
-   Implementation: Both tickets and actors can be found using the [search function](documentation/testing/usertests/user-expectation-9-example-4.jpg). The easiest way to find the autograph or photoshoot tickets with an actor is to view the detail pages for the [selected actor](documentation/testing/usertests/user-expectation-9-example-2.jpg). From there, autograph and photoshoot tickets can be added to the shopping bag. All actors in a price category can be viewed on the detail page for each [ticket category](documentation/testing/usertests/user-expectation-9-example-3.jpg).

![user-expectation-9-example-4](documentation/testing/usertests/user-expectation-9-example-4.jpg)
![user-expectation-9-example-2](documentation/testing/usertests/user-expectation-9-example-2.jpg)
![user-expectation-9-example-3](documentation/testing/usertests/user-expectation-9-example-3.jpg)

#### **Expectation 10: being able to see detailed bag contents and total cost**

-   Requirement: Use bag tools and contexts to calculate the sub-total and VAT, update the bag content, if applicable, and make the contents available on all pages.
-   Implementation: Views and a template to display bag contents using bag tools and contexts were created to display the [shopping bag](documentation/testing/usertests/user-expectation-10.jpg) to the user.

![user-expectation-10](documentation/testing/usertests/user-expectation-10.jpg)

#### **Expectation 11: being able to adjust the number of items in the bag before checkout**

-   Requirement: Same as above.
-   Implementation: The shopping bag display includes an input field where users can update the quantity for each item in the bag. See the screenshot [here](documentation/testing/usertests/user-expectation-11.jpg).

![user-expectation-11](documentation/testing/usertests/user-expectation-11.jpg)

#### **Expectation 12: being able to easily enter payment information**

-   Requirement: Provide an intuitive way for users to enter their payment information
-   Implementation: the [Stripe card element](documentation/testing/usertests/user-expectation-12.jpg) was used for checkout and styled to match the site's theme.

![user-expectation-12](documentation/testing/usertests/user-expectation-12.jpg)

#### **Expectation 13: being able to feel that the personal and payment information is safe and secure**

-   Requirement: Using Django middleware and additional tools like Django-CSP and Django-CORS to make the site as secure as possible. Using Stripe to handle payments, so that the user's payment information never touches the application's server.
-   Implementation: see requirement.

![user-expectation-13](documentation/testing/usertests/user-expectation-13.jpg)
![user-expectation-13-example-2](documentation/testing/usertests/user-expectation-13-example-2.jpg)

#### **Expectation 14: being able to view an order summary before checkout**

-   Requirement: Use bag tools and contexts to calculate the sub-total, update the bag content, if applicable, and make the contents available on all pages.
-   Implementation: Views and a template to display bag contents using bag tools and contexts were created to display the order summary on the checkout page. See an example [here](documentation/testing/usertests/user-expectation-14.jpg).

![user-expectation-14](documentation/testing/usertests/user-expectation-14.jpg)

#### **Expectation 15: receiving an email confirmation after checkout**

-   Requirement: Collect the user's email address, attach it to the order, and send a confirmation email after a successful checkout.
-   Implementation: The checkout view handles the business logic and generates an [order confirmation on screen](documentation/testing/usertests/user-expectation-15.jpg) after a successful checkout. The built-in Django functionality is used to send a [confirmation email](documentation/testing/usertests/user-expectation-15-example-2.jpg) to the user.

![user-expectation-15](documentation/testing/usertests/user-expectation-15.jpg)

![user-expectation-15-example-2](documentation/testing/usertests/user-expectation-15-example-2.jpg)

#### **Expectations 16-18**

Please note that for the following three expectations, an adjustment has been made! The expectations cover CRUD functionality for tickets. During the development process, I realized that all kinds of tickets for convention events (entrance tickets, autograph and photoshoot tickets, and combinations of them) are already implemented. I therefore decided to allow admins to add, edit, and delete actors to/from the event instead.

#### **Expectation 16: being able as a site owner to add actors to the event**

-   Requirement: check whether the user has admin privileges, create a form from the corresponding model, and let the authorized user update the database with the data for the new actor.
-   Implementation: A corresponding form, view, url, template, and navbar-item were generated. The view has a login-required decorator and checks whether the user is also a superuser. The navbar-item is only visible for superusers. See these screenshots for the [form](documentation/testing/usertests/user-expectation-16.jpg), [detail page with confirmation dialogue](documentation/testing/usertests/user-expectation-16-example-2.jpg), and [updated guests page](documentation/testing/usertests/user-expectation-16-example-3.jpg).

![user-expectation-16](documentation/testing/usertests/user-expectation-16.jpg)

![user-expectation-16-example-2](documentation/testing/usertests/user-expectation-16-example-2.jpg)

![user-expectation-16-example-3](documentation/testing/usertests/user-expectation-16-example-3.jpg)

#### **Expectation 17: being able as a site owner to edit an actor's information**

-   Requirement: similar to the above requirement. Provide a form, accessible only for superusers, to update the information and update the database.
-   Implementation: Links to the form to edit an actor's information are available for superusers both on the guests page and on the detail page for each guest. See screenshots [1](documentation/testing/usertests/user-expectation-17.jpg), [2](documentation/testing/usertests/user-expectation-17-example-2.jpg), [3](documentation/testing/usertests/user-expectation-17-example-3.jpg), and [4](documentation/testing/usertests/user-expectation-17-example-4.jpg).

![user-expectation-17](documentation/testing/usertests/user-expectation-17.jpg)
![user-expectation-17-example-2](documentation/testing/usertests/user-expectation-17-example-2.jpg)
![user-expectation-17-example-3](documentation/testing/usertests/user-expectation-17-example-3.jpg)
![user-expectation-17-example-4](documentation/testing/usertests/user-expectation-17-example-4.jpg)

#### **Expectation 18: being able as a site owner to remove an actor from the convention**

-   Requirement: access the corresponding object and remove it from the database
-   Implementation: Links to remove an actor were placed beneath the links to edit the actor's info. Only Superusers can access the links. After the actor has been removed from the database, the admin is redirected to the [updated guests page](documentation/testing/usertests/user-expectation-18.jpg) and a confirmation message is displayed.

![user-expectation-18](documentation/testing/usertests/user-expectation-18.jpg)

## **Functionality Testing**

---

---

## TO BE ADDED / SEE AUTOMATED TESTS

## **Validators**

---

---

### **W3C Markup Validator**

---

For validating my HTML code at first the source code from each page of the generated live site was copied and pasted into the validator on [W3C Markup Validation Service](https://validator.w3.org/). At first, several errors, e.g. regarding labels and missing closing tags, were reported. These errors have been fixed and the tests repeated. The last test runs were done using 'Check by address' for all pages except the bag, checkout, checkout success page, and add guest page. For these, the source code was used. The results are presented below:

**Result for homepage:**

-   No errors reported. Two warnings.

**Result for guests page:**

-   No errors or warnings reported.

**Result for timetable page:**

-   No errors or warnings reported.

**Result for tickets page:**

-   No errors or warnings reported.

**Result for ticket details page** (Photoshoot category A exemplary for all ticket details pages)

-   No errors or warnings reported after several fixes.

**Result for packages page:**

-   No errors or warnings reported.

**Result for package details page** (diamond package exemplary for all packages):

-   No errors or warnings reported after several fixes.

**Result for bag page**

-   No errors or warnings reported after several fixes.

**Result for checkout page**

-   No errors reported. Three warnings.

**Result for checkout success page**

-   No errors or warnings reported.

**Result for profile page**

-   No errors or warnings reported.

**Result for add guest page**

-   One error reported: "Attribute placeholder is only allowed when the input type is email, number, password, search, tel, text, or url"

**Result for site notice page**

-   No errors or warnings reported.

**Result for privacy policy page**

-   No errors or warnings reported.

### **W3C CSS Validator**

---

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) reported no errors when using 'Validate by direct input'. 34 warnings were reported due to vendor extensions. Using 'Validate by URI' leads to 9 errors. All those errors are from the bulma.min.css file. 259 warnings are reported in total. 12 warnings are for vendor extensions from my css-file, and the rest for vendor extensions from the bulma.min.css-file.

![w3c-css](documentation/testing/w3c-results/w3c-css.jpg)

### **WAVE Validator**

---

The [web accessibility evaluation tool](https://wave.webaim.org/) was used to check the site's accessibility features.

-   **Homepage:**

    All three alerts are caused by short paragraphs that to Wave appear to be headings.

    ![homepage](documentation/testing/wave-results/homepage.jpg)
    ![homepage-details](documentation/testing/wave-results/homepage-details.jpg)

---

-   **Guests page:**

    No errors or alerts reported.

    ![guests](documentation/testing/wave-results/guests.jpg)

---

-   **Guest detail page** (Jason Isaacs exemplary for all guest details pages):

    Both alerts are caused by short paragraphs that to Wave appear to be headings.

    ![guest-detail](documentation/testing/wave-results/guest-detail.jpg)
    ![guest-detail_details](documentation/testing/wave-results/guest-detail_details.jpg)

---

-   **Timetable page:**

    No errors or alerts reported.

![timetable](documentation/testing/wave-results/timetable.jpg)

---

-   **Tickets page:**

    Both alerts are caused by short paragraphs that to Wave appear to be headings.

    ![tickets](documentation/testing/wave-results/tickets.jpg)
    ![tickets_details](documentation/testing/wave-results/tickets_details.jpg)

---

-   **Ticket details page** (Autograph Ticket Price Category B including radio elements exemplary for all ticket details pages):

    No errors or alerts reported.

    ![autograph-ticket-detail](documentation/testing/wave-results/autograph-ticket-detail.jpg)

---

-   **Packages page:**

    One caused by a short paragraph that to Wave appears to be a heading.

    ![packages](documentation/testing/wave-results/packages.jpg)
    ![packages_details](documentation/testing/wave-results/packages_details.jpg)

---

-   **Package details page** (Diamond package exemplary for all packages):

    No errors or alerts reported.

    ![package-details](documentation/testing/wave-results/packages_details.jpg)

---

-   **Registration page:**

    One alert due to an redundant link.

    ![registration](documentation/testing/wave-results/registration.jpg)

---

-   **Login page:**

    No errors or alerts reported.

    ![login](documentation/testing/wave-results/login.jpg)
    ![registration-detail](documentation/testing/wave-results/registration-detail.jpg)

---

-   **Profile page:**

    Following the approach from the Boutique Ado walk-through, the labels for all form inputs were removed, and the content placed as placeholder text inside the input fields. This causes errors due to missing form labels on all pages including forms. For this page, 5 missing form labels and 1 missing select label are reported. Additionally, 3 alerts due to possible headings are reported.

    ![profile](documentation/testing/wave-results/profile.jpg)
    ![profile-detail](documentation/testing/wave-results/profile-detail.jpg)

---

-   **Add guest page:**

    Ten errors due to missing form labels are reported.

    ![add-guest](documentation/testing/wave-results/add-guest.jpg)

---

-   **Logout page:**

    No errors or alerts reported.

    ![logout](documentation/testing/wave-results/logout.jpg)

---

-   **Site notice page:**

    All alerts are caused by short paragraphs that to Wave appear to be a heading.

    ![site-notice](documentation/testing/wave-results/site-notice.jpg)

---

-   **Privacy policy:**

    No errors or alerts reported.

    ![privacy-policy](documentation/testing/wave-results/privacy-policy.jpg)

---

### **Lighthouse**

---

The results for both the mobile version and the desktop version are displayed. For the mobile version, the performance is lower than I'd prefer. The main factors are render-blocking resources (mainly bulma.min.css, jquery-3.6.0.min.js, base.css, and base.js) and are for the most part (external sources) outside of my control.

Please note that I only checked pages created by me.

-   **Homepage:**

**homepage-mobile:**

![homepage-mobile](documentation/testing/lighthouse-results/homepage-mobile.jpg)

**homepage-desktop:**

![homepage-desktop](documentation/testing/lighthouse-results/homepage-desktop.jpg)

-   **Guests page:**

**guests-mobile:**

![guests-mobile](documentation/testing/lighthouse-results/guests-mobile.jpg)

![guests-mobile_opportunities](documentation/testing/lighthouse-results/guests-mobile_opportunities.jpg)

**guests-desktop**:

![guests-desktop](documentation/testing/lighthouse-results/guests-desktop.jpg)

-   **Timetable page:**

**timetable-mobile:**

![timetable-mobile](documentation/testing/lighthouse-results/timetable-mobile.jpg)

**timetable-desktop:**

![timetable-desktop](documentation/testing/lighthouse-results/timetable-desktop.jpg)

-   **Tickets page:**

**tickets-mobile:**

![tickets-mobile](documentation/testing/lighthouse-results/tickets-mobile.jpg)

**tickets-desktop:**

![tickets-desktop](documentation/testing/lighthouse-results/tickets-desktop.jpg)

-   **Tickets detail page** (Autograph ticket price category B exemplary for all ticket details pages):

**ticket_detail-mobile:**

![ticket_detail-mobile](documentation/testing/lighthouse-results/ticket_detail-mobile.jpg)

**ticket_detail-desktop:**

![ticket_detail-desktop](documentation/testing/lighthouse-results/ticket_detail-desktop.jpg)

-   **Packages page:**

**packages-mobile:**

![packages-mobile](documentation/testing/lighthouse-results/packages-mobile.jpg)

**packages-desktop**:

![packages-desktop](documentation/testing/lighthouse-results/packages-desktop.jpg)

-   **Package detail page** (Diamond package exemplary for all package detail pages):

**package_detail-mobile:**

![package_detail-mobile](documentation/testing/lighthouse-results/package_detail-mobile.jpg)

**package_detail-desktop:**

![package_detail-desktop](documentation/testing/lighthouse-results/package_detail-desktop.jpg)

-   **Bag page:**

**bag-mobile:**

![bag-mobile](documentation/testing/lighthouse-results/bag-mobile.jpg)

**bag-desktop:**

![bag-desktop](documentation/testing/lighthouse-results/bag-desktop.jpg)

-   **Checkout page:**

**checkout-mobile:**

The performance for this page is very poor. Render-blocking resources cost 2.27 seconds, the total blocking time is 700ms, and both the first contentful paint with 3.7 seconds, and the largest contentful paint with 4.2 seconds take too long. I have no explanation for the huge discrepancy compared to the results for the desktop version below.

![checkout-mobile](documentation/testing/lighthouse-results/checkout-mobile.jpg)
![checkout-mobile_metrics](documentation/testing/lighthouse-results/checkout-mobile_metrics.jpg)
![checkout-mobile_opportunities](documentation/testing/lighthouse-results/checkout-mobile_opportunities.jpg)

**checkout-desktop:**

![checkout-desktop](documentation/testing/lighthouse-results/checkout-desktop.jpg)

-   **Checkout success page:**

**checkout-success_mobile:**

![checkout-success_mobile](documentation/testing/lighthouse-results/checkout-success_mobile.jpg)

**checkout-success-desktop:**

![checkout-success_mobile](documentation/testing/lighthouse-results/checkout-success_desktop.jpg)

-   **Profile page:**

**profile-mobile:**

![profile-mobile](documentation/testing/lighthouse-results/profile-mobile.jpg)

**profile-desktop:**

![profile-desktop](documentation/testing/lighthouse-results/profile-desktop.jpg)

-   **Add guest page:**

**add-guest_mobile:**

![add-guest_mobile](documentation/testing/lighthouse-results/add-guest_mobile.jpg)

**add-guest_desktop:**

![add-guest_desktop](documentation/testing/lighthouse-results/add-guest_desktop.jpg)

-   **Site notice page:**

**site-notice_mobile:**

![site-notice_mobile](documentation/testing/lighthouse-results/site-notice_mobile.jpg)

**site-notice_desktop:**

![site-notice_desktop](documentation/testing/lighthouse-results/site-notice_desktop.jpg)

-   **Privacy policy page:**

**privacy-policy_mobile:**

![privacy-policy_mobile](documentation/testing/lighthouse-results/privacy-policy_mobile.jpg)

**privacy-policy_desktop:**

![privacy-policy_desktop](documentation/testing/lighthouse-results/privacy-policy_desktop.jpg)

### **JShint**

---

No errors were reported for base.js or stripe_elements.js using [JSHint](https://jshint.com/).

![base](documentation/testing/jshint-results/base.jpg)
![stripe_elements](documentation/testing/jshint-results/stripe_elements.jpg)

### **Python**

---

Each .py-file has been formatted using the autopep8-extension for VSCode with the parameters '--max-line-length 79 --in-place --aggressive --aggressive' to guarantee PEP8-compliance. No errors have been reported by pylint.

## **Usability Testing**

---

---

Family, friends and colleagues were asked to test the site on their computers and/or mobile devices and their preferred browsers. The first page load can sometimes take very long. This happens when the app is 'asleep'. This is a limitation of the free Heroku account. No issues regarding the navigation of the site were reported. Feedback regarding the style of the CTA button on the homepage and the 'Add to shopping bag' buttons on the actor/ticket/package detail pages has been taken into account and the buttons now match the style of the buttons from the register and login pages. Feedback regarding the readability due to poor contrast has been taken into account as well and the text color for disclaimers has been adjusted to the default color and a red border has been added. No other issues were reported.

## **Compatibility Testing**

---

---

## **Responsiveness**

---

---

To test responsiveness, I used Google Chrome Developer Tools and Sizzy. Several problems could be identified and corrected, e.g. https://github.com/Ryagg/scifi_zone/commit/2241f748c2b2963ba7e46a47f00a220ae7ef11ba. For the remaining bugs refer to the Bugs section below. Apart from that, the site content is displayed correctly on all viewports.

## **Bugs**

---

---

-   Uploaded images don't match the size of the existing images due to the applied transformations before uploading the original images.
-   When logged in as an admin, the search bar input field causes overflow for some viewports and the navbar items are not centred for viewports from 1024px to 1215px.

![admin-searchbar](documentation/testing/bugs/admin-searchbar.jpg)
![admin-searchbar-complete](documentation/testing/bugs/admin-searchbar-complete.jpg)
![admin-searchbar-centered](documentation/testing/bugs/admin-searchbar-centered.jpg)

-   For all viewports the country select label on the checkout page is longer than the other input fields.

![county-select-label](documentation/testing/bugs/country-select-label.jpg)

-   For viewports with 320px, the heading 'Billing address' doesn't fit.

![checkout-heading-320px](documentation/testing/bugs/checkout-heading-320px.jpg)

-   Hovering over the checkbox on the login page causes the text next to it to use the Bulma default for hover and become difficult to read due to poor contrast

![login-checkbox](documentation/testing/bugs/login-checkbox.jpg)
