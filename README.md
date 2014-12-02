Simple Package Locator
======================

This is a simple parcel or package locator. Just enter the package no and it will display
your providor's package tracking online service. Visit the [online demo](http://whimpy.beta.scapp.io/)

Why do I need this?

Well, if you have ever wanted to track a package you know the hassle to do so: You need
to know where to look. This service solves that problem, just enter your package No and
it will display the matching tracking service.

Currently supported delivery services 
=====================================

* Swiss Post

Contribute by adding a locator service

How to run/develop locally
==========================

```
cd <project dir>
virtualenv env
source env/bin/activate
cd whimpy
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

How to deploy
=============

(assuming cloudfoundry PaaS)

```
cd whimpy
cf push
```

The `manifest.yml` lists all requirements. The buildpack is determined by my PaaS automatically.
It is based on this generic python buildpack: 

```
https://github.com/cloudfoundry/python-buildpack
```


