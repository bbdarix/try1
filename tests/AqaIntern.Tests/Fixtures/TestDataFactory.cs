using Newtonsoft.Json;
using AqaIntern.Tests.Models;

namespace AqaIntern.Tests.Fixtures;

public static class TestDataFactory
{
    public static UserDto BuildUserFromJson(string json)
    {
        var user = JsonConvert.DeserializeObject<UserDto>(json);
        if (user is null)
        {
            throw new InvalidOperationException("Не удалось десериализовать JSON в UserDto.");
        }

        return user;
    }
}
