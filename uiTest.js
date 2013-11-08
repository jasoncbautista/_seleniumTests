var assert= require('assert'),
test = require('selenium-webdriver/testing'),
webdriver= require('selenium-webdriver');

var driver =  // new webdriver.Builder().build();
    new webdriver.Builder()
    .withCapabilities(webdriver.Capabilities.chrome())
        .build();
var By = webdriver.By;

// Start s
test.describe('Google Search', function() {
    test.it('should work', function() {
        driver.get("http://www.google.com");
        driver.findElement(By.name("q")).sendKeys("webdriver");
        driver.findElement(By.name("btnG")).click();
        debugger;
        driver.getTitle().then(function(title) {
             console.log(title);
             assert.equal("webdriver - Google Search", title);
        });

    });
});



// driver.quit();

