<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![MIT License][blog-shield]][blog-url]
<!-- ABOUT THE PROJECT -->
## About The CVS Vaccine Checker

This script checks for covid-19 vaccines near you. 

To run it, you'll need python 3.x installed on your computer, along with the packages requests, beepy, and time. See here for how to install those from code academy: https://www.codecademy.com/articles/install-python

Once you have those, save the script in a folder on your desktop. You'll need to open the script and do some very easy editing that I've marked out using `###`. There are instructions at the top for you too :) This should be easy enough for someone comfortable with technology. Ask for help on NextDoor - it's where I answer a lot of tech questions for my neighbors!

Once you've updated the script with your state and cities, navigate your command line from the tutorial above to that folder, and type `python3 vaccine.py`. Like magic, it will run!

## Usage

This script is for monitoring the appointment website without clicking refresh 1Billion times. It is not going to automatically book for you. And if you fork this and create an automated booking applet, I will personally send 1000 adolscent, chewing puppies to your house. And nobody wants that.  Speaking of contributing...

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/burgamacha/CVS-vaccine-checker.svg?style=for-the-badge
[contributors-url]: https://github.com/burgamacha/CVS-vaccine-checker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/burgamacha/CVS-vaccine-checker.svg?style=for-the-badge
[forks-url]: https://github.com/burgamacha/CVS-vaccine-checker/network/members
[stars-shield]: https://img.shields.io/github/stars/burgamacha/CVS-vaccine-checker.svg?style=for-the-badge
[stars-url]: https://github.com/burgamacha/CVS-vaccine-checker/stargazers
[license-shield]: https://img.shields.io/github/license/burgamacha/CVS-vaccine-checker.svg?style=for-the-badge
[license-url]: https://github.com/burgamacha/CVS-vaccine-checker/blob/master/LICENSE.txt
[blog-shield]: https://img.shields.io/badge/medium-Read%20about%20this%20on%20Medium-lightgrey.svg?style=for-the-badge
[blog-url]: https://python.plainenglish.io/how-i-built-a-cvs-vaccine-appointment-availability-checker-in-python-6beb379549e4

## My Experience

I added a check of the local county portal and ran this script for a few hours over several days before my tier became eligible just to collect some stats. CVS was releasing appointment slots mostly between 2 and 4 AM and I saw none at the county portal. So when my turn did arrive (50+, no comorbidities), I started the script and went to bed. It woke me early in the morning and even though CVS said "available", I was unable to secure an appointment. After several tries, at multiple locations, I gave up and went back to bed. The next day, the script announced success at my local county portal and, unlike the CVS false positives, I got an appointment on the first try. Within the next few minutes, my wife and at least two co-workers also succeeded by going to the county.

YMMV but adding my county portal did the trick for me. 

HTH, Bob
