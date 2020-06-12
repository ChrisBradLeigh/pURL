# pURL
Python Based URL Shortener 

**https://short.chrisleigh.dev/**

## How to Use
Prefix your long url to generate a shortened version.<br>

## Install
There is a script for creating a purl service in ubuntu.
Define the following Env VARS for the script:<br>
 * **PURL_DEFAULT_URL** = http://default.example.com/
  - This is the default URL that you get redirected to if the 5 Letter code does not work.
 * **PURL_HOST_URL** = http://short.example.com/
  - The base URL for the 5 Letter code to be appended to
Prefered DIR: /var/www/
