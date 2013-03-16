Feature: Paging
  In order to load next page
  As a browser extension user
  We should scroll to bottom of the page

  Scenario Outline: Scroll to bottom and load next page
    Given I go to "<url>"
      And Content-Type of the page should be "<content_type>"
      And I should see a element "a[rel='next']"
      And I should see a element ".autopagerize_page_element"
      And I should not see "test page num: 2"
     When I scroll to bottom of the page
     Then I should be at "<url>"
      And I should see "test page num: 2" within 5 seconds

  Examples:
    | url                                   | content_type          |
    | http://localhost:5000/html5/normal    | text/html             |
    | http://localhost:5000/xhtml5/normal   | application/xhtml+xml |
    | http://localhost:5000/html4.01/normal | text/html             |
    | http://localhost:5000/xhtml1.1/normal | application/xhtml+xml |
    | http://localhost:5000/html5/tr        | text/html             |
    | http://localhost:5000/xhtml5/tr       | application/xhtml+xml |
    | http://localhost:5000/html4.01/tr     | text/html             |
    | http://localhost:5000/xhtml1.1/tr     | application/xhtml+xml |
