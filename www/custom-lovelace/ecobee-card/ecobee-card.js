class EcobeeCard extends HTMLElement {
    _fire(type, detail, options) {
      options = options || {};
      detail = (detail === null || detail === undefined) ? {} : detail;
      const event = new Event(type, {
        bubbles: options.bubbles === undefined ? true : options.bubbles,
        cancelable: Boolean(options.cancelable),
        composed: options.composed === undefined ? true : options.composed
      });
      event.detail = detail;
      this.dispatchEvent(event);
      return event;
    }

    set hass(hass) {
      if (!this.content) {
        const card = document.createElement('ha-card');
        const link = document.createElement('link');
        link.type = 'text/css';
        link.rel = 'stylesheet';
        link.href = '/local/custom-lovelace/ecobee-card/ecobee-card.css';
        card.appendChild(link);

        card.addEventListener('click', event => {
          this._fire('hass-more-info', { entityId: this.config.entity });
        })

        this.content = document.createElement('div');
        this.content.className = 'card';
        card.appendChild(this.content);
        this.appendChild(card);
      }

      const stateObj = hass.states[this.config.entity];

      const transform_operation_mode = {
          "heat": `<svg style="width:35px;height:35px" viewBox="0 0 24 24">
              <path fill="#F9A825" d="M11.71,19C9.93,19 8.5,17.59 8.5,15.86C8.5,
              14.24 9.53,13.1 11.3,12.74C13.07,12.38 14.9,11.53 15.92,
              10.16C16.31,11.45 16.5,12.81 16.5,14.2C16.5,16.84 14.36,19 11.71,
              19M13.5,0.67C13.5,0.67 14.24,3.32 14.24,5.47C14.24,7.53 12.89,9.2
              10.83,9.2C8.76,9.2 7.2,7.53 7.2,5.47L7.23,5.1C5.21,7.5 4,10.61 4,
              14A8,8 0 0,0 12,22A8,8 0 0,0 20,14C20,8.6 17.41,3.8 13.5,0.67Z" />
              </svg>`,
          "cool": `<svg style="width:35px;height:35px" viewBox="0 0 25 25">
              <path fill="#64B5F6" d="M20.79,13.95L18.46,14.57L16.46,
              13.44V10.56L18.46,9.43L20.79,10.05L21.31,8.12L19.54,7.65L20,
              5.88L18.07,5.36L17.45,7.69L15.45,8.82L13,7.38V5.12L14.71,
              3.41L13.29,2L12,3.29L10.71,2L9.29,3.41L11,5.12V7.38L8.5,8.82L6.5,
              7.69L5.92,5.36L4,5.88L4.47,7.65L2.7,8.12L3.22,10.05L5.55,9.43L7.55,
              10.56V13.45L5.55,14.58L3.22,13.96L2.7,15.89L4.47,16.36L4,
              18.12L5.93,18.64L6.55,16.31L8.55,15.18L11,16.62V18.88L9.29,
              20.59L10.71,22L12,20.71L13.29,22L14.7,20.59L13,18.88V16.62L15.5,
              15.17L17.5,16.3L18.12,18.63L20,18.12L19.53,16.35L21.3,15.88L20.79,
              13.95M9.5,10.56L12,9.11L14.5,10.56V13.44L12,14.89L9.5,
              13.44V10.56Z" />
              </svg>`,
          "auto": `<svg style="width:35px;height:35px" viewBox="0 0 25 25">
              <path d="m23.465 14.058-2.33 0.62-2-1.13v-2.88l2-1.13 2.33 0.62
              0.52-1.93-1.77-0.47 0.46-1.77-1.93-0.52-0.62 2.33-2
              1.13-2.45-1.44v-2.26l1.71-1.71-1.42-1.41-1.29 1.29-1.29-1.29-1.42
              1.41 1.71 1.71v2.26l-2.5 1.44-2-1.13-0.58-2.33-1.92 0.52 0.47
              1.77-1.77 0.47 0.52 1.93 2.33-0.62 2 1.13v2.89l-2
              1.13-2.33-0.62-0.52 1.93 1.77 0.47-0.47 1.76 1.93 0.52 0.62-2.33
              2-1.13 2.45 1.44v2.26l-1.71 1.71 1.42 1.41 1.29-1.29 1.29 1.29
              1.41-1.41-1.7-1.71v-2.26l2.5-1.45 2 1.13 0.62 2.33
              1.88-0.51-0.47-1.77 1.77-0.47-0.51-1.93m-11.29-3.39 2.5-1.45 2.5
              1.45v2.88l-2.5 1.45-2.5-1.45z" fill="#64b5f6"/>
              <path d="m8.0151 19.508c-1.78 0-3.21-1.41-3.21-3.14 0-1.62
              1.03-2.76 2.8-3.12s3.6-1.21 4.62-2.58c0.39 1.29 0.58 2.65 0.58
              4.04 0 2.64-2.14 4.8-4.79 4.8m1.79-18.33s0.74 2.65 0.74 4.8c0
              2.06-1.35 3.73-3.41 3.73-2.07 0-3.63-1.67-3.63-3.73l0.03-0.37c-2.02
              2.4-3.23 5.51-3.23 8.9a8 8 0 0 0 8 8 8 8 0 0 0 8
              -8c0-5.4-2.59-10.2-6.5-13.33z" fill="#f9a825"/>
              </svg>`,
          "off": "off",
      }
      const transform_botdot = {
        "heat": "dot_heat_color",
        "cool": "dot_neutral_color",
        "auto": "dot_heat_color",
        "off": "#000000",
      }
      const transform_midbotdot = {
        "heat": "dot_heat_color",
        "cool": "dot_neutral_color",
        "auto": "dot_neutral_color",
        "off": "#000000",
      }
      const transform_midtopdot = {
        "heat": "dot_neutral_color",
        "cool": "dot_cool_color",
        "auto": "dot_neutral_color",
        "off": "#000000",
      }
      const transform_topdot = {
        "heat": "dot_neutral_color",
        "cool": "dot_cool_color",
        "auto": "dot_neutral_color",
        "off": "#000000",
      }

      const transform_climate_mode_icon  = {
        "Sleep": `<ha-icon icon="mdi:power-sleep"></ha-icon> Sleep`,
        "Home":  `<ha-icon icon="mdi:home"></ha-icon> Home`,
        "Away": `<ha-icon icon="mdi:key-variant"></ha-icon> Away`,
      }

      const midbotdot = transform_midbotdot[stateObj.attributes.operation_mode];
      const midtopdot = transform_midtopdot[stateObj.attributes.operation_mode];
      const topdot = transform_topdot[stateObj.attributes.operation_mode];
      const transform_spt_operation_mode = {
        "heat": `<span class="dot dot6 ${midtopdot}"></span>
                 <div class="setpoint setpoint_heatcool operation_heat_color">
                  <p style="margin-top: 16px">
                   ${stateObj.attributes.temperature}
                  </p>
                 </div>
                 <span class="dot dot6 ${midbotdot}"></span>`,
        "cool": `<span class="dot dot6 ${midtopdot}"></span>
                 <span class="setpoint setpoint_heatcool operation_cool_color">
                  <p style="margin-top: 16px">
                   ${stateObj.attributes.temperature}
                  </p>
                 </span>
                 <span class="dot dot6 ${midbotdot}"></span>`,
        "auto": `<span class="setpoint setpoint_auto operation_heat_color">
                  <p style="margin-top: 12px">
                   ${stateObj.attributes.target_temp_high}
                  </p>
                 </span>
                 <span class="dot dot6 ${midbotdot}"></span>
                 <span class="setpoint setpoint_auto operation_cool_color">
                   <p style="margin-top: 12px">
                     ${stateObj.attributes.target_temp_low}
                   </p>
                </span>`,
        "off": ``,
      }
      const climate_mode = transform_climate_mode_icon[stateObj.attributes.climate_mode];
      const icon_operation_mode = transform_operation_mode[stateObj.attributes.operation_mode];
      const spt_operation_mode = transform_spt_operation_mode[stateObj.attributes.operation_mode];
      const botdot = transform_botdot[stateObj.attributes.operation_mode];

      this.content.innerHTML = `
        <div class="ecobee_card">
          <div class="grid-container">
            <div class="grid-item"></div>
            <div class="ecobee1 ecobee_mode">
              ${icon_operation_mode}
            </div>
            <div class="grid_circles">
  	          <span class="dot dot1 ${topdot}"></span>
              <span class="dot dot2 ${topdot}"></span>
              <span class="dot dot3 ${topdot}"></span>
              <span class="dot dot4 ${topdot}"></span>
              ${spt_operation_mode}
              <span class="dot dot4 ${botdot}"></span>
              <span class="dot dot3 ${botdot}"></span>
              <span class="dot dot2 ${botdot}"></span>
              <span class="dot dot1 ${botdot}"></span>
            </div>
            <div class="grid-item"></div>
            <div class="ecobee1 ecobee_humidity">
              <ha-icon icon="mdi:water-percent"></ha-icon>${stateObj.attributes.actual_humidity} %
            </div>
            <div class="grid-item"></div>
            <div class="ecobee1 ecobee_temperature">
              ${stateObj.attributes.current_temperature}&deg
            </div>
            <div class="grid-item"></div>
            <div class="ecobee1 ecobee_div">
              ${climate_mode}
            </div>
          </div>
        </div>
       `;
    }

    setConfig(config) {
      if (!config.entity || config.entity.split(".")[0] !== "climate") {
        throw new Error("Specify an entity from within the climate domain.");
      }

      this.config = config;
    }
}

customElements.define('ecobee-card', EcobeeCard);

