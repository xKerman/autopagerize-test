Feature: Paging
    In order to load next page
    As a browser extension user
    We should scroll to bottom of the page

    Scenario: Scroll to bottom and load next page
        Given I go to "http://localhost:5000/html5/"
          And I should see a link that contains the text "next" and the url "/html5/page/2"
          And I should not see "test page num: 2"
         When I scroll to bottom of the page
         Then I should be at "http://localhost:5000/html5/"
          And I should see "test page num: 2" within 5 seconds
