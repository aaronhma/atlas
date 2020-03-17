# 🚀 Atlas
```
       _______ _                _____ 
    /\|__   __| |        /\    / ____|
   /  \  | |  | |       /  \  | (___  
  / /\ \ | |  | |      / /\ \  \___ \ 
 / ____ \| |  | |____ / ____ \ ____) |
/_/    \_\_|  |______/_/    \_\_____/ 

🚀 This is Atlas. Fast. Fuel efficient. The official rocket of Firebolt Space Agency.
We chose to build Atlas not because it is easy, but because it is hard.

- Aaron Ma & Rohan Fernandes
```

![Atlas](./images/moon.jpg)

Atlas is an end-to-end open source platform for rockets. It contains a comprehensivre, flexible ecosystem of tools, libraries, and community resources that lets researcher push state-of-the-art research in rocket science and developers to easily integrate Atlas into their existing rocket codebase.

Atlas was originally developed by two middle school students, Aaron Ma and Rohan Fernandes.

Atlas provides stable Python APIs, along with currently developing C++ binding API. Support for other languages are future plans.

## Versions

*Versions may change at any time, and released marked "🎖" may change at any time, without notice, per descretion at The Atlas Authors.*

**Atlas 0.0.1 Alpha:**

Atlas 0.0.1, commonly referred to the latest release will be released on April 1, 2020.

**🎖 Atlas 0.0.1 Beta:**

Atlas 0.0.2, codenamed Disco Dingo, is planned to be released on June 5, 2020.

**🎖 Atlas 0.0.1 rc0:**

Atlas 0.0.3, codenamed Lunar Loggerhead, is planned to be released on December 21, 2020.

**🎖 Atlas 0.0.1 rc1:**

Atlas 0.0.0, codenamed Bionic Beaver, is planned to be released on February 28, 2021.

**🎖 Atlas 0.0.1:**

Atlas 0.0.1, codenamed Utopic Unicorn, is planned to be released on August 16, 2021.

**🎖 Atlas 0.0.2:**

Atlas 0.0.2, codenamed Saucy Salamandar, is planned to be released on November 29, 2021.

**🎖 Atlas 0.0.3:**

Atlas 0.0.3, codenamed Wily Werewolf, is planned to be released on April 6, 2022.

🎖 Future Dates Are TBA

## Alert! Please Read!
We, Aaron Ma and Rohan Fernandes are preparing a special holiday release for April Fool's Day 2020. Stay tuned for updates!

FOR ROHAN & AARON:

Please check your assignments and grades in ASSIGNMENTS.md

FOR ATLAS GROUND CREW:

In the Storage Room, we have provided disinfecting sprays and hand sanitizer. Use hand sanitizer often and use the disinfecting sprays to spray in the Atlas capsule in the morning and evening. Mahalo for your cooperation!

## Atomic Base Info
**Alert!** Atomic Base is still *unstable*. If Atomic Base crashes, please do not be alarmed. Note that Atomic Base is a side project to simplify Travis CI and building for Atlas and is *not to be used for anything else*.

## Atlas Info
@TODO(aaronhma): Update

**Rohan; Atlas Info**
```
Atlas is a SpaceShip that travels to the moon. We built it becasue we wanted to help the space industry with its rocket missioin.

Now, I made the HoneyComb and SkyHawk Part. HoneyComb is a Website created

to control parts of the SpaceShip as well as provide entertainment.

SkyHawk is a time management app built using Microsoft Xamarin it uses C# to do the CodeBehind and XAML to show the User Interace.

SkyHawk was built because onboard atlas people don't

have very good time agament as there is not sense of time on the ship.  SkyHawk combines Python, and C# 

to create wonderfule and amazing games and it is built with Java and Swift 

Now Project Omega is about helping with Coronavirus which put the whole earth in a lockdown. As there were not many Tests and people needed help.

Omega helps with Coronavirus Concerns using Python and Machine Learning as well as C#. This application will hopefully create a less concern.

The Rocket is made by Aaron Ma. He used C++ and Python for Rocket Functionality
```

![Loading...](./svg/loader/material.svg) Loading...

## Getting Started Guide
Welcome to the wonderful world of Atlas! Atlas is full of easy-to-use features, but you must calibrate Atlas correctly before you take it out for a spin.

🎖 Experimental. It really won't work...

1. Get Atlas.
```bash
# This will not work on most Windows or Linux:
git clone git+https://bitbucket.org/aaronhma/atlas
```

2. Install and build Atlas.
```bash
cd PATH_TO_ATLAS
bash scripts/install.sh
bash scripts/build.sh --path-to-honeycomb $PATH_TO_HONEYCOMB
```

3. Start Atlas server.
```bash
bash scripts/atlas.sh start
```

4. Start Honeycomb by following the Honeycomb Quickstart Guide below, written by the Honeycomb maintainer.
```
cd $PATH_TO_HONEYCOMB
```

## Honeycomb Quickstart Guide(written by Rohan):
**The Docs: For Testing**

To start: Go to the HoneyComb Folder 
```
Execute Command: python server.py 
```
This starts the Server

In your terminal you will see a url

By default, you will go to `localhost:7777`, unless you changed the port number or the port number is already in use.

**ERROR HANDLING WITH HOSTS**

If it goes to another website, go to HoneyComb's server.py and in app.run change the Port to another number 

To change in do this: `Port = {number}`: where nuumber is the port number you want and then, you can go to `localhost:{number}`

**Short Cut for LocalHost**

What you can do is copy the link or **Windows**: Crtl + Click **Mac** command c + command v **Linux**: control c + control v

@TODO: Rohan make docs for OnBoard, Aaron supply OS for machine running the code

**Website**


**TADA** You will see the website.

[If you still get errors contact the honeycomb writer](mailto:rohanf6219@gmail.com)

@TODO(aaronhma): figure out a way to access firebolt internal with a login

![Loading...](./svg/loader/material.svg) Loading...

## Examples
@TODO(rohan): write docs

@TODO(aaronhma): create atlas examples

## Atlas Status
| Component    | Status                                    | Submitted By    |  Remarks    |
| ------------ |   -------------                           | -----           | ----        |
| Stage 1  🎖  | ![Build Passing](./svg/build/passing.svg) | aaronhma        | Passed.     |
| Stage 2  🎖  | ![Build Failing](./svg/build/failing.svg) | aaronhma        | Failed.     |
| Stage 3  🎖  | ![Build Failing](./svg/build/failing.svg) | aaronhma        | Failed.     |
| Honeycomb    | ![Build Passing](./svg/build/passing.svg) | rohan           | Passed.     |
| SkyHawk      | ![Build Failing](./svg/build/failing.svg) | aaronhma, rohan | Failed.     |
| Skyforce     | ![Build Running](./svg/build/running.svg) | aaronhma, rohan | Building... |
| PTurtle      | ![Build Passing](./svg/build/passing.svg) | rohan           | Passed.     |
| Omega        | ![Build Running](./svg/build/running.svg) | aaronhma, rohan | Building... |

[Information not correct? Contact maintainer to correct](mailto:hi@aaronhma.com)

**Combined with mini-projects: Skyforce, PTurtle and more!**
![Aaron Ma](./svg/signature/aaron.svg)
![Rohan Fernandes](./svg/signature/rohan.svg)