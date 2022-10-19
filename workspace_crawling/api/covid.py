


def today():
    service_key="4MM5kqUQkB%2BYVvyI4Zx3ZZyb%2BCM2qNJtMntfhBMMBR8eXZD48J7sNd520Pot2kXYJhxWFq1HNYrloOWjm6eHqg%3D%3D"
    url = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}"
    print(url)



if __name__ == '__main__':
    today()