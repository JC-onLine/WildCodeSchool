// This file is use to Django data include in JavaScript
// Note: Need to use 'json_script' parser in Django template
// Tuto: https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/
// Author note: "it prevents the problem from ever occurring in your code,
//               because your JavaScript never passes through templating.
//               You can reduce your XSS risk even further by banning
//               inline scripts on your site. You’d do this with a
//               Content Security Policy (CSP) using the script-src directive"

// Django url for JavaScript Websockets:
const DJANGO_URL = JSON.parse(
  document.getElementById('DJANGO_URL').textContent);

// Application settings
let app_settings = JSON.parse(
  document.getElementById('app_settings').textContent);

// Application data: database to display on page boot
let page_boot_db = JSON.parse(
  document.getElementById('page_boot_db').textContent);
