var assert= require('assert'),
test = require('selenium-webdriver/testing'),
webdriver= require('selenium-webdriver');

var driver =  // new webdriver.Builder().build();
    new webdriver.Builder()
    .withCapabilities(webdriver.Capabilities.chrome())
        .build();
var By = webdriver.By;



// Start s
test.describe('Sqor', function() {
    test.it('should work', function() {
        driver.get("http://www.sqor.com");
        driver.findElement(By.className("dropdown") ).click();
    });
});



// driver.quit();

