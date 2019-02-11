#!/bin/bash

cd /config/www/fontawesome
wget https://raw.githubusercontent.com/thomasloven/hass-fontawesome/master/hass-fontawesome-brands.html
wget https://raw.githubusercontent.com/thomasloven/hass-fontawesome/master/hass-fontawesome-regular.html
wget https://raw.githubusercontent.com/thomasloven/hass-fontawesome/master/hass-fontawesome-solid.html

cd /config/www/custom-lovelace/auto-entities
wget https://raw.githubusercontent.com/thomasloven/lovelace-auto-entities/master/auto-entities.js

cd /config/www/custom-lovelace/button-card
wget https://raw.githubusercontent.com/kuuji/button-card/master/button-card.js

cd /config/www/custom-lovelace/button-entity-row
wget https://raw.githubusercontent.com/custom-cards/button-entity-row/master/button-entity-row.js

cd /config/www/custom-lovelace/card-loader
wget https://raw.githubusercontent.com/thomasloven/lovelace-card-loader/master/card-loader.js

cd /config/www/custom-lovelace/card-modder
wget https://raw.githubusercontent.com/thomasloven/lovelace-card-modder/master/card-modder.js

cd /config/www/custom-lovelace/compact-custom-header
wget https://raw.githubusercontent.com/maykar/compact-custom-header/master/compact-custom-header.js
wget https://raw.githubusercontent.com/maykar/compact-custom-header/master/compact-custom-header-editor.js

cd /config/www/custom-lovelace/fold-entity-row
wget https://raw.githubusercontent.com/thomasloven/lovelace-fold-entity-row/master/fold-entity-row.js

cd /config/www/custom-lovelace/light-entity-row
wget https://raw.githubusercontent.com/custom-cards/light-entity-row/master/light-entity-row.js

cd /config/www/custom-lovelace/popup-card
wget https://raw.githubusercontent.com/thomasloven/lovelace-popup-card/master/popup-card.js

cd /config/www/custom-lovelace/slider-entity-row
wget https://raw.githubusercontent.com/thomasloven/lovelace-slider-entity-row/master/slider-entity-row.js

cd /config/www/custom-lovelace/time-input-row
wget https://raw.githubusercontent.com/thomasloven/lovelace-time-input-row/master/time-input-row.js

cd /config/www/custom-lovelace/tracker-card
wget https://raw.githubusercontent.com/custom-cards/tracker-card/master/tracker-card.js