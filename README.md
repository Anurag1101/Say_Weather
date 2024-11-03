# WeatherVoice

A Simple Python Program for Real-Time Weather Updates with Voice Feedback
This project is a Python-based weather information app that fetches the current temperature of any city and provides a spoken response with the weather information. Using the requests library to call a weather API, the program retrieves the latest weather data, and with pyttsx3 (a text-to-speech engine), it reads the data aloud.

Features
Real-Time Weather Information: Fetches the current temperature for any city entered by the user.
Voice Feedback: Speaks out the weather information using a text-to-speech engine.
Continuous Mode: Allows users to check the weather for multiple cities in a loop.
User-Friendly: Simply type in the name of a city and hear the current weather conditions.
Technologies Used
Python: The core programming language.
Requests: For making HTTP requests to the weather API.
Pyttsx3: For converting text to speech offline.
Prerequisites
Python 3.x installed on your machine.
API Key for WeatherAPI. (A sample key is used in this example, but replace it with your own.)
Required Python packages:
bash
Copy code
pip install requests pyttsx3
Setup
Clone or Download the Repository:

If using Git:
bash
Copy code
git clone https://github.com/yourusername/WeatherVoice.git
cd WeatherVoice
Or download it directly from your GitHub repository.
Move to the Project Directory: Navigate to the directory where the project is located:

bash
Copy code
cd "C:\Users\anura\OneDrive\Desktop\Python\Say_Weather"
Obtain API Key: Sign up on WeatherAPI and get your API key. Replace 3d17c583de334f9195491352240311 in the code with your key.

Run the Program:

bash
Copy code
python weather_voice.py
Usage
When prompted, enter the name of a city to get the current temperature in Celsius.
The program will print the temperature and announce it aloud.
To check another city, simply enter a new city name when prompted.
To stop the program, close the terminal window or use a KeyboardInterrupt (Ctrl+C).
Example Output
csharp
Copy code
Enter the name of city: London
The weather of London is 15 degree Celsius
(Spoken aloud: "The weather of London is 15 degree Celsius")

Future Improvements
Potential features to add:

Additional weather details (humidity, conditions).
Enhanced error handling for invalid city names or network issues.
Graphical User Interface (GUI) for easier usage.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
WeatherAPI for providing weather data.
Pyttsx3 for offline text-to-speech capabilities.
Enjoy real-time weather updates with a voice assistant built in Python!
