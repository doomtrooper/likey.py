Likey.py
=============

Introduction
------------

This is a *python3* compatible script to download top 5 liked pictures uploaded by a **FACEBOOK page**.
Note: Won't be working if the FACEBOOK page is *protected*.

Working
----------

- *Facebook* allows get and post request through the host **graph.facebook.com**.
- http.client was used to set-up a connection with the FB host.
- An access token is generated from *https://developers.facebook.com* and is provided as a input when the script is running.
- Then a GET request is sent to the host which gives a response in binary stream. This binary stram is then converted into **json** dictionary using *json* pyhton3 module.
- Then the dictionary is sorted on the basis of likes.
- Then the script downloads the top 5 uploaded pics of the page and saves then into a directory of name same as their FB  page name.

Modules Used
----------
- http.request
- json
- urllib
- os
