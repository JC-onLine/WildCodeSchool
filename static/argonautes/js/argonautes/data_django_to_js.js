// This file is use to Django data include in JavaScript
// Note: Need to use 'json_script' parser in Django template
// Tuto: https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/

// Django url for JavaScript Websockets:
const DJANGO_URL = JSON.parse(
  document.getElementById('django_url').textContent);

// Application data: database to display on page boot
const boot_page_db = JSON.parse(
  document.getElementById('boot_page_db').textContent);
