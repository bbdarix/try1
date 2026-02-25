# AQA Intern Pet Project (C#)

Простой pet-проект для позиции **Intern AQA** на C# с покрытием:

- **UI** (Selenium)
- **API** (RestSharp)
- **JSON** (десериализация + JSON Schema)

## Что внутри

- `UiTests.cs` — UI-тест логина на SauceDemo через Selenium
- `ApiTests.cs` — API-тест на `reqres.in`
- `JsonSchemaTests.cs` — проверка десериализации и схемы JSON

## Стек

- .NET 8
- NUnit
- FluentAssertions
- Selenium WebDriver + ChromeDriver
- RestSharp
- Newtonsoft.Json
- Newtonsoft.Json.Schema

## Запуск

```bash
dotnet restore
dotnet test AqaInternPetProject.sln
```
