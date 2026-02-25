using RestSharp;

namespace AqaIntern.Tests.Base;

public sealed class ApiClient
{
    private readonly RestClient _client;

    public ApiClient(string baseUrl)
    {
        _client = new RestClient(baseUrl);
    }

    public async Task<RestResponse> GetAsync(string resource)
    {
        var request = new RestRequest(resource, Method.Get);
        return await _client.ExecuteAsync(request);
    }
}
