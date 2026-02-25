using FluentAssertions;
using Newtonsoft.Json.Linq;
using AqaIntern.Tests.Base;

namespace AqaIntern.Tests.Tests;

[TestFixture]
public class ApiTests
{
    [Test]
    public async Task GetUser_ShouldReturn200_AndExpectedUserData()
    {
        var client = new ApiClient("https://reqres.in/api/");

        var response = await client.GetAsync("users/2");

        response.IsSuccessful.Should().BeTrue();
        response.StatusCode.Should().Be(System.Net.HttpStatusCode.OK);
        response.Content.Should().NotBeNullOrWhiteSpace();

        var json = JObject.Parse(response.Content!);
        json["data"]!["id"]!.Value<int>().Should().Be(2);
        json["data"]!["email"]!.Value<string>().Should().Contain("@");
    }
}
