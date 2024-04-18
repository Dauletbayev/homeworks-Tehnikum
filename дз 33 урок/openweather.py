import aiohttp
import asyncio

async def parse_weather():
    params = {"q": "Ташкент", "appid": "3b55e2ff6e5dd329726472ab4724ffb4", "units": "metric"}
    url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    temperature = data.get("main", {}).get("temp")
                    if temperature is not None:
                        print(f"Temperature in Ташкент: {temperature}°C")
                    else:
                        print("Temperature data not available")
                else:
                    print(f"Failed to fetch weather data: {response.status}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    await parse_weather()

if __name__ == "__main__":
    asyncio.run(main())
