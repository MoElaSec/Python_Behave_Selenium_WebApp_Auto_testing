# PyBDD: Automate testing for WebApps with selenium & Cucumber/behave
[![AUTOMATION](https://img.shields.io/badge/automation-selenium-brightgreen)](https://github.com/SeleniumHQ/selenium)
[![BDD](https://img.shields.io/badge/BDD-behave-brown)](https://github.com/behave/behave)
[![CLI](https://img.shields.io/badge/CLI-click-purple)](https://github.com/pallets/click)

A CLI tool used to fuly test WebApps using Python Behave+Selenuim+Click

Feature  | Step implmentation
------------- | -------------
![image](https://user-images.githubusercontent.com/48570596/116403066-2ceb7800-a83e-11eb-9dbc-a98036168cf1.png)  | ![image](https://user-images.githubusercontent.com/48570596/116403250-658b5180-a83e-11eb-9735-2d017ec2707b.png)


### 👨‍💻Dev-Env:
create a `venv` or `pipenv` and run:
```
pip install behave
pip install selenium
pip install click
```

### ✨Usage:
```
python main.py [name_feature]
```
for example to test the dresses page:

`python main.py dresses`



```
Commands:
  all
  contact-us
  dresses
  logo
  sign-in
  sign-up
  tops

```
---

> ``📝``uncomment the `behave.ini` to get only feature summary in the terminal.
