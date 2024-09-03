# osu-mapdesc-generator

This project allows you to generate BBCode blocks for your ranked osu! beatmaps.
Clicking the arrows will direct you to your previous / next ranked beatmap.

![Preview](https://github.com/user-attachments/assets/101816ef-d81f-49c2-9da3-7d77dcf62103)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)

## Features

- **Only requires osu! profile**: Only osu! profile link is needed.
- **Automated BBCode Generation**: Quickly generate BBCode blocks for osu! beatmaps.

## Requirements

Before running the script, ensure you have the following installed:

### 1. Python

Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

### 2. Required Python Libraries

You need to install **Selenium** and **webdriver_manager**  by running the following command in the terminal:
```bash
pip install selenium webdriver_manager
```

## How to Use

1. **Run the Script**:
   - In your terminal or command prompt, navigate to the directory containing the project files.
   - Run the following command:
     ```bash
     python bbcode_generator.py
     ```

2. **Provide the Required Input**:
   - When prompted, enter your osu! profile link in the terminal and press `Enter`.

3. **Wait for the Process to Complete**:
   - The script will take a few seconds to process the data. During this time, a Chrome browser will pop up and scrape the necessary information from the linked osu! profile.

5. **Retrieve the Generated BBCode**:
   - Once the script has finished running, a text file (`generated_bbcodes.txt`) will be generated in the same folder.
   - Open the text file to find the BBCode that has been generated for your osu! beatmaps.

6. **Apply the BBCode**:
   - Manually copy and paste the first line of the BBCode to your first ranked beatmap, you should see it links to the second ranked beatmap (if it exists).
   - Each line corresponds to one ranked beatmap.


## Versions

### Version 1.0.0 - Initial Release
- **Date Released**: 2024-09-03
- **Features**:
  - Basic BBCode generation for osu! ranked beatmaps.
  - Supports navigation between previous and next beatmaps using arrows.
  - Outputs generated BBCode to `generated_bbcodes.txt`.
