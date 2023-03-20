# image_classifinator

<h2 align="center">Regards to Doofenshmirtz.</h2>

###

<br clear="both">

<div align="center">
  <img height="270" src="https://64.media.tumblr.com/a3572e5023605f19085461b7d7846c6d/tumblr_n2pmq8yjwz1r38f9do1_500.gifv"  />
</div>

###



## Summary: reads text in images and compares them with other images and categorizes them into folders

you need to install the modules required for the code to run. 
You can use the following commands to load the modules specified
in the import lines in the code:

```bash
  pip install pytesseract
```
```bash
  pip install opencv-python
```
```bash
  pip install python-Levenshtein
```

## explanation of the project
First, a loop is created to scan the images in the directory contained in the `image_dir` variable.

Inside the loop, each image is read and the text in the image is read with the `pytesseract.image_to_string()` function.

Next, the `distance()` function is used to calculate the similarity ratio between the texts. 
This function calculates the Levenshtein distance value between two texts and returns it as a similarity ratio.

According to the similarity ratio, the picture is saved in two different folders as "similar" or "different". <br/>
If the similarity rate is **70** or higher, the picture is saved in the `similar` folder. <br/>
If the similarity rate is **70** or less, the image is saved in the `different` folder.

Working in this way, the program scans the texts in the images and classifies the images with the same text.

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/fatihpurtas" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="fatihpurtas" height="30" width="40" /></a>
<a href="https://medium.com/@fatih.purtas" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@fatih.purtas" height="30" width="40" /></a>
<a href="https://discord.gg/Zwynex#3506" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="Zwynex#3506" height="30" width="40" /></a>
</p>
