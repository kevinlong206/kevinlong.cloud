FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
COPY . ./csharpmicroservice
WORKDIR /csharpmicroservice/
RUN dotnet build -c Release -o output
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS runtime
COPY --from=build /csharpmicroservice/output .
ENTRYPOINT ["dotnet", "csharp.dl