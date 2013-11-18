var assert= require('assert'),
test = require('selenium-webdriver/testing'),
webdriver= require('selenium-webdriver');

var driver =  // new webdriver.Builder().build();
    new webdriver.Builder()
    .withCapabilities(webdriver.Capabilities.chrome())
        .build();
var By = webdriver.By;


 // By.cssSelector(".blah , .b2lah")
// Start s
test.describe('Sqor', function() {
    test.it('should work', function() {
        driver.get("http://sqorweb.local/");
        var menu = driver.findElement(By.className("dropdown") );
        setTimeout(function() {

            menu.click();
            clickSubMenuLink();
        }, 1000);


        var clickSubMenuLink = function(sport) {

            setTimeout(function() {
                // alert("hi");

                var itemMenu= driver.findElements(By.cssSelector("dropdown a") );
                itemMenu[0].click();

            }, 50);

        };
        // var links = menu.findElement(By.tagName("a") );
        // links.click()

    });
});



// driver.quit();

