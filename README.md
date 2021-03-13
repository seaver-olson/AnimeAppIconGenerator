# AnimeAppIconGenerator

## On first Installation:
- open the commands directory with `cd commands`
- run `python3.8 setup.py`

## How to use:
  To merge images into an App Icon first you have to find an image of your application icon, for example the [Apple Settings Icon](https://github.com/Gasai-Olson/AnimeAppIconGenerator/blob/main/img/setting.png), and then a image to add on top, for example [Ichigo from Darling in the Franxx](https://github.com/Gasai-Olson/AnimeAppIconGenerator/blob/main/img/example.png).  
  
Once you have your two images make sure they have transparent backgrounds and then add them to your `images` directory that was created by running `setup.py`
  
From there you only have to call the command `startsetup(folder, icon, image)` from `startprocess.py`.  Run `python3.8 startprocess.py folder icon image` replacing folder, icon, and image with their respective names

### An example of using this file:

  `python3.8 startprocess.py settingicon setting.png example.jpeg`
