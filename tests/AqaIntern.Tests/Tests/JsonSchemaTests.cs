using FluentAssertions;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using AqaIntern.Tests.Fixtures;

namespace AqaIntern.Tests.Tests;

[TestFixture]
public class JsonSchemaTests
{
    [Test]
    public void UserJson_ShouldDeserialize_AndMatchSchema()
    {
        var json = """
                   {
                     "id": 2,
                     "email": "janet.weaver@reqres.in",
                     "first_name": "Janet",
                     "last_name": "Weaver"
                   }
                   """;

        var user = TestDataFactory.BuildUserFromJson(json);

        user.Id.Should().Be(2);
        user.Email.Should().Contain("@");
        user.FirstName.Should().NotBeNullOrWhiteSpace();
        user.LastName.Should().NotBeNullOrWhiteSpace();

        var schema = JSchema.Parse(
            """
            {
              "type": "object",
              "required": ["id", "email", "first_name", "last_name"],
              "properties": {
                "id": { "type": "integer" },
                "email": { "type": "string", "format": "email" },
                "first_name": { "type": "string" },
                "last_name": { "type": "string" }
              }
            }
            """);

        var jObject = JObject.Parse(json);
        jObject.IsValid(schema).Should().BeTrue();
    }
}
