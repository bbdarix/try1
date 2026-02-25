using FluentAssertions;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace AqaIntern.Tests.Tests;

[TestFixture]
public class UiTests
{
    [Test]
    public void Login_ShouldOpenInventoryPage()
    {
        var options = new ChromeOptions();
        options.AddArgument("--headless=new");
        options.AddArgument("--no-sandbox");
        options.AddArgument("--disable-dev-shm-usage");

        using var driver = new ChromeDriver(options);

        driver.Navigate().GoToUrl("https://www.saucedemo.com/");

        driver.FindElement(By.CssSelector("[data-test='username']")).SendKeys("standard_user");
        driver.FindElement(By.CssSelector("[data-test='password']")).SendKeys("secret_sauce");
        driver.FindElement(By.CssSelector("[data-test='login-button']")).Click();

        driver.Url.Should().Contain("inventory.html");
        driver.Title.Should().Contain("Swag Labs");
    }
}
