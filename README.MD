# SERPAPİ APP

---
## ![a.png](IMAGES/a.png) CONTENTS
### - [Description](#dpng-description)
### - [Setup](#cpng-setup)
### - [Usage](#fpng-usage)
### - [THIRD PARTY LICENSES](#bpng-third-party-licenses)<br>

---
## ![d.png](IMAGES/d.png) Description
This project isn't intended to be innovative. The main goal is to practice working with API services.

However, this doesn't mean it's useless. It can be a helpful project depending on how you use it.

For example, by looking at the API service files in the project, you can better understand how the SerpApi service works or even learn something new about using API services.

---

## ![c.png](IMAGES/c.png) Setup
1. Step:
Create a profile on the [**SerpApi website**](https://serpapi.com/). Get an API key from the account you created<br><br><br>
2. Step:
Clone the folder named "**jsons**" inside the repo. Write your API key information into the "**api.json**" file inside the cloned folder.<br><br><br>
3. Step:
Install the PyInstaller module on your computer.
```
pip install pyinstaller
```
<br>

4. Step:
Take the files inside the repo and put them into a folder. Run the CMD panel as administrator inside this folder<br><br>

5. Step:
Write the following code in the opened panel.
```
pyinstaller --onefile --hidden-import="pygetwindow;requests" --noconsole ^
--add-data "Popular_Destinations_api_service.py;." ^
--add-data "parameter_bringer.py;." ^
--add-data "Nutrition_Information_api_service.py;." ^
--add-data "News_api_service.py;." ^
--add-data "Jobs_API_service.py;." ^
--add-data "Immersive_Products_api_service.py;." ^
--add-data "file_funcs.py;." ^
--add-data "courses_API_service.py;." ^
main.py
```
<br>

6. Step:
A folder named "dist" will be created inside your folder. Inside it, you will find the .exe file of our application.<br><br><br>

7. Step:
Put the folder named "**jsons**" into the same location as this .exe file. Don’t forget Step 2.  <br><br>

### Note: Don’t forget to install the other third-party software

---
## ![f.png](IMAGES/f.png) Usage
After completing the steps in the Installation section, run the generated .exe file.

- A text file named "questions" will appear. From this file, you can choose the API service you want to use.

- Based on your API selection, the requested data will be generated in a text file named "temp_file" and as a list.

- After closing the "temp_file", you will return to the panel file.

- If you want to exit the application, simply press the "q" key.

---

## ![b.png](IMAGES/b.png) THIRD PARTY LICENSES

### ![e.png](IMAGES/e.png) [Requets](https://pypi.org/project/requests/)
- **License** : Apache License 2.0
- **Meaning** : It is open and permissive; it grants the right to copy, modify, and distribute, including for commercial use<br>

### ![e.png](IMAGES/e.png) [PyInstaller](https://pypi.org/project/pyinstaller/)
- **License** : GNU GPLv2
- **Meaning** : You can distribute the .exe file you created with PyInstaller without being bound by GPL conditions <br>

### ![e.png](IMAGES/e.png) [PyGetWindow](https://pypi.org/project/PyGetWindow/)
- **License** : BSD 3-Clause
- **Meaning** : You can freely use, modify, and distribute the software, including for commercial purposes

